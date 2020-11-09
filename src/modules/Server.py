from src.modules.Event import Event

class Server(object):

    def __init__(self):
        self.__events = []

    def attend(self, interim, current_time, duration):
        if not self.busy(current_time):
            self.__events.append(Event(interim.getName(), current_time, current_time+duration, duration))

    def busy(self, current_time):
        last_event = None
        if len(self.__events) > 0:
            last_event = self.__events[-1]
        return not (last_event == None or last_event.getEnd() <= current_time)