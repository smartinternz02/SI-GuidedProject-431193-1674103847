from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle
import os
app=Flask(__name__)
with open('C:/Users/tsjis/OneDrive/Desktop/Cab Price Predictor/model.pkl','rb') as handle:
    model=pickle.load(handle)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/prediction',methods=['POST','GET'])
def prediction():
    return render_template('index1.html')
@app.route('/Home',methods=['POST','GET'])
def my_home():
    return render_template('index.html')
@app.route('/predict',methods=['POST','GET'])
def predict():
    input_feature=[float(x) for x in request.form.values()]
    feature_values=[np.array(input_feature)]
    feature_name=['cab_type','name','product_id','source','destination']
    x=pd.DataFrame(feature_values,columns=feature_name)
    
    prediction=model.predict(x)
    print("prediction is:",prediction)
    
    return render_template("result.html",prediction=prediction[0])
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True, use_reloader=False)
