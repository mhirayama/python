import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
from matplotlib.backends.backend_pdf import PdfPages

df = pd.read_csv('pokemon/Pokemon.csv')

df['Legendary'] = df['Legendary'].astype(int)

from sklearn.decomposition import PCA

pca = PCA()
X_pca = pca.fit_transform(df.loc[:, 'HP':'Speed'])
df_pca =pd.DataFrame(X_pca, columns = ['1st', '2nd', '3rd', '4th', '5th', '6th'])

df_pca['Legendary'] = df['Legendary']

fig, ax = plt.subplots(figsize = (12, 8))

df_pca.plot(kind = 'scatter', x = '1st', y = '2nd', s = 100, c = 'Legendary', cmap = 'winter', alpha = 0.5, ax =ax)

pdf = PdfPages('test.pdf')

#plt.show()

pdf.savefig()

pdf.close()
