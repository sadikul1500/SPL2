from oopBraille.BrailleToBangla import BrailleToBangla
from oopBraille.brailleToEnglish import BrailleToEnglish

class BrailleToText:
    def __init__(self, fileList):
        self.fileList = fileList

    def getText(self, x):
        for fileName in self.fileList:
            print(fileName)
            file = open(fileName, 'r', )
            # file = open(fileName, 'r')

            lines = file.readlines()
            print(lines)
            text = ''
            #brailleToBangla = BrailleToBangla.BrailleToBangla()
            for line in lines:
                words = line.split(' space ')
                # print(words)
                for word in words:
                    letters = word.split(' ')
                    text += x.getBrailleToText(letters)  # (letters)
                text += '\n'

            #print(text)
            #outText = processedText.getPostTextProcess(text)
            #print(outText)
            file.close()
