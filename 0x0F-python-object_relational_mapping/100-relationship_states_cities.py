#!/usr/bin/python3
"""
    Lists all State objects from the database
"""

from relationship_state import Base, State
from relationship_city import City
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
    new_city = City(name='San Francisco')
    new = State(name='California')
    new.cities.append(new_city)
    session.add(new)
    session.add(new_city)

    session.commit()
    session.close()
