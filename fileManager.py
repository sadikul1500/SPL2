import os
from os.path import join

class FileManager:
    def __init__(self, fileList):   #folderpath
        self.fileList = fileList

    def getFiles(self):
        #braille_code = os.listdir(self.fileLocation)
        final_list = self.fileList[:]
        for iFile in final_list:

            if iFile.lower().endswith(('.txt', '.doc', '.docx')):
                pass
            else:
                print("invalid file " + iFile + "removed")
                final_list.remove(iFile)

        return final_list