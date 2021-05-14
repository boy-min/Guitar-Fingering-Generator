class Hand:
    def __init__(self, size=0, length=0) :
        self.__size = size
        self.__length = length

    def set(self, size, length) :
        self.__size = size
        self.__length = length

    def get(self, key = None) :
        if key == None : 
            return {'size' : self.__size, 'length' : self.__length}
        
        return {'size' : self.__size, 'length' : self.__length}.get(key)
