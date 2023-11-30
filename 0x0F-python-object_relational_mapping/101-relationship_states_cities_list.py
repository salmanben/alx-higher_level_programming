#!/usr/bin/python3
""" lists the State object with the name passed as argument from the database
"""
import sys
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from relationship_city import City
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for obj in session.query(State).order_by(State.id):
        print(obj.id, obj.name, sep=": ")
        for city_ins in obj.cities:
            print("    ", end="")
            print(city_ins.id, city_ins.name, sep=": ")
