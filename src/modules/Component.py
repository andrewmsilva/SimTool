from src.modules.Random import Random

class Component(object):

    def __init__(self, name, target=None):
        self.__name = name
        self.__target = target
        self.__random = None
    
    def getName(self):
        return self.__name
    
    def getTarget(self):
        return self.__target
    
    def setRandom(self, min_range, max_range, distribution):
        self.__random = Random(min_range, max_range, distribution)
    
    def getMinRange(self):
        return self.__random.getMinRange()
    
    def getMaxRange(self):
        return self.__random.getMaxRange()

    def getDistribution(self):
        return self.__random.getDistribution()
    
    def getRandomNumber(self):
        return self.__random.getRandomNumber()

    def printLog(self, *args):
        print(self.__name+':', *args)