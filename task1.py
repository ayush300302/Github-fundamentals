temperature = [28, 30, 29, 31, 32, 30, 29, 33, 31, 30]
humidity = [45, 50, 48, 52, 55, 53, 49, 47, 51, 50]

import statistics

avg_temp = sum(temperature) / len(temperature)
median_temp = statistics.median(temperature)

avg_humidity = sum(humidity) / len(humidity)
median_humidity = statistics.median(humidity)

print("Weather Analysis of Gandhinagar (Last 10 Days)\n")

print("Temperature Data:", temperature)
print("Average Temperature:", avg_temp)
print("Median Temperature:", median_temp)

print("\nHumidity Data:", humidity)
print("Average Humidity:", avg_humidity)
print("Median Humidity:", median_humidity)
