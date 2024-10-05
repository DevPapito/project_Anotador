class Framer():
    def __init__(self,instanceWindow,instanceTTK):
        
        self.__instanceWindow = instanceWindow
        self.__instanceTTK = instanceTTK
        self.__frame = None
    
    def frame(self,color:str,positionX:int,positionY:int,width:int,height:int):

        self.__frame = self.__instanceTTK.Frame(self.__instanceWindow,bootstyle=color)
        self.__frame.place(x=positionX,y=positionY,height=height,width=width)
    