from flask import Flask
from marshmallow import Schema, fields, pre_load, validate, ValidationError
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Pais(db.Model):
    __tablename__ = 'paises'
    pai_id = db.Column(db.Integer, primary_key=True)
    pai_nom = db.Column(db.String(150), nullable=False)

    def __init__(self, pai_id, pai_nom):
        self.pai_id = pai_id
        self.pai_nom = pai_nom


class PaisSchema(ma.Schema):
    pai_id = fields.Integer(dump_only=True)
    pai_nom = fields.String(required=True)
