from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

#データセットの読み込み、cancer.dataとcancer.targetをそれぞれX,yとする
cancer = load_breast_cancer()

#データの分割
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify = cancer.target, random_state = 0)

#モデルの作成
clf = KNeighborsClassifier(n_neighbors = 3).fit(X_train, y_train)

#正解率の計算
print(round(clf.score(X_test, y_test), 3))
