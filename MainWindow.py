from ttkbootstrap.constants import *
import ttkbootstrap as ttk

from packageGrafic.Label import Label
from packageGrafic.WindowStyle import  WindowStyle
from packageGrafic.Framer import Framer
from packageGrafic.Inputs import Inputs
from packageGrafic.Button import Button
from packageGrafic.Texts import Texts

from packageBackEnd.DataTratament import DataTratament
from packageBackEnd.CreateData import CreateData

class MainWindow():

    _window = ttk.Window(themename='darkly')
    _windowStyle = WindowStyle(_window,ttk)

    frameScapeButtons = Framer(_window,ttk)
    frameAreaText = Framer(_window,ttk)

    frameGraphic01 = Framer(_window,ttk)

    fileName = Inputs(_window,ttk)
    filePath = Inputs(_window,ttk)

    roundToggle = Inputs(_window,ttk)

    envietButton = Button(_window,ttk)

    label01 = Label(_window,ttk)
    label02 = Label(_window,ttk)
    label03 = Label(_window,ttk)
    label04 = Label(_window,ttk)
    label05 = Label(_window,ttk)
    
    textEntry01 = Texts(_window,ttk)
    textEntry02 = Texts(_window,ttk)

    @classmethod
    def main(cls):

        # FRONT-END -------------------------------
        
        cls._windowStyle.style('Anotador','900x600')

        # frames

        cls.frameScapeButtons.frame('dark',10,10,310,580)
        cls.frameAreaText.frame('secondary',330,10,560,580)
        cls.frameGraphic01.frame('#303030',10,140,310,30)

        # entrys

        getName = cls.fileName.entry('light',20,30,290,30)
        getPath = cls.filePath.entry('light',20,95,290,30)
        
        # labels

        cls.label01.label('#303030',20,10,135,25,"Nome do Arquivo")
        cls.label02.label('#303030',20,75,210,25,"Caminho de Armazenamento")
        cls.label03.label('#222222',10,142,50,25,"Html")
        cls.label04.label('#222222',85,142,100,25,"MarkDown")
        cls.label05.label('#303030',15,295,200,25,"Topicos Importantes")

        # checkbutton
        
        getRounded,getBoolean = cls.roundToggle.rounded('light',50,145,100,100)

        # textEntrys

        getText1 = cls.textEntry01.text(15,320,300,265)
        getText2 = cls.textEntry02.text(340,20,540,560)

        # BACK-END --------------------------------

        dataTratament = DataTratament()
        
        # button/function

        cls.envietButton.command(lambda:CreateData.createFile(filePath=dataTratament.forPathsFormater(dataTratament.noSpacer(getPath.get())),
                                                              fileName=dataTratament.forPathsFormater(dataTratament.noSpacer(getName.get())),
                                                              modeFile=getBoolean.get(),
                                                              text1=getText1.get("1.0","end-1c"),
                                                              text2=getText2.get("1.0","end-1c")))

        cls.envietButton.buttonOutline('success',60,200,200,50,"Envie")

        cls._window.mainloop()

if __name__ == '__main__':
    MainWindow().main()