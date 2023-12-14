import numpy as np
from filter import FilterOption, filter
from tools import get_column_mean
from csv_reader import CsvReader
import matplotlib.pyplot as plt

plt.style.use('dark_background')
dataset = CsvReader('GlobalWeatherRepository.csv')

plt.figure(figsize=(10, 6), edgecolor="black")

regions_list = []
humidity_list = []

for row in dataset.rows:
    reg = row.get("timezone").split("/")[0]
    if reg not in regions_list:
        regions_list.append(reg)

for i in range(len(regions_list)):
    humidity_values = []
    for row in dataset.rows:
        if row.get("timezone").split("/")[0] == regions_list[i]:
            humidity_values.append(row.get("humidity"))

    humidity_list.append(humidity_values)

plt.boxplot(humidity_list, labels=regions_list)
plt.xticks(rotation=20)
plt.title("Box Plot of Average Humidity by Regions")
plt.xlabel("Region")
plt.ylabel("Humidity (%)")
plt.show()
