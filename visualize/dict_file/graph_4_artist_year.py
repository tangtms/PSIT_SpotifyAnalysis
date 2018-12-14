import dict_year
def artist_year():
    data = dict_year.dict_year
    artist_year = {}
    for i in data.keys():
        if data[i][1] not in artist_year:
            artist_year[data[i][1]] =  data[i][0] #OGANIC:2000
        else:
            artist_year[data[i][1]] += data[i][0]
    sort_artist_year = [v[0] for v in sorted(artist_year.items(), key=lambda i: (-i[1], i[0]))]
    print(sort_artist_year[0], artist_year[sort_artist_year[0]])
artist_year()
