#!/usr/bin/python3
"""documentation here for 7"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    db = {'drivername': 'mysql+mysqldb',
          'host': 'localhost',
          'port': '3306',
          'username': sys.argv[1],
          'password': sys.argv[2],
          'database': sys.argv[3]}
    url = URL.create(**db)
    engine = create_engine(url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and print them
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
