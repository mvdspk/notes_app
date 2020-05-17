import json
import os
from flask import Flask
from flask_restplus import Resource, Api
from V1.controller import v1, app
from settings import HOST_IP, HOST_PORT

app.register_blueprint(v1)
log = get_logger()
if __name__ == '__main__':
    app.run(host=0.0.0.0 ,port=5000, debug=True)
