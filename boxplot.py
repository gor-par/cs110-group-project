import matplotlib.pyplot as plt
from csv_reader import CsvReader

# Loading the dataset
dataset = CsvReader('GlobalWeatherRepository.csv')

# Setting the style for the plot
plt.style.use('dark_background')

# Creating a new figure for the plot
plt.figure(figsize=(10, 6), edgecolor="black")

regions_list = []
humidity_list = []

# Extracting unique region names from the dataset
for row in dataset.rows:
    reg = row.get("timezone").split("/")[0]
    if reg not in regions_list:
        regions_list.append(reg)

# Populating the humidity_list with values for each region
for i in range(len(regions_list)):
    humidity_values = []
    for row in dataset.rows:
        if row.get("timezone").split("/")[0] == regions_list[i]:
            humidity_values.append(row.get("humidity"))

    humidity_list.append(humidity_values)

# Creating a box plot with humidity values for each region
plt.boxplot(humidity_list, labels=regions_list)
plt.xticks(rotation=20)
plt.title("Box Plot of Average Humidity by Regions")
plt.xlabel("Region")
plt.ylabel("Humidity (%)")

# Displaying the plot
plt.show()
