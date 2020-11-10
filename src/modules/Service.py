from src.modules.Random import Random
from src.modules.Server import Server
from src.modules.Interim import Interim
from copy import deepcopy

class Service(Random):
    
    def __init__(self, name, target, min_range, max_range, distribution, num_servers=1, discipline='FCFS'):
        super(Service, self).__init__(min_range, max_range, distribution)

        if not (isinstance(name, str)):
            raise ValueError('Name must be a string')
        self.__name = name

        if not (isinstance(target, str)):
            raise ValueError('Target must be a string')
        self.__target = target

        if not (isinstance(num_servers, int) and num_servers > 0):
            raise ValueError('Number of num_servers must be an integer greater than 0')
        self.__numServers = num_servers
        self.__initServers()
        
        if not (discipline == 'FCFS' or discipline == 'LCFS'):
            raise ValueError('Queue discipline must be "FCFS" or "LCFS"')
        self.__discipline = discipline

        self.__queue = []
        self.__output = []

    def __initServers(self):
        self.__servers = [ Server() for i in range(self.__numServers) ]
    
    def getName(self):
        return self.__name
    
    def getTarget(self):
        return self.__target
    
    def receiveInterim(self, interim):
        if not (isinstance(interim, Interim)):
            raise ValueError('Only Interim objects can be imputed')
        self.__queue.append(interim)
    
    def sendInterims(self, current_time):
        output = []
        removed = 0
        for i in range(len(self.__output)):
            try:
                interim = self.__output[i]
                if interim.getTime() <= current_time:
                    output.append(deepcopy(interim))
                    del self.__output[i-removed]
                    removed += 1
            except:
                pass
        
        return output
    
    def __getNextInterim(self):
        interim = None
        if self.__discipline == 'FCFS':
            interim = deepcopy(self.__queue[0])
            del self.__queue[0]
        elif self.__discipline == 'LCFS':
            interim = deepcopy(self.__queue[-1])
            del self.__queue[-1]
        return interim
    
    def attend(self, current_time):
        for i in range(self.__numServers):
            server = self.__servers[i]
            if len(self.__queue) > 0:
                if not server.busy(current_time):
                    interim = self.__getNextInterim()
                    duration = self.getRandomNumber()
                    server.attend(interim, current_time, duration)
                    print(self.__name+':', interim.getName(), 'arrived at', interim.getTime(), 'and attended by server', i, 'from', current_time, 'to', current_time+duration)

                    interim.appendEvent(self.__name, current_time, duration)
                    self.__output.append(interim)