#!/usr/bin/python3
"""Fetches all cities in the City table"""

if __name__ == "__main__":
    import sys
    from model_city import City
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
        ))

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City, State).join(
            State,
            City.state_id == State.id,
            isouter=False).order_by(City.id)

    for result in results:
        print("{}: ({}) {}".format(
            result.State.name,
            result.City.id,
            result.City.name))
