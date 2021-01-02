from src.modules.Component import Component

class Terminator(Component):

    def __init__(self, name):
        super(Terminator, self).__init__(name)
        self.reset()

    def reset(self):
        self.__output = []
    
    @property
    def output(self):
        return self.__output
    
    def receiveEntity(self, entity):
        self.printLog('{}: {} finished the simulation at {}'.format(self.name, entity.name, entity.currentTime))
        self.__output.append(entity)
    
    def saveMe(self, writer, columns):
        row = { key: None for key in columns }
        row['type'] = 'T'
        row['name'] = self.name

        writer.writerow(row)