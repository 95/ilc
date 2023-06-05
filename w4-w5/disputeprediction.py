# Import required libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE

# Load dataset
dataset = pd.read_csv('C:\\Users\\defra\\Downloads\\sales.csv', error_bad_lines=False)
df = dataset.copy()

# Preprocessing
# Convert 'created_at' to datetime
df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')

# Extract features from 'created_at'
df['year'] = df['created_at'].dt.year
df['month'] = df['created_at'].dt.month
df['day'] = df['created_at'].dt.day
df['day_of_week'] = df['created_at'].dt.dayofweek
df['hour'] = df['created_at'].dt.hour

# Drop 'created_at'
df = df.drop(['created_at'], axis=1)

# Fill missing numeric values with median
numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
df[numeric_columns] = df[numeric_columns].apply(lambda x: x.fillna(x.median()))

# Convert string categories to numeric
categorical_columns = df.select_dtypes(include=[object]).columns.tolist()
df[categorical_columns] = df[categorical_columns].apply(lambda x: LabelEncoder().fit_transform(x.astype(str)))

# Separate features and target variable
X = df.drop('disputed', axis=1)
y = df['disputed']

# Split data into training and test sets (obvious)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Handle imbalance with SMOTE
smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X_train, y_train)

# Logistic Regression
lr = LogisticRegression(max_iter=1000)
lr.fit(X_res, y_res)

# Predict and evaluate Logistic Regression
y_pred_lr = lr.predict(X_test)
print("Logistic Regression Classifier Report: \n", classification_report(y_test, y_pred_lr))

# Random Forest Classifier
rf = RandomForestClassifier()
rf.fit(X_res, y_res)

# Predict and evaluate Random Forest Classifier
y_pred_rf = rf.predict(X_test)
print("Random Forest Classifier Report: \n", classification_report(y_test, y_pred_rf))
