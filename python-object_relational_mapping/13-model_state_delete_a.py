#!/usr/bin/python3
"""script that deletes all State objects with a name containing the letter
a from the database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    db = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                     argv[2],
                                                     argv[3])
    eng = create_engine(db)
    Base.metadata.create_all(eng)
    Session = sessionmaker(eng)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%'))
    for state in states:
        session.delete(state)
    session.commit()
