#from tkinter.filedialog import askopenfilename
#from tkinter.filedialog import askdirectory
#from tkinter import Tk
import tkinter
from tkinter import filedialog
from oopBraille import BrailleToBangla
from oopBraille import fileManager
from os.path import join

#Tk.withdraw()
root = tkinter.Tk()
filez = filedialog.askopenfilenames(parent=root, title='Choose files')
fileList = list(filez)
#folderPath = askdirectory()
fileManager = fileManager.FileManager(fileList)
fileList = fileManager.getFiles()
#fileName = 'G:\\5 th semester\\spl2\\dataFrom Online\\data_jackson.txt'
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
            text += brailleToBangla.getBrailleToBangla(letters) #(letters)
        text += '\n'

    print(text)
    file.close()
quit()
