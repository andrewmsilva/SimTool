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
    
    def run(self):
        self.__currentTime = 0
        for generator in self.__generators:
            entities = generator.entities(self.__currentTime)
            service = self.__findServiceByName(generator.getDestination())
            service.addToQueue(entities)
