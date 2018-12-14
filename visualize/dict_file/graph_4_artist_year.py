import dict_year
def artist_year():
    data = dict_year._year
    artist_year = {}
    for i in data.keys():
        if data[i][1] not in artist_year:
            artist_year[data[i][1]] =  data[i][0] #OGANIC:2000
        else:
            artist_year[data[i][1]] += data[i][0]
    sort_artist_year = [v[0] for v in sorted(artist_year.items(), key=lambda i: (-i[1], i[0]))]
    print(sort_artist_year[0], artist_year[sort_artist_year[0]])
    for i in sort_artist_year:
        print(i, artist_year[i])
artist_year()
# ALL 247875921
# The Toys 8534491
# Atom Chanakan 7194833
# BTS 7148502
# BLACKPINK 6810406
# Ed Sheeran 5794695
# Room 39 5389441
# Post Malone 4247444
# Charlie Puth 4206773
# Lauv 3703832
# Lipta 3429268