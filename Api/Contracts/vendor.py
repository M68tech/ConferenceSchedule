import json


class Vendor:
    def __init__(self, vendor_name: str, vendor_description: str, vendor_website: str):
        self.name = vendor_name
        self.description = vendor_description
        self.website = vendor_website

    def serialize(self):
        return self.__dict__
