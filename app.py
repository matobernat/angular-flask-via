import connexion as connexion
from flask import Flask, render_template, request, jsonify, make_response, Response
from flask_marshmallow import Marshmallow
from flask_restx import Api, Resource
import requests
import json
from flask_sqlalchemy import SQLAlchemy
import os.path



"""Define Flask app"""
flask_app = Flask(__name__)


# basedir = os.path.abspath(os.path.dirname(__file__))
# # Create the Connexion application instance
# connex_app = connexion.App(__name__, specification_dir=basedir)
#
# # Get the underlying Flask app instance
# app = connex_app.app
#
# flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
# flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# # Configure the SQLAlchemy part of the app instance
# app.config['SQLALCHEMY_ECHO'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'users.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#


# db = SQLAlchemy(app)
#
# # Initialize Marshmallow
# ma = Marshmallow(app)
#
# class users(db.Model):
#     _id = db.Column("id", db.Integer, primary_key=True)
#     text = db.Column(db.String(100))
#
#     def __init__(self, text):
#         self.text = text





app = Api(app=flask_app,
          version="1.0",
          title="VIA app",
          description="Covid app for via",
          doc='/documentation',
          base_url="/static/")







user_messages = ["Nice app", "i would love more color", "more animation!"]

"""Define namespaces"""
covid_name_space = app.namespace("covid", description='Get info about covid')
time_name_space = app.namespace("time", description='Get time')
internal_name_space = app.namespace("internal", description='internal api about user messages')
app_name_space = app.namespace("", description='rendering page')


def fillDatabase(db:SQLAlchemy, msgs):
    for m in msgs:
        usr = users(m)
        db.session.add(usr)
    db.session.commit()
    print(users.query.all())


# fillDatabase(db,user_messages)

@app_name_space.route("/static/")
# @app.route("/static/")
class PageController(Resource):
    @app.doc(responses={200: 'OK', 400: 'Invalid Argument'}, description="Render the page")
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return Response(response=render_template('index.html'))
        # return make_response(render_template('index.html'), 200, headers)
        # return render_template('index.html')



print("BOL SOM TU ALE ASI NIC")


@covid_name_space.route("/<string:countrywithdate>/countrydata")
class CountryData(Resource):
    @app.doc(responses={200: 'OK'}, description="Get covid history by country")  # Documentation of route
    def get(self,countrywithdate="usa,2020-06-02"):  # GET method of REST
        if (countrywithdate.find(",") < 0):
            return covid_name_space.abort(400, status="input format should be [STATE,DATE] ", statusCode="400")
        country,date = countrywithdate.split(',')
        print("input: " + country+", "+ date)
        print(type(get_external_covid_history_by_country()))
        return get_external_covid_history_by_country(country,date)
        # return (jsonify(get_external_covid_history_by_country(country,date)), 200);



# @app.route('/countrydata', methods=["GET"])
# def get_python_data():
#     print("callling endpoint 123 ")
#     print(type(get_external_covid_history_by_country()))
#     return (jsonify(get_external_covid_history_by_country()), 200)
#     # return json.dumps(response)


@covid_name_space.route("/countries")  # Define the route
class Countries(Resource):
    @app.doc(responses={200: 'OK', 400: 'Invalid Argument'}, description="Get all available countries")
    def get(self):
        print("callling endpoint countries")
        print(type(get_external_covid_countries()))
        print(get_external_covid_countries())
        return get_external_covid_countries()
        # return (jsonify(get_external_covid_countries()), 200)


# @app.route('/countries', methods=["GET"])
# def get_countries():
#     print("callling endpoint countries")
#     print(type(get_external_covid_countries()))
#     print(get_external_covid_countries())
#     return (jsonify(get_external_covid_countries()), 200)



@time_name_space.route("/time")  # Define the route
class Time(Resource):
    @app.doc(responses={200: 'OK', 400: 'Invalid Argument'}, description="Get current time")
    def get(self):
        print(get_external_time())
        return get_external_time()
        # return (jsonify(get_external_time()), 200)



@internal_name_space.route("/messages")  # Define the route
class getMessages(Resource):
    @app.doc(responses={200: 'OK', 400: 'Invalid Argument'}, description="Get all the messages from users")
    def get(self):
        print(user_messages)
        return user_messages
        # return jsonify(user_tips)
        # return (jsonify(user_tips), 200)


@internal_name_space.route("/delmessages")  # Define the route
class deleteMessages(Resource):
    @app.doc(responses={200: 'OK', 400: 'Invalid Argument'}, description="Delete all messages from the users")
    def delete(self):
        print(user_messages)
        temp = user_messages.copy()
        user_messages.clear()
        print(user_messages)
        return temp
        # return jsonify(user_tips)
        # return (jsonify(user_tips), 200)


@internal_name_space.route("/<string:message>/messages")  # Define the route
class insertMessages(Resource):
    @app.doc(responses={200: 'OK', 400: 'Invalid Argument'}, description="Insert message")
    def put(self,message):
        print(message)
        user_messages.append(message)
        # msg = messages(message)
        # db.session.add(msg)
        # db.session.commit()


        return message
        # return (jsonify(tip), 200)




def get_external_time():
    url = "https://world-clock.p.rapidapi.com/json/cet/now"

    headers = {
        'x-rapidapi-host': "world-clock.p.rapidapi.com",
        'x-rapidapi-key': "a58fe6510emsh281e768b1d4dca5p107ee4jsn291d5e2e10c0"
    }

    response = requests.request("GET", url, headers=headers)

    print("\nPRINTING DAteE\n")
    print(response.text)
    print("\nPRINTING DAtE\n")
    return response.json()

def get_external_covid_history_by_country(country="usa", day="2020-06-02"):
    # GET historical statistics for a country
    url = "https://covid-193.p.rapidapi.com/history"

    querystring = {"country": country, "day": day}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "a58fe6510emsh281e768b1d4dca5p107ee4jsn291d5e2e10c0"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    return  response.json()


def get_external_covid_countries():
    url = "https://covid-193.p.rapidapi.com/countries"

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "a58fe6510emsh281e768b1d4dca5p107ee4jsn291d5e2e10c0"
    }

    response = requests.request("GET", url, headers=headers)

    print(type(response), "RESPONSE")
    return response.json()




# db.create_all()
flask_app.run()
# app.run(host="0.0.0.0", debug=True)