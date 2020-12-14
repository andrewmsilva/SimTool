from src.modules.Entity import Entity
from src.modules.Component import Component

class Generator(Component):

    def __init__(self, name, target, min_range, max_range, distribution='uniform', entity_name='entity'):
        super(Generator, self).__init__(name, target)

        self.setRandom(min_range, max_range, distribution)

        self.__entityName = entity_name
        self.__nextEntity = None
        self.__nextId = 0
    
    def getEntity(self, current_time=0):
        if self.__nextEntity == None or self.__nextEntity.getTime() < current_time:
            self.__nextEntity = Entity(self.__entityName+' '+str(self.__nextId), current_time + self.getRandomNumber())
            self.__nextId += 1
        if current_time == self.__nextEntity.getTime():
            return self.__nextEntity
        else:
            return False