import json


class Pet:
    def __init__(self, name=None):
        self.name = name


class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed


class ExportJSON:
    def to_json(self):
        pass


class ExportXML:
    def to_xml(self):
        pass


class ExDog(Dog, ExportJSON, ExportXML):
    def __init__(self, name, breed=None):
        super().__init__(name, breed)
