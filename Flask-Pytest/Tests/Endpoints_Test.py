import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_Home(client):
    response = client.get('/api/')
    assert response.status_code == 200
    assert b'Home Page' in response.data


def test_Student_info(client):
    response = client.get('/api/info')
    data = response.json
    assert response.status_code == 200
    assert data["Message"] == "Fetched"
@pytest.mark.parametrize("input_data,expected_data",[({'name':'alice','roll': 1},{"Message":"changed"}),
                                                     ({'name':'alice','roll': 5},{"Message":"Failed"})
                                                     ])
def test_Student_Edit(client,input_data,expected_data):
    response = client.post('/api/edit' ,json = input_data )
    assert response.status_code == 200
    assert response.json == expected_data


@pytest.mark.parametrize("input_data,expected_data,expected_status_code",[
    ({
        'Name' : 'Ashok',
        'Roll' : 1 , 
        'Contact' : "90239 xxxxx"
    },{'Message' : "Already Exist"},409),
    (
       {
        'Name' : 'Ashokselvan',
        'Roll' : 7 , 
        'Contact' : "96239 xxxxx"
    } ,{"Message" : "Success"},200
    )
])
def test_student_add(client,input_data,expected_data,expected_status_code):
    response = client.post('/api/add',json = input_data)
    assert response.status_code == expected_status_code
    assert response.json == expected_data