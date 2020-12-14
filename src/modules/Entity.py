from src.modules.Event import Event

class Entity(object):

    def __init__(self, name, initial_time):
        self.__name = name
        self.__events = [Event(self.__name, initial_time, initial_time, 0)]

    def getName(self):
        return self.__name
    
    def getTime(self):
        last_event = self.__events[-1]
        return last_event.getEnd()
    
    def getLastDuration(self):
        last_event = self.__events[-1]
        return last_event.getDuration()
    
    def appendEvent(self, component_name, current_time, duration):
        self.__events.append(Event(component_name, current_time, current_time+duration, duration))