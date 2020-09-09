import pytest
import requests
from collections import Counter
import random,json
import random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))
def test_getdetails():
    
    url = 'http://127.0.0.1:5000/api/details' # The root url of the flask app


    data ={
			"cityid": random.randint(1,1000),
            "numberid":  random.randint(1,1000),
	         "healthinsuranceid":  random.randint(1,1000),
            "id":  random.randint(1,1000),
            "name":randomword(8),
            "healthcareid": random.randint(1,1000),
            "regionid": random.randint(1,1000),
            "countryid": 413,
            "status": "oksafe",
            "lastname": randomword(9)
         }

    response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    print(response.json())
    print(response.request.headers['Content-Type'])

    assert(response.status_code)  == 200
    
