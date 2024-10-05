class Texts():
    def __init__(self,instanceWindow,instanceTTK):

        self.__instanceWindow = instanceWindow
        self.__instanceTTK = instanceTTK
    
    def text(self,positonX:int,positonY:int,width:int,height:int):

        text = self.__instanceTTK.Text(self.__instanceWindow)
        
        text.place(x=positonX, y=positonY, width=width, height=height)
        return text
    
    def textScrolled(self,color:str,positionX:int,positionY:int,width:int,height:int):

        text = self.__instanceTTK.ScrolledText(self.__instanceTTK,bootstyle=color,wrap=self.__instanceTTK.WORD)
        text.place(x=positionX, y= positionY, width=width,height=height)
        
        return text
    
 
    
    
