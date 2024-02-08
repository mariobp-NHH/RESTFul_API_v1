from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import os

application = Flask(__name__)
api = Api(application)

api.add_resource(Home, '/')

if __name__ == '__main__':
    application.run(debug=True)
