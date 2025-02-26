from PySide6.QtWidgets import QMainWindow

from Windows.MainWindow_Controller import MainWindow_Controller
from Windows.MainWindow_UI import Ui_MainWindow


class MainWindow_Form(QMainWindow):
    def __init__(self):
        super(MainWindow_Form,self).__init__()
        self.ui=  Ui_MainWindow()
        self.ui.setupUi(self)
        self.cntlr= MainWindow_Controller(self, self.ui)
        #self.initilizeComponents()

 #   def initilizeComponents(self):
