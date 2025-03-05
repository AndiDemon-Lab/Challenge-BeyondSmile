import pandas as pd
from sklearn.model_selection import LeaveOneGroupOut, KFold, cross_val_predict
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, BaggingClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
from sklearn.metrics import roc_auc_score, accuracy_score, f1_score
import numpy as np
import os
import pickle
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load dataset
save_dir = '../sliding_windows'
with open(os.path.join(save_dir, "full_dataset_labeled_neu.pkl"), "rb") as f:
    df = pickle.load(f)

# df = df.dropna()
# au_columns = [col for col in df.columns if col.startswith("au_AU")]
# df[au_columns] = df[au_columns].fillna(df[au_columns].median())
df['leftEyeOpenProbability'] = df['leftEyeOpenProbability'].fillna(df['leftEyeOpenProbability'].median())
df['rightEyeOpenProbability'] = df['rightEyeOpenProbability'].fillna(df['rightEyeOpenProbability'].median())
df['smilingProbability'] = df['smilingProbability'].fillna(df['smilingProbability'].median()) 
df = df[['timestamp','participant_id','rightEyeOpenProbability', "leftEyeOpenProbability", 'smilingProbability','date', 'depression_episode']]


df = df.dropna()
# Preprocessing
le = LabelEncoder()
df['participant_id'] = le.fit_transform(df['participant_id'])

X = df.drop(['depression_episode', 'timestamp'], axis=1)
y = df[['depression_episode']]

# Opsional: Oversampling jika diperlukan
# sm = SMOTE(random_state=42)
# X_res, y_res = sm.fit_resample(X, y)
# X = pd.DataFrame(X_res, columns=X.columns)
# y = pd.DataFrame(y_res, columns=y.columns)

# Cek distribusi kelas secara keseluruhan


# Jika grouping dengan participant_id + date menghasilkan grup homogen,
# gunakan grouping berdasarkan participant_id saja.
# groups = (X['participant_id'].astype(str) + '_' + X['date'].astype(str)).values
groups = df['participant_id'].values

# Hapus kolom grouping dari fitur
X = X.drop(columns=['participant_id', 'date'])

# Pastikan target y berbentuk array 1D
y = y.values.ravel()





# Inisialisasi LeaveOneGroupOut
logo = LeaveOneGroupOut()

# Daftar model ensemble
ensemble_models = {
    'RandomForest': RandomForestClassifier(random_state=42),
    'GradientBoosting': GradientBoostingClassifier(random_state=42),
    'XGBoost': XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42),
    'LightGBM': LGBMClassifier(random_state=42, verbose=-1),
    'CatBoost': CatBoostClassifier(verbose=0, random_state=42),
    'AdaBoost': AdaBoostClassifier(random_state=42),
    'Bagging': BaggingClassifier(n_estimators=10, random_state=42)
}

# Storage untuk hasil metrik
df_results = []

# Loop untuk cross-validation dengan LeaveOneGroupOut
for train_idx, test_idx in logo.split(X.values, y, groups=groups):
    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]
    
    # Lewati fold jika hanya terdapat satu kelas
    if len(np.unique(y_test)) < 2:
        continue

    # Terapkan SMOTE hanya pada data training
    sm = SMOTE(random_state=42)
    X_train_res, y_train_res = sm.fit_resample(X_train, y_train)
    
    for model_name, model in ensemble_models.items():
        # Nested Cross-Validation untuk training (KFold)
        inner_cv = KFold(n_splits=5)
        
        # Prediksi probabilitas dengan cross_val_predict menggunakan data yang sudah di-resample
        y_proba_train = cross_val_predict(
            model, X_train_res, y_train_res, cv=inner_cv, 
            method='predict_proba', n_jobs=-1
        )[:, 1]
        
        # Latih model pada data training yang sudah di-resample
        model.fit(X_train_res, y_train_res)
        print(f"Model {model_name} telah dilatih pada data training (SMOTE)")
        
        # Prediksi pada data test (data asli, tanpa SMOTE)
        y_pred = model.predict(X_test)
        if hasattr(model, "predict_proba"):
            y_proba = model.predict_proba(X_test)[:, 1]
        else:
            y_proba = model.decision_function(X_test)
        
        # Hitung metrik evaluasi
        try:
            auroc = roc_auc_score(y_test, y_proba)
        except ValueError:
            auroc = np.nan
        
        df_results.append({
            'model': model_name,
            'participant': groups[test_idx[0]],
            'auroc': auroc,
            'accuracy': accuracy_score(y_test, y_pred),
            'f1': f1_score(y_test, y_pred)
        })

# Simpan dan tampilkan hasil jika ada
if df_results:
    df_results = pd.DataFrame(df_results)
    df_summary = df_results.groupby('model')[['auroc', 'accuracy', 'f1']].mean().reset_index()
    df_summary.to_csv('result/hybrid_eyeSmile_median.csv', index=False)
    print(df_summary)
else:
    print("No results were collected. Please check your cross-validation splits and data balance.")
