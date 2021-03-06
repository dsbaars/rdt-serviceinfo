"""
Data objects

Module containing import object types used throughout the serviceinfo package.
"""

class Service(object):
    """
    Service describes an unique transportation service on a certain date.
    Each service has an ID, a servicenumber, two or more stops and metadata,
    like cancellation status or the mode of transportation.
    """

    service_id = 0
    servicenumber = 0
    cancelled = False
    stops = []
    service_date = None
    transport_mode = None
    transport_mode_description = None
    company_code = None
    company_name = None

    # Used by ServiceStore to specifiy data source, defaults to None:
    source = None

    def __init__(self):
        self.stops = []

    def __repr__(self):
        return "<Service i%s / %s%s-%s @ %s [%s stops]>" % (self.service_id,
            self.transport_mode, self.servicenumber, self.get_destination_str(),
            self.get_servicedate_str(), len(self.stops))

    def get_servicedate_str(self):
        """
        Retrieve the servicedate as a string in YYYY-MM-DD format.
        """

        return self.service_date.strftime('%Y-%m-%d')

    def get_destination(self):
        """
        Retrieve the last stop for this service.
        """

        return self.stops[-1]

    def get_destination_str(self):
        """
        Retrieve the stop code of the last stop for this service.
        """

        return self.get_destination().stop_code


class ServiceStop(object):
    """
    ServiceStop objects describe one single stop of a service.
    A ServiceStop contains data like the stop_code and stop_name of a station,
    arrival- and departure date/time, cancellation status, etc.
    """

    service_id = 0
    stop_code = None
    stop_name = None
    departure_time = None
    scheduled_departure_platform = None
    actual_departure_platform = None
    departure_delay = 0
    arrival_time = None
    scheduled_arrival_platform = None
    actual_arrival_platform = None
    arrival_delay = 0
    cancelled_arrival = False
    cancelled_departure = False
    servicenumber = 0
    attributes = []

    def __init__(self, stop_code, stop_name=None):
        self.stop_code = stop_code
        self.stop_name = stop_name
        self.attributes = []

    def __repr__(self):
        return "<ServiceStop @ %s>" % self.stop_code

    def get_departure_platform(self):
        """
        Return the departure platform. Uses the actual platform if set, returns
        the scheduled departure platform otherwise.
        """

        if self.actual_departure_platform is not None:
            return self.actual_departure_platform
        else:
            return self.scheduled_departure_platform

    def get_attribute_dicts(self):
        attrs = []
        for attribute in self.attributes:
            attrs.append(attribute.get_dict())
        return attrs

    def set_attribute_dicts(self, dicts):
        self.attributes = []
        for attribute in dicts:
            self.attributes.append(Attribute.from_dict(attribute))

class Attribute(object):
    code = None
    description = None
    processing_code = None

    CODE_BOARDING_ONLY = 6
    CODE_UNBOARDING_ONLY = 7

    def __init__(self, code, description):
        self.code = code
        self.description = description

    def get_dict(self):
        return {"code": self.code,
                "description": self.description,
                "processing_code": self.processing_code}

    @staticmethod
    def from_dict(dict):
        attr = Attribute(dict['code'], dict['description'])
        attr.processing_code = dict['processing_code']
        return attr