import numpy as np

class RandomInterval(object):
    
    def __init__(self, interval, distribution='uniform'):
        if not (isinstance(interval, tuple) and all(isinstance(value, (int, float)) for value in interval) and interval[0] < interval[1]):
            raise ValueError('Interval must be a tuple containing two int or float values, where A < B')
        self.__interval = interval

        if not (distribution == 'uniform' or distribution == 'normal'):
            raise ValueError('Distribution must be "uniform" or "normal"')
        self.__distribution = distribution
    
    def get(self):
        num = None

        if self.__distribution == 'uniform':
            num = np.random.uniform(self.__interval[0], self.__interval[1])
        elif self.__distribution == 'normal':
            interval = range(self.__interval[0], self.__interval[1]+1)
            num = np.random.normal(np.mean(interval), np.std(interval))
        
        return num