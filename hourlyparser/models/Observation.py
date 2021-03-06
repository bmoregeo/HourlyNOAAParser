__author__ = 'christopherfricke'
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from geoalchemy import Point, GeometryColumn

from hourlyparser import settings

engine = create_engine(settings.db_instance, echo=True)

Base = declarative_base()


class Observation(Base):
    __tablename__ = 'observation'

    reading_id = Column(Integer, primary_key=True)
    station_id = Column(String(10))
    location = Column(String(50))
    dewpoint_f = Column(Float)
    heat_index_f = Column(Float)
    mean_wave_degrees = Column(Float)
    mean_wave_dir = Column(String(20))
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
    weather = Column(String(50))
    windchill = Column(Float)
    wind_dir = Column(String(20))
    wind_degrees = Column(String(10))
    wind_mph = Column(Float)
    wind_gust_mph = Column(Float)
    shape = GeometryColumn(Point(2))

    def __init__(self):
        """Constructor"""
        pass

    def __repr__(self):
        return "<User('%s','%s')>" % (self.reading_id, self.observation_time)


users_table = Observation.__table__

Base.metadata.create_all(engine)