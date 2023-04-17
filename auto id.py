import uuid 

class Body(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    primary_contact = db.Column(db.String(55), nullable=False)
    cause_of_death = db.Column(db.String(100), nullable=False)
    date_of_arrival = db.Column(db.String(20), nullable=False)