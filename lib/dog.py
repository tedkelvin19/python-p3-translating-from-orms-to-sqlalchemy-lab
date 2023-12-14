from models import Dog
from sqlalchemy import create_engine
def create_table(base):
    engine = create_engine('sqlite:///database.db')
    with engine.connect() as connection:
        base.metadata.create_all(connection)
def save(session, dog):
    pass
    session.add(dog)
    session.commit()
    return session
def get_all(session):
    pass
    return session.query(Dog).all()

def find_by_name(session, name):
    pass
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    pass
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    pass
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    pass
    dog.breed = breed
    session.commit()
    return session