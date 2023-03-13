import requests
import json
import xmltodict


class StationsController:
    def __init__(self):
        self.url = "https://api.bart.gov/api/stn.aspx?cmd=stns&key=MW9S-E7SL-26DU-VV8V"


    def response(self):
        xml = requests.get(self.url).content
        dictionary = xmltodict.parse(xml)
        js = json.dumps(dictionary)
        return js
