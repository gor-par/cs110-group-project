from csv_reader import CsvReader
from filter import FilterOption, filter
import matplotlib.pyplot as plt

data = CsvReader('nordics_weather.csv')
year_range = range(2015, 2020)


negative_query = [
    FilterOption("number", "smaller", "tavg", 0, None),
    FilterOption("string", "equal", "country", "Norway", None),
]

negative_rows = filter(data.rows, negative_query)

yearly_negative_counts = []
yearly_spring_negative_counts = []
yearly_fall_negative_counts = []

for year in year_range:
    this_year_query = [
        FilterOption("date", "after", "date",
                     f'12/31/{year-1}', '%m/%d/%Y'),
        FilterOption("date", "before", "date",
                     f'01/01/{year+1}', '%m/%d/%Y'),
    ]

    this_year_rows = filter(negative_rows, this_year_query)

    yearly_negative_counts.append(len(this_year_rows))

    this_spring_query = [
        FilterOption("date", "during", "date", (3, 5), '%m/%d/%Y'),
    ]

    this_spring_rows = filter(this_year_rows, this_spring_query)

    yearly_spring_negative_counts.append(len(this_spring_rows))

    this_fall_query = [
        FilterOption("date", "during", "date", (9, 11), '%m/%d/%Y'),
    ]

    this_fall_rows = filter(this_year_rows, this_fall_query)

    yearly_fall_negative_counts.append(len(this_fall_rows))


x = list(range(5))  # Generating x-values from 0 to 4
width = 0.2  # width of the bars


fig, ax = plt.subplots(layout='constrained')


# Plotting each dataset separately but side by side
for i, data in enumerate([yearly_negative_counts, yearly_spring_negative_counts, yearly_fall_negative_counts]):
    offset = width * i
    ax.bar([val + offset for val in x], data,
           width=width, label=f"Dataset {i+1}")


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Temperature (Celsius)')
ax.set_xlabel('Year')
ax.set_title('Change in average temperatures over the years')
ax.set_ylim(0, 200)

ax.set_xticks([val + width for val in x])
ax.set_xticklabels(list(range(2015, 2020)))


plt.legend(["Year", "Spring", "Fall"])
plt.show()
