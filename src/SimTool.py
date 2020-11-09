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
            interim = generator.getNext(self.__currentTime)
            if interim:
                service = self.__findServiceByName(generator.getTarget())
                service.inputInterim(interim)
    
    def __runServices(self):
        for service in self.__services:
            service.attend(self.__currentTime)
    
    def run(self, stop_at=None, stop_until=None):
        self.__currentTime = 0
        
        while (stop_at == None or self.__currentTime <= stop_at):
            self.__runGenerators()
            self.__runServices()
            self.__currentTime += 1
