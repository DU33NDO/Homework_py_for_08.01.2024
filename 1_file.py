class Car:
    def __init__(self):
        self.mark = None
        self.year_of_release = None
        self.manufacturer = None
        self.volume_eng = None
        self.color = None
        self.cost = None

    def __repr__(self):
        return f"Mark - {self.mark}, Year of release - {self.year_of_release}, Manufacturer - {self.manufacturer}, Engine's Volume - {self.volume_eng}, Color - {self.color}, Cost - {self.cost} tenge"

    def get_mark(self):
        return self.mark

    def set_mark(self, mark):
        self.mark = mark

    def get_year_of_release(self):
        return self.get_year_of_release

    def set_year_of_release(self, year_of_release):
        self.year_of_release = year_of_release

    def get_manufacturer(self):
        return self.manufacturer

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_volume_eng(self):
        return self.volume_eng

    def sete_volume_eng(self, volume_eng):
        self.volume_eng = volume_eng

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost


mark = input("Car's mark: ")
year_of_release = int(input("Year of release: "))
manufacturer = input("manufacturer: ")
volume_eng = int(input("Volume of engine: "))
color = input("color of a car: ")
cost = int(input("cost in tenge: "))

ex = Car()
ex.set_mark(mark)
ex.set_year_of_release(year_of_release)
ex.set_manufacturer(manufacturer)
ex.sete_volume_eng(volume_eng)
ex.set_color(color)
ex.set_cost(cost)
print(ex)
