import csv
import os

class CarBase:

    def __init__(self, brand, photo_file_name, carrying):

        import pdb
        pdb.set_trace()
        self.brand = brand
        self.photo_file_name = photo_file_name
        try:
            self.carrying = float(carrying)

        except ValueError:
            pass



    def get_photo_file_ext(self):
        ext = os.path.splitext(self.photo_file_name)[1]
        return ext


class Car(CarBase):
    car_type = 'car'
    passenger_seats_count = None


    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


    passenger = property()

    @passenger.getter
    def get_passenger(self):
        return self.passenger_seats_count

class Truck(CarBase):
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)

        count_whl = body_whl.count('x')
        try:
            if body_whl != '' and body_whl != None and count_whl <= 2:
                self.body_whl = body_whl
                lis = self.body_whl.split('x')
                self.body_length = float(lis[0])
                self.body_width = float(lis[1])
                self.body_height = float(lis[2])
            else:
                self.body_whl = float(0)
                self.body_length = float(0)
                self.body_width = float(0)
                self.body_height = float(0)
        except ValueError:
            self.body_whl = float(0)
            self.body_length = float(0)
            self.body_width = float(0)
            self.body_height = float(0)

    def get_body_volume(self):
        capacity = self.body_width * self.body_height * self.body_length
        return capacity


class SpecMachine(CarBase):
    car_type = 'spec_machine'
    extra = None

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


    extra1 = property()

    @extra1.getter
    def get_extra(self):
        return self.extra


def get_car_list(file_name):
    ''' Парсит объекты из csv'''
    car_lists = []

    def get_ext(somefilename):
        if somefilename != '.jpeg' and somefilename != '.jpg' and somefilename != '.png' and somefilename != '.gif':
            result = somefilename.endswith(('.jpeg', '.jpg', '.png', '.gif'))
            return result



    def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    with open(file_name, 'r') as csv_fd:
        data = csv.DictReader(csv_fd, delimiter=';')
        for row in data:
            if row['car_type'] == 'car':
                if row['brand'] != None and row['photo_file_name'] != None and row['carrying'] != None and row[
                    'passenger_seats_count'] != None:
                    if row['brand'] != '' and row['photo_file_name'] != '' and row['carrying'] != '' and row[
                        'passenger_seats_count'] != '' and row['passenger_seats_count'].isdigit() == True and (row['carrying'].isdigit() == True or isfloat(row['carrying']) == True) \
                            and get_ext(row['photo_file_name']) == True:
                        car = Car(row['brand'], row['photo_file_name'], row['carrying'], row['passenger_seats_count'])
                        car_lists.append(car)

            elif row['car_type'] == 'truck':
                if row['brand'] != None and row['photo_file_name'] != None and row['carrying'] != None:
                    if row['brand'] != '' and row['photo_file_name'] != '' and row['carrying'] != '' and (row['carrying'].isdigit() == True or isfloat(row['carrying']) == True)\
                            and get_ext(row['photo_file_name']) == True:
                        truck = Truck(row['brand'], row['photo_file_name'], row['carrying'], row['body_whl'])
                        car_lists.append(truck)

            elif row['car_type'] == 'spec_machine':
                if row['brand'] != None and row['photo_file_name'] != None and row['carrying'] != None and row['extra'] != None:
                    if row['brand'] != '' and row['photo_file_name'] != '' and row['carrying'] != '' and row['extra'] != '' and (row['carrying'].isdigit() == True or isfloat(row['carrying']) == True)\
                            and get_ext(row['photo_file_name']) == True:
                        specmachine = SpecMachine(row['brand'], row['photo_file_name'], row['carrying'], row['extra'])
                        car_lists.append(specmachine)

    return car_lists

#print(len(get_car_list(r'C:\Users\Denis\Desktop\Скрипты\Cars\coursera_week3_cars.csv')))
