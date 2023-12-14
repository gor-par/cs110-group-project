import math
import matplotlib.pyplot as plt
from csv_reader import CsvReader
import matplotlib.patches as patches
from filter import FilterOption, filter

# Setting the style for the plot
plt.style.use('dark_background')

# Loading the dataset
dataset = CsvReader('GlobalWeatherRepository.csv')

# Creating subplots and loading the map image
fig, ax = plt.subplots()
img = plt.imread('map.png')
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
# Function to plot temperature point
def plot_temperature_point(ax, lon, lat, temp, color):
    ax.text(lon, lat, '+', color=color)


# Mapping temperature ranges to colors
color_map = {40: 'darkred', 30: 'red', 20: 'orange', 10: 'yellow', 0: 'green', -10: 'blue'}

# Plotting temperature points on the map based on temperature ranges
for row in dataset.rows:
    lat, lon, temp = (row.get('latitude'), row.get('longitude'),
                      row.get('temperature_celsius'))

    # Finding the appropriate color based on temperature
    color = next(
        (color for threshold, color in color_map.items()
         if threshold < temp <= threshold + 10),
        'darkblue'
    )

    # Plotting temperature point using the function
    plot_temperature_point(ax, lon, lat, temp, color)

# adding the title
plt.title('Temperature Distribution Map')
# Displaying the plot
plt.show()

