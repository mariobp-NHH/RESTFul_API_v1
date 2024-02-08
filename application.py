from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
api = Api(application)

DBVAR = f"postgresql://{os.environ['RDS_USERNAME']}:{os.environ['RDS_PASSWORD']}@{os.environ['RDS_HOSTNAME']}/{os.environ['RDS_DB_NAME']}"
application.config['SECRET_KEY'] = '1dfc4dedcdsdsd5b2ffa3a090dfc34f845fd'
application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR 

db = SQLAlchemy(application) 


api.add_resource(Home, '/')

if __name__ == '__main__':
    application.run(debug=True)
