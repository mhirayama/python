import numpy as np
import matplotlib.pyplot as plt
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

from sklearn.model_selection import KFold, cross_val_score

kfold = KFold(n_splits = 5, shuffle = True, random_state = 0)

log_reg_score = cross_val_score(log_reg, X ,y, cv = kfold)
tree_clf_score = cross_val_score(tree_clf, X, y, cv = kfold)

y_pred_log_reg = log_reg.predict(X_test)
y_pred_tree_clf = tree_clf.predict(X_test)

from sklearn.metrics import precision_recall_curve

precision, recall ,threshold = precision_recall_curve(y_test, y_pred_tree_clf)

plt.figure(figsize = (12, 8))
plt.plot(precision, recall)
plt.xlabel("Precision")
plt.ylabel("Recall")
plt.show()

precision, recall ,threshold = precision_recall_curve(y_test, y_pred_log_reg)

plt.figure(figsize = (12, 8))
plt.plot(precision, recall)
plt.xlabel("Precision")
plt.ylabel("Recall")
plt.show()
