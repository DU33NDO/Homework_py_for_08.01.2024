from datetime import datetime, timedelta


class Stadium:
    def __init__(self):
        self.name = None
        self.date = None
        self.country = None
        self.city = None
        self.capacity = None

    def __repr__(self):
        return f"Name: {self.name}, Open date: {self.date}, Country: {self.country}, City: {self.city}, Capacity: {self.capacity}"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_country(self):
        return self.country

    def set_country(self, country):
        self.country = country

    def get_city(self):
        return self.country

    def set_city(self, country):
        self.country = country

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, capacity):
        self.capacity = capacity


name = input("name: ")
date = datetime.strptime(input("Open date: "), "%d.%m.%Y")
country = input("Country: ")
city = input("City: ")
capacity = int(input("Capacity: "))

ex2 = Stadium()
ex2.set_name(name)
ex2.set_date(date)
ex2.set_city(city)
ex2.set_country(country)
ex2.set_capacity(capacity)
print(ex2)
