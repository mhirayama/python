import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('titanic/train.csv')

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

from sklearn.preprocessing import LabelEncoder

cat_features = ['Sex', 'Embarked']

for col in cat_features:
    lbl = LabelEncoder()
    df[col] = lbl.fit_transform(list(df[col].values))

X = df.drop(columns = ['PassengerId', 'Survived', 'Name', 'Ticket', 'Cabin'])
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

tree = DecisionTreeClassifier().fit(X_train, y_train)
print(tree.score(X_test, y_test))

rnd_forest = RandomForestClassifier(n_estimators=500, max_depth = 5, random_state = 0).fit(X_train, y_train)
print(rnd_forest.score(X_test, y_test))

test_df = pd.read_csv('titanic/test.csv')

test_df['Age'] = test_df['Age'].fillna(test_df['Age'].mean())
test_df['Fare'] = test_df['Fare'].fillna(test_df['Fare'].mode()[0])

for col in cat_features:
    lbl = LabelEncoder()
    test_df[col] = lbl.fit_transform(list(test_df[col].values))

X_pred = test_df.drop(columns = ['PassengerId', 'Name', 'Ticket', 'Cabin'])
ID = test_df['PassengerId']

prediction = rnd_forest.predict(X_pred)

submisson = pd.DataFrame({
    'PassengerId': ID,
    'Survived': prediction
})

submisson.to_csv('titanic/submisson.csv', index = False)
