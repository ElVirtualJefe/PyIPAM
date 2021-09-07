from sqlalchemy.dialects.postgresql import UUID
import datetime,uuid

from . import db

class vLanModel(db.Model):
    """
    vLAN Model
    """

    __tablename__ = "vlans"

    id = db.Column(UUID(True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(48))
    vlanNumber = db.Column(db.SmallInteger)
    description = db.Column(db.String(250))
    subnets = db.relationship('subnetModel', backref='subnets', lazy=True)
    dateLastEdited = db.Column(db.DateTime)

    def __repr__(self):
        return f"<vLAN: {self.vlanNumber} - {self.name}>"
