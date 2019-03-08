import credentials
import oauth2 as oauth
import urllib3
import json
import pytemperature
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    url_for)
from bson.json_util import dumps
import googlemaps
import pprint
from datetime import datetime



# app = Flask(__name__)

app=Flask(__name__, static_url_path = "/static", static_folder = "static")
def convertms2mph(num):
    perHour=num*(3600/1)
    perHour=num*(3600/1)
    return perHour/1609


class weatherClass:

    def find_city(self,value):
        self.value=value
        url=f"api.openweathermap.org/data/2.5/weather?q={value}&appid=277fd4ecc69a5d9fb08bd31f26881477"
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        results=json.loads(r.data)
        return results

    def create_dict(self,d):
        self.d=d
        #current temp
        temp=d["main"]
        fahrenheit=pytemperature.k2f(temp["temp"])
        night_temp=pytemperature.k2f(temp["temp_min"])

        #current speed
        speed=d["wind"]["speed"]
        mph=round(convertms2mph(speed))
        
        #current humidity
        humidity=d["main"]["humidity"]

        #location
        # location=d[]
        
        #current cloud
        cover=d["weather"][0]["description"]

         #current id
        ids=d["weather"][0]["id"]
        
        dict_main={"temp":fahrenheit,"wind":mph,"humidity":humidity,"description":cover,"id":ids,"min_temp":night_temp}
        return dict_main
        
       


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/",methods=["POST","GET"])
def all_data():
    if request.method =="POST":
        address=request.form['search']
        gmaps = googlemaps.Client(key='AIzaSyDJnHmIXjElSUi093cL4RocGRddfKYuxIc')
        place_result=gmaps.places(query=f"{address}",open_now=False)
        city=place_result["results"][0]['formatted_address']
        findCity=weatherClass()
        dict_main=weatherClass()
        v=findCity.find_city(city)
        dm=dict_main.create_dict(v)
        dm.update({"location":place_result["results"][0]['formatted_address']})
        return dumps(dm)