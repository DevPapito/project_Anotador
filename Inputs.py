class Inputs():
    def __init__(self,instanceWindow,instanceTTK):
        
        self.__instanceWindow = instanceWindow
        self.__instanceTTK = instanceTTK
    
    def entry(self,color:str,positionX:int,positionY:int,width:int,height:int):

        entry = self.__instanceTTK.Entry(self.__instanceWindow,bootstyle=color)
        entry.place(x=positionX,y=positionY,width=width,height=height)
    
    def rounded(self, color:str, positionX:int, positionY:int, width:int, height:int):

        rounded = self.__instanceTTK.Checkbutton(self.__instanceWindow,bootstyle=f"{color},round-toggle")
        rounded.place(x=positionX,y=positionY)
