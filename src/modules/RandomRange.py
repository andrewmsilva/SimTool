import numpy as np

class RandomRange(object):
    
    def __init__(self, min, max, distribution='uniform'):
        if not (isinstance(min, int)):
            raise ValueError('Min value must be integer')
            
        if not (isinstance(max, int)):
            raise ValueError('Max value must be integer')

        if not (min < max):
            raise ValueError('Min value must be lower than max value')

        self.__min = min
        self.__max = max

        if not (distribution == 'uniform' or distribution == 'normal'):
            raise ValueError('Distribution must be "uniform" or "normal"')
        self.__distribution = distribution
    
    def getNumber(self):
        num = -1

        while num < self.__min or num > self.__max:
            if self.__distribution == 'uniform':
                num = np.random.uniform(self.__min, self.__max)
            elif self.__distribution == 'normal':
                interval = range(self.__min, self.__max+1)
                num = np.random.normal(np.mean(interval), np.std(interval))
        
        return int(num)