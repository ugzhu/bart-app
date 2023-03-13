import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
sys.path.append(os.path.dirname(SCRIPT_DIR+"/api"))
sys.path.append(os.path.dirname(SCRIPT_DIR+"/web"))
from api.trips import TripsController
from api.station import StationController
from api.stations import StationsController
from web.index import IndexController


def api_stations():
    controller = StationsController()
    output = controller.response().encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    return output, response_headers, status


def api_trips(path):
    controller = TripsController(path)
    output = controller.response().encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    return output, response_headers, status


def api_station(path):
    controller = StationController(path)
    output = controller.response().encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    return output, response_headers, status


def web_index():
    controller = IndexController()
    output = controller.response().encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    return output, response_headers, status


def application(environ, start_response):
    path = environ['PATH_INFO']

    if path == '/stations':
        output, response_headers, status = api_stations()
        start_response(status, response_headers)
        return [output]

    if '/trips' in path:
        output, response_headers, status = api_trips(path)
        start_response(status, response_headers)
        return [output]

    if '/station' in path:
        output, response_headers, status = api_station(path)
        start_response(status, response_headers)
        return [output]

    if path == '/':
        output, response_headers, status = web_index(path)
        start_response(status, response_headers)
        return [output]

    output = b''
    status = '303 See Other'
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output))),
                        ('Location', f'https://bart.yujiezhu.net/')]
    start_response(status, response_headers)
    return [output]

def start_response(a, b):
    pass


if __name__ == '__main__':
    environ1 = {'PATH_INFO': '/stations',
                'REQUEST_METHOD': 'GET'}
    environ2 = {'PATH_INFO': ' /station/source/MLBR',
                'REQUEST_METHOD': 'GET'}
    environ3 = {'PATH_INFO': ' /trips/source/MLBR/dest/WARM',
                'REQUEST_METHOD': 'GET'}
    output = application(environ3, start_response)
    print(output)