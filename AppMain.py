import sys

from PySide6 import QtWidgets

from Windows.MainWindow_Form import MainWindow_Form

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MyMainWindow = MainWindow_Form()
    MyMainWindow.show()
    sys.exit(app.exec())