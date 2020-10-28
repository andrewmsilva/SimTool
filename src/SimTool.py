from src.modules.Generator import Generator
from src.modules.Service import Service

class Enviroment(object):
    __generator = None
    __services = []
    __currentTime = 0

    def createGenerator(self, *args, **kwargs):
        self.__generator = Generator(*args, **kwargs)
    
    def createService(self, *args, **kwargs):
        self.__services.append(Service(*args, **kwargs))
    
    def run(self, until):
        self.__currentTime = 0
        
        generations = 0
        while until == None or generations < until:
            generations += 1
            self.__currentTime = self.__generator.new(self.__currentTime)
            print(self.__currentTime)
