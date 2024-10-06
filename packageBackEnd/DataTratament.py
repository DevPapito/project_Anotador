class DataTratament():

    def noSpacer(self,data:str):

        return data.strip()

    def forPathsFormater(self,dataPath:str):
        
        newData = dataPath.replace('\\','\\\\')

        return newData
