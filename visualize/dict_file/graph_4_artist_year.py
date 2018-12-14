import dict_year
def artist_year():
    data = dict_year.dict_year
    artist_year = {}
    for i in data.keys():
        if data[i][1] not in artist_year:
            artist_year[data[i][1]] =  data[i][0] #OGANIC:2000
        else:
            artist_year[data[i][1]] += data[i][0]

    print(len(data))
artist_year()
