from src.modules.RandomRange import RandomRange

class Attendance(object):

    def __init__(self, start, end, duration):
        if not (isinstance(start, (int, float))):
            raise ValueError('Start time must be int or float')
        self.__start = start

        if not (isinstance(end, (int, float))):
            raise ValueError('End time must be int or float')
        self.__end = end

        if not (isinstance(duration, (int, float))):
            raise ValueError('Duration time must be int or float')
        self.__duration = duration
    
    def getStart(self):
        return self.__start
    
    def getEnd(self):
        return self.__end
    
    def getDuration(self):
        return self.__duration

class Server(object):
    __events = []
        

class Service(object):
    __queue = []

    def __init__(self, name, destination, duration_range, num_servers=1, discipline='FCFS', distribution='uniform'):
        if not (isinstance(name, str)):
            raise ValueError('Name must be a string')
        self.__name = name

        if not (isinstance(destination, str)):
            raise ValueError('Destination must be a string')
        self.__destination = destination

        if not (isinstance(num_servers, int) and num_servers > 0):
            raise ValueError('Number of num_servers must be an integer greater than 0')
        self.__numServers = num_servers
        
        if not (discipline == 'FCFS' or discipline == 'LCFS'):
            raise ValueError('Queue discipline must be "FCFS" or "LCFS"')
        self.__discipline = discipline

        self.__randomDuration = RandomRange(duration_range[0], duration_range[1], distribution)
    
    def __initServers(self):
        self.__servers = [ Server() for i in range(self.__numServers) ]
    
    def getName(self):
        return self.__name
    
    def getDestination(self):
        return self.__destination
    
    def addToQueue(self, entity):
        self.__queue.append(entity)
    
    def getQueue(self):
        return self.__queue
    
    def attend(self, start):
        pass
