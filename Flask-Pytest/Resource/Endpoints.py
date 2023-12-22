from flask_restful   import Resource , request , jsonify
from flask  import jsonify , json , abort


students = [
    {
        'Name' : 'Ashok',
        'Roll' : 1 , 
        'Contact' : "90239 xxxxx"
    },
    {
        'Name' : 'John',
        'Roll' : 2 , 
        'Contact' : "90639 xxxxx"
    }
    
]


class Home(Resource):
    def get(self):
        return "Home Page"
    

class Student_InfoEdit(Resource):
    #Endpoint to display the Student information
    def get(self):
        return jsonify({"Students" : students})
    

class Student_Edit(Resource):
    #Endpoint to edit the student name
    def post(self):
        data = request.get_json()
        New_name = data["name"]
        Roll_No = data['roll']
        Roll_Numbers = [student['Roll'] for student in students]
        if Roll_No in Roll_Numbers:
            for student in students:
                if student ['roll'] == Roll_No:
                    student ['Name'] = New_name
                continue
        else:
            abort(404)


class Student_add(Resource):
    #Endpoint to add student
    def post(self):
        data = request.get_json()
        existing = [student['Roll'] for student in students]
        if data['roll'] in existing :
            return jsonify({'response' : "Already Exist"})
        else:
            return jsonify({"response" : "Success"})
