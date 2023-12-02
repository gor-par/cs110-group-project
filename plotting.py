import matplotlib.pyplot as plt
import csv

file = open('GlobalWeatherRepository.csv', 'r')

reader = csv.reader(file)

next(reader)

x = []
y = []

for row in reader:
    x.append(row[0])
    y.append(row[1])


file.close()

plt.plot(x, y, color='red', linestyle='-', marker='o', label='Data')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('CSV Data Plot')

plt.legend()

plt.show()


