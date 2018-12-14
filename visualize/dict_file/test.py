import dict_month
import dict_year
test = dict_year._year
count = 0
for i in test.keys():
    count += test[i][0]
print(count)