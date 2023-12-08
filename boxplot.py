import matplotlib.pyplot as plt
from csv_reader import CsvReader

dataset = CsvReader('GlobalWeatherRepository.csv')

plt.figure(figsize=(10, 6))
data = []
for row in dataset.rows:
    data.append(row.get("temperature_celsius"))
plt.boxplot(data)
plt.title("Boxplot of Average Monthly Temperature")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")

date = []
for row in dataset.rows:
    date.append(row.get("last_updated"))


plt.show()


plt.title("Boxplot of Average Monthly Temperature in Yerevan, Armenia (2023)")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.show()
