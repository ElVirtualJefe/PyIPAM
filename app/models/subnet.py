from sqlalchemy.dialects.postgresql import UUID
import datetime,uuid

from . import db

class subnetModel(db.Model):
    """
    Subnet Model
    """

    # table name
    __tablename__ = 'subnets'

    id = db.Column(UUID(True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(48))
    ipAddresses = db.relationship('ipAddressModel', backref='ipAddresses', lazy=True)

    def __repr__(self):
        return f"<Subnet Name: {self.name}>"

