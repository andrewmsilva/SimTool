from src.modules.RandomInterval import RandomInterval

class Generator(object):

    def __init__(self, name, destination, generation_interval, distribution='uniform'):
        if not (isinstance(name, str)):
            raise ValueError('Name must be a string')
        self.__name = name

        if not (isinstance(destination, str)):
            raise ValueError('Destination must be a string')
        self.__destination = destination

        self.__randomGeneration = RandomInterval(generation_interval, distribution)

    def new(self, current_time):
        interval = -1
        while interval < 0:
            interval = self.__randomGeneration.get()
        
        return round(current_time+interval, 2)