from datetime import datetime, timedelta, date
import requests
import json

### API
def actual_api():
    api_call = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    api = json.loads(api_call.content)
    return api

def history_api():
    api_call = requests.get("https://api.coindesk.com/v1/bpi/historical/close.json?start=2013-09-01&end=" + datetime.now().strftime("%Y-%m-%d"))
    apiH = json.loads(api_call.content)
    return apiH


### DATE
def year():
    year = int(datetime.now().strftime("%Y"))
    return year
def month():
    month = int(datetime.now().strftime("%m"))
    return month
def day():
    day = int(datetime.now().strftime("%d"))
    return day
def hour():
    hour = int(datetime.now().strftime("%H"))
    return hour
def minute():
    minute = int(datetime.now().strftime("%M"))
    return minute
def second():
    second = int(datetime.now().strftime("%S"))
    return second


def daterange(start_date, end_date): # Date loop
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def date_loop_logic():
    x = []
    start_date = date(2013, 9, 1)
    end_date = date(int(datetime.now().strftime("%Y")), int(datetime.now().strftime("%m")), int(datetime.now().strftime("%d")))
    for single_date in daterange(start_date, end_date):
        x.append(single_date.strftime("%Y-%m-%d"))
    return x
        

def date_loop(): # Get date from beginning to end
    x = date_loop_logic()
    y = unwrap_data(x)
    if len(y) != len(x):
        x.pop()
    return (y, x)


def unwrap_data(y): #Unwrap data to price
    a = []
    apiH = history_api()
    for i in y:
        try:
            a.append(apiH["bpi"][i])
        except:
            print("Error in unwraping data. Propably date isn't updated within api. *Ignore*")
    return a
