import json
from flask import Flask
from Api.BusinessLogic import Days

app = Flask(__name__)

def getDay(day):

    newDay = Days.GetDay(day)

    return json.dumps(newDay.serialize())



class DaysController:

 newDay:str
