# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 812)
        MainWindow.setMinimumSize(QSize(1000, 600))
        MainWindow.setMaximumSize(QSize(1440, 900))
        MainWindow.setStyleSheet(u"background-color: rgb(46, 68, 99)")
        self.actionKopyala = QAction(MainWindow)
        self.actionKopyala.setObjectName(u"actionKopyala")
        self.actionYap_t_r = QAction(MainWindow)
        self.actionYap_t_r.setObjectName(u"actionYap_t_r")
        self.wgt_main = QWidget(MainWindow)
        self.wgt_main.setObjectName(u"wgt_main")
        self.wgt_main.setStyleSheet(u"background-color: rgb(46, 68, 99);")
        self.verticalLayout = QVBoxLayout(self.wgt_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frm_top = QFrame(self.wgt_main)
        self.frm_top.setObjectName(u"frm_top")
        self.frm_top.setMinimumSize(QSize(800, 50))
        self.frm_top.setMaximumSize(QSize(16777215, 100))
        self.frm_top.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_top.setFrameShadow(QFrame.Shadow.Raised)
        self.SicaklikLabel = QLabel(self.frm_top)
        self.SicaklikLabel.setObjectName(u"SicaklikLabel")
        self.SicaklikLabel.setGeometry(QRect(354, 17, 63, 16))
        self.SicaklikLabel.setMaximumSize(QSize(16777215, 16))
        self.label_7 = QLabel(self.frm_top)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(449, -10, 53, 70))
        self.BasincLabel_2 = QLabel(self.frm_top)
        self.BasincLabel_2.setObjectName(u"BasincLabel_2")
        self.BasincLabel_2.setGeometry(QRect(425, 17, 16, 16))
        self.BasincLabel_2.setMaximumSize(QSize(16777215, 16))
        self.label_10 = QLabel(self.frm_top)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(1369, -10, 22, 70))
        self.BasincLabel = QLabel(self.frm_top)
        self.BasincLabel.setObjectName(u"BasincLabel")
        self.BasincLabel.setGeometry(QRect(568, 17, 44, 16))
        self.BasincLabel.setMaximumSize(QSize(16777215, 16))
        self.label_3 = QLabel(self.frm_top)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(111, -10, 84, 70))
        self.label_4 = QLabel(self.frm_top)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(203, -10, 9, 70))
        self.TasiyiciYukseklikLabel_2 = QLabel(self.frm_top)
        self.TasiyiciYukseklikLabel_2.setObjectName(u"TasiyiciYukseklikLabel_2")
        self.TasiyiciYukseklikLabel_2.setGeometry(QRect(910, 15, 39, 20))
        self.TasiyiciYukseklikLabel_2.setMaximumSize(QSize(16777215, 20))
        self.PilGerilimiLabel_2 = QLabel(self.frm_top)
        self.PilGerilimiLabel_2.setObjectName(u"PilGerilimiLabel_2")
        self.PilGerilimiLabel_2.setGeometry(QRect(1249, 17, 20, 16))
        self.PilGerilimiLabel_2.setMaximumSize(QSize(16777215, 16))
        self.label_6 = QLabel(self.frm_top)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(312, -10, 34, 70))
        self.PilGerilimiLabel = QLabel(self.frm_top)
        self.PilGerilimiLabel.setObjectName(u"PilGerilimiLabel")
        self.PilGerilimiLabel.setGeometry(QRect(1174, 17, 67, 16))
        self.PilGerilimiLabel.setMaximumSize(QSize(16777215, 16))
        self.BasincLabel_3 = QLabel(self.frm_top)
        self.BasincLabel_3.setObjectName(u"BasincLabel_3")
        self.BasincLabel_3.setGeometry(QRect(620, 17, 50, 16))
        self.BasincLabel_3.setMaximumSize(QSize(16777215, 16))
        self.label_2 = QLabel(self.frm_top)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(97, -10, 6, 70))
        self.label_12 = QLabel(self.frm_top)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(1029, -10, 31, 70))
        self.label_11 = QLabel(self.frm_top)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(957, -10, 64, 70))
        self.GorevYukuHizLabel = QLabel(self.frm_top)
        self.GorevYukuHizLabel.setObjectName(u"GorevYukuHizLabel")
        self.GorevYukuHizLabel.setGeometry(QRect(1068, 17, 51, 16))
        self.GorevYukuHizLabel.setMaximumSize(QSize(16777215, 16))
        self.GorevYukuHizLabel_2 = QLabel(self.frm_top)
        self.GorevYukuHizLabel_2.setObjectName(u"GorevYukuHizLabel_2")
        self.GorevYukuHizLabel_2.setGeometry(QRect(1127, 17, 39, 16))
        self.GorevYukuHizLabel_2.setMaximumSize(QSize(16777215, 16))
        self.label = QLabel(self.frm_top)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(4, -10, 85, 70))
        self.label_5 = QLabel(self.frm_top)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, -10, 84, 70))
        self.GorevYukuYukseklikLabel = QLabel(self.frm_top)
        self.GorevYukuYukseklikLabel.setObjectName(u"GorevYukuYukseklikLabel")
        self.GorevYukuYukseklikLabel.setGeometry(QRect(678, 15, 85, 20))
        self.GorevYukuYukseklikLabel.setMaximumSize(QSize(16777215, 20))
        self.label_8 = QLabel(self.frm_top)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(510, -10, 50, 70))
        self.TasiyiciYukseklikLabel = QLabel(self.frm_top)
        self.TasiyiciYukseklikLabel.setObjectName(u"TasiyiciYukseklikLabel")
        self.TasiyiciYukseklikLabel.setGeometry(QRect(818, 15, 84, 20))
        self.TasiyiciYukseklikLabel.setMaximumSize(QSize(16777215, 20))
        self.label_9 = QLabel(self.frm_top)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(1277, -10, 84, 70))
        self.GorevYukuYukseklikLabel_2 = QLabel(self.frm_top)
        self.GorevYukuYukseklikLabel_2.setObjectName(u"GorevYukuYukseklikLabel_2")
        self.GorevYukuYukseklikLabel_2.setGeometry(QRect(771, 15, 39, 20))
        self.GorevYukuYukseklikLabel_2.setMaximumSize(QSize(16777215, 20))
        self.label_13 = QLabel(self.frm_top)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 70, 101, 16))
        self.label_14 = QLabel(self.frm_top)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(230, 70, 121, 16))
        self.label_15 = QLabel(self.frm_top)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(490, 70, 111, 16))
        self.label_16 = QLabel(self.frm_top)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(700, 70, 58, 16))
        self.label_17 = QLabel(self.frm_top)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(830, 70, 58, 16))
        self.label_18 = QLabel(self.frm_top)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(940, 70, 58, 16))
        self.label_19 = QLabel(self.frm_top)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(1310, 70, 58, 16))
        self.label_20 = QLabel(self.frm_top)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(1050, 70, 58, 16))
        self.label_21 = QLabel(self.frm_top)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(1180, 70, 58, 16))

        self.verticalLayout.addWidget(self.frm_top)

        self.frm_middle = QFrame(self.wgt_main)
        self.frm_middle.setObjectName(u"frm_middle")
        self.frm_middle.setStyleSheet(u"background-color: rgb(13, 17, 23)")
        self.frm_middle.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_middle.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frm_middle)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frm_middle_left = QFrame(self.frm_middle)
        self.frm_middle_left.setObjectName(u"frm_middle_left")
        self.frm_middle_left.setMinimumSize(QSize(300, 0))
        self.frm_middle_left.setMaximumSize(QSize(250, 16777215))
        self.frm_middle_left.setStyleSheet(u"background-color: rgb(118, 152, 194);\n"
"/*rgb(155, 195, 244)")
        self.frm_middle_left.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_middle_left.setFrameShadow(QFrame.Shadow.Raised)
        self.arasWidget = QWidget(self.frm_middle_left)
        self.arasWidget.setObjectName(u"arasWidget")
        self.arasWidget.setGeometry(QRect(40, 410, 201, 101))
        self.sistemBaslatButton = QPushButton(self.frm_middle_left)
        self.sistemBaslatButton.setObjectName(u"sistemBaslatButton")
        self.sistemBaslatButton.setGeometry(QRect(60, 50, 171, 51))
        self.sistemBaslatButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #800000; /* DarkRed (derin, kapal\u0131 bordo) */\n"
"    border: 1px solid #6A0DAD; /* DarkOrchid (hafif mor alt tonlu kapal\u0131 bordo \u00e7er\u00e7eve) */\n"
"    padding: 8px 16px;\n"
"    border-radius: 5px;\n"
"    font-size: 14px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #6A0DAD; /* \u00dczerine gelince biraz daha morumsu kapal\u0131 bordo */\n"
"    border: 1px solid #800000;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #A52A2A; /* Brown (k\u0131z\u0131l kahvemsi kapal\u0131 bordo) */\n"
"    border: 1px solid #8B0000; /* Daha derin bordo \u00e7er\u00e7eve */\n"
"    padding-left: 10px;\n"
"    padding-top: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A0522D; /* Sienna (soluk, toprak tonlu bordo) */\n"
"    border: 1px solid #800000;\n"
"    color: #CD853F; /* Peru */\n"
"}")
        self.telemetriAlButton = QPushButton(self.frm_middle_left)
        self.telemetriAlButton.setObjectName(u"telemetriAlButton")
        self.telemetriAlButton.setGeometry(QRect(60, 120, 171, 41))
        self.telemetriAlButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #800000; /* DarkRed (derin, kapal\u0131 bordo) */\n"
"    border: 1px solid #6A0DAD; /* DarkOrchid (hafif mor alt tonlu kapal\u0131 bordo \u00e7er\u00e7eve) */\n"
"    padding: 8px 16px;\n"
"    border-radius: 5px;\n"
"    font-size: 14px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #6A0DAD; /* \u00dczerine gelince biraz daha morumsu kapal\u0131 bordo */\n"
"    border: 1px solid #800000;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #A52A2A; /* Brown (k\u0131z\u0131l kahvemsi kapal\u0131 bordo) */\n"
"    border: 1px solid #8B0000; /* Daha derin bordo \u00e7er\u00e7eve */\n"
"    padding-left: 10px;\n"
"    padding-top: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A0522D; /* Sienna (soluk, toprak tonlu bordo) */\n"
"    border: 1px solid #800000;\n"
"    color: #CD853F; /* Peru */\n"
"}")
        self.ayrilmaGerceklestirButton = QPushButton(self.frm_middle_left)
        self.ayrilmaGerceklestirButton.setObjectName(u"ayrilmaGerceklestirButton")
        self.ayrilmaGerceklestirButton.setGeometry(QRect(60, 180, 171, 41))
        self.ayrilmaGerceklestirButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #800000; /* DarkRed (derin, kapal\u0131 bordo) */\n"
"    border: 1px solid #6A0DAD; /* DarkOrchid (hafif mor alt tonlu kapal\u0131 bordo \u00e7er\u00e7eve) */\n"
"    padding: 8px 16px;\n"
"    border-radius: 5px;\n"
"    font-size: 14px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #6A0DAD; /* \u00dczerine gelince biraz daha morumsu kapal\u0131 bordo */\n"
"    border: 1px solid #800000;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #A52A2A; /* Brown (k\u0131z\u0131l kahvemsi kapal\u0131 bordo) */\n"
"    border: 1px solid #8B0000; /* Daha derin bordo \u00e7er\u00e7eve */\n"
"    padding-left: 10px;\n"
"    padding-top: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A0522D; /* Sienna (soluk, toprak tonlu bordo) */\n"
"    border: 1px solid #800000;\n"
"    color: #CD853F; /* Peru */\n"
"}")
        self.videoSecButton = QPushButton(self.frm_middle_left)
        self.videoSecButton.setObjectName(u"videoSecButton")
        self.videoSecButton.setGeometry(QRect(60, 240, 171, 41))
        self.videoSecButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #800000; /* DarkRed (derin, kapal\u0131 bordo) */\n"
"    border: 1px solid #6A0DAD; /* DarkOrchid (hafif mor alt tonlu kapal\u0131 bordo \u00e7er\u00e7eve) */\n"
"    padding: 8px 16px;\n"
"    border-radius: 5px;\n"
"    font-size: 14px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #6A0DAD; /* \u00dczerine gelince biraz daha morumsu kapal\u0131 bordo */\n"
"    border: 1px solid #800000;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #A52A2A; /* Brown (k\u0131z\u0131l kahvemsi kapal\u0131 bordo) */\n"
"    border: 1px solid #8B0000; /* Daha derin bordo \u00e7er\u00e7eve */\n"
"    padding-left: 10px;\n"
"    padding-top: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A0522D; /* Sienna (soluk, toprak tonlu bordo) */\n"
"    border: 1px solid #800000;\n"
"    color: #CD853F; /* Peru */\n"
"}")
        self.videoGonderButton = QPushButton(self.frm_middle_left)
        self.videoGonderButton.setObjectName(u"videoGonderButton")
        self.videoGonderButton.setGeometry(QRect(60, 300, 171, 41))
        self.videoGonderButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #800000; /* DarkRed (derin, kapal\u0131 bordo) */\n"
"    border: 1px solid #6A0DAD; /* DarkOrchid (hafif mor alt tonlu kapal\u0131 bordo \u00e7er\u00e7eve) */\n"
"    padding: 8px 16px;\n"
"    border-radius: 5px;\n"
"    font-size: 14px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #6A0DAD; /* \u00dczerine gelince biraz daha morumsu kapal\u0131 bordo */\n"
"    border: 1px solid #800000;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #A52A2A; /* Brown (k\u0131z\u0131l kahvemsi kapal\u0131 bordo) */\n"
"    border: 1px solid #8B0000; /* Daha derin bordo \u00e7er\u00e7eve */\n"
"    padding-left: 10px;\n"
"    padding-top: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A0522D; /* Sienna (soluk, toprak tonlu bordo) */\n"
"    border: 1px solid #800000;\n"
"    color: #CD853F; /* Peru */\n"
"}")
        self.sistemDurdurButton = QPushButton(self.frm_middle_left)
        self.sistemDurdurButton.setObjectName(u"sistemDurdurButton")
        self.sistemDurdurButton.setGeometry(QRect(60, 360, 171, 41))
        self.sistemDurdurButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #800000; /* DarkRed (derin, kapal\u0131 bordo) */\n"
"    border: 1px solid #6A0DAD; /* DarkOrchid (hafif mor alt tonlu kapal\u0131 bordo \u00e7er\u00e7eve) */\n"
"    padding: 8px 16px;\n"
"    border-radius: 5px;\n"
"    font-size: 14px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #6A0DAD; /* \u00dczerine gelince biraz daha morumsu kapal\u0131 bordo */\n"
"    border: 1px solid #800000;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #A52A2A; /* Brown (k\u0131z\u0131l kahvemsi kapal\u0131 bordo) */\n"
"    border: 1px solid #8B0000; /* Daha derin bordo \u00e7er\u00e7eve */\n"
"    padding-left: 10px;\n"
"    padding-top: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A0522D; /* Sienna (soluk, toprak tonlu bordo) */\n"
"    border: 1px solid #800000;\n"
"    color: #CD853F; /* Peru */\n"
"}")

        self.horizontalLayout_3.addWidget(self.frm_middle_left)

        self.frm_middle_middle = QFrame(self.frm_middle)
        self.frm_middle_middle.setObjectName(u"frm_middle_middle")
        self.frm_middle_middle.setStyleSheet(u"background-color: rgb(5, 69, 105);\n"
"")
        self.frm_middle_middle.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_middle_middle.setFrameShadow(QFrame.Shadow.Raised)
        self.graphs_container = QWidget(self.frm_middle_middle)
        self.graphs_container.setObjectName(u"graphs_container")
        self.graphs_container.setGeometry(QRect(0, 0, 761, 491))
        self.gridLayout = QGridLayout(self.graphs_container)
        self.gridLayout.setObjectName(u"gridLayout")

        self.horizontalLayout_3.addWidget(self.frm_middle_middle)

        self.frm_middle_right = QFrame(self.frm_middle)
        self.frm_middle_right.setObjectName(u"frm_middle_right")
        self.frm_middle_right.setMinimumSize(QSize(300, 0))
        self.frm_middle_right.setMaximumSize(QSize(250, 500))
        self.frm_middle_right.setStyleSheet(u"background-color: rgb(118, 152, 194);")
        self.frm_middle_right.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_middle_right.setFrameShadow(QFrame.Shadow.Raised)
        self.camera_label = QLabel(self.frm_middle_right)
        self.camera_label.setObjectName(u"camera_label")
        self.camera_label.setGeometry(QRect(27, 85, 211, 111))

        self.horizontalLayout_3.addWidget(self.frm_middle_right)


        self.verticalLayout.addWidget(self.frm_middle)

        self.frm_bottom = QFrame(self.wgt_main)
        self.frm_bottom.setObjectName(u"frm_bottom")
        self.frm_bottom.setMaximumSize(QSize(16777215, 100))
        self.frm_bottom.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_bottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frm_bottom)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.terminal_plainTextEdit = QPlainTextEdit(self.frm_bottom)
        self.terminal_plainTextEdit.setObjectName(u"terminal_plainTextEdit")
        self.terminal_plainTextEdit.setStyleSheet(u"background-color: rgb(71, 69, 71);\n"
"")

        self.verticalLayout_4.addWidget(self.terminal_plainTextEdit)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout.addWidget(self.frm_bottom)

        MainWindow.setCentralWidget(self.wgt_main)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionKopyala.setText(QCoreApplication.translate("MainWindow", u"Kopyala", None))
        self.actionYap_t_r.setText(QCoreApplication.translate("MainWindow", u"Yap\u0131\u015ft\u0131r", None))
        self.SicaklikLabel.setText(QCoreApplication.translate("MainWindow", u"S\u0131cakl\u0131k:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Bas\u0131n\u00e7 1:", None))
        self.BasincLabel_2.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.BasincLabel.setText(QCoreApplication.translate("MainWindow", u"Bas\u0131n\u00e7:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Uydu Stat\u00fcs\u00fc:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.TasiyiciYukseklikLabel_2.setText(QCoreApplication.translate("MainWindow", u"250 m", None))
        self.PilGerilimiLabel_2.setText(QCoreApplication.translate("MainWindow", u"7 V", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"13.00", None))
        self.PilGerilimiLabel.setText(QCoreApplication.translate("MainWindow", u"Pil Gerilimi:", None))
        self.BasincLabel_3.setText(QCoreApplication.translate("MainWindow", u"0.9 ATM", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"50 m", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0130rtifa Fark\u0131:", None))
        self.GorevYukuHizLabel.setText(QCoreApplication.translate("MainWindow", u"\u0130ni\u015f H\u0131z\u0131:", None))
        self.GorevYukuHizLabel_2.setText(QCoreApplication.translate("MainWindow", u"10 m/s", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Paket Numaras\u0131:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"G\u00f6nderme Saati:", None))
        self.GorevYukuYukseklikLabel.setText(QCoreApplication.translate("MainWindow", u"G\u00f6rev Y\u00fck\u00fc Y\u00fckseklik:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"0.9 ATM", None))
        self.TasiyiciYukseklikLabel.setText(QCoreApplication.translate("MainWindow", u"Ta\u015f\u0131y\u0131c\u0131 Y\u00fckseklik:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Pil Durumu %:", None))
        self.GorevYukuYukseklikLabel_2.setText(QCoreApplication.translate("MainWindow", u"300 m", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"GPS1 LATITUDE:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"GPS1 LONGITUDE:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"GPS1 ALTITUDE:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Pitch:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Roll:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Yaw:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Tak\u0131m No:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u" S1 Data:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"S2 Data:", None))
        self.sistemBaslatButton.setText(QCoreApplication.translate("MainWindow", u"Sistemi Ba\u015flat", None))
        self.telemetriAlButton.setText(QCoreApplication.translate("MainWindow", u"Telemetri Al", None))
        self.ayrilmaGerceklestirButton.setText(QCoreApplication.translate("MainWindow", u"Ayr\u0131lmay\u0131 Ger\u00e7ekle\u015ftir", None))
        self.videoSecButton.setText(QCoreApplication.translate("MainWindow", u"Video Se\u00e7", None))
        self.videoGonderButton.setText(QCoreApplication.translate("MainWindow", u"Video G\u00f6nder", None))
        self.sistemDurdurButton.setText(QCoreApplication.translate("MainWindow", u"Sistemi Durdur", None))
        self.camera_label.setText("")
    # retranslateUi

