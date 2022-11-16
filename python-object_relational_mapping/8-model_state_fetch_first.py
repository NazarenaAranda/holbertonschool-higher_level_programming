#!/usr/bin/python3
""" """
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
    first_state = session.query(State).order_by(State.id).first()
    if first_state is not None:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
