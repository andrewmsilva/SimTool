from src.modules.Event import Event

class Resource(object):

    def __init__(self, name, never_busy=False):
        self.__name = name
        self.__neverBusy = never_busy
        self.__events = []
    
    @property
    def name(self):
        return self.__name
    
    @property
    def events(self):
        return self.__events

    def process(self, entity, current_time, duration):
        if not self.busy(current_time):
            self.__events.append(Event(entity.name, current_time, current_time+duration, duration))

    def busy(self, current_time):
        if self.__neverBusy:
            return False
        last_event = None
        if len(self.__events) > 0:
            last_event = self.__events[-1]
        return not (last_event == None or last_event.end <= current_time)

    def idleTime(self, end_time):
        if self.__neverBusy:
            return None
        idle_time = 0
        last_time = 0
        for event in self.__events:
            idle_time += event.start - last_time
            last_time = event.end
        idle_time += end_time - last_time
        return idle_time