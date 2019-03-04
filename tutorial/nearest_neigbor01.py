import mglearn

X, y = mglearn.datasets.make_forge() #データセットの生成

from sklearn.neighbors import KNeighborsClassifier #最近傍法の読み込み
from sklearn.model_selection import train_test_split #トレインデータとテストデータを分割するライブラリ

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0) #データの分割

clf = KNeighborsClassifier(n_neighbors = 3) #最近傍法のクラスを生成
clf.fit(X_train, y_train) #モデルの作成、学習

print(clf.predict(X_test)) #テストデータを使って学習モデルから予測する

print(y_test) #実際のデータ

print(round(clf.score(X_test, y_test), 3)) #正解率の計算

clf_10 = KNeighborsClassifier(n_neighbors = 10) パラメーターを変更してみる
clf_10.fit(X_train, y_train) #モデルの作成
print(round(clf_10.score(X_test, y_test), 3)) #正解率の計算

#パラメーターを1から15まで変更して繰り返す
for n_neighbors in range(1, 16):
    clf = KNeighborsClassifier(n_neighbors = n_neighbors).fit(X_train, y_train)
    print("Test set accuracy : n_neighbors = {}, {:.2f}".format(n_neighbors, clf.score(X_test, y_test)))
