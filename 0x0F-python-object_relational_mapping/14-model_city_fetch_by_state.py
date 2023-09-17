#!/usr/bin/python3
"""
    Lists all State objects from the database
"""

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                            sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for row in session.query(City).order_by(City.id).all():
        state = session.query(State).filter(State.id == row.state_id).first()
        print("{}: ({}) {}".format(state.name, row.id, row.name))

    session.close()
