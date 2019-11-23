# library and dataset
from matplotlib import pyplot as plt
import csv

x = []
y = []

# loading csv file into csvreader:
with open('vgsales.csv', 'r') as data:
    reader = csv.reader(data, delimiter=',')
    # establish counter
    counter = 0
    for r in reader:
        if (r[1]) != 'Name':
            x.append(r[1])
            y.append(r[6])
            counter += 1
            if counter == 10:
                break
# plot with matplotlib
plt.stem( x, y)
plt.xlabel("Game Name")
plt.ylabel("NA Sales in Millions")
plt.title("Top Game Sales in North America")
plt.show()
