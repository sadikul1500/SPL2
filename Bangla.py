from word import CommonSymbols
from collections import defaultdict


class Bangla(CommonSymbols):
    banglaDictionary = defaultdict(list)

    symbolToKar = {
        "অ": "", "আ": "া",
        "ই": "ি", "ঈ": "ী",
        "উ": "ু", "ঊ": "ূ",
        "এ": "ে", "ঐ": "ৈ",
        "ও": "ো", "ঔ": "ৌ", "ঋ": "ৃ"
    }
    # print(symbolToKar)

    vol_spe = {
        "010100": "ই",
        "101001": "উ",
        "101010": "ও"
    }

    volume = {
        "100000": "অ", "001110": "আ",
        "001010": "ঈ", "110011": "ঊ",
        '000010111010': 'ঋ', "100010": "এ",
        "001100": "ঐ", "010101": "ঔ",
    }

    numbers = {
        '010110': '০', '100000': '১',
        '110000': '২', '100100': '৩',
        '100110': '৪', '100010': '৫',
        '110100': '৬', '110110': '৭',
        '110010': '৮', '010100': '৯',
    }

    consonant = {
        "101000": "ক", "101101": "খ", "110110": "গ", "110001": "ঘ", "001101": "ঙ",
        "100100": "চ", "100001": "ছ", "010110": "জ", "101011": "ঝ", "010010": "ঞ",
        "011111": "ট", "010111": "ঠ", "110101": "ড", "111111": "ঢ", "001111": "ণ",
        "011110": "ত", "100111": "থ", "100110": "দ", "011101": "ধ", "101110": "ন",
        "111100": "প", "110100": "ফ", "110000": "ব", "111001": "ভ", "101100": "ম",
        "101111": "য", "111010": "র", "111000": "ল",
        "100101": "শ", "011100": "স", "111101": "ষ", "110010": "হ", "111110": "ক্ষ",
        "100011": "জ্ঞ", "110111": "ড়", "111011": "ঢ়", "010001": "য়", '010000011110': 'ৎ',
        "000100": "্‌", "000011": "ং", "000001": "ঃ", "001000": "ঁ",
    }

    fourLetters = {
        'কষময': 'ক্ষ্ম্য', 'নতরয': 'ন্ত্র্য',
    }

    def __init__(self):
        pass

    def getFourLetters(self):
        return self.fourLetters

    def getconsonant(self):
        return self.consonant

    def getNumbers(self):
        return self.numbers

    def getVolume(self):
        return self.volume

    def getVol_spe(self):
        return self.vol_spe

    def getSymbolToKar(self):
        return self.symbolToKar

    def getBanglaDictionary(self):
        #dd = defaultdict(list)
        for d in (
        self.vol_spe, self.volume, self.punctuation, self.consonant, self.hosonto, self.dot):  # you can list as many input dicts as you want here
            for key, value in d.items():
                self.banglaDictionary[key].append(value)

        return self.banglaDictionary
