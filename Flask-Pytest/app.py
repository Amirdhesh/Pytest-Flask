from flask import Flask,request
from flask_restful import Api
    
app = Flask(__name__)
api = Api(app)

from Resource.Endpoints import Home

api.add_resource(Home,'/api/')


if __name__ == "__main__":
    app.run(debug = True)