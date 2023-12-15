from csv_reader import CsvReader
from filter import FilterOption, filter
import matplotlib.pyplot as plt

date_format = "%Y-%m-%d"
data = CsvReader('stockholm.csv')
year_range = range(1997, 2023)

negative_query = [
    FilterOption("number", "smaller", "TMIN", 0, None),
]


negative_rows = filter(data.rows, negative_query)


yearly_negative_counts = []
yearly_spring_negative_counts = []
yearly_fall_negative_counts = []

for year in year_range:
    this_year_query = [
        FilterOption("date", "after", "DATE",
                     f'{year-1}-12-31', date_format),
        FilterOption("date", "before", "DATE",
                     f'{year+1}-01-01', date_format),
    ]

    this_year_rows = filter(negative_rows, this_year_query)

    yearly_negative_counts.append(len(this_year_rows))

    this_spring_query = [
        FilterOption("date", "during", "DATE", (3, 5), date_format),
    ]

    this_spring_rows = filter(this_year_rows, this_spring_query)

    yearly_spring_negative_counts.append(len(this_spring_rows))

    this_fall_query = [
        FilterOption("date", "during", "DATE", (9, 11), date_format),
    ]

    this_fall_rows = filter(this_year_rows, this_fall_query)

    yearly_fall_negative_counts.append(len(this_fall_rows))


# ]


# yerevan_rows = filter(data.rows, query)
# yearly_rows = []
# yearly_average_temps = []
# yearly_average_mins = []


# # # separate data into yearly lists
# for year in year_range:
#     this_year_query = [
#         FilterOption("date", "after", "DATE", f'{year}-01-01', date_format),
#         FilterOption("date", "before", "DATE", f'{year}-12-31', date_format),
#     ]

#     this_year_general_rows = filter(yerevan_rows, this_year_query)
#     yearly_rows.append(this_year_general_rows)


# for year_rows in yearly_rows:
#     this_year_average_temp = get_column_mean(year_rows, "TMAX")
#     yearly_average_temps.append(this_year_average_temp)

#     this_year_average_min = get_column_mean(year_rows, "TMIN")
#     yearly_average_mins.append(this_year_average_min)


# plot_lists = [
#     yearly_average_temps,
#     yearly_average_mins,
# ]

# x = range(20)
# width = 0.2

# fig, ax = plt.subplots(layout='constrained')


# for i, this_list in enumerate(plot_lists):
#     plot_lists[i] = [fahr_to_cel(element) for element in this_list]


# ax.set_ylabel('Temperature (Celsius)')
# ax.set_xlabel('Year')
# ax.set_title('Change in average temperatures over the years')

# ax.set_ylim(-10, 70)


# plt.legend()


# ax.set_title('Climate Change')

# plt.show()


x = list(range(26))  # Generating x-values from 0 to 4
width = 0.2  # width of the bars


fig, ax = plt.subplots(layout='constrained')


ax.plot(year_range, yearly_negative_counts, label="Year")
ax.plot(year_range, yearly_spring_negative_counts, label="Spring")
ax.plot(year_range, yearly_fall_negative_counts, label="Fall")


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of days')
ax.set_xlabel('Year')
ax.set_title('Change in cold day distribution')
# ax.set_ylim(0, 200)

ax.set_xticks(range(1997, 2022, 3))


plt.legend()
plt.show()
