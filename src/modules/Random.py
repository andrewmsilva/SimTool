import numpy as np

class Random(object):
    
    def __init__(self, min_range, max_range, distribution):
        if not (isinstance(min_range, int)):
            raise ValueError('Min value must be an integer')
            
        if not (isinstance(max_range, int)):
            raise ValueError('Max value must be an integer')

        if not (min_range < max_range):
            raise ValueError('Min value must be lower than max_range value')

        self.__minRange = min_range
        self.__maxRange = max_range

        if not (distribution == 'uniform' or distribution == 'normal'):
            raise ValueError('Distribution must be "uniform" or "normal"')
        self.__distribution = distribution
    
    def getRandomNumber(self):
        num = -1

        while num < self.__minRange or num > self.__maxRange:
            if self.__distribution == 'uniform':
                num = np.random.uniform(self.__minRange, self.__maxRange)
            elif self.__distribution == 'normal':
                interval = range(self.__minRange, self.__maxRange+1)
                num = np.random.normal(np.mean(interval), np.std(interval))
        
        return int(num)