class Terminator(object):

    def __init__(self, name):
        if not (isinstance(name, str)):
            raise ValueError('Name must be a string')
        self.__name = name

        self.__interims = []
    
    def getName(self):
        return self.__name

    def receiveInterim(self, interim):
        print(self.__name+':', interim.getName(), 'finished the simulation at', interim.getTime())
        self.__interims.append(interim)