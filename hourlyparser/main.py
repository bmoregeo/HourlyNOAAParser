__author__ = 'christopherfricke'
#- Global
import logging

#- Local
import settings
import hourlyzip

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename=settings.log,
                    level=logging.INFO)


if __name__ == '__main__':
    hz = hourlyzip.hourlyzip(settings.xml_url, settings.temp_path, settings.db_instance)
    hz.download()
    hz.load()

    del hz