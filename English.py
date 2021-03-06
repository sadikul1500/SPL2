from oopBraille.CommonSymbols import CommonSymbols
from collections import defaultdict

class English(CommonSymbols):
    englishDictionary = defaultdict(list)

    english_numbers = {
        '010110': '0', '100000': '1',
        '110000': '2', '100100': '3',
        '100110': '4', '100010': '5',
        '110100': '6', '110110': '7',
        '110010': '8', '010100': '9',
    }

    english_alphabet = {
        '100000': 'a', '110000': 'b', '100100': 'c', '100110': 'd', '100010': 'e',
        '110100': 'f', '110110': 'g', '110010': 'h', '010100': 'i', '010110': 'j',
        '101000': 'k', '111000': 'l', '101100': 'm', '101110': 'n', '101010': 'o',
        '111100': 'p', '111110': 'q', '111010': 'r', '011100': 's', '011110': 't',
        '101001': 'u', '111001': 'v', '010111': 'w', '101101': 'x', '101111': 'y',
        '101011': 'z',
    }

    def __init__(self):
        CommonSymbols.__init__(self)
        print('english')
        pass

    def getEnglishNumbers(self):
        return self.english_numbers

    def getEnglishAlphabets(self):
        return self.english_alphabet

    def getEnglishDictionary(self):
        for d in (self.english_alphabet, self.punctuation, self.dot):  # you can list as many input dicts as you want here
            for key, value in d.items():
                self.englishDictionary[key].append(value)

        return self.englishDictionary
