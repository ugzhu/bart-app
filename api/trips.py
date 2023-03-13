import requests
import json
import xmltodict


class TripsController:
    def __init__(self, path):
        self.origin, self.destination = path.split("/")[3], path.split("/")[5]
        self.url = f"https://api.bart.gov/api/sched.aspx?cmd=depart&" \
              f"orig={self.origin}&dest={self.destination}&" \
              f"key=MW9S-E7SL-26DU-VV8V&time=now"

    def response(self):
        xml = requests.get(self.url).content
        dictionary = xmltodict.parse(xml)
        js = json.dumps(dictionary)
        return js
