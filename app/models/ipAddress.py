from enum import unique
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

import datetime,uuid

from marshmallow import fields,Schema
from sqlalchemy.dialects.postgresql.base import MACADDR
from sqlalchemy.orm import defaultload
from sqlalchemy.sql.sqltypes import NullType


from . import db

class ipAddressModel(db.Model):
    """
    IP Address Model
    """

    # table name
    __tablename__ = 'ipAddresses'

    id = db.Column(UUID(True), primary_key=True, default=uuid.uuid4)
    subnet_id = db.Column(UUID(True), db.ForeignKey('subnets.id'), nullable=False)
    ipAddress = db.Column(db.BigInteger, unique=True, index=True, nullable=False)
    is_gateway = db.Column(db.Boolean, default=False, nullable=False)
    description = db.Column(db.String(200))
    hostname = db.Column(db.String(64))
    macAddress = db.Column(db.String(17))
    owner = db.Column(db.String(40))
    state_id = db.Column(UUID(True))#, db.ForeignKey('state.id'), nullable=False)
    lastSeen = db.Column(db.DateTime)

    def __repr__(self):
        return f"<id {id}>"

