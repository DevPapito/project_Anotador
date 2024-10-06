import os

class CreateData():
    def __init__(self,filePath:str,fileName:str,modeFile:bool,text1:str,text2:str):

        self.__filePath = filePath
        self.__fileName = fileName
        self.__modeFile = modeFile
        self.__text1 = text1
        self.__text2 = text2
    
    def createFile(self):

        try:    

            completePath = (f'{self.__filePath}{self.__fileName}')

            if (self.__modeFile):

                completePath + '.md'

                self.fileWrite(completePath)
            
            elif (not self.__modeFile):

                completePath + '.html'

                self.fileWrite(completePath)

        except Exception:

            print(Exception)
        
    def fileWrite(self,file:str):

        with open(file,'w') as fw:

            fw.write(self.__text1)
            fw.write(self.__text2)
    
