"""
PSIT - music analysis
turn year csv into dict
"""
import csv

data_dict_year = {}
def check():
    with open('./convert/year/regional-th-year-2017-2018.csv', encoding="utf-8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        num = 0
        for i in readCSV:
            if i[1].lower not in data_dict:
                data_dict[i[1]] = [int(i[3]), i[2]]
            else:
                data_dict[i[1]] = [data_dict[i[1]][3]+int(i[3]), data_dict[i[1]][2]]
    print(data_dict_year)
check()