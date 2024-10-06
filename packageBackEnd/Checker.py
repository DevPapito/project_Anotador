
class Checker():

    @classmethod
    def chacked(cls,filePath:str,fileName:str):

        # filePath 

        print('Verificacao inicializada!')

        try:

            # filePath 

            cls.checkedFilePath(filePath=filePath)
            cls.checkedFileName(fileName=fileName)

        except IOError:
                
            raise NotImplementedError('Erro de entrada!')

        finally:

            print('Verificacao finalizada!')

    @classmethod
    def checkedFilePath(cls, filePath:str):

        if (not '\\' in filePath or len(filePath) == 0):
            
            raise NotImplementedError('Caminho de arquivo vazio ou sem barras de diretorio')
        
    @classmethod
    def checkedFileName(cls,fileName:str):

        if (len(fileName) == 0 or len(fileName) < 6):

            raise NotImplementedError('Nome de arquivo vazio ou pequeno de mais(minimo 6 caracteres)')

