from src.modules.Component import Component

class Terminator(Component):

    def __init__(self, name):
        super(Terminator, self).__init__(name)

        self.__entities = []
    
    def receiveEntity(self, entity):
        self.printLog(entity.getName(), 'finished the simulation at', entity.getTime())
        self.__entities.append(entity)
    
    def saveMe(self, writer, columns):
        row = { key: None for key in columns }
        row['type'] = 'T'
        row['name'] = self.getName()

        writer.writerow(row)