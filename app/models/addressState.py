from sqlalchemy.dialects.postgresql import UUID
import datetime,uuid

from . import db

class addressStateModel(db.Model):
    """
    Address State Model
    """

    __tablename__ = "addressStates"

    id = db.Column(UUID(True), primary_key=True, default=uuid.uuid4)
    state = db.Column(db.String(48))

    def __repr__(self):
        return f"<State: {self.state}>"
