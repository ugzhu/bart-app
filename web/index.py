import os


class IndexController:
    def __init__(self):
        pass

    def response(self):
        response = ""
        path = os.path.dirname(os.path.abspath(__file__)) + "/index.html"

        with open(path) as f:
            for line in f:
                response += line

        return response
