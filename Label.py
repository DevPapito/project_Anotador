class Label():
    def __init__(self,instanceWindow,instanceTTK):

        self.__instanceWindow = instanceWindow
        self.__instanceTTK = instanceTTK
    
    def label(self,color:str, positionX:int, positionY:int, width:int, height:int,text:str):

        label = self.__instanceTTK.Label(self.__instanceWindow,text=text,background=color)
        label.place(x=positionX, y=positionY, width=width, height=height)
