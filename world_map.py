import math
from csv_reader import CsvReader
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from filter import FilterOption, filter

plt.style.use('dark_background')
dataset = CsvReader('GlobalWeatherRepository.csv')

fig, ax = plt.subplots()
img = plt.imread('visuals/map.png')
ax.imshow(img, extent=[-180, 180, -90, 90])


# define a function that formats the coordinates
def format_coord(x, y):
    return f'lon={x:.2f}, lat={y:.2f}'


ax.format_coord = format_coord
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')

for row in dataset.rows:
    # get the latitude and longitude values from the dictionary
    lat = row.get('latitude')
    lon = row.get('longitude')

    temp = row.get('temperature_celsius')
    # Assume temp is the temperature variable
    if temp > 40:
        ax.text(lon, lat, '+', color='darkred')
    elif 30 < temp <= 40:
        ax.text(lon, lat, '+', color='red')
    elif 20 < temp <= 30:
        ax.text(lon, lat, '+', color='orange')
    elif 10 < temp <= 20:
        ax.text(lon, lat, '+', color='yellow')
    elif 0 < temp <= 10:
        ax.text(lon, lat, '+', color='green')
    elif -10 < temp <= 0:
        ax.text(lon, lat, '+', color='blue')
    else:
        ax.text(lon, lat, '+', color='darkblue')

plt.show()
