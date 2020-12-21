from src.modules.Event import Event

class Entity(object):

    def __init__(self, name, initial_time):
        self.__name = name
        self.__events = [Event(self.__name, initial_time, initial_time, 0)]

    @property
    def name(self):
        return self.__name
    
    @property
    def currentTime(self):
        last_event = self.__events[-1]
        return last_event.end
    
    @property
    def lastDuration(self):
        last_event = self.__events[-1]
        return last_event.duration
    
    def appendEvent(self, component_name, current_time, duration):
        self.__events.append(Event(component_name, current_time, current_time+duration, duration))