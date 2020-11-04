from src.modules.RandomRange import RandomRange

class Generator(object):

    def __init__(self, name, destination, generation_range, distribution='uniform'):
        if not (isinstance(name, str)):
            raise ValueError('Name must be a string')
        self.__name = name

        if not (isinstance(destination, str)):
            raise ValueError('Destination must be a string')
        self.__destination = destination

        self.__random = RandomRange(generation_range[0], generation_range[1], distribution)
        self.__next = None
    
    def getName(self):
        return self.__name
    
    def getDestination(self):
        return self.__destination
    
    def getNext(self, current_time=0):
        if self.__next == None or self.__next < current_time:
            self.__next = current_time + self.__random.getNumber()
        
        return current_time == self.__next