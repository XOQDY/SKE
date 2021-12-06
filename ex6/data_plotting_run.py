import data_processing as dp
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
bars = [] # list of countries
temperature = [] # average temperature of each country
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
for country in dp.countries_data:
    if country['EU'] == 'yes':
        numEU += 1
    else:
        numNotEU += 1
plt.pie([numEU, numNotEU], labels=['EU', 'not EU'], autopct='%1.1f%%')
plt.show()

# Bar chart showing population of countries that are in EU but do not have coastline

# your code here
bars = []
population = []
dict = dp.population_countries_no_coastline_in_EU(dp.countries_data)
for key, value in dict.items():
    bars.append(key)
    population.append(float(value))

numbars = len(bars)
width = .75
plt.bar(range(numbars), population, width, align='center', color='firebrick')
plt.xlabel('countries')
plt.ylabel('population')
plt.xticks(range(numbars), bars, rotation='vertical')
print(bars)
print(population)
plt.show()

# Pie chart showing number of EU cities versus non-EU cities

# your code here
numEU = 0
numNotEU = 0
color = ['lime', 'deepskyblue']
for cities in dp.cities_in_EU(dp.cities_data, dp.countries_data).values():
    if cities == 'yes':
        numEU += 1
    else:
        numNotEU += 1
plt.pie([numEU, numNotEU], labels=['EU', 'not EU'], autopct='%1.1f%%', colors=color)
plt.show()

# Scatter plot of players showing minutes played versus passes made;
# color each player based on their position (goalkeeper, defender, midfielder, forward)

# your code here
g_x = []
g_y = []
d_x = []
d_y = []
m_x = []
m_y = []
f_x = []
f_y = []
for player in dp.players_data:
    if player['position'] == 'goalkeeper':
        g_x.append(float(player['minutes']))
        g_y.append(float(player['passes']))
    elif player['position'] == 'defender':
        d_x.append(float(player['minutes']))
        d_y.append(float(player['passes']))
    elif player['position'] == 'midfielder':
        m_x.append(float(player['minutes']))
        m_y.append(float(player['passes']))
    elif player['position'] == 'forward':
        f_x.append(float(player['minutes']))
        f_y.append(float(player['passes']))

plt.xlabel('minutes')
plt.ylabel('passes')
plt.scatter(g_x, g_y)
plt.scatter(d_x, d_y)
plt.scatter(m_x, m_y)
plt.scatter(f_x, f_y)
plt.show()

# Bar chart showing average number of passes made by each player position (defender, midfielder, forward, goalkeeper)

# your code here
bars = ['defender', 'midfielder', 'forward', 'goalkeeper']
passes = []
for i in dp.average_passes(dp.players_data):
    passes.append(i)

numbars = len(bars)
width = .75
plt.bar(range(numbars), passes, width, align='center', color='tan')
plt.xlabel('position')
plt.ylabel('passes')
plt.xticks(range(numbars), bars, rotation='vertical')
print(bars)
print(passes)
plt.show()

# Bar chart showing the survival rate in each passenger class;
# the three bars should be labeled 'first', 'second', 'third'

# your code here
bars = ['first', 'second', 'third']
survival_rate = []
for i in range(1, 4):
    survival_rate.append(dp.class_survival_rate(i, dp.titanic_data))

numbars = len(bars)
width = .75
plt.bar(range(numbars), survival_rate, width, align='center', color='violet')
plt.xlabel('passenger class')
plt.ylabel('survival rate')
plt.xticks(range(numbars), bars, rotation='vertical')
print(bars)
print(survival_rate)
plt.show()

# Pie chart showing the number of male survivors versus female survivors

# your code here
male = dp.gender_survival_number('M', dp.titanic_data)
female = dp.gender_survival_number('F', dp.titanic_data)
color = ['navy', 'crimson']
plt.pie([male, female], labels=['male', 'female'], autopct='%1.1f%%', colors=color)
plt.show()
