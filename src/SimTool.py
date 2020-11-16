from src.modules.Generator import Generator
from src.modules.Service import Service
from src.modules.Terminator import Terminator

class Enviroment(object):

    def __init__(self):
        self.__components = []
        self.__currentTime = 0

    # Component creation methods
    
    def __nameAvailability(self, name):
        for component in self.__components:
            if component.getName() == name:
                return False
        return True
    
    def createGenerator(self, name, *args, **kwargs):
        if not self.__nameAvailability(name):
            raise ValueError('Component name "' + name + '" is already in use!')
        self.__components.append(Generator(name, *args, **kwargs))
    
    def createService(self, name, *args, **kwargs):
        if not self.__nameAvailability(name):
            raise ValueError('Component name "' + name + '" is already in use!')
        self.__components.append(Service(name, *args, **kwargs))
    
    def createTerminator(self, name, *args, **kwargs):
        if not self.__nameAvailability(name):
            raise ValueError('Component name "' + name + '" is already in use!')
        self.__components.append(Terminator(name, *args, **kwargs))
    
    # Component get methods

    def __getComponentByName(self, name):
        for component in self.__components:
            if component.getName() == name:
                return component
    
    def __getComponentByType(self, component_type):
        for component in self.__components:
            if isinstance(component, component_type):
                yield component
    
    # Component running methods

    def __runGenerators(self):
        if self.__currentTime <= self.__stopAt:
            for generator in self.__getComponentByType(Generator):
                interim = generator.getNext(self.__currentTime)
                if interim:
                    component = self.__getComponentByName(generator.getTarget())
                    component.receiveInterim(interim)
    
    def __runServices(self):
        for service in self.__getComponentByType(Service):
            component = self.__getComponentByName(service.getTarget())
            if component:
                interims = service.sendInterims(self.__currentTime)
                for interim in interims:
                    component.receiveInterim(interim)
        
            service.attend(self.__currentTime)

    # Evironment running methods

    def __isRunning(self):
        result = False
        for service in self.__getComponentByType(Service):
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
