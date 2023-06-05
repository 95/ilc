#importing libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#importing dataset
dataset = pd.read_csv('C:\\Users\\defra\\Downloads\\brca.csv')
X = dataset.iloc[:, 1:-1].values #independent variable matrix
y = dataset.iloc[:, -1].values #dependent variable vector

# b = 0, m = 1
le = LabelEncoder()
y = le.fit_transform(y)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a scaler
scaler = StandardScaler()

# Fit on the training data
scaler.fit(X_train)

# Transform both the training data and the test data
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Create a logistic regression classifier
classifier = LogisticRegression()

# Fit the classifier on the training data
classifier.fit(X_train, y_train)

# Use the classifier to predict labels for the test set
y_pred = classifier.predict(X_test)

# Print accuracy score
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

#from sklearn.model_selection import cross_val_score

#classifier = LogisticRegression()

# Perform cross-validation
#scores = cross_val_score(classifier, X_train, y_train, cv=10)

# Print each of the scores and the average score
#print('Cross-validation scores:', scores)
#print('Average cross-validation score:', scores.mean())

from sklearn.model_selection import GridSearchCV

# Define the model
model = LogisticRegression(solver='liblinear')

# Define the parameters to search over
param_grid = {
    'C': np.logspace(-4, 4, 20), # log-spaced sequence of 20 values between 10^-4 and 10^4
    'penalty': ['l1', 'l2']
}

# Create a GridSearchCV object
grid_search = GridSearchCV(model, param_grid, cv=10, scoring='accuracy')

# Fit the GridSearchCV object to the data
grid_search.fit(X_train, y_train)

# Print the best parameters and the best score
print('Best parameters:', grid_search.best_params_)
print('Best score:', grid_search.best_score_)

best_model = LogisticRegression(penalty='l1', C=0.615848211066026, solver='liblinear')
best_model.fit(X_train, y_train)
best_pred = best_model.predict(X_test)

# Print accuracy score
accuracy = accuracy_score(y_test, best_pred)
print(f'Accuracy: {accuracy}')
