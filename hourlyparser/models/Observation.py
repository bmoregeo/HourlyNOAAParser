__author__ = 'christopherfricke'
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from hourlyparser import settings

engine = create_engine(settings.db_instance, echo=True)

Base = declarative_base()


class Observation(Base):
    __tablename__ = 'observation'

    reading_id = Column(Integer, primary_key=True)
    station_id = Column(String(10))
    latitude = Column(Float)
    longitude = Column(Float)
    location = Column(String)
    dewpoint_f = Column(Float)
    heat_index_f = Column(Float)
    mean_wave_degrees = Column(Float)
    mean_wave_dir = Column(String)
    observation_time_rfc822 = Column(DateTime)
    pressure_mb = Column(Float)
    pressure_tendency_mb = Column(Float)
    relative_humidity = Column(Float)
    temp_f = Column(Float)
    tide_ft = Column(Float)
    visibility_mi = Column(Float)
    water_column_height = Column(Float)
    water_temp_f = Column(Float)
    wave_height_ft = Column(Float)
    weather = Column(String)
    windchill = Column(Float)
    wind_dir = Column(String)
    wind_degrees = Column(String)
    wind_mph = Column(Float)
    wind_gust_mph = Column(Float)

    def __init__(self):
        """Constructor"""
        pass

    def __repr__(self):
        return "<User('%s','%s')>" % (self.reading_id, self.observation_time)


users_table = Observation.__table__

Base.metadata.create_all(engine)