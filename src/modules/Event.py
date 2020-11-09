class Event(object):

    def __init__(self, interim_name, start, end, duration):
        if not (isinstance(interim_name, str)):
            raise ValueError('Interim name must be a string')
        self.__interimName = interim_name
        
        if not (isinstance(start, int)):
            raise ValueError('Start time must be an integer')
        self.__start = start

        if not (isinstance(end, int)):
            raise ValueError('End time must be an integer')
        self.__end = end

        if not (isinstance(duration, int)):
            raise ValueError('Duration time must be an integer')
        self.__duration = duration
    
    def getInterimName(self):
        return self.__interimName
    
    def getStart(self):
        return self.__start
    
    def getEnd(self):
        return self.__end
    
    def getDuration(self):
        return self.__duration