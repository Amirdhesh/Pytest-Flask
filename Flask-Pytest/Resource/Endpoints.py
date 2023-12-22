from flask_restful   import Resource , request 
from flask  import jsonify 


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
    

class Student_Info(Resource):
    #Endpoint to display the Student information
    def get(self):
        return jsonify({"Message":"Fetched","Students" : students})
    

class Student_Edit(Resource):
    #Endpoint to change the student name
    def post(self):
        data = request.get_json()
        New_name = data["name"]
        Roll_No = data['roll']
        Roll_Numbers = [student['Roll'] for student in students]
        if Roll_No in Roll_Numbers:
            for student in students:
                if student ['Roll'] == Roll_No:
                    student ['Name'] = New_name
                    return {"Message":"changed"}
                   
        else:
            return {"Message":"Failed"}


class Student_add(Resource):
    #Endpoint to add student
    def post(self):
        data = request.get_json()
        existing_rollno = [student['Roll'] for student in students]
        if data['Roll'] in existing_rollno :
            response = jsonify({'Message' : "Already Exist"})
            response.status_code = 409
            return response
        else:
            response = jsonify({"Message" : "Success"})
            response.status_code = 200
            return response
