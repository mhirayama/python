import numpy as np
from sklearn.datasets import make_moons

moons = make_moons(n_samples = 200, noise = 0.2, random_state = 0)
X = moons[0]
y = moons[1]

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

log_reg = LogisticRegression().fit(X_train, y_train)
tree_clf = DecisionTreeClassifier().fit(X_train, y_train)

print(log_reg.score(X_test, y_test))
print(tree_clf.score(X_test, y_test))

from sklearn.model_selection import KFold, cross_val_score

kfold = KFold(n_splits = 5, shuffle = True, random_state = 0)

log_reg_score = cross_val_score(log_reg, X ,y, cv = kfold)
tree_clf_score = cross_val_score(tree_clf, X, y, cv = kfold)

print(log_reg_score)
print(tree_clf_score)

print(log_reg_score.mean())
print(tree_clf_score.mean())

from sklearn.metrics import confusion_matrix

y_pred_log_reg = log_reg.predict(X_test)
y_pred_tree_clf = tree_clf.predict(X_test)

cm_log_reg = confusion_matrix(y_test, y_pred_log_reg)
cm_tree_clf = confusion_matrix(y_test, y_pred_tree_clf)

print(cm_log_reg)
print("\n")
print(cm_tree_clf)

from sklearn.metrics import precision_score, recall_score, f1_score

print("precision log_reg:\n", precision_score(y_test, y_pred_log_reg))
print("\n")
print("precision tree_clf:\n", precision_score(y_test, y_pred_tree_clf))

print("recall log_reg:\n", recall_score(y_test, y_pred_log_reg))
print("\n")
print("recall tree_clf:\n", recall_score(y_test, y_pred_tree_clf))

print("f1 log_reg:\n", f1_score(y_test, y_pred_log_reg))
print("\n")
print("f1 tree_clf:\n", f1_score(y_test, y_pred_tree_clf))
