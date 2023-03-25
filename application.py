from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            Gender=request.form.get('Gender'),
            Age=request.form.get('Age'),
            Occupation=int(request.form.get('Occupation')),
            City_Category=request.form.get('City_Category'),
            Stay_In_Current_City_Years=request.form.get('Stay_In_Current_City_Years'),
            Marital_Status=int(request.form.get('Marital_Status')),
            Product_Category_1=int(request.form.get('Product_Category_1')),
            Product_Category_2=float(request.form.get('Product_Category_2')),
            Product_Category_3=float(request.form.get('Product_Category_3'))
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        return render_template('home.html',results=results[0])


if __name__=="__main__":
    app.run(host="0.0.0.0")  