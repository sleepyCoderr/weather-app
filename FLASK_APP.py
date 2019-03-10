import credentials
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
from datetime import datetime
import datetime



app=Flask(__name__, static_url_path = "/static", static_folder = "static")

def convertms2mph(num):
    perHour=num*(3600/1)
    perHour=num*(3600/1)
    return perHour/1609


def amORpm():
    currentDT = datetime.datetime.now()
    hour="%d" % currentDT.hour
    if 0<=int(hour)<=6:
        icon="night"
        return icon
    elif 6<=int(hour)<=18:
        icon="day"
        return icon
    else:
        icon="night"
        return icon



class weatherClass:

    def find_city(self,value):
        results=[];
        self.value=value
        links=[f"api.openweathermap.org/data/2.5/forecast?q={value}&appid=277fd4ecc69a5d9fb08bd31f26881477",f"api.openweathermap.org/data/2.5/weather?q={value}&appid=277fd4ecc69a5d9fb08bd31f26881477"]
        
        http = urllib3.PoolManager()
        for url in links:
            r = http.request('GET', url)
            data=json.loads(r.data)
            results.append(data)
        return results;

    def create_dict(self,d):
        self.d=d

        #current temp
        temp=d[1]["main"]["temp"]
        fahrenheit=pytemperature.k2f(temp)

        #tonight temp
        temp_night=d[0]['list'][2]["main"]["temp_min"]
        fahrenheit2=pytemperature.k2f(temp_night)

        #tomorrow temp
        tomorrow=d[0]['list'][5]["main"]["temp_max"]
        fahrenheit3=pytemperature.k2f(tomorrow)
                
        #current humidity
        humidity=d[0]["list"][1]['main']['humidity'];

        #location
        # location=d[]
        
        #current cloud
        cover=d[1]["weather"][0]["description"]

         #current id
        ids=d[1]["weather"][0]['id']
        
        #tonight id
        ids2=d[0]['list'][2]["weather"][0]['id']
        
        #tomorrow id
        ids3=d[0]['list'][5]["weather"][0]['id']

        #current wind
        wind=d[1]["wind"]["speed"]
        mph=round(convertms2mph(wind),2)

        #current amORpm
        time=amORpm()

        dict_main={"current":fahrenheit,"tonight":fahrenheit2,"wind":mph,
        "humidity":humidity,"description":cover,"id":ids,"tomo_id":ids3,
        "tonight_id":ids2,"tomorrow":fahrenheit3,"time":time};
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
        return dumps(dm);