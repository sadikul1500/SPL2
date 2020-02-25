from oopBraille.BanglaTextProcess import BanglaTextProcess
from oopBraille import Bangla

class BrailleToBangla(BanglaTextProcess):

    bangla = Bangla.Bangla()

    def __init__(self):
        #self.text = text
        #self.textProcess = textProcess + BanglaTextProcess(self.text)
        BanglaTextProcess.__init__(self)
        print('braille to Bangla')

    '''
    def getText(self, text):
        textToProcess = BanglaTextProcess.BanglaTextProcess()
        return textToProcess.textProcess(text)
    '''
    def getBrailleToText(self, text):
        outText = self.textProcess(text)

        #length = len(outText)
        # for i in range(length):
        i = 0
        while i < len(outText):
            # print(i, text[i])
            if outText[i] in self.bangla.getVol_spe() and i > 0 and outText[i - 1] == '100000':
                outText = outText[:i - 1] + outText[i:]
            elif outText[i] in self.bangla.getSymbolToKar().keys() and i > 0 and\
                    outText[i - 1] in self.bangla.getConsonant().values():
                outText = outText[:i] + self.bangla.getSymbolToKar().get(outText[i]) + outText[i + 1:]

            i += 1

        #print('outText', outText)
        return outText
