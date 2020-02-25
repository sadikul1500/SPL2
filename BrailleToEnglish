from oopBraille import English
from oopBraille import DoubleMap

#Bangla
class BrailleToEnglish:

    english = English.English()
    numeral_sign = '001111'

    def __init__(self):
        #self.letters = letters
        print('bangla text process')

    def numberProcess(self, letters, bracket_count, i, length):
        if letters[i] in self.english.operator.keys():
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
            i] in self.english.getEnglishNumbers().keys()):
            if i + 1 < length and letters[i] == '001010' and letters[i + 1] == '001010':
                return self.english.getOperator().get(letters[i] + letters[i + 1])[0], bracket_count, i+1

            elif letters[i] == '000011' and letters[i + 1] == '011011':
                return self.english.getOperator().get(letters[i] + letters[i + 1])[0],\
                       bracket_count, i+1

            elif letters[i] == '000001' and letters[i + 1] == '011011':
                return '[', bracket_count, i+1

            elif letters[i] == '011011' and letters[i + 1] == '000001':
                return ']', bracket_count, i+1



    def getBrailleToText(self, letters):
        #print(self.letters)

        length = len(letters)
        num = False
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
                        '''
                    elif letters[i] == '000100' and i + 2 < length:

                        text += dd.get(
                            letters[i + 1])[0] + hos + dd.get(letters[i + 2])[0]
                        i += 2
                        # print(2)
                        # print(hos)



                    elif letters[i] == '000101' and i + 4 < length:
                        # joint = ''
                        joint = dd.get(letters[i + 1])[0] + dd.get(letters[i + 2])[0] + dd.get(letters[i + 3])[0] + \
                                dd.get(letters[i + 4])[0]
                        if joint in self.english.getFourLetters().keys():
                            for key, value in self.bangla.getFourLetters().items():
                                if joint == key:
                                    text += dd.get(letters[i + 1])[0] + hos + dd.get(letters[i + 2])[0] + hos + \
                                            dd.get(letters[i + 3])[0] + hos + dd.get(letters[i + 4])[0]
                                    i += 4
                                    # print('4')
                                    break

                        else:
                            # joint = dd.get(letters[i + 1]) + dd.get(letters[i + 2]) + dd.get(letters[i + 3])

                            text += dd.get(letters[i + 1])[0] + hos + dd.get(letters[i + 2])[0] + hos + \
                                    dd.get(letters[i + 3])[0]
                            i += 3


                        '''
                    else:

                        for k, v in dd.items():
                            if letters[i] == k:
                                text += v[0]

                                break
                            else:
                                text += k

                    num = False

            i += 1
        text += ' '
        return text
