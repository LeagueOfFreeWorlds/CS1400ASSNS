class Wordinator:
    # Construct:
    def __init__(self, value):
        self.__value = value
    # Retrieve instance of second word value:
    def getValue(self):
        return self.__value
    def __add__(self, other):
        return Wordinator(self.__value + other.getValue())
    def __sub__(self, other):
        return Wordinator(self.__value + other.getValue())
    def __str__(self):
        return str(self.__value)
    def __mul__(self, other):
        return Wordinator(self.__value * other.getValue())
    def __mod__(self, other):
        return Wordinator(self.__value % other.getValue())
    def __lt__(self, other):
        return Wordinator(self.__value < other.getValue)


