from langdetect import detect
import json
import dict_month
def th_national_month(dic):
    lang_dict = dict()
    th = 0
    inter = 0
    for i in dic:
        try:
            lang = detect(str(i))
            if lang == "th":
                th += 1
            else:
                inter += 1
            #th += 1 if lang == "th" else 0
            #inter += 1 if lang != "th" else 0
        except:
            continue

    #th = (th/inter)*100
    #inter = abs(th-100)
    print("TH = %i\nInter = %i" %(th, inter))
th_national_month(dict_month._1)
th_national_month(dict_month._2)
th_national_month(dict_month._3)
th_national_month(dict_month._4)
th_national_month(dict_month._5)
th_national_month(dict_month._1)
