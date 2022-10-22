class Ciclista:
    def __init__(self):
        self.__name=None
        self.__age=None
        self.__country=None
        self.__time=None

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def country(self):
        return self.__country

    @property
    def time(self):
        return self.__time

    #setters
    @name.setter
    def name(self,name):
        self.__name=name

    @age.setter
    def age(self,age):
        self.__age=age

    @country.setter
    def country(self,country):
        self.__country=country

    @time.setter
    def time(self,time):
        self.__time=time
        