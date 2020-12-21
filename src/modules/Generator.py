from src.modules.Entity import Entity
from src.modules.Component import Component

class Generator(Component):

    def __init__(self, name, target, min_range, max_range, distribution='uniform', entity_name='entity'):
        super(Generator, self).__init__(name, target)

        self.setRandom(min_range, max_range, distribution)

        self.__entityName = entity_name
        self.__nextEntity = None
        self.__nextId = 0
    
    def generateEntity(self, current_time=0):
        if self.__nextEntity == None or self.__nextEntity.currentTime < current_time:
            self.__nextEntity = Entity(self.__entityName+' '+str(self.__nextId), current_time + self.getRandomNumber())
            self.__nextId += 1
        if current_time == self.__nextEntity.currentTime:
            return self.__nextEntity
        else:
            return False
    
    def saveMe(self, writer, columns):
        row = { key: None for key in columns }
        row['type'] = 'G'
        row['name'] = self.name
        row['target'] = self.target
        row['min_range'] = self.minRange
        row['max_range'] = self.maxRange
        row['distribution'] = self.distribution
        row['entity_name'] = self.__entityName

        writer.writerow(row)