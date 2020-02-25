import tkinter
from tkinter import filedialog
from oopBraille import BrailleToBangla
from oopBraille import brailleToEnglish
from oopBraille import BrailleToText
from oopBraille import fileManager
from oopBraille.postTextProcess import PostTextProcess
from oopBraille.BrailleToText import BrailleToText

root = tkinter.Tk()
filez = filedialog.askopenfilenames(parent=root, title='Choose files')
fileList = list(filez)

fileManager = fileManager.FileManager(fileList)
fileList = fileManager.getFiles()
processedText = PostTextProcess()
brailleToText = BrailleToText(fileList)
text = ''
#brailleToText = None

language = input('select language\n 1. Bangla\n2. English\n')
if language == '2' or language.find('e'):
    convert = brailleToEnglish.BrailleToEnglish()

else:
    convert = BrailleToBangla.BrailleToBangla()

text = brailleToText.getText(convert)
text = processedText.getPostTextProcess(text)
print(text)



'''
for fileName in fileList:
    print(fileName)
    file = open(fileName, 'r', )
    #file = open(fileName, 'r')

    lines = file.readlines()
    print(lines)
    text = ''
    brailleToBangla = BrailleToBangla.BrailleToBangla()
    for line in lines:
        words = line.split(' space ')
        # print(words)
        for word in words:
            letters = word.split(' ')
            text += brailleToBangla.getBrailleToText(letters) #(letters)
        text += '\n'

    print(text)
    outText = processedText.getPostTextProcess(text)
    print(outText)
    file.close()
quit()
'''
