"""
PSIT - music analysis
turn month csv into dict
"""
import csv

data_dict_month = {}
def check():
    with open('./convert/monthy/regional-th-monthly-2017-09.csv', encoding="utf-8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        num = 0
        for i in readCSV:
            if i[1].lower not in data_dict:
                data_dict[i[1]] = [int(i[3]), i[2]]
            else:
                data_dict[i[1]] = [data_dict[i[1]][3]+int(i[3]), data_dict[i[1]][2]]
    f = open('./visualize/dict_file/dict_month_2017_09', "w")
    f.write(data_dict_month)
check()