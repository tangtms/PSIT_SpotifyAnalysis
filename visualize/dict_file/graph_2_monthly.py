import dict_month_1
import dict_month_2
import dict_month_3
import dict_month_4
import dict_month_5
import dict_month_6
import dict_month_7
import dict_month_8
import dict_month_9
import dict_month_10
import dict_month_11
import dict_month_12
import dict_month_13
month1 = dict_month_1.dict_month_1
month2 = dict_month_2.dict_month_2
month3 = dict_month_3.dict_month_3
month4 = dict_month_4.dict_month_4
month5 = dict_month_5.dict_month_5
month6 = dict_month_6.dict_month_6
month7 = dict_month_7.dict_month_7
month8 = dict_month_8.dict_month_8
month9 = dict_month_9.dict_month_9
month10 = dict_month_10.dict_month_10
month11 = dict_month_11.dict_month_11
month12 = dict_month_12.dict_month_12
month13 = dict_month_13.dict_month_13
def main():
    list_all_month = [month1, month2, month3, month4, month5, month6, month7, month8, month9, month10, month11, month12, month13]
    all_month = []
    for i in list_all_month:
        all_month.append(sum_month(i))
    print(all_month)
def sum_month(data):
    count = 0
    for i in data:
        count += data[i][0]
    return count
main()
