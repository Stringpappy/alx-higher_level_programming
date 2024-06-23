#!/usr/bin/python3
""" Python file similar to model_state.py named model_city.py
  that contains the class definition of a City"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    make_session = sessionmaker(bind=engine)
    session = make_session()

    city_l = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in city_l:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
