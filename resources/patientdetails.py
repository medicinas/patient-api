from flask import request
from flask_restful import Resource
from Model import db,PatientDetailsmd,PatientDetailschema

patient_schema = PatientDetailschema(many=True)
patient_schemas = PatientDetailschema()

class PatientDetails(Resource):
    def get(self):
        details = PatientDetailsmd.query.all()
        details = patient_schema.dump(details).data
        return {'status': 'success', 'data':details}, 200

    def post(self):
        json_data = request.get_json(force=True)
        print(json_data)
  
        details=PatientDetailsmd(json_data['name'],json_data['lastname'],json_data['status'],json_data['healthinsuranceid'],json_data['healthcareid'],json_data['countryid'],json_data['numberid'],json_data['regionid'],json_data['cityid'])
    
        db.session.add(details)
        db.session.commit()


        return { "status": 'success', 'data': 'ok' }, 200