
from flask import Flask,request, render_template
import pickle
import sklearn

#set up application
app=Flask(__name__) 

#defining prediction function
def prediction(lst):
    filename='fmodel1.pickle'
    with open(filename,'rb') as file:
        model=pickle.load(file)
    pred_value=model.predict([lst])
    return pred_value 


#creating web pages
@app.route('/',methods=['POST','GET'])
def index():
    pred=3
    if request.method=='POST':
        exercise =request.form['Exercise_2.0_yes']
        asthma =request.form['Asthma_1.0_yes']
        chronic =request.form['COPD/Chronic_Bronchitis_1.0_yes']
        arthritis =request.form['Arthritis_1.0_yes']
        depressive =request.form['Depressive_disorder_1.0_yes']
        concentration =request.form['Concentration_Difficulty_1.0_yes']
        walking =request.form['Serious_Walking_Difficulty_1.0_yes']
        employment =request.form['Employment_Status_8.0_yes']


        feature_list=[]
        feature_list.append(float(exercise))
        feature_list.append(float(asthma))
        feature_list.append(float(chronic))
        feature_list.append(float(arthritis))
        feature_list.append(float(depressive))
        feature_list.append(float(concentration))
        feature_list.append(float(walking))
        feature_list.append(float(employment))
        
        print(feature_list)
        pred=prediction(feature_list)
     
    return render_template("index.html",pred=pred)


if __name__=='__main__':
    app.run(debug=True)


