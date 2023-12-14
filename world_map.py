import math
import matplotlib.pyplot as plt
from csv_reader import CsvReader  # Assuming you have a CSV reader module
import matplotlib.patches as patches
from filter import FilterOption, filter  # Assuming you have a filtering module

# Setting the style for the plot
plt.style.use('dark_background')

# Loading the dataset
dataset = CsvReader('GlobalWeatherRepository.csv')

# Creating subplots and loading the map image
fig, ax = plt.subplots()
img = plt.imread('visuals/map.png')
ax.imshow(img, extent=[-180, 180, -90, 90])


# Defining a function to format coordinates
def format_coord(x, y):
    """
    Format coordinates: lon=x.xx, lat=y.yy.
    """
    return f'lon={x:.2f}, lat={y:.2f}'


# Assigning the format_coord function to the axes
ax.format_coord = format_coord
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')

# Plotting temperature points on the map based on temperature ranges
for row in dataset.rows:
    # Getting latitude and longitude values
    lat = row.get('latitude')
    lon = row.get('longitude')

    # Getting the temperature variable
    temp = row.get('temperature_celsius')

    # Assigning colors based on temperature ranges and plotting on the map
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

# Displaying the plot
plt.show()
