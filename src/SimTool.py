from src.modules.Generator import Generator
from src.modules.Process import Process
from src.modules.Router import Router
from src.modules.Terminator import Terminator

import csv

class Model(object):

    def __init__(self, start_time=0, stop_time=100):
        self.__components = {}
        self.__stopTime = None
        self.__startTime = start_time
        self.__stopTime = stop_time
        self.__currentTime = start_time
        # Columns for saving and loading
        self.__columns = [
            # Component type (M=Model, G=Generator, P=Process, R=Router, and T=Terminator)
            'type',
            # Model attributes (first row)
            'start_time', 'stop_time',
            # Component attributes
            'name', 'target',
            # Random attributes
            'min_range', 'max_range', 'distribution',
            # Generator attributes
            'entity_name',
            # Process attributes
            'num_resources', 'resource_name', 'discipline'
        ]

    # Component creation methods
    
    def __nameInUse(self, name):
        return name in self.__components.keys()
    
    def createGenerator(self, name, *args, **kwargs):
        if self.__nameInUse(name):
            raise ValueError('Component name "' + name + '" is already in use!')
        self.__components[name] = Generator(name, *args, **kwargs)
    
    def createProcess(self, name, *args, **kwargs):
        if self.__nameInUse(name):
            raise ValueError('Component name "' + name + '" is already in use!')
        self.__components[name] = Process(name, *args, **kwargs)
    
    def createRouter(self, name, *args, **kwargs):
        if self.__nameInUse(name):
            raise ValueError('Component name "' + name + '" is already in use!')
        self.__components[name] = Router(name, *args, **kwargs)
    
    def createTerminator(self, name, *args, **kwargs):
        if self.__nameInUse(name):
            raise ValueError('Component name "' + name + '" is already in use!')
        self.__components[name] = Terminator(name, *args, **kwargs)
    
    # Component methods
    
    def __getComponentsByType(self, component_type):
        for name, component in self.__components.items():
            if isinstance(component, component_type):
                yield component
    
    def __routeEntity(self, origin, entity):
        target = self.__components[origin.getTarget()]
        if isinstance(target, (Process, Terminator)):
            target.receiveEntity(entity)
        elif isinstance(target, Router):
            self.__routeEntity(target, entity)

    def __runGenerators(self):
        if self.__currentTime <= self.__stopTime:
            for generator in self.__getComponentsByType(Generator):
                entity = generator.getEntity(self.__currentTime)
                if entity:
                    self.__routeEntity(generator, entity)
    
    def __runProcesses(self):
        for process in self.__getComponentsByType(Process):
            entities = process.outputEntities(self.__currentTime)
            for entity in entities:
                self.__routeEntity(process, entity)
            
            process.process(self.__currentTime)

    # Model running methods

    def __isRunning(self):
        result = False
        for process in self.__getComponentsByType(Process):
            if not process.isEmpty():
                result = True
        return result or self.__currentTime <= self.__stopTime
    
    def run(self):
        self.__currentTime = self.__startTime
        
        while self.__isRunning():
            self.__runGenerators()
            self.__runProcesses()
            self.__currentTime += 1
        print('Simulation ended')
    
    # Model saving and loading

    def __writeMe(self, writer):
        row = { key: None for key in self.__columns }
        row['type'] = 'M'
        row['start_time'] = self.__startTime
        row['stop_time'] = self.__stopTime

        writer.writerow(row)

    def save(self, csv_name):
        with open(csv_name, mode='w') as opened_file:
            writer = csv.DictWriter(opened_file, fieldnames=self.__columns)
            writer.writeheader()
            
            self.__writeMe(writer)

            for name, component in self.__components.items():
                component.writeMe(writer, self.__columns)