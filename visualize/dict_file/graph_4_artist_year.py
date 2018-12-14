import dict_year
def artist_year():
    all_steam = 247875921
    data = dict_year._year
    artist_year = {}
    for i in data.keys():
        if data[i][1] not in artist_year:
            artist_year[data[i][1]] =  data[i][0] #OGANIC:2000
        else:
            artist_year[data[i][1]] += data[i][0]
    sort_artist_year = [v[0] for v in sorted(artist_year.items(), key=lambda i: (-i[1], i[0]))]
    #1st artist
    #print(sort_artist_year[0], artist_year[sort_artist_year[0]])

    #for i in sort_artist_year:
    #        print(i, artist_year[i])
    count = 0
    for i in range(10):
        count += artist_year[sort_artist_year[i]]
        print(i+1, sort_artist_year[i], artist_year[sort_artist_year[i]], artist_year[sort_artist_year[i]]/all_steam*100)
    print(all_steam - count)
artist_year()
# ALL 247875921
# 1 The Toys 8534491 3.4430496377258044
# 2 Atom Chanakan 7194833 2.902594560606796
# 3 BTS 7148502 2.883903354210835
# 4 BLACKPINK 6810406 2.7475060798664668
# 5 Ed Sheeran 5794695 2.3377401792891375
# 6 Room 39 5389441 2.1742495109075155
# 7 Post Malone 4247444 1.7135363462754416
# 8 Charlie Puth 4206773 1.697128540371616
# 9 Lauv 3703832 1.4942282352629161
# 10 Lipta 3429268 1.3834615263012982