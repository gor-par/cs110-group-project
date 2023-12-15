from csv_reader import CsvReader
from filter import FilterOption, filter
import matplotlib.pyplot as plt

data = CsvReader('GlobalWeatherRepository.csv')
date_format = '%Y-%m-%d %H:%M'


countries = ["Armenia", 'Azerbaijan', "Georgia",
             "Rwanda", "Singapore", "Switzerland"]

autumn_query = [
    FilterOption("string", "equal", "country", countries, None),
    # FilterOption("date", 'during', 'last_updated', (9, 11), date_format),
    FilterOption("string", 'equal', 'condition_text', ['Sunny', "Clear"], None)
]

autumn_rows = filter(data.rows, autumn_query)


sunny_day_counts = {}
for country in countries:
    country_query = [FilterOption("string", "equal", "country", country, None)]
    sunny_day_counts[country] = len(filter(autumn_rows, country_query))


x = list(range(6))

fig, ax = plt.subplots(layout='constrained')


for i, country in enumerate(countries):
    ax.bar(i, sunny_day_counts[country], label=country)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Sunny/Clear Days')
ax.set_xlabel('Country')
ax.set_title('Sunny days per region')

ax.set_xticks(x)
ax.set_xticklabels(countries)


plt.legend()
plt.show()
