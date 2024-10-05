class Button():
    def __init__(self,instanceWindow,instanceTTK):

        self.__instanceWindow = instanceWindow
        self.__instanceTTK = instanceTTK
        self.__command = None
    
    def button(self,color:str,positionX:int,positionY:int,width:int,height:int,text:str):

        button = self.__instanceTTK.Button(self.__instanceWindow,bootstyle=color,text=text,command=self.__command)
        button.place(x=positionX, y=positionY, width=width, height=height)
    
    def buttonOutline(self,color:str,positionX:int,positionY:int,width:int,height:int,text:str):

        button = self.__instanceTTK.Button(self.__instanceWindow,bootstyle=f'{color}-outline',text=text,command=self.__command)
        button.place(x=positionX, y=positionY, width=width, height=height)
    
    # setCommand
    def command(self,command):

        self.__command = command
    
    
    

