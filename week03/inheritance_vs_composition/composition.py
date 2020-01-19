import json


class Pet:
    def __init__(self, name=None):
        self.name = name


class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed


class PetExport:
    def export(self, pet):
        raise NotImplementedError


class ExportJSON(PetExport):
    def export(self, pet):
        return json.dumps({
            'name': pet.name,
            'breed': pet.breed
        })


class ExportXML(PetExport):
    def export(self, pet):
        return f"""<?xml version="1.0" encoding="utf-8"?>
<dog>
    <name>{pet.name}</name>
    <breed>{pet.breed}</breed
</dog>
"""


class ExDog(Dog):
    def __init__(self, name, breed=None, exporter=None):
        super().__init__(name, breed)
        self._exporter = exporter or ExportJSON()
        if not isinstance(self._exporter, PetExport):
            raise ValueError

    def export(self):
        return self._exporter.export(self)


def main():
    dog = ExDog('Rax', 'Shepherd', exporter=ExportJSON())
    print(dog.export())


if __name__ == '__main__':
    main()
