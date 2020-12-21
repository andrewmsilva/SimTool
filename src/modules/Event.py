class Event(object):

    def __init__(self, entity_name, start, end, duration):
        self.__entityName = entity_name
        self.__start = start
        self.__end = end
        self.__duration = duration
    
    @property
    def name(self):
        return self.__entityName
    
    @property
    def start(self):
        return self.__start
    
    @property
    def end(self):
        return self.__end
    
    @property
    def duration(self):
        return self.__duration