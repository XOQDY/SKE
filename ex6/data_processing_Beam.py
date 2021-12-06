import csv

# open Cities.csv file with csv.DictReader and read its content into a list of dictionary, cities_data
cities_data = []
with open('Cities.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities_data.append(r)

# open Countries.csv file with csv.DictReader and read its content into a list of dictionary, countries_data
countries_data = []
with open('Countries.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries_data.append(r)


def min_max_temp(cities_data):
    """Returns a list whose first and second elements are the min and the max temperatures of all the
    cities in cities_data.
    """
    temps = []
    for r in cities_data:
        temps.append(float(r['temperature']))
    return [min(temps), max(temps)]


def country_list(cities_data):
    """Returns a list of all the countries represented in cities_data.
    """
    countries = []
    for r in cities_data:
        if r['country'] not in countries:
            countries.append(r['country'])
    return countries


# ADD
def city_list(cities_data):
    city = []
    for i in cities_data:
        if i["city"] not in city:
            city.append(i["city"])
    return city


def latitude_list(cities_data):
    latitude = []
    for i in cities_data:
        if i["latitude"] not in latitude:
            latitude.append(i["latitude"])
    return latitude


# ADD


def average_country_temp(cities_data):
    """
    Return a dictionary whose key:value pair is country name:its average temp. The size of the
    returned dictionary must equal the number of countries represented.
    """
    d = dict()
    for country in country_list(cities_data):
        t = []
        for r in cities_data:
            if r['country'] == country:
                t.append(float(r['temperature']))
        d[country] = sum(t) / len(t)
    return d


def country_max_diff_temperature(cities_data):
    """Returns a tuple with information about a country whose minimum and maximum city temperatures differ the most in
    the following format: (the country whose minimum and maximum city temperatures differ the most, min temperature
    , max temperature, max temperature - min temperature)
    """
    country = []
    max_min = []
    difference = []
    for i in range(len(cities_data)):
        value_country = []
        if cities_data[i]['country'] not in country:
            country.append(cities_data[i]['country'])
            for n in range(len(cities_data)):
                if cities_data[i]['country'] == cities_data[n]['country']:
                    value_country.append(float(cities_data[n]['temperature']))
            max_min.append([max(value_country), min(value_country)])
            difference.append(max(value_country) - min(value_country))

    position = difference.index(max(difference))
    result = (country_list(cities_data)[position], max_min[position][1], max_min[position][0], f'{max(difference):.2f}')
    return result


def northern_southern_most_cities(cities_data):
    """Returns a list of tuples with information about the northernmost and southernmost cities together with their
    associated countries in the following format: [(northernmost city, its country), (southernmost city, its country)]
    """
    latitude = []
    for i in cities_data:
        latitude.append(i["latitude"])
    city = []
    for i in cities_data:
        city.append(i["city"])
    country = []
    for i in cities_data:
        country.append(i["country"])

    northernmost = (city[latitude.index(max(latitude))], country[latitude.index(max(latitude))])
    southernmost = (city[latitude.index(min(latitude))], country[latitude.index(min(latitude))])
    return [northernmost, southernmost], min(latitude), max(latitude)


def population_countries_no_coastline_in_EU(countries_data):
    """Returns a dictionary whose keys are countries in EU but do not have coastline; the value associated with each
    key is the population of that country
    """
    country_population = {}
    for i in range(len(countries_data)):
        if countries_data[i]['EU'] == 'yes' and countries_data[i]['coastline'] == 'no':
            country_population.update({countries_data[i]['country']: countries_data[i]['population']})
    return country_population


def cities_in_EU(cities_data, countries_data):
    """Returns a dictionary whose key:value pair is "name of city":"EU membership", e.g., "Graz":"yes" or 'Aalborg':'no'
    ; the size of the dictionary must equal the number of cities represented in cities_data
    """
    # Hint:
    # Use nested for in loops to generate the dictionary:
    #
    city_eu = {}
    for city in range(len(cities_data)):
        for country in range(len(countries_data)):
            if cities_data[city]['country'] == countries_data[country]['country']:
                city_eu.update({cities_data[city]['city']: countries_data[country]['EU']})
    return city_eu


def average_EU_city_temperature(cities_data, countries_data):
    """Returns a tuple with two elements: (the average temperature of all the cities in EU countries, the average
    temperature of all the cities not in EU countries)
    """
    eu = []
    neu = []
    for city in cities_data:
        for country in countries_data:
            if city['country'] == country['country']:
                if country['EU'] == "yes":
                    eu.append(float(city['temperature']))
                if country['EU'] == "no":
                    neu.append(float(city['temperature']))

    ave_eu = sum(eu) / len(eu)
    ave_neu = sum(neu) / len(neu)
    result = (ave_eu, ave_neu)
    return result


# open Players.csv file with csv.DictReader and read its content into a list of dictionary, players_data
players_data = []
with open('Players.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        players_data.append(r)

# open Teams.csv file with csv.DictReader and read its content into a list of dictionary, teams_data
teams_data = []
with open('Teams.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        teams_data.append(r)


def average_passes(players_data):
    """Returns a tuple with four elements; the first, second, third, and fourth elements show the average number of
    passes made by defenders, midfielders, forwards, and goalkeepers, respectively
    """
    defend = []
    mid = []
    forward = []
    goal = []
    for row in players_data:
        if row['position'] == 'defender':
            defend.append(int(row['passes']))
        if row['position'] == 'midfielder':
            mid.append(int(row['passes']))
        if row['position'] == 'forward':
            forward.append(int(row['passes']))
        if row['position'] == 'goalkeeper':
            goal.append(int(row['passes']))

    result = (sum(defend) / len(defend), sum(mid) / len(mid), sum(forward) / len(forward), sum(goal) / len(goal))
    return result


def max_GF_GA_ratio(teams_data):
    """Returns the string name of a team with highest ratio of goalsFor to goalsAgainst
    """
    ratio = []
    for row in teams_data:
        rat = float(row['goalsFor']) / float(row['goalsAgainst'])
        ratio.append(rat)
    return teams_data[ratio.index(max(ratio))]['team']


def whose_player_list(players_data, teams_data):
    """Returns a list of tuples; each tuple has information about a player who is on a team ranked in the top 20
    , plays less than 200 minutes and makes more than 100 passes; the format for each tuple is
    (player's surname, team played for, team ranking, minutes played, number of passes)
    """
    # Reminder: Convert minutes and passes to integers before comparing to values
    ranking_20 = []
    for i in range(20):
        ranking_20.append(teams_data[i]['team'])
    whose = []
    for row in players_data:
        if row['team'] in ranking_20 and int(row['minutes']) < 200 and int(row['passes']) > 100:
            who = (row['surname'], row['team'], ranking_20.index(row['team']) + 1, row['minutes'], row['passes'])
            whose.append(who)
    return whose


def team_list_passes_per_minute(players_data, teams_data):
    """Returns a list of tuples; each tuple has information about a team and its passes per minute value generated
    by its players
    """
    result = []
    for team in teams_data:
        sum_p = []
        p_per_m = 1
        for player in players_data:
            if player['team'] == team['team']:
                sum_p.append(float(player['passes']))
            minute = int(team['games']) * 90
            p_per_m = sum(sum_p) / minute
        information = (team['team'], f'{p_per_m:.2f}')
        result.append(information)
    return result


# open Titanic.csv file with csv.DictReader and read its content into a list of dictionary, titanic_data
titanic_data = []
with open('Titanic.csv') as f:
    rows = csv.DictReader(f)
    for r in rows:
        titanic_data.append(r)


def number_married_women_embarked(place_embarked, age_threshold, titanic_data):
    """Returns the number of married women over age_threshold embarked at place_embarked

    Your test code must include at least five test cases with different combinations of place_embarked and age_threshold
    """
    marry = []
    for i in range(len(titanic_data)):
        if titanic_data[i]['embarked'] == place_embarked:
            if titanic_data[i]['age'] != '':
                if float(titanic_data[i]['age']) > age_threshold:
                    if 'Mrs' in titanic_data[i]['first']:
                        marry.append(titanic_data[i]['first'])
    return len(marry)


def class_survival_rate(passenger_class, titanic_data):
    """Returns the survival rate of a given passenger_class

    Your test case must test all the three passenger classes
    """
    live, passenger = 0, 0
    for i in range(len(titanic_data)):
        if int(titanic_data[i]['class']) == passenger_class:
            passenger += 1
            if titanic_data[i]['survived'] == 'yes':
                live += 1

    return live / passenger


def gender_survival_number(passenger_gender, titanic_data):
    """Returns the number of survivors for a given gender, M (male) or F (female)

    Your test case must test both genders
    """
    number = 0
    for i in titanic_data:
        if i['survived'] == 'yes':
            if passenger_gender == i['gender']:
                number += 1
    return number


def twin_list(titanic_data):
    """Returns a list of tuples of pairs of passengers who are likely to be twin children, i.e., same last name
    , same age, same place of embarkment, and age is under 18
    ; each tuple has the following format: (person1's "last name" + "first name", person2's "last name" + "first name")
    """
    result = []
    for i in range(len(titanic_data)):
        for n in range(len(titanic_data)):
            if titanic_data[i]['last'] == titanic_data[n]['last']:
                if titanic_data[i]['age'] != '' and float(titanic_data[i]['age']) < 18:
                    if titanic_data[i]['age'] == titanic_data[i + 1]['age']:
                        if titanic_data[i]['embarked'] == titanic_data[n]['embarked']:
                            twin = f"{titanic_data[i]['last']} {titanic_data[i]['first']}"
                            twin2 = f"{titanic_data[i + 1]['last']} {titanic_data[i + 1]['first']}"
                            result.append((twin, twin2))
                            break
    return result
