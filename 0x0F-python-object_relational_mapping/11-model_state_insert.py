#!/usr/bin/python3
""" script that adds the State object “Louisiana” to the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    make_session = sessionmaker(bind=engine)
    session = make_session()

    new_State = State(name='Louisiana')
    session.add(new_State)
    session.commit()

    print(new_State.id)
