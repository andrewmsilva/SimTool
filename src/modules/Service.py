from src.modules.Random import Random
from src.modules.Server import Server
from src.modules.Interim import Interim

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

        self.__input = []
        self.__output = []

    def __initServers(self):
        self.__servers = [ Server() for i in range(self.__numServers) ]
    
    def getName(self):
        return self.__name
    
    def getTarget(self):
        return self.__target
    
    def inputInterim(self, interim):
        if not (isinstance(interim, Interim)):
            raise ValueError('Only Interim objects can be added to queue')
        self.__input.append(interim)
    
    def getQueue(self):
        return self.__input
    
    def __getNextInterim(self):
        if self.__discipline == 'FCFS':
            return self.__input.pop(0)
        elif self.__discipline == 'LCFS':
            return self.__input.pop()
    
    def attend(self, current_time):
        for i in range(self.__numServers):
            server = self.__servers[i]
            if len(self.__input) > 0:
                if not server.busy(current_time):
                    interim = self.__getNextInterim()
                    duration = self.getRandomNumber()
                    server.attend(interim, current_time, duration)
                    print(self.__name+':', interim.getName(), 'arrived at', interim.getTime(), 'and attended by server', i, 'from', current_time, 'to', current_time+duration)

                    #interim.appendEvent(current_time, duration)
                    self.__output.append(interim)
