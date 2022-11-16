#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa """
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
    Session = sessionmaker(bind=eng)
    session = Session()
    for state in session.query(State):
        print("{}: {}".format(state.id, state.name))
