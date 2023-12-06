import matplotlib.pyplot as plt
import matplotlib.patches as patches
from csv_reader import CsvReader
from filter import FilterOption, filter
import tools

dataset = CsvReader('GlobalWeatherRepository.csv')

plt.figure(facecolor="darkgrey", edgecolor="white")
prompt = input("enter the desired country/ies to plot temp for: ")
country_filter = [
    FilterOption('string', 'equal', 'country', [f'{prompt}'])
]
temp = []
feels = []
wet = []
pres = []

# loop over the filtered rows and append the values to the lists
for row in filter(dataset.rows, country_filter):
    temp.append(row.get('temperature_celsius'))
    feels.append(row.get('feels_like_celsius'))
    wet.append(row.get('humidity'))
    pres.append(row.get('pressure_mb'))

# plot the graphs using the lists as x and y values
plt.plot(feels, temp, 'y', label='relation of feeling')
plt.plot(wet, temp, 'b', label='depending on humidity')
plt.plot(pres, temp, 'r', label='depending on pressure')

plt.xlabel('temperature')
plt.ylabel('other factors')
plt.legend()  # add a legend to show the labels
plt.show()