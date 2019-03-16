import numpy as np
import pandas as pd

df = pd.read_csv('npb/player_records.csv')

columns_list = ['年度', '所属球団', '登板', '勝利' ,'敗北', 'セーブ' ,'H' ,'HP', '完投', '完封勝', '無四球', '勝率', '打者',
               '投球回', '安打', '本塁打', '四球', '死球', '三振', '暴投', 'ボーク', '失点', '自責点', '防御率', '名前']

df = df.loc[:, columns_list]

df['防御率'] = pd.to_numeric(df['防御率'], errors = 'coerce')

df.dropna(inplace = True)

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples

df = df[df['年度'] == 2018]

data_df = df.drop(columns = ['年度', '所属球団', '名前'])

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_df)

data = np.array(data_df)
data_scaled = np.array(data_scaled)

distortions = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters = k, n_init= 10, max_iter = 100)
    kmeans.fit(data_scaled)
    distortions.append(kmeans.inertia_)

n_clusters = 6
kmeans = KMeans(n_clusters = n_clusters, n_init= 10, max_iter = 100)
kmeans.fit(data_scaled)
cluster_labels = kmeans.predict(data_scaled)

pd.set_option('display.max_columns', 30)

df['cluster'] = cluster_labels

print(df[df['cluster'] == 0])
print(df[df['cluster'] == 1])
print(df[df['cluster'] == 2])
print(df[df['cluster'] == 3])
print(df[df['cluster'] == 4])
print(df[df['cluster'] == 5])
