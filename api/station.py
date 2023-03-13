import requests
import json
import xmltodict


class StationController:
    def __init__(self, path):
        station = path.split("/")[3]
        self.url = f"https://api.bart.gov/api/stn.aspx?cmd=stninfo&orig={station}&key=MW9S-E7SL-26DU-VV8V"

    def response(self):
        xml = requests.get(self.url).content
        dictionary = xmltodict.parse(xml)
        js = json.dumps(dictionary)
        return js
