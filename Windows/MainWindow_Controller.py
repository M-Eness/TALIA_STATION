from PySide6.QtWidgets import QMainWindow

from Windows.MainWindow_UI import Ui_MainWindow


class MainWindow_Controller():
    def __init__(self, mainWindow:QMainWindow, ui:Ui_MainWindow):
        self.mainWindow= mainWindow
        self.ui= ui

    def pbtn_start_clicked(self):
        self.ui.pushButton.setText("")