#!/usr/bin/python3
"""
    Lists all State objects from the database
"""

from model_state import Base, State
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                            sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url)
    param = "SELECT * FROM states ORDER BY id ASC"
    result = engine.execute(param)
    for row in result:
        if 'a' in row[1]:
            print("{}: {}".format(row[0], row[1]))
