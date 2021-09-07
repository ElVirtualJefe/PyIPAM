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
    masterSubnet_id = db.Column(UUID(True), db.ForeignKey('subnets.id'), nullable=True)
    vlan_id = db.Column(UUID(True), db.ForeignKey('vlans.id'), nullable=True)
    allowRequests = db.Column(db.Boolean, default=False, nullable=False)
    dateLastEdited = db.Column(db.DateTime)
    dateLastScanned = db.Column(db.DateTime)
    dateLastDiscovered = db.Column(db.DateTime)
    doDiscovery = db.Column(db.Boolean)
    doScan = db.Column(db.Boolean)

    def __repr__(self):
        return f"<Subnet Name: {self.name}>"

