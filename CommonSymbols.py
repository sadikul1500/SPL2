class CommonSymbols:
    punctuation = {
        '001001': '-', '010011': '|', '000001011001': '‘', '001011001000': '’',
        '000001011011': '[', '011000': ';', '011010': '!', '000011011011': '=',
        '001010001010': '*', '011011001000': ']', '010010': ':', '001011': '"',
        '011001': '“', '011011': '(', '010000': ',', '001100': '/', '000010': '$'

    }

    operator = {
        '001001': '-', '000011011011': '=', '001010001010': '*', '001110': '>', '110001': '<',
        '010000': ',', '001100': '/', '011011': '(', '001101': '+', '100101': '%', '000110': '^',
    }

    hosonto = {
        '011001': '?', '011011': ')', '001011': '্'
    }

    dot = {
        '010000': '.'
    }

    twelveDots = {
        '000011011011': '=', '001010001010': '*', '000001011011': '[', '000001011001': '‘', '001011001000': '’',
        '011011001000': ']',
        '000010111010': 'ঋ', '010000011110': 'ৎ'
    }

    double_mapping = {
        '011001': '?', '001011': '"', "011011": '(', '010000': ','
    }

    def __init__(self):
        print('common symbols')
        pass

    def getHosonto(self):
        return self.hosonto

    def getOperator(self):
        return self.operator

    def getTwelveDots(self):
        return self.twelveDots

    def getDouble_mapping(self):
        return self.double_mapping

    def getPunctuation(self):
        return self.punctuation

    def getDot(self):
        return self.dot
