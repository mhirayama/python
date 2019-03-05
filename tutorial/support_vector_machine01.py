import mglearn
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.datasets import load_iris

iris = load_iris() #データセットの読み込み

X = iris.data[50:, 2:] #50以降で3つ目と4つ目のカラムのデータを読み込み
y = iris.target[50:] - 1 #ターゲットの配列が1と2で構成されているので-1して0と1に変更

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify = y, random_state = 0) #データの分割

svm = LinearSVC().fit(X_train, y_train) #モデルの作成
svm_100 = LinearSVC(C = 100).fit(X_train, y_train) #パラメータを100にして過学習でモデルを作成
svm_001 = LinearSVC(C = 0.01).fit(X_train, y_train) #パラメータを0.01にして学習不足でモデル作成

#それぞれの正解率の表示
print("score on training set: {:.2f}".format(svm.score(X_train, y_train)))
print("score on test set: {:.2f}".format(svm.score(X_test, y_test)))

print("score on training set: {:.2f}".format(svm_100.score(X_train, y_train)))
print("score on test set: {:.2f}".format(svm_100.score(X_test, y_test)))

print("score on training set: {:.2f}".format(svm_001.score(X_train, y_train)))
print("score on test set: {:.2f}".format(svm_001.score(X_test, y_test)))
