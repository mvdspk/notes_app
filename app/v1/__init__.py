import threading
import time
import util
from flask import Flask, jsonify, Blueprint, request
from flask_restplus import Api, Resource, fields, reqparse
from service import Database 
#TODO: need to decidewhich logger we use
#from logger import get_logger

app = Flask(__name__)
v1 = Blueprint('v1', __name__, url_prefix='/api/v1/controller')
api = Api(app, version='1.0', title='Note App API',
          description='APIs to create, read, update and delete a note',
          )
note_operations=Database()
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response          
class ApiModels:
    def __init__(self):
        self.model_note = api.model('note_text', {
            'noteid': fields.String,
            'content': fields.String,
            'lastsaved': fields.DateTime(dt_format='rfc822')
        })


        self.model_note_list = api.model('test model list', {"model_note": fields.Nested(self.model_note, as_list=True)})
apimodels = ApiModels()

@api.route('/note/<string:userid>')
class GetAllNotes(Resource):
    @api.doc('Get test collection as a list')
    @api.response(200, 'Success', apimodels.model_note_list)
    @api.response(404, 'NotFound')
    @api.response(500, 'InternalServerError')
    def get(self):
        try:
            result = note_operations.get_note_by_id()
            if not result:
                return{'NotFound': 'No note found'}, 404
            return jsonify(result)
        except Exception as ex:
            return {'InternalServerError': 'couldnt fetch the data'}, 500


@api.route('/note/<string:noteid>/<string:>')
@api.doc(params={'noteid':'Note Id'})
class GetNoteById(Resource):
    @api.doc('Get test collection by note id')
    @api.response(200, 'Success', apimodels.model_note_list)
    @api.response(404, 'NotFound')
    @api.response(500, 'InternalServerError')
    def get(self, testexecutionid):
        try:
            result={"notes": [{"note1": "content":"something"},{"note2": "content": "something"}] }
            return jsonify(result)
        except Exception as ex:
            return {'InternalServerError': 'couldnt fetch data for the execution id provided'}, 500

