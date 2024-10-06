from .Checker import Checker

class CreateData():

    checke = Checker()

    @classmethod
    def createFile(cls,filePath:str,fileName:str,modeFile:bool,text1:str,text2:str):

        cls.checke.chacked(filePath=filePath,fileName=fileName)

        try:

            completePath = (f'{filePath}{fileName}')

            if (modeFile):

                completePath = (f'{completePath}.md')
                cls.fileWrite(completePath,text1,text2)
        
            else:

                completePath = (f'{completePath}.html')
                cls.fileWrite(completePath,text1,text2)
            
            print('Arquivo criado')
        
        except FileNotFoundError:
        
            raise NotImplementedError('Diretorio ou arquivo nao existentes')

    # types structures files 

    @classmethod
    def fileWrite(cls,filer:str,text1:str,text2:str):
            
            with open(filer,'w') as fw:
                 
                 if ('.md' in filer):
                 
                    fw.write(cls.mdScruture(text1,text2))

                 else:
                      
                    fw.write(cls.htmlScruture(text1,text2))


    # types scructures files

    @classmethod
    def mdScruture(cls,text1:str,text2:str):
         
         STRUCTURE = f"""# Firts Topics
_________
{text2}
_________
Off Topics
{text1}"""

         return STRUCTURE
    
    @classmethod
    def htmlScruture(cls,text1:str,text2:str):
         
         STRUCTURE = f"""<h1>Firts Topcis</h1>
<p>-------------</p>
{text2}
<p>-------------</p>
<h2>Off Topics</h2>
{text1}"""
         
         return STRUCTURE