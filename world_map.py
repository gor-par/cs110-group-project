import matplotlib.pyplot as plt
import matplotlib.patches as patches
from csv_reader import CsvReader
from filter import FilterOption, filter
import math

dataset = CsvReader('GlobalWeatherRepository.csv')

fig, ax = plt.subplots()
img = plt.imread('hope.png')  # change this to the path of your image file
ax.imshow(img, extent=[-180, 180, -90, 90])


# define a function that formats the coordinates
def format_coord(x, y):
    return f'lon={x:.2f}, lat={y:.2f}'  # change the names of the variables here


ax.format_coord = format_coord
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')

for row in dataset.rows:
    # get the latitude and longitude values from the dictionary
    lat = row.get('latitude')
    lon = row.get('longitude')
    # get the message to print from the dictionary
    temp = row.get('temperature_celsius')
    if temp > 0:
        ax.text(lon, lat, '+', color='darkred')
    if temp < 0:
        ax.text(lon, lat, '+', color='darkblue')

plt.show()
