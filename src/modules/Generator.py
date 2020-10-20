import numpy as np

class Generator(object):

    def __init__(self, name, interval, destination, distribution='uniform'):
        if not (isinstance(name, str)):
            raise ValueError('Name must be a string')
        self.__name = name

        if not (isinstance(interval, tuple) and all(isinstance(value, (int, float)) for value in interval) and interval[0] < interval[1]):
            raise ValueError('Interval must be a tuple containing two int or float values, where A < B')
        self.__interval = interval

        if not (isinstance(destination, str)):
            raise ValueError('Destination must be a string')
        self.__destination = destination
        
        if not (distribution == 'uniform' or distribution == 'normal'):
            raise ValueError('Distribution must be "uniform" or "normal"')
        self.__distribution = distribution
    
    def __randomNumber(self):
        num = None
        if self.__distribution == 'uniform':
            num = np.random.uniform(self.__interval[0], self.__interval[1])
        elif self.__distribution == 'normal':
            interval = range(self.__interval[0], self.__interval[1]+1)
            num = np.random.normal(np.mean(interval), np.std(interval))
        return num

    def generate(self, current_time):
        interval = -1
        while interval < 0:
            interval = self.__randomNumber()
        
        return round(current_time+interval, 2)