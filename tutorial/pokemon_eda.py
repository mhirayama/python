import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

df = pd.read_csv('pokemon/Pokemon.csv')

print(df.head())
print("\n")

print(df.info())
print("\n")

print(df.shape)
print("\n")

print(df.describe())
print("\n")

print(df.nunique())
print("\n")

print(df.isnull().sum())
print("\n")

print(df.index)
print("\n")

print(df.columns)
print("\n")

df['Legendary'] = df['Legendary'].astype(int)
print(df.head())
print("\n")

fig, ax = plt.subplots(figsize = (12, 8))
df.plot(kind = 'scatter', x = 'HP', y = 'Attack', s = 100, c = 'Legendary', cmap = 'winter', alpha = 0.5, ax =ax)
plt.savefig("pokemon_hp_attack.png",bbox_inches='tight')
plt.close("pokemon_hp_attack.png")

print(df.loc[:, 'HP':'Speed'].corr())
print("\n")


pg = sns.pairplot(df.loc[:, 'HP':'Speed'])
pg.savefig("pokemon_pairplot.png",bbox_inches='tight')
plt.close("pokemon_pairplot.png")

plt.figure(figsize=(12, 8))
sns.heatmap(df.loc[:, 'HP':'Speed'].corr(), annot=True, fmt='g', cmap='Blues')
plt.savefig("pokemon_heatmap.png",bbox_inches='tight')
plt.close("pokemon_heatmap.png")

from sklearn.decomposition import PCA
pca = PCA()

X_pca = pca.fit_transform(df.loc[:, 'HP':'Speed'])
df_pca =pd.DataFrame(X_pca, columns = ['1st', '2nd', '3rd', '4th', '5th', '6th'])

print(df_pca.head())
print("\n")

print(pca.explained_variance_ratio_)
print("\n")

plt.figure(figsize = (12, 8))
plt.plot(np.hstack([0,pca.explained_variance_ratio_.cumsum()]))
plt.xlabel('n_components', fontsize = 15)
plt.ylabel('explained_variance_ratio_', fontsize = 15)
plt.savefig("pokemon_hstack.png",bbox_inches='tight')
plt.close("pokemon_hstack.png")

print(pca.components_)
print("\n")

plt.figure(figsize = (14, 12))
sns.heatmap(pca.components_,
           cmap = 'Blues',
           annot = True,
           annot_kws = {'size': 20},
           fmt = '1.1f',
           xticklabels = df.loc[:, 'HP' : 'Speed'].columns,
           yticklabels = ['1st', '2nd', '3rd', '4th', '5th', '6th'])
plt.savefig("pokemon_heatmap2.png",bbox_inches='tight')
plt.close("pokemon_heatmap2.png")

df_pca['Legendary'] = df['Legendary']

fig, ax = plt.subplots(figsize = (12, 8))

df_pca.plot(kind = 'scatter', x = '1st', y = '2nd', s = 100, c = 'Legendary', cmap = 'winter', alpha = 0.5, ax =ax)

plt.savefig("pokemon.png",bbox_inches='tight')

plt.close("pokemon.png")
