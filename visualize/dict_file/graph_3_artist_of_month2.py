import dict_month_2
def artist_of_month():
    data = dict_month_2.dict_month_2
    artist_month = {}
    for i in data.keys():
        if data[i][1] not in artist_month:
            artist_month[data[i][1]] = data[i][0]
        else:
            artist_month[data[i][1]] += data[i][0]
    sort_artist_month = [v[0] for v in sorted(artist_month.items(), key=lambda i: (-i[1], i[0]))]
    print(sort_artist_month[0], artist_month[sort_artist_month[0]])

artist_of_month()
