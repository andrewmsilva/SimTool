from src.modules.RandomInterval import RandomInterval

class Generator(object):

    def __init__(self, name, destination, generation_interval, max_generation, distribution='uniform'):
        if not (isinstance(name, str)):
            raise ValueError('Name must be a string')
        self.__name = name

        if not (isinstance(destination, str)):
            raise ValueError('Destination must be a string')
        self.__destination = destination

        if not (isinstance(max_generation, (int, float))):
            raise ValueError('Max generation must be an int or float')
        self.__maxGeneration = max_generation

        self.__randomGeneration = RandomInterval(generation_interval, distribution)
    
    def getName(self):
        return self.__name
    
    def getDestination(self):
        return self.__destination
    
    def entities(self, current_time=0):
        entities = []
        while current_time <= self.__maxGeneration:
            current_time = self.newEntity(current_time)
            if current_time <= self.__maxGeneration:
                entities.append(current_time)
        return entities

    def newEntity(self, current_time=0):
        interval = -1
        while interval < 0:
            interval = self.__randomGeneration.get()
        
        return round(current_time+interval, 2)