import os
import pandas as pd
import json
import requests

class create_report:
    def __init__(self, list, data):
        self.list = list
        self.data = data

    def get_columns(self):
        with open(self.list) as _list:
            columns = _list.read()
            _columns = []
            for i in json.loads(columns):
                _columns.append(i)
            return _columns

    def read_complience_records(self,file):
        df = pd.read_csv(self.data, low_memory=False)
        availColumns = []
        # Looping through the filed columns to check them against the csv columns
        for i in self.get_columns():
            try:
                # Checking for a string in the csv columns that matches the string in the list.json doc
                result = [origColField for origColField in df.columns.tolist() if i in origColField]
                if (len(result) > 0):
                    # append the column to a new list
                    availColumns.append(result[0])
                else:
                    pass
            except ValueError as e:
                pass

        complience_records = df[availColumns].to_json(file+'.json', orient="records")
        data = './'+file+'.json'
        f = open(data, "r")
        c = json.loads(f.read())
        return c

# Complience Calculations
def compleince(url, yes_score , no_socre , na_socre ,null_socre,type_of_score):

    major = requests.get(url=url)
    data = major.json()
    length = len(data)
    for i in range(length):
        for ii in data[i]:
            if data[i][ii] == 'yes':
                data[i][ii] = yes_score
            elif data[i][ii] == 'no':
                data[i][ii] = no_socre
            elif data[i][ii] == 'na':
                data[i][ii] = na_socre
            elif data[i][ii] is None:
                data[i][ii] = null_socre

    complience = []

    for i in range(length):
        sum = 0;
        owner = data[i]['g2/prdcr_nm']
        for ii in data[i]:
            if type(data[i][ii]) == int:
                sum = sum + data[i][ii]
        #score = sum / len(data[i])

        complience.append( {'name': owner, type_of_score: sum } )

    return list(complience)


def merge_lists(base_url):
    Mm = compleince(url=base_url+'/type/major', na_socre=1, yes_score=1, no_socre=1,null_socre='_', type_of_score='major')
    mm = compleince(url=base_url+'/type/minor', na_socre=0, yes_score=1, no_socre=-1,null_socre='_', type_of_score='minor')
    """
    for iii in range(len(mm)):
       complience_score = round(((mm[iii]['minor']/115) * 100) , 0)
       cScore = {'Minor Must control points': complience_score}
       mm[iii].update(cScore)"""

    value_to_compare = ["name"]

    for i, elem in enumerate(Mm):
        mm_dict = mm[i]
        for key in value_to_compare:
            try:
               # mm_dict.update({"major":Mm[i]['major']})
                mm_dict.update({"major":100})
            except KeyError:
                print("key {} not found".format(key))
            except:
                raise
    return mm


