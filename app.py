
# importing the necessary dependencies
from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            Pclass = float(request.form['Pclass'])
            Age = float(request.form['Age'])
            SibSp = float(request.form['SibSp'])
            Parch = float(request.form['Parch'])
            Fare = float(request.form['Fare'])
            Sex = float(request.form['Sex'])

            filename = 'dtree.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[Pclass,Age,SibSp,Parch,Fare,Sex]])
            print('survived', prediction)
            return render_template('results.html', response = prediction)
            # showing the prediction results in a UI))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
        #return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8001, debug=True)
	#application.run(debug=True) # running the app