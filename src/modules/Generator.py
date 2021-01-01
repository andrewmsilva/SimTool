from src.modules.Entity import Entity
from src.modules.Component import Component

class Generator(Component):

    def __init__(self, name, target, min_range, max_range, distribution='uniform', max_entities=10, entity_name='entity'):
        super(Generator, self).__init__(name, target)

        self.setRandom(min_range, max_range, distribution)

        self.__entityName = entity_name
        self.__maxEntities = max_entities
        self.__remainingEntities = max_entities
        self.__nextEntity = None

    @property
    def remainingEntities(self):
        return self.__remainingEntities
    
    def generateEntity(self, current_time):
        if self.__remainingEntities > 0:
            if self.__nextEntity == None or self.__nextEntity < current_time:
                self.__nextEntity = current_time + self.getRandomNumber()
            if self.__nextEntity == current_time:
                entity = Entity(self.__entityName+' '+str(self.__maxEntities-self.__remainingEntities), current_time)
                self.__remainingEntities -= 1
                return entity
        return False
    
    def saveMe(self, writer, columns):
        row = { key: None for key in columns }
        row['type'] = 'G'
        row['name'] = self.name
        row['target'] = self.target
        row['min_range'] = self.minRange
        row['max_range'] = self.maxRange
        row['distribution'] = self.distribution
        row['max_entities'] = self.__maxEntities
        row['entity_name'] = self.__entityName

        writer.writerow(row)