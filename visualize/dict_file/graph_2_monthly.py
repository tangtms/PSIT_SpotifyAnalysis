import dict_month as m

def main():
    list_all_month = [m._1, m._2, m._3, m._4, m._5, m._6, m._7, m._8, m._9, m._10, m._11, m._12, m._13]
    all_month = []
    for i in list_all_month:
        all_month.append(sum_month(i))
    print("RESULT #2")
    print(all_month)
def sum_month(data):
    count = 0
    for i in data:
        count += data[i][0]
    return count
main()
