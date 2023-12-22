from flask import Flask,request
from flask_restful import Api
    
app = Flask(__name__)
api = Api(app)

from Resource.Endpoints import (
    Home,
    Student_Info,
    Student_Edit
    Student_add
    )

api.add_resource(Home,'/api/')
api.add_resource(Student_InfoEdit,'/api/Info')
api.add_resource(Student_add,'/api/')


if __name__ == "__main__":
    app.run(debug = True)