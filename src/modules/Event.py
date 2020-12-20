class Event(object):

    def __init__(self, entity_name, start, end, duration):
        self.__entityName = entity_name
        self.__start = start
        self.__end = end
        self.__duration = duration
    
    def getInterimName(self):
        return self.__entityName
    
    def getStart(self):
        return self.__start
    
    def getEnd(self):
        return self.__end
    
    def getDuration(self):
        return self.__duration