import numpy as np
import pandas as pd

df = pd.read_csv('titanic/train.csv')

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

X = df.drop(columns = ['PassengerId', 'Survived', 'Name', 'Ticket', 'Cabin'])
y = df['Survived']

from sklearn.preprocessing import LabelEncoder

cat_features = ['Sex', 'Embarked']

for col in cat_features:
    lbl = LabelEncoder()
    X[col] = lbl.fit_transform(list(df[col].values))

from sklearn.preprocessing import StandardScaler

num_feature = ['Age', 'Fare']

for col in num_feature:
    scaler = StandardScaler()
    X[col] = scaler.fit_transform(np.array(df[col].values).reshape(-1, 1))

X = pd.get_dummies(X, columns = ['Pclass', 'SibSp', 'Embarked'], drop_first = True)

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

from sklearn.model_selection import GridSearchCV

param = {
    'C' : [0.01, 0.1, 1, 10, 100]
}

grid_search = GridSearchCV(SVC(), param_grid = param, cv = 5)
grid_search.fit(X_train, y_train)

print(grid_search.best_params_)

print(grid_search.score(X_test, y_test))

from sklearn.model_selection import cross_val_score

scores = cross_val_score(GridSearchCV(SVC(), param_grid = param, cv = 5), X, y, cv = 5)
print(scores)

print(scores.mean())
