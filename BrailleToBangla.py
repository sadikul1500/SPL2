from word import BanglaTextProcess
from word import Bangla

class BrailleToBangla:

    bangla = Bangla.Bangla()

    def __init__(self, text):
        self.text = text
        #self.textProcess = textProcess + BanglaTextProcess(self.text)
        print('braille to bangla')


    def getText(self):
        textToProcess = BanglaTextProcess.BanglaTextProcess(self.text)
        return textToProcess.textProcess()

    def getBrailleToBangla(self):
        outText = self.getText()

        #length = len(outText)
        # for i in range(length):
        i = 0
        while i < len(outText):
            # print(i, text[i])
            if outText[i] in self.bangla.getVol_spe() and i > 0 and outText[i - 1] == '100000':
                outText = outText[:i - 1] + outText[i:]
            elif outText[i] in self.bangla.getSymbolToKar().keys() and i > 0 and\
                    outText[i - 1] in self.bangla.getConsonant().values():
                text = outText[:i] + self.bangla.getSymbolToKar().get(outText[i]) + outText[i + 1:]

            i += 1

        print('outText', outText)
        return outText


