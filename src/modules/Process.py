from src.modules.Component import Component
from src.modules.Resource import Resource
from src.modules.Entity import Entity
from copy import deepcopy

class Process(Component):
    
    def __init__(self, name, target, min_range, max_range, distribution='uniform', num_resources=1, resource_name='resource', discipline='FCFS'):
        super(Process, self).__init__(name, target)

        self.setRandom(min_range, max_range, distribution)

        self.__numResources = num_resources
        self.__resourceName = resource_name
        self.__resources = [ Resource(self.__resourceName+' '+str(i)) for i in range(self.__numResources) ]
        
        self.__discipline = discipline
        self.__queue = []

        self.__output = []
    
    def receiveEntity(self, entity):
        self.printLog(entity.getName(), 'entered the queue at', entity.getTime())
        self.__queue.append(entity)
    
    def outputEntities(self, current_time):
        output = []
        removed = 0
        for i in range(len(self.__output)):
            try:
                entity = self.__output[i]
                if entity.getTime() <= current_time:
                    self.printLog(entity.getName(), 'finished the process at', current_time, 'with duration', entity.getLastDuration())
                    output.append(deepcopy(entity))
                    del self.__output[i-removed]
                    removed += 1
            except:
                pass
        
        return output
    
    def isEmpty(self):
        return len(self.__queue) == 0 and len(self.__output) == 0
    
    def __getNextEntity(self):
        entity = None
        if self.__discipline == 'FCFS':
            entity = deepcopy(self.__queue[0])
            del self.__queue[0]
        elif self.__discipline == 'LCFS':
            entity = deepcopy(self.__queue[-1])
            del self.__queue[-1]
        return entity
    
    def process(self, current_time):
        for i in range(self.__numResources):
            resource = self.__resources[i]
            if len(self.__queue) > 0:
                if not resource.busy(current_time):
                    entity = self.__getNextEntity()
                    duration = self.getRandomNumber()
                    resource.process(entity, current_time, duration)
                    self.printLog(entity.getName(), 'started the process at', current_time, 'by', resource.getName())

                    entity.appendEvent(self.getName(), current_time, duration)
                    self.__output.append(entity)