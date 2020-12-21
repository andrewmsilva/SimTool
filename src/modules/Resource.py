from src.modules.Event import Event

class Resource(object):

    def __init__(self, name):
        self.__name = name
        self.__events = []
    
    @property
    def name(self):
        return self.__name

    def process(self, entity, current_time, duration):
        if not self.busy(current_time):
            self.__events.append(Event(entity.name, current_time, current_time+duration, duration))

    def busy(self, current_time):
        last_event = None
        if len(self.__events) > 0:
            last_event = self.__events[-1]
        return not (last_event == None or last_event.end <= current_time)