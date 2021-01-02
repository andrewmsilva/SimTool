from src.modules.Random import Random

class Component(object):

    def __init__(self, name, target=None):
        self.__name = name
        self.__target = target
        self.__random = None
    
    def reset(self):
        pass
    
    @property
    def name(self):
        return self.__name

    @property
    def target(self):
        return self.__target
    
    def setRandom(self, min_range, max_range, distribution):
        self.__random = Random(min_range, max_range, distribution)
    
    @property
    def minRange(self):
        return self.__random.minRange
    
    @property
    def maxRange(self):
        return self.__random.maxRange

    @property
    def distribution(self):
        return self.__random.distribution
    
    def getRandomNumber(self):
        return self.__random.getRandomNumber()

    def printLog(self, message):
        print(self.__name+': '+message)