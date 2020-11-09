from src.modules.Event import Event

class Interim(object):

    def __init__(self, name, initial_time):
        if not (isinstance(name, str)):
            raise ValueError('Name must be a string')
        self.__name = name

        if not (isinstance(initial_time, int)):
            raise ValueError('Initial time must be an integer')
        self.__events = [Event(self.__name, initial_time, initial_time, 0)]

    def getName(self):
        return self.__name
    
    def getTime(self):
        last_event = self.__events[-1]
        return last_event.getEnd()
    
    def appendEvent(self, current_time, duration):
        self.__events.append(Event(self.__name, current_time, current_time+duration, duration))