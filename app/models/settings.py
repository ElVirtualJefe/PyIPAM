from sqlalchemy.dialects.postgresql import UUID
import datetime,uuid

from . import db

class settingsModel(db.Model):
    """
    Settings Model
    """

    __tablename__ = "settings"

    id = db.Column(UUID(True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(48))
    value = db.Column(db.String(120))

    def __repr__(self):
        return f"<Setting - {self.name}: {self.value}>"
