from src.modules.Generator import Generator
from src.modules.Process import Process
from src.modules.Router import Router
from src.modules.Terminator import Terminator

import csv

class Model(object):

    def __init__(self):
        self.__components = {}
        self.__currentTime = 0
        self.__simulationFile = 'simulation.txt'
        self.__reportsFile = 'reports.txt'
        # Columns for saving and loading
        self.__columns = [
            # Component attibutes
            'type', # G=Generator, P=Process, R=Router, and T=Terminator
            'name', 'target',
            # Random attributes
            'min_range', 'max_range', 'distribution',
            # Generator attributes
            'max_entities', 'entity_name',
            # Process attributes
            'num_resources', 'resource_name', 'discipline'
        ]
    
    # Simulation log methods

    def __createLog(self):
        with open(self.__simulationFile, 'w'):
            pass

    def __printLog(self, message):
        with open(self.__simulationFile, 'a') as f:
            f.write(message+'\n')

    # Component creation methods
    
    def __nameInUse(self, name):
        return name in self.__components.keys()
    
    def createGenerator(self, name, *args, **kwargs):
        if self.__nameInUse(name):
            raise ValueError('Component name "' + name + '" is already in use!')
        self.__components[name] = Generator(name, *args, **kwargs)
        self.__components[name].printLog = self.__printLog
    
    def createProcess(self, name, *args, **kwargs):
        if self.__nameInUse(name):
            raise ValueError('Component name "' + name + '" is already in use!')
        self.__components[name] = Process(name, *args, **kwargs)
        self.__components[name].printLog = self.__printLog
    
    def createRouter(self, name, *args, **kwargs):
        if self.__nameInUse(name):
            raise ValueError('Component name "' + name + '" is already in use!')
        self.__components[name] = Router(name, *args, **kwargs)
        self.__components[name].printLog = self.__printLog
    
    def createTerminator(self, name, *args, **kwargs):
        if self.__nameInUse(name):
            raise ValueError('Component name "' + name + '" is already in use!')
        self.__components[name] = Terminator(name, *args, **kwargs)
        self.__components[name].printLog = self.__printLog
    
    # Component methods
    
    def __getComponentsByType(self, component_type):
        for name, component in self.__components.items():
            if isinstance(component, component_type):
                yield component
    
    def __routeEntity(self, origin, entity):
        target = self.__components[origin.target]
        if isinstance(target, (Process, Terminator)):
            target.receiveEntity(entity)
        elif isinstance(target, Router):
            self.__routeEntity(target, entity)

    def __runGenerators(self):
        for generator in self.__getComponentsByType(Generator):
            entity = generator.generateEntity(self.__currentTime)
            if entity:
                self.__routeEntity(generator, entity)
    
    def __runProcesses(self):
        for process in self.__getComponentsByType(Process):
            entities = process.outputEntities(self.__currentTime)
            for entity in entities:
                self.__routeEntity(process, entity)
            
            process.process(self.__currentTime)
    
    # Reports methods

    def __createReports(self):
        for name, component in self.__components.items():
            if isinstance(component, Process):
                idleness = component.idleness(self.__currentTime)
                print(idleness)
        with open(self.__reportsFile, 'w') as f:
            pass

    # Model running method

    @property
    def running(self):
        for name, component in self.__components.items():
            if (isinstance(component, Generator) and component.remainingEntities > 0) or (isinstance(component, Process) and component.processing > 0):
                return True
        return False
    
    def run(self):
        self.__currentTime = 0
        
        self.__createLog()
        self.__printLog('Model: simulation started')
        while self.running:
            self.__runGenerators()
            self.__runProcesses()
            self.__currentTime += 1
        self.__printLog('Model: simulation ended')

        self.__createReports()
    
    # Model saving and loading

    def save(self, csv_name):
        with open(csv_name, mode='w') as opened_file:
            writer = csv.DictWriter(opened_file, fieldnames=self.__columns)
            writer.writeheader()
            
            for name, component in self.__components.items():
                component.saveMe(writer, self.__columns)

    def load(csv_name):
        model = Model()
        with open(csv_name, mode='r') as opened_file:
            reader = csv.DictReader(opened_file)
            
            for row in reader:
                if row['type'] == 'G' and isinstance(model, Model):
                    model.createGenerator(
                        name=row['name'],
                        target=row['target'],
                        min_range=int(row['min_range']),
                        max_range=int(row['max_range']),
                        distribution=row['distribution'],
                        max_entities=int(row['max_entities']),
                        entity_name=row['entity_name']
                    )
                elif row['type'] == 'P' and isinstance(model, Model):
                    model.createProcess(
                        name=row['name'],
                        target=row['target'],
                        min_range=int(row['min_range']),
                        max_range=int(row['max_range']),
                        distribution=row['distribution'],
                        num_resources=int(row['num_resources']),
                        resource_name=row['resource_name'],
                        discipline=row['discipline']
                    )
                elif row['type'] == 'R' and isinstance(model, Model):
                    model.createRouter(
                        name=row['name'],
                        targets=row['target'].split('$$'),
                        distribution=row['distribution']
                    )
                elif row['type'] == 'T' and isinstance(model, Model):
                    model.createTerminator(
                        name=row['name']
                    )
        return model