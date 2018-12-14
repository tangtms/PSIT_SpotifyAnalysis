import dict_month
month1 = dict_month.dict_month_1
count = 0
for i in month1.keys():
    count += month1[i][0]
print(count)