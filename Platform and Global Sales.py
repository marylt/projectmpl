import matplotlib.pyplot as plt
import pandas as pd
import csv

# loading csv file into dataframe
df = pd.read_csv('vgsales.csv')
df.head()

# defining df parameters for pie chart
sums = df.groupby(df["Platform"])["Global_Sales"].sum()
plt.axis('equal');
plt.pie(sums, labels=sums.index, autopct='%1.1f%%', shadow=True);
plt.title('Platforms by Global Sales')
plt.show()