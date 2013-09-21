__author__ = 'christopherfricke'
import datetime
import local_settings

verbose = False

xml_url = 'http://w1.weather.gov/xml/current_obs/all_xml.zip'
temp_path = '/Users/christopherfricke/Source/Weather/NOAAHourly/HourlyParser/temp_path'

log = '/Users/christopherfricke/Source/Weather/NOAAHourly/HourlyParser/logs/log.txt'

db_instance = local_settings.db_instance

xml_items = [
    ('station_id', str),
    ('latitude', float),
    ('longitude', float),
    ('location', str),
    ('dewpoint_f', str),
    ('heat_index_f', float),
    ('mean_wave_degrees', str),
    ('mean_wave_dir', str),
    ('observation_time_rfc822', datetime.date),
    ('pressure_mb', float),
    ('pressure_tendency_mb', float),
    ('relative_humidity', float),
    ('temp_f', float),
    ('tide_ft', float),
    ('visibility_mi', float),
    ('water_column_height', float),
    ('wave_height_ft', float),
    ('water_temp_f', float),
    ('weather', str),
    ('wind_dir', str),
    ('wind_degrees',int),
    ('wind_mph', float),
    ('wind_gust_mph', float),
    ('windchill_f', float),
]