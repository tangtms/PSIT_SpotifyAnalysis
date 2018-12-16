import dict_month
def artist_of_month(data):
    artist_month = {}
    for i in data.keys():
        if data[i][1] not in artist_month:
            artist_month[data[i][1]] = data[i][0]
        else:
            artist_month[data[i][1]] += data[i][0]
    sort_artist_month = [v[0] for v in sorted(artist_month.items(), key=lambda i: (-i[1], i[0]))]
    print(sort_artist_month[0], artist_month[sort_artist_month[0]])

artist_of_month(dict_month._1)
artist_of_month(dict_month._2)
artist_of_month(dict_month._3)
artist_of_month(dict_month._4)
artist_of_month(dict_month._5)
artist_of_month(dict_month._6)
artist_of_month(dict_month._7)
artist_of_month(dict_month._8)
artist_of_month(dict_month._9)
artist_of_month(dict_month._10)
artist_of_month(dict_month._11)
artist_of_month(dict_month._12)
