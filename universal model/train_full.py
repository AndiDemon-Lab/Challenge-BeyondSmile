import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, BaggingClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
from sklearn.metrics import roc_auc_score, accuracy_score, f1_score
import numpy as np
import os
import pickle
from sklearn.model_selection import LeaveOneGroupOut
from imblearn.combine import SMOTEENN
from sklearn.preprocessing import LabelEncoder

save_dir = '../sliding_windows'
with open(os.path.join(save_dir, "full_dataset_labeled_neu.pkl"), "rb") as f:
    df = pickle.load(f)

# Preprocessing
le = LabelEncoder()
df['participant_id'] = le.fit_transform(df['participant_id'])
df = df.dropna()

# Pisahkan fitur dan target dengan BENAR (tanpa participant_id)
X = df.drop(['depression_episode','timestamp', 'date', 'participant_id'], axis=1)  # Hapus participant_id dari fitur
y = df['depression_episode'].values.ravel()  # Konversi ke array 1D
groups = df['participant_id'].values  # Array numpy untuk grouping

# Konversi ke numpy array untuk akses lebih cepat
X_np = X.values

# Model dengan parameter teroptimasi
ensemble_models = {
    'RandomForest': RandomForestClassifier(random_state=42),
    'GradientBoosting': GradientBoostingClassifier(random_state=42),
    'XGBoost': XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42),
    'LightGBM': LGBMClassifier(random_state=42, verbose=-1),
    'CatBoost': CatBoostClassifier(verbose=0, random_state=42),
    'AdaBoost': AdaBoostClassifier(random_state=42),
    'Bagging': BaggingClassifier(n_estimators=10, random_state=42)
}

# Hapus model yang lambat jika diperlukan
# del ensemble_models['GradientBoosting']
# del ensemble_models['CatBoost']

logo = LeaveOneGroupOut()
sm = SMOTEENN(random_state=42) 
results = []

for train_idx, test_idx in logo.split(X_np, y, groups=groups):
    X_train, X_test = X_np[train_idx], X_np[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]
    
    # Handle class imbalance hanya di data training
    X_res, y_res = sm.fit_resample(X_train, y_train)
    
    for model_name, model in ensemble_models.items():
        try:
            model.fit(X_res, y_res)
            
            # Prediksi
            y_pred = model.predict(X_test)
            y_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else [0]*len(y_test)
            
            # Simpan hasil
            results.append({
                'model': model_name,
                'participant': groups[test_idx[0]],
                'auroc': roc_auc_score(y_test, y_proba) if len(np.unique(y_test)) > 1 else np.nan,
                'accuracy': accuracy_score(y_test, y_pred),
                'f1': f1_score(y_test, y_pred)
            })
        except Exception as e:
            print(f"Error dengan {model_name}: {str(e)}")

# Simpan hasil
df_results = pd.DataFrame(results)
df_summary = df_results.groupby('model')[['auroc', 'accuracy', 'f1']].mean().reset_index()
df_summary.to_csv('result/optimized_results.csv', index=False)
print("Hasil ringkasan:")
print(df_summary)
