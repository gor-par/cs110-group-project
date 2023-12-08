from tools import get_column_mean, get_values
from filter import FilterOption, filter
from csv_reader import CsvReader
import matplotlib.pyplot as plt

dataset = CsvReader('GlobalWeatherRepository.csv')

countries = set()  # use a set to store the unique countries
for row in dataset.rows:
    countries.add(row.get("country"))  # add the country to the set

avg_temps = []
for country in countries:
    country_filter = [
        FilterOption('string', 'equal', 'country', country),
    ]
    avg_temps.append(get_column_mean(filter(dataset.rows, country_filter), 'temperature_celsius'))

# Plot a histogram of average temperature
plt.hist(avg_temps, bins=10, color="green", ec="black")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.title("Histogram of Average Temperature for all Countries")
plt.show()
