from csv_reader import CsvReader
from filter import FilterOption, filter
from tools import get_column_mean
import matplotlib.pyplot as plt

data = CsvReader('nordics_weather.csv')

norway_query = [
    FilterOption("string", "equal", "country", "Norway", None),
]

norway_winter_only_query = [
    FilterOption("string", "equal", "country", "Norway", None),
    FilterOption("date", 'during', 'date', (12, 2), '%m/%d/%Y')
]

norway_rows = filter(data.rows, norway_query)
norway_yearly_rows = []
yearly_average_temps = []
yearly_average_mins = []

norway_winter_rows = filter(data.rows, norway_winter_only_query)
norway_yearly_winter_rows = []
yearly_winter_average_temps = []
yearly_winter_average_mins = []


# separate data into yearly lists
for year in range(2015, 2020):
    this_year_query = [
        FilterOption("date", "after", "date", f'1/1/{year}', '%m/%d/%Y'),
        FilterOption("date", "before", "date", f'12/31/{year}', '%m/%d/%Y'),
    ]

    this_year_general_rows = filter(norway_rows, this_year_query)
    norway_yearly_rows.append(this_year_general_rows)

    this_year_winter_rows = filter(norway_winter_rows, this_year_query)

    norway_yearly_winter_rows.append(this_year_winter_rows)


for year_rows in norway_yearly_rows:
    this_year_average_temp = get_column_mean(year_rows, "tavg")
    yearly_average_temps.append(this_year_average_temp)

    this_year_average_min = get_column_mean(year_rows, "tmin")
    yearly_average_mins.append(this_year_average_min)

for year_rows in norway_yearly_winter_rows:
    this_winter_average_temp = get_column_mean(year_rows, "tavg")
    yearly_winter_average_temps.append(this_winter_average_temp)

    this_winter_average_min = get_column_mean(year_rows, "tmin")
    yearly_winter_average_mins.append(this_winter_average_min)


x = list(range(5))  # Generating x-values from 1 to 4
width = 0.2  # width of the bars


fig, ax = plt.subplots(layout='constrained')


# Plotting each dataset separately but side by side
for i, data in enumerate([yearly_average_temps, yearly_average_mins, yearly_winter_average_temps, yearly_winter_average_mins]):
    offset = width * i
    ax.bar([val + offset for val in x], data,
           width=width, label=f"Dataset {i+1}")


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Temperature (Celsius)')
ax.set_xlabel('Year')
ax.set_title('Change in average temperatures over the years')
ax.set_ylim(-7, 6)

ax.set_xticks([val + width for val in x])
ax.set_xticklabels(list(range(2015, 2020)))


plt.legend(["Yearly Average", "Yearly Min", "Winter Average", "Winter Min"])
plt.show()
