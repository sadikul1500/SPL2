from oopBraille import English
from oopBraille import DoubleMap

#english
class BrailleToEnglish:

    english = English.English()
    numeral_sign = '001111'
    capital_sign = '000001'

    def __init__(self):
        #self.letters = letters
        print('english text process')

    def numberProcess(self, letters, bracket_count, i, length):
        if letters[i] in self.english.getOperator().keys():
            if letters[i] == '011011' and bracket_count == 0:
                bracket_count += 1
                return '(', bracket_count, i

            elif letters[i] == '011011' and bracket_count == 1:
                bracket_count = 0
                return ')', bracket_count, i

            else:
                return self.english.getOperator().get(letters[i])[0], bracket_count, i
            # print('num false')

        elif letters[i] in self.english.getEnglishNumbers().keys():
            return self.english.getEnglishNumbers().get(letters[i])[0], bracket_count, i

        elif (letters[i] not in self.english.getOperator().keys() or letters[
            i] in self.english.getEnglishNumbers().keys()) and i + 1 < length:
            if  letters[i] == '001010' and letters[i + 1] == '001010':
                return self.english.getOperator().get(letters[i] + letters[i + 1])[0], bracket_count, i+1

            elif letters[i] == '000011' and letters[i + 1] == '011011':
                return self.english.getOperator().get(letters[i] + letters[i + 1])[0],\
                       bracket_count, i+1

            elif letters[i] == '000001' and letters[i + 1] == '011011':
                return '[', bracket_count, i+1

            elif letters[i] == '011011' and letters[i + 1] == '000001':
                return ']', bracket_count, i+1

            else:
                return '', bracket_count, i

        else:
            return '', bracket_count, i


    def getBrailleToText(self, letters):
        #print(self.letters)

        length = len(letters)
        num = False
        capital = False
        i = 0
        text = ''
        #global
        bracket_count = 0
        #hos = self.bangla.getHosonto().get('001011')[0]
        dd = self.english.getEnglishDictionary()

        while i < length:
            if num:
                txt, bracket_count, i = self.numberProcess(letters, bracket_count, i, length)
                text += txt


            elif not num:
                if i == 0 and letters[i] == self.numeral_sign:
                    num = True

                elif letters[i] == self.numeral_sign and\
                        (letters[i - 1] in self.english.getPunctuation().keys() or letters[i - 1] == self.english.getDot()):
                    num = True


                else:
                    if i + 1 < length and (letters[i] + letters[i + 1]) in self.english.getTwelveDots().keys():
                        text += self.english.getTwelveDots().get(letters[i] + letters[i + 1])[0]
                        i += 1
                    elif letters[i] in self.english.getDouble_mapping().keys():
                        doubleMap = DoubleMap.DoubleMap(letters, i, bracket_count)
                        text += doubleMap.getCharFromDoubbleMap()
                        bracket_count = doubleMap.getBracket_count()
                        i += 1

                    elif letters[i] == self.capital_sign and i+1<length and letters[i+1] == self.capital_sign:
                        text += self.capital_sign+self.capital_sign
                        i += 1

                    elif letters[i] == self.capital_sign:
                        capital = True

                    else:
                        flag = 0
                        for k, v in dd.items():
                            if letters[i] == k:
                                if capital == True:
                                    text += v[0].upper()
                                    capital = False
                                else:
                                    text += v[0]
                                flag = 1
                                #print('ok')
                                break
                        if flag == 0:
                            text += letters[i]

                    num = False

            i += 1
        text += ' '
        return text

