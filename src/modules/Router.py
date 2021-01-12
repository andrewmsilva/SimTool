from src.modules.Component import Component

class Router(Component):

    def __init__(self, name, targets, distribution='uniform'):
        super(Router, self).__init__(name)
        self.__targets = targets

        self.setRandom(0, len(targets)-1, distribution)
    
    @property
    def target(self):
        target = self.__targets[self.getRandomNumber()]
        self.printLog('{}: routing to {}'.format(self.name, target))
        return target
    
    def saveMe(self, writer, columns):
        row = { key: None for key in columns }
        row['type'] = 'R'
        row['name'] = self.name
        row['target'] = '$$'.join(self.__targets)
        row['distribution'] = self.distribution

        writer.writerow(row)