"""
PSIT - music analysis
turn month csv into dict
"""
import csv
import codecs

data_dict = {}
def check():
    with open('./convert/monthy/regional-th-monthly-2018-09.csv', encoding="utf-8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for i in readCSV:
            if i[1] not in data_dict:
                data_dict[i[1]] = [int(i[3]), i[2]]
            else:
                data_dict[i[1]] = [data_dict[i[1]][0]+int(i[3]), i[2]]
    f = codecs.open('./visualize/dict_file/dict_month.py', "a", "utf-8")
    f.write("\ndict_month_13 = "+ str(data_dict))
check()
