import pickle

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import mutual_info_score
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, auc
from sklearn.model_selection import KFold
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb

from tqdm.auto import tqdm

import warnings
warnings.filterwarnings('ignore')


# parameters
eta = 0.1
max_depth = 5
min_child_weight = 5
output_file = f'model_eta={eta}_max_depth={max_depth}_min_child_weight={min_child_weight}.bin'

# data loading and preparation
df = pd.read_csv(r'C:\Users\fdiazl\Downloads\Banking Dataset Classification\new_train.csv')
df['y'] = df['y'].map({'yes': 1, 'no': 0})

feature_selection = ['duration', 'previous', 'campaign', 'age'
                    ,'poutcome', 'month', 'contact', 'job', 'default'
                    ,'loan']

df = df[feature_selection + ['y']]

for columna in ['duration', 'previous', 'campaign', 'age']:
    df[columna] = df[columna].fillna(df[columna].median())

df['poutcome'] = df['poutcome'].fillna('nonexistent')           
df['month'] = df['month'].fillna('may')

df['contact'] = df['contact'].fillna('cellular')

for columna in ['job', 'default','loan']:
    df[columna] = df[columna].fillna('unknown')

# train final model
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=42)

df_full_train = df_full_train.reset_index(drop=True)
y_full_train = df_full_train.y.values
df_full_train.drop(['y', 'pdays'], axis=1, inplace=True)

dicts_full_train = df_full_train.to_dict(orient='records')
dv = DictVectorizer(sparse=False)
X_full_train = dv.fit_transform(dicts_full_train)

y_test = df_test.y.values
df_test.drop(['y', 'pdays'], axis=1, inplace=True)
dicts_test = df_test.to_dict(orient='records')
X_test = dv.transform(dicts_test)

features = list(dv.get_feature_names_out())

dfull_train = xgb.DMatrix(X_full_train, label=y_full_train, 
        feature_names=features )

dtest = xgb.DMatrix(X_test, label=y_test, feature_names=features )

xgb_params = {
    'eta': 0.1, 
    'max_depth': 5,
    'min_child_weight': 5,
    
    'objective': 'binary:logistic',
    'eval_metric': 'auc',

    'nthread': 8,
    'seed': 1,
    'verbosity': 1,
}

model = xgb.train(xgb_params, dfull_train, num_boost_round=100)

y_pred = model.predict(dtest)
auc = roc_auc_score(y_test, y_pred)
print(f"XGBoost AUC: {auc:.3f}")