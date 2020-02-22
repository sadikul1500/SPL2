#from tkinter.filedialog import askopenfilename
#from tkinter import Tk
from word import BrailleToBangla

#Tk.withdraw()
fileName = 'G:\\f drive\\1IIT\\5th semester\\SPL2\\test.txt'
print(fileName)
file = open(fileName, 'r')

lines = file.readlines()
print(lines)
text = ''
brailleToBangla = BrailleToBangla.BrailleToBangla(lines)
for line in lines:
    words = line.split(' space ')
    # print(words)
    for word in words:
        letters = word.split(' ')
        text += brailleToBangla.getBrailleToBangla() #(letters)
    text += '\n'

print(text)
file.close()
quit()
