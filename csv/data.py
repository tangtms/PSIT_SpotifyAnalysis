import csv
# with open('regional-th-weekly-latest_1.csv', newline='') as csvfile:
    # spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    # for row in spamreader:
        # print(', '.join(row))
data_dict = {}
def check():
    with open('regional-th-weekly-latest_1.csv', encoding="utf-8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        num = 0
        for i in readCSV:
            #next(readCSV, None) #Skip header
            if i[1].lower not in data_dict:
                data_dict[i[1]] = [int(i[3]), i[2]]
            else:
                data_dict[i[1]] = [data_dict[i[1]][3]+int(i[3]), data_dict[i[1]][2]]
            #if row[1].lower() in txt.lower():
            #    return row[0]
        #return None
    print(data_dict)
check()