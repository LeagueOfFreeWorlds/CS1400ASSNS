import random
class Wordinator:
    # Construct:
    def __init__(self, word):
        self.__word = word
    # Retrieve instance of second word value:
    def __getWord(self):
        return self.__word

    def __add__(self, other):
        return self.__word.capitalize() + other.__getWord()

    def __sub__(self, other):
        word1 = list(self.__word)
        word2 = list(other.__getWord())
        fword1 = []
        fword2 = []
        for i in word1:
            if i.isupper():
                fword1.append(i.lower())
            else:
                fword1.append(i.upper())
        for i in word2:
            if i.isupper():
                fword2.append(i.lower())
            else:
                fword2.append(i.upper())
        return ''.join(fword1), ''.join(fword2)

    def __str__(self):
        return str(self.__word)

    def __truediv__(self, other):
        word = (self.__word + other.__getWord())
        wordL = list(word)
        random.shuffle(wordL)
        return ''.join(wordL)

    def __mul__(self, other):
        return self.__word.upper() * other.__getWord()

    def __mod__(self, other):
        w1Len = len(self.__word)
        w2Len = len(other.__getWord())
        w1C = w1Len // 2
        w2C = w2Len // 2
        cOneLen = w1C // 2
        cTwoLen = w2C // 2
        qOne1 = (w1C - 1)
        qTwo1 = (w2C - 1)
        crOneLen = (w1C - 2)
        return self.__word[crOneLen, w1C + crOneLen], other.__getWord()[cTwoLen, w2C + cTwoLen]

    def backWordSlice(self):
        word = self.__word[::-1]
        return word

    def backWordManual(self):
        word = list(self.__word)
        wLen = len(word)
        backWord = ''
        for i in range(wLen, 0, -1):
            backWord += word[i - 1]
        return backWord

