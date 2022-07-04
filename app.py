
from flask import Flask, render_template, request, redirect
from Feature_extractor import FEATURE_PEDICTION
import os
import numpy as np 
from werkzeug.utils import secure_filename   

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
app.config['UPLOAD_PATH'] = 'images/'             # Storage path    
@app.route("/",methods=['GET','POST'])
def upload_file():                                       # This method is used to upload files 
        if request.method == 'POST':
                f = request.files['imagefile']
                print(f.filename)
                #f.save(secure_filename(f.filename))
                filename = secure_filename(f.filename)
                f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
                return redirect("/")           # Redirect to route '/' for displaying images on fromt end

if __name__ == '__main__':
    app.run(port=3000, debug=True)