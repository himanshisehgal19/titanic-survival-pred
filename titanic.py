from flask import Flask,render_template,redirect,request
import pandas as pd 
import numpy as np
import joblib


app=Flask(__name__)
model=joblib.load("model.pkl")
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/',methods=['POST'])
def marks():
    if request.method == 'POST':
        var1=float(request.form['glucose'])
        var3=float(request.form['bldp'])
        var4=float(request.form['skinth'])
        var5=float(request.form['insulin'])
        var6=float(request.form['bmi'])
        #var10=float(request.form['vare'])
        varyx=str(request.form['vary'])
        if varyx=='male':
            var2=1.0
        else:
            var2=0.0
        listoftit=[var6,var2,var1,var4,var3,var5]
        predictn=model.predict([listoftit])
        print(listoftit)
        print(predictn)
        output=str(predictn)
        prediction=output[1]
        

    return render_template("index.html", predicted=prediction,output=output)
if __name__== '__main__':
    app.run(debug=True)