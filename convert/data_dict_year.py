"""
PSIT - music analysis
turn year csv into dict
"""
import csv
import codecs

data_dict = {}
def check():
    with open('./convert/year/regional-th-year-2017-2018.csv', encoding="utf-8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for i in readCSV:
            if i[1] not in data_dict:
                data_dict[i[1]] = [int(i[3]), i[2]]
            else:
                data_dict[i[1]] = [data_dict[i[1]][0]+int(i[3]), i[2]]
    f = codecs.open('./visualize/dict_file/dict_year.py', "w", "utf-8")
    f.write("\n_year = "+ str(data_dict))
check()
