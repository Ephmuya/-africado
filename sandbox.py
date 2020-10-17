import os
import pandas as pd
import json

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
fields = ROOT_DIR + '/list.json'
major_fields = ROOT_DIR + '/major.json'
minor_fields = ROOT_DIR + '/minor.json'
complience_data = ROOT_DIR + '/complience.csv'

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

    def read_complience_records(self):
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

        complience_records = df[availColumns].to_json("Icomplience_records.json", orient="records")

        return complience_records


test = create_report(minor_fields,complience_data)
complience_test_output = test.read_complience_records()
cc = json.dumps(complience_test_output)
print(cc)

