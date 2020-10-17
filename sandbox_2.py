import requests
import json

def compleince(url, yes_score , no_socre , na_socre ,type_of_score):

    major = requests.get(url=url)
    data = major.json()
    length = len(data)
    for i in range(length):
        for ii in data[i]:
            if data[i][ii] == 'yes':
                data[i][ii] = yes_score
            if data[i][ii] == 'no':
                data[i][ii] = no_socre
            elif data[i][ii] == None:
                pass
            elif data[i][ii] == 'na':
                data[i][ii] = na_socre

    complience = []
    for i in range(length):
        sum = 0;
        owner = data[i]['g2/prdcr_nm']
        for ii in data[i]:
            if type(data[i][ii]) == int:
                sum = sum + data[i][ii]
        score = sum / len(data[i])
        complience.append( {'name': owner, type_of_score: score } )


    return list(complience)


def merge_lists():
    Mm = compleince(url='http://127.0.0.1:5000/type/major', na_socre=100, yes_score=100, no_socre=0, type_of_score='major')
    mm = compleince(url='http://127.0.0.1:5000/type/minor', na_socre=50, yes_score=95, no_socre=75, type_of_score='minor')

    for iii in range(len(mm)):
       complience_score = (115 - mm[iii]['minor']) * 0.05
       cScore = {'Minor Must control points': complience_score}
       mm[iii].update(cScore)

    value_to_compare = ["name"]

    for i, elem in enumerate(Mm):
        mm_dict = mm[i]
        for key in value_to_compare:
            try:
                mm_dict.update({"major":Mm[i]['major']})
            except KeyError:
                print("key {} not found".format(key))
                # may be a raise here.
            except:
                raise
    return mm
merge_lists()