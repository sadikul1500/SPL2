from word import CommonSymbols

class DoubleMap:
    commonSymbol = CommonSymbols.CommonSymbols()

    def __init__(self, letters, position, bracket_count):
        self.letters = letters
        self.position = position
        self.bracket_count = bracket_count
        print('double map')

    def getCharFromDoubbleMap(self):

        char = self.letters[self.position]
        length = len(self.letters)
        #global bracket_count

        if char == '011001':
            if self.position + 1 == length:
                return '?'
            else:
                return '“'
        elif char == '001011':
            if self.position + 1 == length or\
                    self.letters[self.position] in self.commonSymbol.getPunctuation().keys():
                return '"'
            else:
                return '‍্'
        elif char == '011011':
            if self.bracket_count == 1:
                self.bracket_count = 0
                return ')'
            else:
                self.bracket_count += 1
                return '('

        elif char == '010000':
            if self.position + 1 == length or length > 3:
                return ','
            else:
                return '.'

    def getBracket_count(self):
        return self.bracket_count
