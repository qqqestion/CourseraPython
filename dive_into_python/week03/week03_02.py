import csv
import os.path


class CarBase:
    def __init__(self, car_type, photo_path, brand, carrying):
        self.car_type = car_type
        self.photo_file_name = photo_path
        self.brand = brand
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]

    @staticmethod
    def _check_params(car_type, photo_path, brand, carrying):
        root, ext = os.path.splitext(photo_path)
        return car_type == '' or root == '' or \
               ext == '' or brand == '' or carrying == ''

    @classmethod
    def create_car_by_label(cls, car_type, photo_path, brand, carrying,
                            pass_count, body_whl, extra):
        if cls._check_params(car_type, photo_path, brand, carrying):
            raise ValueError('create_car_by_label: invalid args')

        if car_type == 'car' and extra == '' and body_whl == '':
            car = Car(photo_path=photo_path, brand=brand, carrying=carrying,
                      passenger_seats_count=pass_count)
        elif car_type == 'truck' and pass_count == '' and extra == '':
            car = Truck(photo_path=photo_path, brand=brand, carrying=carrying,
                        body_whl=body_whl)
        elif car_type == 'spec_machine' and pass_count == '' and body_whl == '':
            car = SpecMachine(photo_path=photo_path, brand=brand,
                              carrying=carrying, extra=extra)
        else:
            raise ValueError('create_car_by label: unknown car_type!')
        return car


class Car(CarBase):
    def __init__(self, brand, photo_path, carrying, passenger_seats_count):
        if passenger_seats_count == '':
            raise ValueError('__init__(Car(CarBase)): passenger_seats == \'\'')
        super().__init__(car_type='car', photo_path=photo_path, brand=brand,
                         carrying=carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_path, carrying, body_whl):
        body_split = body_whl.split('x')
        if len(body_split) != 3:
            body_split = (0, 0, 0)
        super().__init__(car_type='truck', photo_path=photo_path, brand=brand,
                         carrying=carrying)
        length, width, height = body_split
        self.body_length = float(length)
        self.body_width = float(width)
        self.body_height = float(height)

    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width


class SpecMachine(CarBase):
    def __init__(self, brand, photo_path, carrying, extra):
        if extra == '':
            raise ValueError('__init__SpecMachine(CarBase): extra == \'\'')
        super().__init__(car_type='spec_machine', photo_path=photo_path,
                         brand=brand, carrying=carrying)
        self.extra = extra


def read_car(params):
    if len(params) != 7:
        raise ValueError('read_car: not enough info')
    label, brand, pass_count, photo_path, body_whl, carrying, extra = tuple(params)
    car = CarBase.create_car_by_label(label, photo_path, brand, carrying,
                                      pass_count, body_whl, extra)
    return car


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            try:
                car = read_car(row)
                car_list.append(car)
            except ValueError:
                continue

    return car_list


def main():
    cars = get_car_list('../files/test.csv')
    print(len(cars))
    for car in cars:
        print(car.__dict__)


if __name__ == '__main__':
    main()
