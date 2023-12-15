from csv_reader import CsvReader
from filter import FilterOption, filter
from tools import get_column_mean
from utils import fahr_to_cel
import matplotlib.pyplot as plt

date_format = "%Y-%m-%d"

data = CsvReader('stockholm.csv')


year_range = range(1997, 2023)

query = [
    FilterOption("date", "after", "DATE", '1996-12-31', date_format),
    FilterOption("date", "before", "DATE", '2023-01-01', date_format),
]


stockholm_rows = filter(data.rows, query)
yearly_rows = []
yearly_average_temps = []
yearly_average_mins = []


# # separate data into yearly lists
for year in year_range:
    this_year_query = [
        FilterOption("date", "after", "DATE", f'{year}-01-01', date_format),
        FilterOption("date", "before", "DATE", f'{year}-12-31', date_format),
    ]

    this_year_general_rows = filter(stockholm_rows, this_year_query)
    yearly_rows.append(this_year_general_rows)


for year_rows in yearly_rows:
    this_year_average_temp = get_column_mean(year_rows, "TMAX")
    yearly_average_temps.append(this_year_average_temp)

    this_year_average_min = get_column_mean(year_rows, "TMIN")
    yearly_average_mins.append(this_year_average_min)


plot_lists = [
    yearly_average_temps,
    yearly_average_mins,
]

x = range(20)
width = 0.2

fig, ax = plt.subplots(layout='constrained')


for i, this_list in enumerate(plot_lists):
    plot_lists[i] = [fahr_to_cel(element) for element in this_list]


ax.set_ylabel('Temperature (Celsius)')
ax.set_xlabel('Year')
ax.set_title('Change in average min and max temperatures over the years')

ax.set_ylim(-10, 70)
ax.set_xticks(range(1997, 2022, 3))


ax.plot(year_range, plot_lists[0], label="Yearly Max")
ax.plot(year_range, plot_lists[1], label="Yearly Min")


plt.legend()


ax.set_title('Climate Change')

plt.show()
