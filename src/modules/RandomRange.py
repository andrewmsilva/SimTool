import numpy as np

class RandomRange(object):
    
    def __init__(self, range, distribution='uniform'):
        if not (isinstance(range, tuple) and all(isinstance(value, int) for value in range) and range[0] < range[1]):
            raise ValueError('Range must be a tuple containing two int values, where A < B, A >= 0, and B > 1')
        self.__range = range

        if not (distribution == 'uniform' or distribution == 'normal'):
            raise ValueError('Distribution must be "uniform" or "normal"')
        self.__distribution = distribution
    
    def getNumber(self):
        num = -1

        while num < self.__range[0] or num > self.__range[1]:
            if self.__distribution == 'uniform':
                num = np.random.uniform(self.__range[0], self.__range[1])
            elif self.__distribution == 'normal':
                range = range(self.__range[0], self.__range[1]+1)
                num = np.random.normal(np.mean(range), np.std(range))
        
        return int(num)