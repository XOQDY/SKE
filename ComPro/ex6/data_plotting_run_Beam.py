import data_processing_Beam as dp
import matplotlib.pyplot as plt

# Scatter plot of cities showing latitudes versus temperatures
x = []
y = []
for city in dp.cities_data:
    x.append(float(city['latitude']))
    y.append(float(city['temperature']))
plt.xlabel('latitude')
plt.ylabel('temperature')
plt.scatter(x, y)
plt.show()

# Bar chart showing average temperatures of all cities in each country
bars = []  # list of countries
temperature = []  # average temperature of each country
dict = dp.average_country_temp(dp.cities_data)
for key, value in dict.items():
    bars.append(key)
    temperature.append(value)

numbars = len(bars)
width = .75
plt.bar(range(numbars), temperature, width, align='center')
plt.xlabel('country')
plt.ylabel('temperature')
plt.xticks(range(numbars), bars, rotation='vertical')
print(bars)
print(temperature)
plt.show()

# Pie chart showing number of EU countries versus non-EU countries
numEU = 0
numNotEU = 0
my_colors = ['lightskyblue', 'steelblue']
for country in dp.countries_data:
    if country['EU'] == 'yes':
        numEU += 1
    else:
        numNotEU += 1
plt.pie([numEU, numNotEU], labels=['EU', 'not EU'], autopct='%1.1f%%', colors=my_colors)
plt.show()

# Bar chart showing population of countries that are in EU but do not have coastline

# your code here
country = []
population = []
chart_dict = dp.population_countries_no_coastline_in_EU(dp.countries_data)
for key, value in chart_dict.items():
    country.append(key)
    population.append(float(value))

plt.bar(country, population, color="pink")
plt.title("population of countries that are in EU but do not have coastline", fontsize="13")
plt.xlabel('Country', color="blue", fontsize="12")
plt.ylabel('Population', color="blue", fontsize="12")
plt.show()


# Pie chart showing number of EU cities versus non-EU cities

# your code here
eu_city = dp.cities_in_EU(dp.cities_data, dp.countries_data)
eu = 0
neu = 0
check_eu = []
my_colors = ['grey', 'silver']
for key, value in eu_city.items():
    check_eu.append(value)
for city in range(len(eu_city)):
    if check_eu[city] == 'yes':
        eu += 1
    if check_eu[city] == 'no':
        neu += 1
plt.pie([eu, neu], labels=['EU', 'not EU'], autopct='%1.1f%%', colors=my_colors)
plt.title("number of EU cities versus non-EU cities", fontsize="13")
plt.show()


# Scatter plot of players showing minutes played versus passes made;
# color each player based on their position (goalkeeper, defender, midfielder, forward)

# your code here
player_data = dp.players_data
goal_p, goal_min, defend_p, defend_min, mid_p, mid_min, forward_p, forward_min = [], [], [], [], [], [], [], []
role = ['goalkeeper', 'defender', 'midfielder', 'forward']
for i in range(len(player_data)):
    if player_data[i]['position'] == 'goalkeeper':
        goal_p.append(float(player_data[i]['passes']))
        goal_min.append(float(player_data[i]['minutes']))
    if player_data[i]['position'] == 'defender':
        defend_p.append(float(player_data[i]['passes']))
        defend_min.append(float(player_data[i]['minutes']))
    if player_data[i]['position'] == 'midfielder':
        mid_p.append(float(player_data[i]['passes']))
        mid_min.append(float(player_data[i]['minutes']))
    if player_data[i]['position'] == 'forward':
        forward_p.append(float(player_data[i]['passes']))
        forward_min.append(float(player_data[i]['minutes']))

plt.scatter(goal_p, goal_min, c='green', s=3)
plt.scatter(defend_p, defend_min, c='blue', s=3)
plt.scatter(mid_p, mid_min, c='violet', s=3)
plt.scatter(forward_p, forward_min, c='red', s=3)
plt.title("players showing minutes played versus passes made", fontsize="13")
plt.show()


# Bar chart showing average number of passes made by each player position (defender, midfielder, forward, goalkeeper)

# your code here
passes = dp.average_passes(player_data)
roles = ['defender', 'midfielder', 'forward', 'goalkeeper']
my_colors = ['thistle', 'violet', 'fuchsia', 'purple']
plt.bar(roles, passes, color=my_colors)
plt.title("average number of passes made by each player position", fontsize="13")
plt.show()


# Bar chart showing the survival rate in each passenger class; the three bars should be labeled 'first', 'second'
# , 'third'

# your code here
rate1 = dp.class_survival_rate(1, dp.titanic_data)
rate2 = dp.class_survival_rate(2, dp.titanic_data)
rate3 = dp.class_survival_rate(3, dp.titanic_data)
classes = ['first', 'second', 'third']
my_colors = ['lightcoral', 'brown', 'darkred']
plt.bar(classes, [rate1, rate2, rate3], color=my_colors)
plt.title("survival rate in each passenger class", fontsize="13")
plt.show()


# Pie chart showing the number of male survivors versus female survivors

# your code here
male = dp.gender_survival_number('M', dp.titanic_data)
female = dp.gender_survival_number('F', dp.titanic_data)
my_colors = ['seagreen', 'mediumseagreen']
plt.pie([male, female], labels=['male', 'female'], autopct='%1.1f%%', colors=my_colors)
plt.title("number of EU cities versus non-EU cities", fontsize="13")
plt.show()
