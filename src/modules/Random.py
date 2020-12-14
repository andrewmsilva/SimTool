import numpy as np

class Random(object):
    
    def __init__(self, min_range, max_range, distribution):
        self.__minRange = min_range
        self.__maxRange = max_range
        self.__distribution = distribution
    
    def getRandomNumber(self):
        num = None
        while not num or (num < self.__minRange or num > self.__maxRange):
            if self.__distribution == 'uniform':
                num = np.random.uniform(self.__minRange, self.__maxRange)
            elif self.__distribution == 'normal':
                interval = range(self.__minRange, self.__maxRange+1)
                num = np.random.normal(np.mean(interval), np.std(interval))
        
        return int(num)