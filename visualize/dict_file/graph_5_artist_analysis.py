import dict_month
bts, thetoys, atom, blackpink, ed = [], [], [], [], []
def artist_analysis(data):
    artist = {}
    for i in data.keys():
        if data[i][1] not in artist:
            artist[data[i][1]] =  data[i][0] #OGANIC:2000
        else:
            artist[data[i][1]] += data[i][0]
    sort_artist = [v[0] for v in sorted(artist.items(), key=lambda i: (-i[1], i[0]))]
    #1st artist
    #print(sort_artist[0], artist[sort_artist[0]])

    #for i in sort_artist:
    #        print(i, artist[i])

    # print(artist["BTS"], "BTS") #, artist[sort_artist[i]]/all_steam*100)
    # print(artist["The Toys"], "The Toys")
    # print(artist["Atom Chanakan"], "Atom Chanakan")
    # print(artist["BLACKPINK"], "BLACKPINK")
    # print(artist["Ed Sheeran"], "Ed Sheeran")
    bts.append(artist["BTS"])
    thetoys.append(artist["The Toys"])
    atom.append(artist["Atom Chanakan"])
    blackpink.append(artist["BLACKPINK"])
    ed.append(artist["Ed Sheeran"])
print("RESULT #5")
artist_analysis(dict_month._1)
artist_analysis(dict_month._2)
artist_analysis(dict_month._3)
artist_analysis(dict_month._4)
artist_analysis(dict_month._5)
artist_analysis(dict_month._6)
artist_analysis(dict_month._7)
artist_analysis(dict_month._8)
artist_analysis(dict_month._9)
artist_analysis(dict_month._10)
artist_analysis(dict_month._11)
artist_analysis(dict_month._12)
artist_analysis(dict_month._13)

print(thetoys, atom, bts, blackpink, ed, sep="\n")
# [148038, 158252, 173662, 317829, 286394, 947799, 930720, 845147, 760934, 820052, 488381, 268830, 482292]
# [122923, 104711, 223600, 685558, 662199, 691500, 927766, 688289, 705334, 748211, 639281, 746774, 248687]
# [1015354, 749997, 277442, 501618, 225552, 155189, 152074, 191116, 870979, 1250168, 475615, 1228445, 54953]
# [158709, 140166, 88574, 165420, 151859, 177101, 148703, 55268, 59603, 1523603, 1860023, 1967870, 313507]
# [337860, 467910, 623141, 1003178, 681125, 514297, 461016, 341300, 394812, 404430, 306635, 376767, 78227]