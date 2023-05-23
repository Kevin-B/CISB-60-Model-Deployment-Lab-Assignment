from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os, sys
# get current working path for current directory and change it to the right format regardless of os
curr_path = os.path.dirname(os.path.abspath(sys.argv[0]))
tokens = curr_path.split(os.path.sep)
path = '/'.join(token for token in tokens)

import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

app = Flask(__name__)
app.secret_key = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/')
def index():
    return render_template("submission.html")

@app.route('/prediction', methods=['POST', 'GET'])
def prediction():
    depature_delay = float(request.form['DepDelay'])

    unpickled_linear_model = pickle.load(open(curr_path + '/linearModel.pkl', 'rb'))
    prediction = unpickled_linear_model.predict([[depature_delay]])

    return render_template('prediction.html', prediction = prediction[0][0])

if __name__ == "__main__":
    app.run(debug=True)
