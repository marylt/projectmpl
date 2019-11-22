import matplotlib.pyplot as plt
import csv

x = []
y = []

# loading csv file into csvreader:
with open('vgsales.csv', 'r') as data:
    reader = csv.reader(data, delimiter=',')
    # establish counter:
    counter = 0
    for r in reader:
        if (r[5]) != 'Publisher':
            x.append(r[5])
            y.append(r[10])
            counter += 1
            if counter == 30:
                break

plt.bar(x, y, color='r', edgecolor='b')
plt.xlabel('Publisher')
plt.ylabel('Global Sales in Millions')
plt.title('Global Sales of Game Publishers')
plt.show()
