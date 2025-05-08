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
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

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
        self.widget = QWidget(self.frm_top)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(2, 13, 2220, 188))
        self.gridLayoutTelemetry = QGridLayout(self.widget)
        self.gridLayoutTelemetry.setObjectName(u"gridLayoutTelemetry")
        self.gridLayoutTelemetry.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.gridLayoutTelemetry.setContentsMargins(0, 0, 0, 0)
        self.TakimNoLabel2 = QLabel(self.widget)
        self.TakimNoLabel2.setObjectName(u"TakimNoLabel2")

        self.gridLayoutTelemetry.addWidget(self.TakimNoLabel2, 1, 31, 2, 1)

        self.GorevYukuYukseklikLabel = QLabel(self.widget)
        self.GorevYukuYukseklikLabel.setObjectName(u"GorevYukuYukseklikLabel")
        self.GorevYukuYukseklikLabel.setMaximumSize(QSize(16777215, 20))

        self.gridLayoutTelemetry.addWidget(self.GorevYukuYukseklikLabel, 2, 9, 1, 1)

        self.RollLabel = QLabel(self.widget)
        self.RollLabel.setObjectName(u"RollLabel")

        self.gridLayoutTelemetry.addWidget(self.RollLabel, 1, 16, 1, 1)

        self.S2Label2 = QLabel(self.widget)
        self.S2Label2.setObjectName(u"S2Label2")

        self.gridLayoutTelemetry.addWidget(self.S2Label2, 1, 21, 2, 1)

        self.InisHiziLabel = QLabel(self.widget)
        self.InisHiziLabel.setObjectName(u"InisHiziLabel")
        self.InisHiziLabel.setMaximumSize(QSize(16777215, 16))

        self.gridLayoutTelemetry.addWidget(self.InisHiziLabel, 2, 6, 1, 1)

        self.TakimNoLabel = QLabel(self.widget)
        self.TakimNoLabel.setObjectName(u"TakimNoLabel")

        self.gridLayoutTelemetry.addWidget(self.TakimNoLabel, 1, 18, 2, 1)

        self.GpsLonLabel = QLabel(self.widget)
        self.GpsLonLabel.setObjectName(u"GpsLonLabel")

        self.gridLayoutTelemetry.addWidget(self.GpsLonLabel, 1, 13, 2, 1)

        self.GpsAltLabel2 = QLabel(self.widget)
        self.GpsAltLabel2.setObjectName(u"GpsAltLabel2")

        self.gridLayoutTelemetry.addWidget(self.GpsAltLabel2, 1, 29, 2, 1)

        self.RollLabel2 = QLabel(self.widget)
        self.RollLabel2.setObjectName(u"RollLabel2")

        self.gridLayoutTelemetry.addWidget(self.RollLabel2, 1, 30, 2, 1)

        self.TasiyiciYukseklikLabel2 = QLabel(self.widget)
        self.TasiyiciYukseklikLabel2.setObjectName(u"TasiyiciYukseklikLabel2")
        self.TasiyiciYukseklikLabel2.setMaximumSize(QSize(16777215, 20))

        self.gridLayoutTelemetry.addWidget(self.TasiyiciYukseklikLabel2, 2, 8, 1, 1)

        self.PitchLabel2 = QLabel(self.widget)
        self.PitchLabel2.setObjectName(u"PitchLabel2")

        self.gridLayoutTelemetry.addWidget(self.PitchLabel2, 1, 23, 2, 1)

        self.YawLabel2 = QLabel(self.widget)
        self.YawLabel2.setObjectName(u"YawLabel2")

        self.gridLayoutTelemetry.addWidget(self.YawLabel2, 1, 24, 1, 1)

        self.S2Label = QLabel(self.widget)
        self.S2Label.setObjectName(u"S2Label")

        self.gridLayoutTelemetry.addWidget(self.S2Label, 1, 20, 2, 1)

        self.GpsLatLabel2 = QLabel(self.widget)
        self.GpsLatLabel2.setObjectName(u"GpsLatLabel2")

        self.gridLayoutTelemetry.addWidget(self.GpsLatLabel2, 1, 22, 1, 1)

        self.GpsAltLabel = QLabel(self.widget)
        self.GpsAltLabel.setObjectName(u"GpsAltLabel")

        self.gridLayoutTelemetry.addWidget(self.GpsAltLabel, 1, 14, 2, 1)

        self.GpsLatLabel = QLabel(self.widget)
        self.GpsLatLabel.setObjectName(u"GpsLatLabel")

        self.gridLayoutTelemetry.addWidget(self.GpsLatLabel, 1, 12, 2, 1)

        self.S1Label2 = QLabel(self.widget)
        self.S1Label2.setObjectName(u"S1Label2")

        self.gridLayoutTelemetry.addWidget(self.S1Label2, 1, 25, 1, 1)

        self.Basinc2Label = QLabel(self.widget)
        self.Basinc2Label.setObjectName(u"Basinc2Label")
        self.Basinc2Label.setMaximumSize(QSize(16777215, 16))

        self.gridLayoutTelemetry.addWidget(self.Basinc2Label, 2, 2, 1, 1)

        self.YawLabel = QLabel(self.widget)
        self.YawLabel.setObjectName(u"YawLabel")

        self.gridLayoutTelemetry.addWidget(self.YawLabel, 1, 17, 1, 1)

        self.GpsLonLabel2 = QLabel(self.widget)
        self.GpsLonLabel2.setObjectName(u"GpsLonLabel2")

        self.gridLayoutTelemetry.addWidget(self.GpsLonLabel2, 1, 28, 2, 1)

        self.InisHiziLabel2 = QLabel(self.widget)
        self.InisHiziLabel2.setObjectName(u"InisHiziLabel2")
        self.InisHiziLabel2.setMaximumSize(QSize(16777215, 16))

        self.gridLayoutTelemetry.addWidget(self.InisHiziLabel2, 2, 7, 1, 1)

        self.SicaklikLabel = QLabel(self.widget)
        self.SicaklikLabel.setObjectName(u"SicaklikLabel")
        self.SicaklikLabel.setMaximumSize(QSize(16777215, 16))

        self.gridLayoutTelemetry.addWidget(self.SicaklikLabel, 2, 0, 1, 1)

        self.TasiyiciYukseklikLabel = QLabel(self.widget)
        self.TasiyiciYukseklikLabel.setObjectName(u"TasiyiciYukseklikLabel")
        self.TasiyiciYukseklikLabel.setMaximumSize(QSize(16777215, 20))

        self.gridLayoutTelemetry.addWidget(self.TasiyiciYukseklikLabel, 2, 10, 1, 1)

        self.Basinc2Label2 = QLabel(self.widget)
        self.Basinc2Label2.setObjectName(u"Basinc2Label2")
        self.Basinc2Label2.setMaximumSize(QSize(16777215, 16))

        self.gridLayoutTelemetry.addWidget(self.Basinc2Label2, 2, 5, 1, 1)

        self.PaketNumLabel = QLabel(self.widget)
        self.PaketNumLabel.setObjectName(u"PaketNumLabel")

        self.gridLayoutTelemetry.addWidget(self.PaketNumLabel, 1, 32, 2, 1)

        self.PaketNumLabel2 = QLabel(self.widget)
        self.PaketNumLabel2.setObjectName(u"PaketNumLabel2")

        self.gridLayoutTelemetry.addWidget(self.PaketNumLabel2, 3, 4, 1, 1)

        self.BasincLabel = QLabel(self.widget)
        self.BasincLabel.setObjectName(u"BasincLabel")

        self.gridLayoutTelemetry.addWidget(self.BasincLabel, 1, 27, 1, 1)

        self.GorevYukuYukseklikLabel2 = QLabel(self.widget)
        self.GorevYukuYukseklikLabel2.setObjectName(u"GorevYukuYukseklikLabel2")
        self.GorevYukuYukseklikLabel2.setMaximumSize(QSize(16777215, 20))

        self.gridLayoutTelemetry.addWidget(self.GorevYukuYukseklikLabel2, 2, 11, 1, 1)

        self.UyduStatLabel = QLabel(self.widget)
        self.UyduStatLabel.setObjectName(u"UyduStatLabel")

        self.gridLayoutTelemetry.addWidget(self.UyduStatLabel, 1, 10, 1, 1)

        self.S1Label = QLabel(self.widget)
        self.S1Label.setObjectName(u"S1Label")

        self.gridLayoutTelemetry.addWidget(self.S1Label, 1, 19, 2, 1)

        self.PitchLabel = QLabel(self.widget)
        self.PitchLabel.setObjectName(u"PitchLabel")

        self.gridLayoutTelemetry.addWidget(self.PitchLabel, 1, 15, 1, 1)

        self.PilGerilimiLabel2 = QLabel(self.widget)
        self.PilGerilimiLabel2.setObjectName(u"PilGerilimiLabel2")
        self.PilGerilimiLabel2.setMaximumSize(QSize(16777215, 16))

        self.gridLayoutTelemetry.addWidget(self.PilGerilimiLabel2, 2, 3, 1, 1)

        self.PilGerilimiLabel = QLabel(self.widget)
        self.PilGerilimiLabel.setObjectName(u"PilGerilimiLabel")
        self.PilGerilimiLabel.setMaximumSize(QSize(16777215, 16))

        self.gridLayoutTelemetry.addWidget(self.PilGerilimiLabel, 2, 4, 1, 1)

        self.SicaklikLabel2 = QLabel(self.widget)
        self.SicaklikLabel2.setObjectName(u"SicaklikLabel2")
        self.SicaklikLabel2.setMaximumSize(QSize(16777215, 16))

        self.gridLayoutTelemetry.addWidget(self.SicaklikLabel2, 2, 1, 1, 1)

        self.BasincLabel2 = QLabel(self.widget)
        self.BasincLabel2.setObjectName(u"BasincLabel2")

        self.gridLayoutTelemetry.addWidget(self.BasincLabel2, 1, 26, 1, 1)

        self.UyduStatLabel2 = QLabel(self.widget)
        self.UyduStatLabel2.setObjectName(u"UyduStatLabel2")

        self.gridLayoutTelemetry.addWidget(self.UyduStatLabel2, 0, 10, 1, 1)


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
        self.frm_middle_left.setMaximumSize(QSize(300, 16777215))
        self.frm_middle_left.setStyleSheet(u"background-color: rgb(118, 152, 194);\n"
"/*rgb(155, 195, 244)")
        self.frm_middle_left.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_middle_left.setFrameShadow(QFrame.Shadow.Raised)
        self.sistemBaslatButton = QPushButton(self.frm_middle_left)
        self.sistemBaslatButton.setObjectName(u"sistemBaslatButton")
        self.sistemBaslatButton.setGeometry(QRect(60, 20, 171, 38))
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
        self.telemetriAlButton.setGeometry(QRect(60, 70, 171, 38))
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
        self.ayrilmaGerceklestirButton.setGeometry(QRect(60, 120, 171, 38))
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
        self.videoSecButton.setGeometry(QRect(60, 170, 171, 38))
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
        self.videoGonderButton.setGeometry(QRect(60, 220, 171, 38))
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
        self.sistemDurdurButton.setGeometry(QRect(60, 270, 171, 38))
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
        self.arasWidget = QWidget(self.frm_middle_left)
        self.arasWidget.setObjectName(u"arasWidget")
        self.arasWidget.setGeometry(QRect(40, 310, 200, 121))
        self.layoutWidget = QWidget(self.frm_middle_left)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 440, 178, 73))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.rhrh_input = QLineEdit(self.layoutWidget)
        self.rhrh_input.setObjectName(u"rhrh_input")
        self.rhrh_input.setStyleSheet(u"QLineEdit {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 4px;\n"
"}")

        self.verticalLayout_2.addWidget(self.rhrh_input)

        self.rhrh_button = QPushButton(self.layoutWidget)
        self.rhrh_button.setObjectName(u"rhrh_button")
        self.rhrh_button.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.rhrh_button)


        self.horizontalLayout_3.addWidget(self.frm_middle_left)

        self.frm_middle_middle = QFrame(self.frm_middle)
        self.frm_middle_middle.setObjectName(u"frm_middle_middle")
        self.frm_middle_middle.setStyleSheet(u"background-color: rgb(5, 69, 105);\n"
"")
        self.frm_middle_middle.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_middle_middle.setFrameShadow(QFrame.Shadow.Raised)
        self.graphs_container = QWidget(self.frm_middle_middle)
        self.graphs_container.setObjectName(u"graphs_container")
        self.graphs_container.setGeometry(QRect(0, 0, 761, 501))
        self.gridLayout = QGridLayout(self.graphs_container)
        self.gridLayout.setObjectName(u"gridLayout")

        self.horizontalLayout_3.addWidget(self.frm_middle_middle)

        self.frm_middle_right = QFrame(self.frm_middle)
        self.frm_middle_right.setObjectName(u"frm_middle_right")
        self.frm_middle_right.setMinimumSize(QSize(300, 0))
        self.frm_middle_right.setMaximumSize(QSize(300, 10000))
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
        self.TakimNoLabel2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>1111</p></body></html>", None))
        self.GorevYukuYukseklikLabel.setText(QCoreApplication.translate("MainWindow", u"G\u00f6rev Y\u00fck\u00fc Y\u00fckseklik:", None))
        self.RollLabel.setText(QCoreApplication.translate("MainWindow", u"Roll:", None))
        self.S2Label2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.InisHiziLabel.setText(QCoreApplication.translate("MainWindow", u"\u0130ni\u015f H\u0131z\u0131:", None))
        self.TakimNoLabel.setText(QCoreApplication.translate("MainWindow", u"Tak\u0131m No:", None))
        self.GpsLonLabel.setText(QCoreApplication.translate("MainWindow", u"GPS1 LONGITUDE:", None))
        self.GpsAltLabel2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.RollLabel2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.TasiyiciYukseklikLabel2.setText(QCoreApplication.translate("MainWindow", u"250 m", None))
        self.PitchLabel2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.YawLabel2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.S2Label.setText(QCoreApplication.translate("MainWindow", u"S2 Data:", None))
        self.GpsLatLabel2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.GpsAltLabel.setText(QCoreApplication.translate("MainWindow", u"GPS1 ALTITUDE:", None))
        self.GpsLatLabel.setText(QCoreApplication.translate("MainWindow", u"GPS1 LATITUDE:", None))
        self.S1Label2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.Basinc2Label.setText(QCoreApplication.translate("MainWindow", u"Bas\u0131n\u00e7 2:", None))
        self.YawLabel.setText(QCoreApplication.translate("MainWindow", u"Yaw:", None))
        self.GpsLonLabel2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.InisHiziLabel2.setText(QCoreApplication.translate("MainWindow", u"10 m/s", None))
        self.SicaklikLabel.setText(QCoreApplication.translate("MainWindow", u"S\u0131cakl\u0131k:", None))
        self.TasiyiciYukseklikLabel.setText(QCoreApplication.translate("MainWindow", u"Ta\u015f\u0131y\u0131c\u0131 Y\u00fckseklik:", None))
        self.Basinc2Label2.setText(QCoreApplication.translate("MainWindow", u"0.9 ATM", None))
        self.PaketNumLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Paket Numaras\u0131: </p></body></html>", None))
        self.PaketNumLabel2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>1000</p></body></html>", None))
        self.BasincLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Bas\u0131n\u00e7: </p></body></html>", None))
        self.GorevYukuYukseklikLabel2.setText(QCoreApplication.translate("MainWindow", u"300 m", None))
        self.UyduStatLabel.setText(QCoreApplication.translate("MainWindow", u"Uydu Stat\u00fcs\u00fc: ", None))
        self.S1Label.setText(QCoreApplication.translate("MainWindow", u" S1 Data:", None))
        self.PitchLabel.setText(QCoreApplication.translate("MainWindow", u"Pitch:", None))
        self.PilGerilimiLabel2.setText(QCoreApplication.translate("MainWindow", u"7 V", None))
        self.PilGerilimiLabel.setText(QCoreApplication.translate("MainWindow", u"Pil Gerilimi:", None))
        self.SicaklikLabel2.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.BasincLabel2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>0.9 ATM</p></body></html>", None))
        self.UyduStatLabel2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.sistemBaslatButton.setText(QCoreApplication.translate("MainWindow", u"Sistemi Ba\u015flat", None))
        self.telemetriAlButton.setText(QCoreApplication.translate("MainWindow", u"Telemetri Al", None))
        self.ayrilmaGerceklestirButton.setText(QCoreApplication.translate("MainWindow", u"Ayr\u0131lmay\u0131 Ger\u00e7ekle\u015ftir", None))
        self.videoSecButton.setText(QCoreApplication.translate("MainWindow", u"Video Se\u00e7", None))
        self.videoGonderButton.setText(QCoreApplication.translate("MainWindow", u"Video G\u00f6nder", None))
        self.sistemDurdurButton.setText(QCoreApplication.translate("MainWindow", u"Sistemi Durdur", None))
        self.rhrh_button.setText(QCoreApplication.translate("MainWindow", u"RHRH KODU GONDER", None))
        self.camera_label.setText("")
    # retranslateUi

