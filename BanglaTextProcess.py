from word import Bangla
from word import DoubleMap

#Bangla
class BanglaTextProcess:

    bangla = Bangla.Bangla()
    numeral_sign = '001111'

    def __init__(self, letters):
        self.letters = letters
        print('bangla text process')

    def numberProcess(self, bracket_count, i, length):
        if self.letters[i] in self.bangla.operator.keys():
            if self.letters[i] == '011011' and bracket_count == 0:
                bracket_count += 1
                return '(', bracket_count, i

            elif self.letters[i] == '011011' and bracket_count == 1:
                bracket_count = 0
                return ')', bracket_count, i

            else:
                return self.bangla.getOperator().get(self.letters[i])[0], bracket_count, i
            # print('num false')

        elif self.letters[i] in self.bangla.getNumbers().keys():
            return self.bangla.getNumbers().get(self.letters[i])[0], bracket_count, i

        elif (self.letters[i] not in self.bangla.getOperator().keys() or self.letters[
            i] in self.bangla.getNumbers().keys()):
            if i + 1 < length and self.letters[i] == '001010' and self.letters[i + 1] == '001010':
                return self.bangla.getOperator().get(self.letters[i] + self.letters[i + 1])[0], bracket_count, i+1

            elif self.letters[i] == '000011' and self.letters[i + 1] == '011011':
                return self.bangla.getOperator().get(self.letters[i] + self.letters[i + 1])[0],\
                       bracket_count, i+1

            elif self.letters[i] == '000001' and self.letters[i + 1] == '011011':
                return '[', bracket_count, i+1

            elif self.letters[i] == '011011' and self.letters[i + 1] == '000001':
                return ']', bracket_count, i+1



    def textProcess(self):
        #print(self.letters)

        length = len(self.letters)
        num = False
        i = 0
        text = ''
        #global
        bracket_count = 0
        hos = self.bangla.getHosonto().get('001011')[0]
        dd = self.bangla.getBanglaDictionary()

        while i < length:
            if num:
                txt, bracket_count, i = self.numberProcess(bracket_count, i, length)
                text += txt


            elif not num:
                if i == 0 and self.letters[i] == self.numeral_sign:
                    num = True

                elif self.letters[i] == self.numeral_sign and\
                        (self.letters[i - 1] in self.bangla.getPunctuation().keys() or self.letters[i - 1] == self.bangla.getDot()):
                    num = True


                else:
                    if i + 1 < length and (self.letters[i] + self.letters[i + 1]) in self.bangla.getTwelveDots().keys():
                        text += self.bangla.getTwelveDots().get(self.letters[i] + self.letters[i + 1])[0]
                        i += 1
                    elif self.letters[i] in self.bangla.getDouble_mapping().keys():
                        doubleMap = DoubleMap.DoubleMap(self.letters, i, bracket_count)
                        text += doubleMap.getCharFromDoubbleMap()
                        bracket_count = doubleMap.getBracket_count()
                        i += 1

                    elif self.letters[i] == '000100' and i + 2 < length:

                        text += dd.get(
                            self.letters[i + 1])[0] + hos + dd.get(self.letters[i + 2])[0]
                        i += 2
                        # print(2)
                        # print(hos)



                    elif self.letters[i] == '000101' and i + 4 < length:
                        # joint = ''
                        joint = dd.get(self.letters[i + 1])[0] + dd.get(self.letters[i + 2])[0] + dd.get(self.letters[i + 3])[0] + \
                                dd.get(self.letters[i + 4])[0]
                        if joint in self.bangla.getFourLetters().keys():
                            for key, value in self.bangla.getFourLetters().items():
                                if joint == key:
                                    text += dd.get(self.letters[i + 1])[0] + hos + dd.get(self.letters[i + 2])[0] + hos + \
                                            dd.get(self.letters[i + 3])[0] + hos + dd.get(self.letters[i + 4])[0]
                                    i += 4
                                    # print('4')
                                    break

                        else:
                            # joint = dd.get(letters[i + 1]) + dd.get(letters[i + 2]) + dd.get(letters[i + 3])

                            text += dd.get(self.letters[i + 1])[0] + hos + dd.get(self.letters[i + 2])[0] + hos + \
                                    dd.get(self.letters[i + 3])[0]
                            i += 3



                    else:

                        for k, v in dd.items():
                            if self.letters[i] == k:
                                text += v[0]

                                break

                    num = False

            i += 1
        text += ' '
        return text


