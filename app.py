from flask import Flask, request, render_template,jsonify,url_for
import pandas as pd
import json
import os
from complience import create_report , merge_lists
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
complience_data = ROOT_DIR + '/data/complience.csv'
#base = 'https://africado.herokuapp.com'
base = 'http://127.0.0.1:5000'
@app.route('/')
def dashboard():

    return render_template('dashboard.html')


@app.route('/type/<type>' , methods=['GET'])
# type = major or minor
def complience(type):
    fields = ROOT_DIR + '/data/'+type+'.json'
    major = create_report(fields,complience_data)
    data = major.read_complience_records(type)
    return jsonify(data)

@app.route('/type/score' , methods=['GET'])
def scores():
    complience   = merge_lists(base)
    return jsonify(complience)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        farmer_csv_data = request.files.get('file')
        with open('data/list.json') as _list:
            data = _list.read()
            _columns = []
            for i in json.loads(data):
                _columns.append(i)
            df = pd.read_csv(farmer_csv_data, low_memory=False)
            # drop unecessary columns
            df = df.drop(
                ['__version__', 'meta/instanceID', '_id', '_uuid', '_submission_time', '_index', '_parent_table_name',
                 '_parent_index', '_tags', '_notes'
                 ], axis=1)
            data_top = df.head()
            for i in data_top:
                try:
                    # remove '/
                    slash = i.index('/')
                    _purge = i.replace(i[:slash + 1], '')
                    df.rename(columns={i: _purge}, inplace=True)

                except ValueError as e:
                    pass
            _df_columns = []
            for i in df.columns:
                _df_columns.append(i)
            common = set(_columns).intersection(_df_columns)
            df_new = df[list(common)]
            df_new = df_new.to_json(orient='index')

        return json.dumps(df_new)
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)