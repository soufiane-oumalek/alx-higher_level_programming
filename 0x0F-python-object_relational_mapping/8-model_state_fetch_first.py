#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                          .format(sys.argv[1], sys.argv[2],
                                sys.argv[3]), pool_pre_ping=true)
    base.metadata.create_all(enging)
    ses = Session(engine)
    one = ses.query(State).order_by(State.id).first()
    
    if one:
        print('{0}: {1}'.format(instance.id, instance.name))
    else
        print("Nothing")
    ses.close()
