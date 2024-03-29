#!/usr/bin/python3
"""
    Lists all State objects from the database
"""

from model_state import Base, State
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
    for row in session.query(State).filter(State.name.like("%a%")).order_by(State.id).all():
        print("{}: {}".format(row.id, row.name))

    session.close()
