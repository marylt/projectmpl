import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import colors
import pandas as pd
import csv

# loading csv file into dataframe
df = pd.read_csv('vgsales.csv')
df.head()

### GRAPHS TO SHOW GENRE/SALES RELATIONSHIP###

# df sorted by sales and genre
    # jp
dfjp = df.sort_values(by = ['JP_Sales', 'Genre'], ascending = False)
dfjp.head()
jpgenres = dfjp['Genre']
jpsales = dfjp['JP_Sales']

    # na
dfna = df.sort_values(by = ['NA_Sales', 'Genre'], ascending = False)
dfna.head()
nagenres = dfna['Genre']
nasales = dfna['NA_Sales']

    # eu
dfeu = df.sort_values(by = ['EU_Sales', 'Genre'], ascending = False)
dfeu.head()
eugenres = dfeu['Genre']
eusales = dfeu['EU_Sales']

# simple scatterplots
    # jp
plt.scatter(jpgenres, jpsales, edgecolors='r', alpha=1.0)
plt.xlabel('Genre')
plt.ylabel('JP_Sales in Millions')
plt.title('Video Game Genre Sales in Japan')
plt.show()

    # na
plt.scatter(nagenres, nasales, edgecolors='g', alpha=1.0)
plt.xlabel('Genre')
plt.ylabel('NA_Sales in Millions')
plt.title('Video Game Genre Sales in North America')
plt.show()

    # eu
plt.scatter(eugenres, eusales, edgecolors='b', alpha=1.0)
plt.xlabel('Genre')
plt.ylabel('EU_Sales in Millions')
plt.title('Video Game Genre Sales in Europe')
plt.show()