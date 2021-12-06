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
        d[country] = sum(t)/len(t)
    return d


def country_max_diff_temperature(cities_data):
    """Returns a tuple with information about a country whose minimum and maximum city temperatures differ the most in
    the following format: (the country whose minimum and maximum city temperatures differ the most, min temperature,
    max temperature, max temperature - min temperature)
    """
    temps_min_max = dict()
    temps_differ = dict()
    for r in country_list(cities_data):
        t = []
        for x in cities_data:
            if r == x['country']:
                t.append(float(x['temperature']))
        temps_min_max[r] = min(t), max(t)
        temps_differ[r] = max(t) - min(t)
    for x in country_list(cities_data):
        if temps_differ[x] == max(temps_differ.values()):
            return x, temps_min_max[x][0], temps_min_max[x][1], temps_differ[x]


def northern_southern_most_cities(cities_data):
    """Returns a list of tuples with information about the northernmost and southernmost cities together with their
    associated countries in the following format: [(northernmost city, its country), (southernmost city, its country)]
    """
    longitude = []
    d = []
    for r in cities_data:
        longitude.append(float(r['longitude']))
    for h in cities_data:
        if float(h['longitude']) == max(longitude):
            d.append(('northernmost city', h['country']))
    for k in cities_data:
        if float(k['longitude']) == min(longitude):
            d.append(('southernmost city', k['country']))
    return d


def population_countries_no_coastline_in_EU(countries_data):
    """Returns a dictionary whose keys are countries in EU but do not have coastline; the value associated with each
    key is the population of that country
    """
    d = dict()
    for r in countries_data:
        if r['EU'] == 'yes' and r['coastline'] == 'no':
            d[r['country']] = r['population']
    return d


def cities_in_EU(cities_data, countries_data):
    """Returns a dictionary whose key:value pair is "name of city":"EU membership", e.g., "Graz":"yes"
    or 'Aalborg':'no'; the size of the dictionary must equal the number of cities represented in cities_data
    """
    # Hint:
    # Use nested for in loops to generate the dictionary:
    #
    d = dict()
    same_city = []
    check_city = []
    for r in cities_data:
        if r['city'] not in check_city:
            check_city.append(r['city'])
        elif r['city'] in check_city:
            same_city.append(r['city'])
    for city in cities_data:
        for country in countries_data:
            if city['country'] == country['country']:
                if city['city'] in same_city:
                    d[city['city'] + '_' + city['country']] = country['EU']
                else:
                    d[city['city']] = country['EU']
                check_city.append(city['city'])
    return d


def average_EU_city_temperature(cities_data, countries_data):
    """Returns a tuple with two elements: (the average temperature of all the cities in EU countries, the average
    temperature of all the cities not in EU countries)
    """
    temps_in_eu = []
    temps_not_in_eu = []
    for r in cities_data:
        for i in countries_data:
            if r['country'] == i['country']:
                if i['EU'] == 'yes':
                    temps_in_eu.append(float(r['temperature']))
                elif i['EU'] == 'no':
                    temps_not_in_eu.append(float(r['temperature']))
    avg_in_eu = sum(temps_in_eu) / len(temps_in_eu)
    avg_not_in_eu = sum(temps_not_in_eu) / len(temps_not_in_eu)
    return avg_in_eu, avg_not_in_eu


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
    defenders = []
    midfielders = []
    forwards = []
    goalkeepers = []
    for r in players_data:
        if r['position'] == 'defender':
            defenders.append(int(r['passes']))
        elif r['position'] == 'midfielder':
            midfielders.append(int(r['passes']))
        elif r['position'] == 'forward':
            forwards.append(int(r['passes']))
        elif r['position'] == 'goalkeeper':
            goalkeepers.append(int(r['passes']))
    avg_d = sum(defenders) / len(defenders)
    avg_m = sum(midfielders) / len(midfielders)
    avg_f = sum(forwards) / len(forwards)
    avg_g = sum(goalkeepers) / len(goalkeepers)
    return avg_d, avg_m, avg_f, avg_g


def max_GF_GA_ratio(teams_data):
    """Returns the string name of a team with highest ratio of goalsFor to goalsAgainst
    """
    d = dict()
    for r in teams_data:
        d[r['team']] = int(r['goalsFor']) / int(r['goalsAgainst'])
    for r in teams_data:
        if d[r['team']] == max(d.values()):
            return r['team']


def whose_player_list(players_data, teams_data):
    """Returns a list of tuples; each tuple has information about a player who is on a team ranked in the top 20, plays
    less than 200 minutes and makes more than 100 passes; the format for each tuple is
    (player's surname, team played for, team ranking, minutes played, number of passes)
    """

    # Reminder: Convert minutes and passes to integers before comparing to values
    ranking = dict()
    d = []
    for i in teams_data:
        ranking[i['team']] = i['ranking']
    for r in players_data:
        if int(ranking[r['team']]) <= 20 and int(r['minutes']) < 200 and int(r['passes']) > 100:
            information_player = r['surname'], r['team'], ranking[r['team']], r['minutes'], r['passes']
            d.append(information_player)
    return d


def team_list_passes_per_minute(players_data, teams_data):
    """Returns a list of tuples; each tuple has information about a team and its passes per minute value generated by
    its players
    """
    d = []
    for r in teams_data:
        passes = []
        for i in players_data:
            if r['team'] == i['team']:
                passes.append(int(i['passes']))
        play = int(r['games']) * 90
        information = r['team'], sum(passes) / play
        d.append(information)
    return d


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
    i = 0
    for r in titanic_data:
        if 'Mrs' in r['first'] and r['age'] != '' and r['embarked'] == place_embarked:
            if float(r['age']) > age_threshold:
                i += 1
    return i


def class_survival_rate(passenger_class, titanic_data):
    """Returns the survival rate of a given passenger_class

    Your test case must test all the three passenger classes
    """
    all = 0
    survived = 0
    for r in titanic_data:
        if int(r['class']) == passenger_class:
            all += 1
            if r['survived'] == 'yes':
                survived += 1
    return survived / all


def gender_survival_number(passenger_gender, titanic_data):
    """Returns the number of survivors for a given gender, M (male) or F (female)

    Your test case must test both genders
    """
    survived = 0
    for r in titanic_data:
        if r['gender'] == passenger_gender:
            if r['survived'] == 'yes':
                survived += 1
    return survived


def twin_list(titanic_data):
    """Returns a list of tuples of pairs of passengers who are likely to be twin children,
     i.e., same last name, same age, same place of embarkment, and age is under 18;
     each tuple has the following format: (person1's "last name" + "first name", person2's "last name" + "first name")
    """
    t = []
    check_last = []
    for r in titanic_data:
        for l in titanic_data:
            if r['last'] == l['last'] and r['first'] != l['first'] and r['age'] == l['age'] \
                    and r['embarked'] == l['embarked'] and r['age'] != '':
                if float(r['age']) < 18:
                    d = r['last'] + ' ' + r['first'], l['last'] + ' ' + l['first']
                    if r['last'] not in check_last:
                        t.append(d)
                        check_last.append(r['last'])
    return t
