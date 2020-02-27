import os
from os.path import join
import tkinter
from tkinter import filedialog

class FileManager:  #files = root.tk.splitlist(files)
    def __init__(self): #folderpath
        pass
        #print(self.fileList)


    def getFiles(self):
        #braille_code = os.listdir(self.fileLocation)
        root = tkinter.Tk()
        fileList = root.tk.splitlist(filedialog.askopenfilenames(parent=root, title='Choose files'))
        final_list = fileList[:]
        for iFile in final_list:

            if iFile.lower().endswith(('.txt', '.doc', '.docx')):
                pass
            else:
                print("invalid file " + iFile + "removed")
                final_list.remove(iFile)

        return final_list
