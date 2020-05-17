import json
import os
from flask import Flask
from flask_restplus import Resource, Api
from v1.controller import v1, app

app.register_blueprint(v1)
if __name__ == '__main__':
    app.run(host="0.0.0.0" ,port=5000, debug=True)
