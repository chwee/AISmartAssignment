from flask import Flask
from flask import request
import json
import numpy as np
import ktrain
from ktrain import text
from datetime import datetime
import sqlite3

#Deep Learning BERT model
#the train model is stored in the folder .\\models\\bert_modelv1

#Data Logging
#the data for the transaction are logged in the Sqlite database predictrecords.db


app = Flask(__name__)
# load the predictor
predictor = ktrain.load_predictor(".\\models\\bert_modelv1")
logdata= True
verbose= True


@app.route("/test")
def test():
    return "server ok"

@app.route("/version")
def ver():
    return "Bert model version 1.0.0"


@app.route("/predict",  methods = ['POST'])
def predict():

    jsondata= request.get_json()
    # print(type(jsondata))
    # print(jsondata['query'])

    casetext = [jsondata['query']]
    # print(casetext[0])

    labels = ['normal', 'attention']
    prediction = predictor.predict(casetext, return_proba=True)
    pred_text = labels[np.argmax(prediction)]
    confidence = prediction[0][np.argmax(prediction)]
    dateTimeObj = datetime.now()
    # print(pred_text)
    # print(confidence)
    # print(str(dateTimeObj))

    if(logdata == True):
        with sqlite3.connect("predictrecords.db") as connection:

            cursor = connection.cursor()

            cursor.execute("insert into log(timelog,casedes,label,confid) values (?, ?, ?,?)",
                           (str(dateTimeObj), str(casetext[0]), str(pred_text), str(confidence)))

            connection.commit()

    # create JSON object
    output = {'prediction': str(pred_text), 'confidence': float(confidence)}

    if(verbose == True):
        print(str(dateTimeObj),'--', str(casetext[0]),'(' ,str(pred_text), ')', '(', str(confidence),')' )

    return json.dumps(output), 200, {'ContentType':'application/json'}

if __name__ == "__main__":
    app.run(host='0.0.0.0',threaded = True)
    # app.run()