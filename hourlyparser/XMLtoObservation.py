__author__ = 'christopherfricke'
#- Global
import xml.dom.minidom
import datetime
import email.utils
import logging
import os

#- Local
import settings
import models.Observation


class XMLtoObservation():
    def __init__(self, xml_document):
        self.xml_document = xml_document
        self.observation = models.Observation.Observation()

    def parse(self):
        dom = xml.dom.minidom.parse(self.xml_document)
        root = dom.getElementsByTagName('current_observation')[0]

        try:
            # Try adding station geometry point
            point = 'POINT(%s %s)' % (root.getElementsByTagName(settings.shape[0])[0].firstChild.nodeValue,
                                      root.getElementsByTagName(settings.shape[1])[0].firstChild.nodeValue)
            setattr(self.observation, 'shape', point)
        except IndexError:
            pass

        for variable in settings.xml_items:
            try:
                try:
                    assert isinstance(variable[0], (list, tuple))  # Is it a list?
                    for sub_variable in variable[1]:
                        sub_root = root.getElementsByTagName(variable[0])[0]
                        attribute = '%s_%s' % (variable[0], sub_variable)
                        value = self._convert(sub_root.getElementsByTagName(sub_variable[0])[0].firstChild.nodeValue,
                                            variable)
                        setattr(self.observation, attribute[0], value)

                except AssertionError:
                    attribute = variable[0],
                    value = self._convert(root.getElementsByTagName(variable[0])[0].firstChild.nodeValue,
                                        variable)


                    setattr(self.observation, attribute[0], value)
            except IndexError:
                if settings.verbose:
                    logging.warning('\tAttribute does not exist: %s' % attribute)

            except AttributeError:
                if settings.verbose:
                    logging.warning('\tAttribute is null: %s' % attribute)

            except UnicodeEncodeError:
                if settings.verbose:
                    logging.warning('\t Unicode error with %s: %s' % (attribute, root.getElementsByTagName(variable[0])[0].firstChild.nodeValue))
        del root
        del dom
        os.remove(self.xml_document)

    def _convert(self, value, variable):
        try:
            if variable[1] == datetime.date:
                try:
                    # Parse it given a string, but if that fails then parse it using email mktime_tz
                    return datetime.datetime.strptime(value, variable[2])
                except (ValueError, IndexError) as e:
                    return datetime.datetime.fromtimestamp(email.utils.mktime_tz(email.utils.parsedate_tz(value)))
            elif variable[1] == str:
                return value
            else:
                return variable[1](value)
        except TypeError:
            if settings.verbose:
                logging.warning('\tCannot Parse %s with function %s' % (value, variable[1]))