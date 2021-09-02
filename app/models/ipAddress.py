from sqlalchemy.dialects.postgresql import UUID

import datetime,uuid

from marshmallow import fields,Schema
from sqlalchemy.orm import defaultload

from . import db

class ipAddressModel(db.Model):
    """
    IP Address Model
    """

    # table name
    __tablename__ = 'ipAddresses'

    ipaddress_id = db.Column(UUID(True), primary_key=True, default=uuid.uuid4)
    subnet_id = db.Column(UUID(True))
    ipAddress = db.Column()

    def __repr__(self):
        return f"<id {id}>"

