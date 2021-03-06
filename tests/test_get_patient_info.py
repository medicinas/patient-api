import pytest
import requests
from collections import Counter
# def test_hello():
#     response = app.test_client().get('/Hello')

#     assert response.status_code == 200
#     assert response.data == b'Hello, World!'

def test_getdetails():


    url = 'http://127.0.0.1:5000/api/details' # The root url of the flask app

    r = requests.get(url) # Assumses that it has a path of "/"
    data = r.json()
    fields = data['data'][0]
    print(fields)
    assert len(fields.keys())==9
    keys=['lastname', 'regionid', 'cityid', 'healthcareid', 'healthinsuranceid', 'status', 'countryid', 'name', 'numberid']
    assert Counter(fields.keys())==Counter(keys)
    assert type(fields['name'])==str
    
    assert r.status_code == 200 # Assumes that it will return a 200 response