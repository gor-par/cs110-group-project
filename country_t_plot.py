import matplotlib.pyplot as plt
import matplotlib.patches as patches
from csv_reader import CsvReader
from filter import FilterOption, filter
import tools

plt.style.use('dark_background')
dataset = CsvReader('GlobalWeatherRepository.csv')

plt.figure(edgecolor="white")
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
plt.plot(temp, feels, 'y', label='relation of feeling')
plt.plot(temp, wet, 'g', label='depending on humidity')
plt.plot(temp, pres, 'b', label='depending on pressure')

plt.xlabel('temperature')
plt.ylabel('other factors')
plt.xlim(0, 40)
plt.ylim(-10, 50)
plt.title(f'Temperature and other factors for {prompt}')
plt.legend()  # add a legend to show the labels
plt.show()

