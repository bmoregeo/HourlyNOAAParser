__author__ = 'christopherfricke'
#- Global
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import zipfile
import requests
import StringIO
import os
import logging

#- Local
import settings
import XMLtoObservation

class hourlyzip():
    def __init__(self, url, temp_path, db_instance):
        self.url = url
        self.temp_path = temp_path
        self.db_instance = db_instance

    def download(self):
        r = requests.get(self.url)
        z = zipfile.ZipFile(StringIO.StringIO(r.content))
        z.extractall(path=self.temp_path)
        del r
        del z

    def load(self):
        engine = create_engine(self.db_instance)

        Session = sessionmaker(bind=engine)
        session = Session()

        for f in os.listdir(self.temp_path):
            logging.info('Extracting %s' % f)
            x = XMLtoObservation.XMLtoObservation(os.path.join(hourlyparser.settings.temp_path, f))
            x.parse()
            session.add(x.observation)

        session.commit()
