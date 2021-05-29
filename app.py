from flask import Flask , jsonify, render_template
from flask.globals import request
from flask_pymongo import PyMongo
import datetime 


app = Flask(__name__)
mongodb_client = PyMongo(app, uri="mongodb+srv://mongodb159:mongodb159@solar-system.meyls.mongodb.net/wisdomleaf")
db = mongodb_client.db

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('home.html')


@app.route('/add_one', methods=['GET', 'POST'])
def add_one():
    if request.method =='POST':
        title = request.form['title']

        startyear = int(request.form['startyear'])
        startmonth = int(request.form['startmonth'])
        startday = int(request.form['startday'])

        endyear = int(request.form['endyear'])
        endmonth = int(request.form['endmonth'])
        endday = int(request.form['endday'])

        start = datetime.datetime(startyear, startmonth, startday)  
        end = datetime.datetime(endyear, endmonth, endday)

        db.appointment.insert_one({'title': title, 
                               'startdate': str(start.strftime("%Y-%m-%d")), 
                               'enddate': str(end.strftime("%Y-%m-%d"))
                               })
                               
    return jsonify(message="inserted")


@app.route('/find_appointment', methods=['GET', 'POST'])
def find_appointment():
    if request.method == 'POST':
        startdate = request.form['startdate']
        enddate = request.form['enddate']

        myquery = { 
                    "$and": [       
                        {"enddate":{"$gte":startdate}},
                        {"enddate":{"$lte":enddate}}
                    ]
          }
        res = db.appointment.find(myquery, {"_id":False})

        complete_result = [r for r in res]
        total_appointment = len(complete_result)

        final_result = {
                        "total_appointments":total_appointment,
                        "results": complete_result 
        }
    return jsonify(final_result)
        
if __name__=='__main__':
    app.run(debug=True)    