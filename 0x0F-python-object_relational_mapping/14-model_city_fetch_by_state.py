#!/usr/bin/python3
"""print cities name"""
if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    ses = Session()
    for state, city in ses.query(City, State)\
            .join(State, State.id == City.state_id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    ses.close()
