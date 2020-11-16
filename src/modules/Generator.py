from src.modules.Random import Random
from src.modules.Interim import Interim

class Generator(Random):

    def __init__(self, name, target, min_range, max_range, distribution='uniform'):
        super(Generator, self).__init__(min_range, max_range, distribution)

        if not (isinstance(name, str)):
            raise ValueError('Name must be a string')
        self.__name = name

        if not (isinstance(target, str)):
            raise ValueError('Target must be a string')
        self.__target = target

        self.__nextInterim = None
        self.__nextId = 0
    
    def getName(self):
        return self.__name
    
    def getTarget(self):
        return self.__target
    
    def getNext(self, current_time=0):
        if self.__nextInterim == None or self.__nextInterim.getTime() < current_time:
            self.__nextInterim = Interim(self.__name+' '+str(self.__nextId), current_time + self.getRandomNumber())
            self.__nextId += 1
        if current_time == self.__nextInterim.getTime():
            return self.__nextInterim
        else:
            return False