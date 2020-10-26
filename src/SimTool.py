from src.modules.Generator import Generator

class Enviroment(object):
    __generator = None
    __currentTime = 0

    def createGenerator(self, *args):
        self.__generator = Generator(*args)
    
    def run(self, until):
        self.__currentTime = 0
        
        generations = 0
        while until == None or generations < until:
            generations += 1
            self.__currentTime = self.__generator.new(self.__currentTime)
            print(self.__currentTime)
