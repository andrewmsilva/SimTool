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
        if self.__currentTime <= self.__stopAt:
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

    def __isRunning(self):
        result = False
        for service in self.__services:
            if not service.isEmpty():
                result = True
        return result or self.__currentTime <= self.__stopAt
    
    def run(self, stop_at):
        if not isinstance(stop_at, int):
            raise ValueError('Stop at must be integer')
        self.__stopAt = stop_at
        self.__currentTime = 0
        
        while self.__isRunning():
            self.__runGenerators()
            self.__runServices()
            self.__currentTime += 1
