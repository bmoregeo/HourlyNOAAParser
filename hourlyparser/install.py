__author__ = 'christopherfricke'
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

import settings
from models import Observation


Base = declarative_base()


def create():

    # create a connection to a sqlite database
    # turn echo on to see the auto-generated SQL
    engine = create_engine(settings.db_instance, echo=True)

    # get a handle on the table object
    users_table = Observation.__table__
    # get a handle on the metadata
    metadata = Base.metadata
    metadata.create_all(engine)

if __name__ == '__main__':
    create()