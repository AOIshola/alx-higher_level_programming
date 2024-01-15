#!/usr/bin/python3
"""List States module"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
        ))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.id==1).first()
#    for state in states:
    print("{}: {}".format(states.id, states.name))
