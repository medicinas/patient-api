import pytest
import requests
from collections import Counter
# def test_hello():
#     response = app.test_client().get('/Hello')

#     assert response.status_code == 200
#     assert response.data == b'Hello, World!'

def test_getdetails():


    url = 'http://127.0.0.1:5000/api/details' # The root url of the flask app

    data ="""{
			"cityid": 931,
            "numberid": 22,
	         "healthinsuranceid": 22,
            "id": 22,
            "name": "we",
            "healthcareid": 413,
            "regionid": 332,
            "countryid": 23,
            "status": "oksafe",
            "lastname": "pos"
         }"""

    response = requests.post(url, data=data, headers={'Content-Type': 'application/json'})
    print(response.json())
    print(response.request.headers['Content-Type'])

    assert(response.status_code)  == 200
    
