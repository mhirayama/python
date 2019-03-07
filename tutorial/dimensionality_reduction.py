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

num_features = ['Age', 'Fare']

for col in num_features:
    scaler = StandardScaler()
    X[col] = scaler.fit_transform(np.array(df[col].values).reshape(-1, 1))

from sklearn.decomposition import PCA

pca = PCA()
X_pca = pca.fit_transform(X)

print(pca.explained_variance_ratio_)

print(pca.components_)
