import matplotlib.pyplot as plt
import csv

x = []
y = []

# loading csv file into dataframe
with open('vgsales.csv', 'r') as data:
    reader = csv.reader(data, delimiter=',')
    sortedreader = sorted(reader, key=lambda r: r[10], reverse=True)
    counter = 1
    for r in sortedreader:
        if (r[5]) != 'Publisher':
            x.append(r[5])
            y.append(r[10])
            counter += 1
            if counter == 10:
                break
# df sorted by sales and publisher

plt.bar(x, y, color='r', edgecolor='b')
plt.xlabel('Publisher')
plt.ylabel('Global Sales in Millions')
plt.title('Global Sales of Game Publishers')
plt.show()
