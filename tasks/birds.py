class User:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show(self):
        print(f'{self.name} ({self.phone})')

class Friend(User):
    def show(self):
        print(f'Имя: {self.name} || Телефон: {self.phone}')

user = User("Виктор Гюго", "+33 1 42 72 10 16")
friend = Friend("Виктор Гюго", "+33 1 42 72 10 16")
user.show()
friend.show()


# импортируем функции из библиотеки math для рассчёта расстояния

from math import radians, sin, cos, acos

class Point:
    def __init__(self, latitude, longitude):
        self.latitude = radians(latitude)
        self.longitude = radians(longitude)

    # считаем расстояние между двумя точками в км
    def distance(self, other):
        cos_d = sin(self.latitude) * sin(other.latitude) + cos(self.latitude) * cos(other.latitude) * cos(
        self.longitude - other.longitude)
        return 6371 * acos(cos_d)

class City(Point):
    def __init__(self, latitude, longitude, name, population):
        self.name = name
        self.population = population
        super().__init__(latitude, longitude)

    def show(self):
        print(f"Город {self.name}, население {self.population} чел.")

class Mountain(Point):
    def __init__(self, name, latitude, longitude, height):
        self.name = name
        self.height = height
        super().__init__(latitude,longitude)

    def show(self):
        print(f"Высота горы {self.name} - {self.height} м.")
    # Переопределите метд show(self):
    # информацию о горе нужно вывести в формате:
    # "Высота горы <название> - <высота> м."

Moscow = City(55,37,"Moscow", 13104177)
Everest = Mountain("Everest", 27, 86, 8848)

Moscow.show()
Everest.show()
print(Point.distance(Moscow,Everest))