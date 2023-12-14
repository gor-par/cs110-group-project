import matplotlib.pyplot as plt
from csv_reader import CsvReader
from filter import FilterOption
from tools import get_column_mean

# Setting the style for the plot
plt.style.use('dark_background')

# Loading the dataset
dataset = CsvReader('GlobalWeatherRepository.csv')

# Using a set to store unique countries
countries = set()

# Populating the set with unique country names from the dataset
for row in dataset.rows:
    countries.add(row.get("country"))  # Adding the country to the set

avg_temps = []

# Calculating average temperatures for each country
for country in countries:
    # Creating a filter to extract rows for a specific country
    country_filter = [
        FilterOption('string', 'equal', 'country', country),
    ]
    # Calculating the average temperature for the filtered rows
    avg_temps.append(get_column_mean(filter(dataset.rows, country_filter), 'temperature_celsius'))

# Plotting a histogram of average temperatures
plt.hist(avg_temps, bins=10, color="green", ec="black")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.title("Histogram of Average Temperature for all Countries")
plt.show()
