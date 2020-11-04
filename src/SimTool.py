from src.modules.Generator import Generator
from src.modules.Service import Service

class Enviroment(object):
    __generators = []
    __services = []
    __currentTime = 0

    def createGenerator(self, *args, **kwargs):
        self.__generators.append(Generator(*args, **kwargs))
    
    def createService(self, *args, **kwargs):
        self.__services.append(Service(*args, **kwargs))
    
    def __findServiceByName(self, name):
        for service in self.__services:
            if service.getName() == name:
                return service
    
    def __runGenerators(self):
        for generator in self.__generators:
            if generator.getNext(self.__currentTime):
                service = self.__findServiceByName(generator.getDestination())
                service.addToQueue(self.__currentTime)
                print(service.getQueue())
    
    def run(self, stop_at=None, stop_until=None):
        self.__currentTime = 0
        
        while (stop_at == None or self.__currentTime <= stop_at):
            self.__runGenerators()
            self.__currentTime += 1
