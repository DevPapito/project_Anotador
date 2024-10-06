class WindowStyle(): 
    def __init__(self,instanceWindow,instanceTTK):

        self._instanceWindow = instanceWindow
        self._instanceTTK = instanceTTK

    def style(self,title:str,size:str):

        self._instanceWindow.title(title)
        self._instanceWindow.geometry(size)    
        self._instanceWindow.resizable(False,False)

