import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, BaggingClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
from sklearn.metrics import roc_auc_score, accuracy_score, f1_score
import numpy as np
import os
import pickle
from sklearn.metrics import roc_auc_score, accuracy_score, f1_score
from sklearn.model_selection import LeaveOneGroupOut
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import LabelEncoder


save_dir = '../sliding_windows'
with open(os.path.join(save_dir, "full_dataset_labeled_neu.pkl"), "rb") as f:
    df = pickle.load(f)

le = LabelEncoder()
df['participant_id'] = le.fit_transform(df['participant_id'])
df = df.dropna()

au_columns = [col for col in df.columns if col.startswith("au_AU")]

df_eyeprob = df[['participant_id']+au_columns+['depression_episode']]

le = LabelEncoder()
df['participant_id'] = le.fit_transform(df['participant_id'])

X = df_eyeprob.drop(columns='depression_episode')
y = df_eyeprob[['depression_episode']]


sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X, y)
X = pd.DataFrame(X_res, columns=X.columns)
y = pd.DataFrame(y_res, columns=y.columns)
groups = X.participant_id
X = X.drop(columns='participant_id')
# Convert groups to NumPy array
groups = groups.to_numpy()
# Pastikan y berbentuk array 1D
y = y.values.ravel()

logo = LeaveOneGroupOut()
# List of ensemble models
ensemble_models = {
    'RandomForest': RandomForestClassifier(random_state=42),
    'GradientBoosting': GradientBoostingClassifier(random_state=42),
    'XGBoost': XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42),
    'LightGBM': LGBMClassifier(random_state=42, verbose=1),
    'CatBoost': CatBoostClassifier(verbose=1, random_state=42),
    'AdaBoost': AdaBoostClassifier(random_state=42),
    'Bagging': BaggingClassifier(n_estimators=10, random_state=42)
}

# Metrics storage
df_results = []

for train_idx, test_idx in logo.split(X.values, y, groups=groups):
    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]
    
    if len(np.unique(y_test)) < 2:
        continue  # Skip jika test set hanya punya 1 kelas

    for model_name, model in ensemble_models.items():
        # Train model
        model.fit(X_train, y_train)
        print(f'Model {model_name} sudah selesai di Training')

        # Predict
        y_pred = model.predict(X_test)
        y_proba = model.predict_proba(X_test)[:, 1]

        # Store metrics
        try:
            auroc = roc_auc_score(y_test, y_proba)
        except ValueError:
            auroc = np.nan

        df_results.append({
            'model': model_name,
            'participant_id': groups[test_idx[0]],
            'auroc': auroc,
            'accuracy': accuracy_score(y_test, y_pred),
            'f1': f1_score(y_test, y_pred)
        })

# Convert results to DataFrame
df_results = pd.DataFrame(df_results)
df_summary = df_results.groupby('model')[['auroc', 'accuracy', 'f1']].mean().reset_index()
df_summary.to_csv(f'result/actionUnit_result.csv', index=False)
print(df_summary)