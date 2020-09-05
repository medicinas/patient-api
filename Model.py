from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()

#The main class for Db
class PatientDetailsmd(db.Model):
    

    __tablename__ = 'PatientDetails'

    name = db.Column(db.String(250), primary_key=True)
    lastname = db.Column(db.String(250), nullable=False)
    status = db.Column(db.String(250), nullable=False)
    healthinsuranceid = db.Column(db.Integer, nullable=False)
    healthcareid = db.Column(db.Integer, nullable=False)

    countryid = db.Column(db.Integer,  nullable=False)
    numberid = db.Column(db.Integer, nullable=False)
    regionid = db.Column(db.Integer,  nullable=False)
    cityid = db.Column(db.Integer,  nullable=False)


    def __init__(self, name,lastname,status,healthinsuranceid,healthcareid,countryid,regionid,cityid,numberid):
        self.name = name
        self.lastname=lastname
        self.status=status
        self.healthcareid=healthcareid
        self.healthinsuranceid=healthinsuranceid
        self.countryid=countryid
        self.numberid=numberid
        self.regionid=regionid
        self.cityid=cityid
 
class PatientDetailschema(ma.Schema):
    #schema for converting toserializable objec
    name = fields.String( primary_key=True)
    lastname = fields.String()
    status =fields.String()
    healthinsuranceid =fields.Integer(required=True)
    healthcareid =fields.Integer(required=True)
    countryid = fields.Integer(required=True)
    numberid = fields.Integer(required=True)
    regionid =fields.Integer(required=True)
    cityid = fields.Integer(required=True)