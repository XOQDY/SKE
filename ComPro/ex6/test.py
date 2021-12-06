   temps_min_max = dict()
    temps_differ = dict()
    max_city = 0
    min_city = 0
    for r in country_list(cities_data):
        t = []
        for x in cities_data:
            if r == x['country']:
                t.append(float(x['temperature']))
        temps_min_max[r] = min(t), max(t)
        temps_differ[r] = max(t) - min(t)
    print(temps_differ)
    for x in country_list(cities_data):
        if temps_differ[x] == max(temps_differ.values()):
            for y in cities_data:
                if temps_min_max[x][0] == float(y['temperature']):
                    max_city = y['city']
            for i in cities_data:
                if temps_min_max[x][1] == float(i['temperature']):
                    min_city = i['city']
            return min_city, max_city, temps_min_max[x][0], temps_min_max[x][1], temps_differ[x]
print(country_max_diff_temperature(cities_data))
