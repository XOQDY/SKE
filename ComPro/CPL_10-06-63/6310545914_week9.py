import csv
import matplotlib.pyplot as plt
cities_data = []
city_temp_tuple = []
with open('cities.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities_data.append(r)


# Question 2
for row in cities_data:
    city_temp_tuple.append((row['city'], float(row['temperature'])))
print(city_temp_tuple)


# Question 3
def list_countries(cities_data):
    city = []
    for row in cities_data:
        if row['country'] not in city:
            city.append(row['country'])
    return city


countries = list_countries(cities_data)
print(len(countries))
print(countries)


# Question 4
def compute_avg_country_temp(cities_data):
    country_temp = dict()
    countries = list_countries(cities_data)
    for x in countries:
        temp = []
        for row in cities_data:
            if row['country'] == x:
                temp.append(float(row['temperature']))
        avg = sum(temp) / len(temp)
        country_temp[x] = avg
    return country_temp


compute_temps = compute_avg_country_temp(cities_data)
print(len(compute_temps))
print(compute_temps)


# Question 5
def read_file(filename):
    with open(filename, "r") as f:
        cities_data = []
        rows = csv.DictReader(f)
        for r in rows:
            cities_data.append(r)
    return cities_data


def extract_to_list(cities_data, data):
    extracted_list = [float(cities_data[i][data]) for i in range(len(cities_data))]
    return extracted_list


cities_data = read_file("cities.csv")
lat = extract_to_list(cities_data, 'latitude')
long = extract_to_list(cities_data, 'longitude')
temps = extract_to_list(cities_data, 'temperature')
high = extract_to_list(cities_data, 'highest')
# Plot scatter plot using x = latitude,
# y = temperature,
# color=longitude
plt.scatter(lat, temps, c=long)
# Add x-axis label
plt.xlabel('Latitude')
# Add y-axis label
plt.ylabel('Temperatures')
# Add label for color bar
plt.colorbar().ax.set_title('Longitude')
# Save plot as image file
plt.savefig('lat_temps_long.png')
# Show plot
plt.show()
plt.scatter(long, temps, c=lat)
plt.xlabel('Longitude')
plt.ylabel('Temperatures')
plt.colorbar().ax.set_title('Latitude')
# Set colormap to the selected one
# See more colormap selection in the reference at the end of Exercise 5
plt.set_cmap('PiYG')
plt.savefig('long_temps_lat.png')
plt.show()


# Question 6
def count_region_freq(cities_data):
    region_frequency = []
    region = []
    for x in range(len(cities_data)):
        if cities_data[x]['region'] not in region:
            region.append(cities_data[x]['region'])
    region_list = [cities_data[x]['region'] for x in range(len(cities_data))]
    for i in region:
        each_region_freq = 0
        for j in range(len(region_list)):
            if i == region_list[j]:
                each_region_freq += 1
        region_frequency.append(each_region_freq)
    return region, region_frequency


region_list, region_freq_list = count_region_freq(cities_data)
# Set up bar colors in bar graph
# See more color names in the reference at the end of Exercise 6
my_colors = ['red','blue','green','orange']
# Plot bar graph using x = unique region list
# y = region frequency
# Bar graph color is set to my_colors list
plt.bar(region_list, region_freq_list, color=my_colors)
plt.xlabel('Region')
plt.ylabel('Frequency')
plt.savefig('region_freq.png')
plt.show()


# Question 7
def find_lowest_highest_avg_city_temp(cities_data):
    avg_temp = compute_avg_country_temp(cities_data)
    avg_max = max(avg_temp.values())
    avg_min = min(avg_temp.values())
    list_max_min = []
    for x in avg_temp.keys():
        if avg_min == avg_temp[x]:
            list_max_min.append(x)
    for x in avg_temp.keys():
        if avg_max == avg_temp[x]:
            list_max_min.append(x)
    return list_max_min


print(find_lowest_highest_avg_city_temp(cities_data[:11]))
print(find_lowest_highest_avg_city_temp(cities_data[-10:]))
print(find_lowest_highest_avg_city_temp(cities_data))


# Question 8
def compute_ave_region_highest(cities):
    region = []
    ave_highest_list = []
    for i in range(len(cities)):
        if cities[i]['region'] not in region:
            region.append(cities[i]['region'])
    region_list = [cities_data[i]['region'] for i in range(len(cities))]
    highest = extract_to_list(cities, 'highest')
    for i in region:
        region_sum = []
        for j in range(len(region_list)):
            if i == region_list[j]:
                region_sum.append(int(highest[j]))
        ave_highest_list.append(sum(region_sum) / len(region_sum))
    return region, ave_highest_list

region_list, ave_highest_list = compute_ave_region_highest(cities_data)
# Set up bar colors in bar graph
# See more color names in the reference at the end of Exercise 6
my_colors = ['gold', 'peru', 'violet', 'skyblue']
# Plot bar graph using x = unique region list
# y = region frequency
# Bar graph color is set to my_colors list
plt.bar(region_list, ave_highest_list, color=my_colors)
plt.xlabel('Region')
plt.ylabel('Average Highest')
plt.savefig('region_freq2.png')
plt.show()
