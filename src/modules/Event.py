class Event(object):

    def __init__(self, interim_name, start, end, duration):
        self.__interimName = interim_name
        self.__start = start
        self.__end = end
        self.__duration = duration
    
    def getInterimName(self):
        return self.__interimName
    
    def getStart(self):
        return self.__start
    
    def getEnd(self):
        return self.__end
    
    def getDuration(self):
        return self.__duration