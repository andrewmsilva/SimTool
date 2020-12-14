import numpy as np

class Random(object):
    
    def __init__(self, min_range, max_range, distribution):
        self.__minRange = min_range
        self.__maxRange = max_range
        self.__distribution = distribution

        if self.__distribution == 'normal':
            interval = range(self.__minRange, self.__maxRange+1)
            self.__mean = np.mean(interval)
            self.__std = np.std(interval)
    
    def getRandomNumber(self):
        num = None
        while not num or (num < self.__minRange or num > self.__maxRange):
            if self.__distribution == 'uniform':
                num = np.random.uniform(self.__minRange, self.__maxRange)
            elif self.__distribution == 'normal':
                num = np.random.normal(self.__mean, self.__std)

        return int(np.rint(num))