import matplotlib.pyplot as plt
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
            y.append(r[10])
            counter += 1
            if counter == 5:
                break
    y.sort()        
plt.bar(x, y, color='b', edgecolor='r')
plt.xlabel('Game Name')
plt.ylabel('Global Sales in Millions')
plt.title('Top Global Selling Games')
plt.show()