from langdetect import detect
import json
import dict_year
def th_national(data):
    lang_dict = dict()
    th = 0
    inter = 0
    for i in data:
        try:
            lang = detect(str(i))
            th += 1 if lang == "th" else 0
            inter += 1 if lang != "th" else 0
        except:
            continue
        # if lang not in lang_dict:
            # lang_dict[lang] = 1
        # else: lang_dict[lang] += 1
    th = (th/inter)*100
    inter = abs(th-100)
    print("RESULT #1")
    print("th %.3f" %th)
    print("inter %.3f" %inter)
th_national(dict_year._year)
