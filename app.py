
from flask import Flask, render_template, request
from Feature_extractor import FEATURE_PEDICTION
import os
import numpy as np 


app = Flask(__name__)
@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    prediction2 = 'no image found'
    try:
        cwd = os.getcwd()
        mydir = os.path.join(cwd, "images")
        for f in os.listdir(mydir):
            os.remove(os.path.join(mydir, f))
        file_exists = os.path.exists("samples.csv")
        if file_exists == True:
            os.remove("samples.csv")
        file_exists = os.path.exists("fulldata.csv")
        if file_exists == True:
            os.remove("fulldata.csv")
        file_exists = os.path.exists("eng.csv")
        if file_exists == True:
            os.remove("eng.csv")
        file_exists = os.path.exists("eng.csv")
        if file_exists == True:
            
            os.remove("eng.csv")
        imagefile= request.files['imagefile']
        filepath=os.path.abspath("images")
        image_path = filepath+ '/' + imagefile.filename
        print('pass1')
        imagefile.save(image_path)
        print('pass2')
        
        
        prediction2 = FEATURE_PEDICTION(image_path)
        if prediction2 ==  1:
            prediction2 = 'low severity of pnemonia'
        elif prediction2 ==  0:
            prediction2 = 'mid severity of pnemonia'
        elif prediction2 ==  -1:
            prediction2 = 'high severity of pnemonia'
    except PermissionError:
        pass
    return render_template('index.html', prediction = prediction2)

if __name__ == '__main__':
    app.run(port=3000, debug=True)