from src.modules.Generator import Generator
from src.modules.Service import Service
from src.modules.Terminator import Terminator

class Enviroment(object):

    def __init__(self):
        self.__generators = []
        self.__services = []
        self.__terminators = []
        self.__currentTime = 0

    def createGenerator(self, *args, **kwargs):
        self.__generators.append(Generator(*args, **kwargs))
    
    def createService(self, *args, **kwargs):
        self.__services.append(Service(*args, **kwargs))
    
    def createTerminator(self, *args, **kwargs):
        self.__terminators.append(Terminator(*args, **kwargs))
    
    def __findComponentByName(self, name):
        for service in self.__services:
            if service.getName() == name:
                return service
        for terminator in self.__terminators:
            if terminator.getName() == name:
                return terminator
    
    def __runGenerators(self):
        for generator in self.__generators:
            interim = generator.getNext(self.__currentTime)
            if interim:
                component = self.__findComponentByName(generator.getTarget())
                component.receiveInterim(interim)
    
    def __runServices(self):
        for service in self.__services:
            component = self.__findComponentByName(service.getTarget())
            if component:
                interims = service.sendInterims(self.__currentTime)
                for interim in interims:
                    component.receiveInterim(interim)
        
            service.attend(self.__currentTime)
    
    def run(self, stop_at=None, stop_until=None):
        self.__currentTime = 0
        
        while (stop_at == None or self.__currentTime <= stop_at):
            self.__runGenerators()
            self.__runServices()
            self.__currentTime += 1
