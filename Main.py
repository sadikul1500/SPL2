from tkinter.filedialog import askopenfilename
from word.BrailleToBangla import BrailleToBangla

fileName = askopenfilename()
file = open(fileName, 'r')

lines = file.readlines()
text = ''
brailleToBangla = BrailleToBangla(lines, '')
for line in lines:
    words = line.split(' space ')
    # print(words)
    for word in words:
        letters = word.split(' ')
        text += brailleToBangla.getBrailleToBangla() #(letters)
    text += '\n'

print(text)