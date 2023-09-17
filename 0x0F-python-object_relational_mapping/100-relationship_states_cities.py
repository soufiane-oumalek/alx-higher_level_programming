#!/usr/bin/python3
"""creates the State “California” with the City “San Francisco” from the
database hbtn_0e_100_usa: (100-relationship_states_cities.py)"""
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    ses = Session()
    nState = State(name='California')
    nCity = City(name='San Francisco', state=nState)
    ses.add_all([nState, nCity])
    ses.commit()
    ses.close()
