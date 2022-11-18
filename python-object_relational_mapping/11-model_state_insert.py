#!/usr/bin/python3
"""script that adds the State object “Louisiana” to the database
hbtn_0e_6_usa"""
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
    state_new = State(name='Louisiana')
    session.add(state_new)
    state = session.query(State).filter_by(name='Louisiana').first()
    print('{}'.format(state_new.id))
    session.commit()
