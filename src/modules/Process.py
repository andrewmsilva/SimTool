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
        self.__discipline = discipline

        self.reset()
    
    def reset(self):
        self.__resources = [ Resource(self.__resourceName+' '+str(i)) for i in range(self.__numResources) ]
        self.__queue = []
        self.__output = []

        self.__queueWaiting = []
        self.__immediateProcessing = 0
        self.__durations = []
    
    # Input and output management
    
    def receiveEntity(self, entity):
        self.printLog('{}: {} entered the queue at {}'.format(self.name, entity.name, entity.currentTime))
        self.__queue.append(entity)
    
    def outputEntities(self, current_time):
        output = []
        removed = 0
        for i in range(len(self.__output)):
            try:
                entity = self.__output[i]
                if entity.currentTime <= current_time:
                    self.printLog('{}: {} finished the process at {} with duration {}'.format(self.name, entity.name, current_time, entity.lastDuration))
                    output.append(deepcopy(entity))
                    del self.__output[i-removed]
                    removed += 1
            except:
                pass
        
        return output
    
    # Processing
    
    @property
    def processing(self):
        return len(self.__queue) > 0 or len(self.__output) > 0
    
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
                    # Scheduling
                    entity = self.__getNextEntity()
                    # Computing waiting time
                    waiting_time = current_time-entity.currentTime
                    if waiting_time > 0:
                        self.__queueWaiting.append(waiting_time)
                    else:
                        self.__immediateProcessing += 1
                    # Processing entity
                    duration = self.getRandomNumber()
                    self.__durations.append(duration)
                    resource.process(entity, current_time, duration)
                    self.printLog('{}: {} started the process at {} by {}'.format(self.name, entity.name, current_time, resource.name))

                    entity.appendEvent(self.name, current_time, duration)
                    self.__output.append(entity)
    
    # Saving

    def saveMe(self, writer, columns):
        row = { key: None for key in columns }
        row['type'] = 'P'
        row['name'] = self.name
        row['target'] = self.target
        row['min_range'] = self.minRange
        row['max_range'] = self.maxRange
        row['distribution'] = self.distribution
        row['num_resources'] = self.__numResources
        row['resource_name'] = self.__resourceName
        row['discipline'] = self.__discipline

        writer.writerow(row)
    
    # Reports

    def reportIdleness(self, end_time):
        return [ resource.idleness(end_time) for resource in self.__resources ]
    
    def reportQueueWaiting(self):
        return self.__queueWaiting
    
    def reportImmediateProcessing(self):
        return self.__immediateProcessing
    
    def reportDurations(self):
        return self.__durations