class CreateData():

    @classmethod
    def createFile(cls,filePath:str,fileName:str,modeFile:bool,text1:str,text2:str):

        try:

            completePath = (f'{filePath}{fileName}')
        
            if (modeFile):

                completePath = (f'{completePath}.md')
                cls.fileWrite(completePath,text1,text2)
        
            else:

                completePath = (f'{completePath}.html')
                cls.fileWrite(completePath,text1,text2)
        
        except Exception:
        
            print(Exception)

    @classmethod
    def fileWrite(cls,filer:str,text1:str,text2:str):
            
            with open(filer,'w') as fw:
                 
                 fw.write(f'{text2}\n')
                 fw.write(text1)
