from flask import Flask, render_template, Request
from flask.globals import request
import tensorflow
from tensorflow.keras import models

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/predict', methods=["POST"])
def predict():
    CreditScore = int(request.form.get('CreditScore'))
    Geography = int(request.form.get('Geography'))
    Gender = int(request.form.get('Gender'))
    Age = int(request.form.get('Age'))
    Tenure = int(request.form.get('Tenure'))
    Balance = int(request.form.get('Balance'))
    NumOfProducts = int(request.form.get('NumOfProducts'))
    HasCrCard = int(request.form.get('HasCrCard'))
    IsActiveMember = int(request.form.get('IsActiveMember'))
    EstimatedSalary = int(request.form.get('EstimatedSalary'))
    #print(CreditScore, Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary)
    print(type(int(CreditScore)))
    test_model = models.load_model('churn_modelling.h5')
    result = test_model.predict([[CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,1]])
    #result = test_model.predict([[1,12,3,14,5,6,2,10,3,12,11]])
    #if (result < 0.5): 
    if (result[0] < 0.5) :
        print('Churn case')
        val = 'Churn case'    
    else:
        print('No Churn')
        val = 'No Churn'

    return render_template("result.html", value = val)

if __name__=='__main__':
    app.run(debug=True)
