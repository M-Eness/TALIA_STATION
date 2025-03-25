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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(927, 800)
        MainWindow.setMaximumSize(QSize(1500, 800))
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
        self.horizontalLayout_2 = QHBoxLayout(self.frm_top)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.SicaklikLabel = QLabel(self.frm_top)
        self.SicaklikLabel.setObjectName(u"SicaklikLabel")
        self.SicaklikLabel.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout.addWidget(self.SicaklikLabel)

        self.BasincLabel_2 = QLabel(self.frm_top)
        self.BasincLabel_2.setObjectName(u"BasincLabel_2")
        self.BasincLabel_2.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout.addWidget(self.BasincLabel_2)

        self.BasincLabel = QLabel(self.frm_top)
        self.BasincLabel.setObjectName(u"BasincLabel")
        self.BasincLabel.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout.addWidget(self.BasincLabel)

        self.BasincLabel_3 = QLabel(self.frm_top)
        self.BasincLabel_3.setObjectName(u"BasincLabel_3")
        self.BasincLabel_3.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout.addWidget(self.BasincLabel_3)

        self.GorevYukuYukseklikLabel = QLabel(self.frm_top)
        self.GorevYukuYukseklikLabel.setObjectName(u"GorevYukuYukseklikLabel")
        self.GorevYukuYukseklikLabel.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.GorevYukuYukseklikLabel)

        self.GorevYukuYukseklikLabel_2 = QLabel(self.frm_top)
        self.GorevYukuYukseklikLabel_2.setObjectName(u"GorevYukuYukseklikLabel_2")
        self.GorevYukuYukseklikLabel_2.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.GorevYukuYukseklikLabel_2)

        self.TasiyiciYukseklikLabel = QLabel(self.frm_top)
        self.TasiyiciYukseklikLabel.setObjectName(u"TasiyiciYukseklikLabel")
        self.TasiyiciYukseklikLabel.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.TasiyiciYukseklikLabel)

        self.TasiyiciYukseklikLabel_2 = QLabel(self.frm_top)
        self.TasiyiciYukseklikLabel_2.setObjectName(u"TasiyiciYukseklikLabel_2")
        self.TasiyiciYukseklikLabel_2.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.TasiyiciYukseklikLabel_2)

        self.IrtifaFarkiLabel = QLabel(self.frm_top)
        self.IrtifaFarkiLabel.setObjectName(u"IrtifaFarkiLabel")
        self.IrtifaFarkiLabel.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout.addWidget(self.IrtifaFarkiLabel)

        self.IrtifaFarkiLabel_2 = QLabel(self.frm_top)
        self.IrtifaFarkiLabel_2.setObjectName(u"IrtifaFarkiLabel_2")
        self.IrtifaFarkiLabel_2.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout.addWidget(self.IrtifaFarkiLabel_2)

        self.GorevYukuHizLabel = QLabel(self.frm_top)
        self.GorevYukuHizLabel.setObjectName(u"GorevYukuHizLabel")
        self.GorevYukuHizLabel.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout.addWidget(self.GorevYukuHizLabel)

        self.GorevYukuHizLabel_2 = QLabel(self.frm_top)
        self.GorevYukuHizLabel_2.setObjectName(u"GorevYukuHizLabel_2")
        self.GorevYukuHizLabel_2.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout.addWidget(self.GorevYukuHizLabel_2)

        self.TasiyiciHiziLabel = QLabel(self.frm_top)
        self.TasiyiciHiziLabel.setObjectName(u"TasiyiciHiziLabel")
        self.TasiyiciHiziLabel.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout.addWidget(self.TasiyiciHiziLabel)

        self.TasiyiciHiziLabel_2 = QLabel(self.frm_top)
        self.TasiyiciHiziLabel_2.setObjectName(u"TasiyiciHiziLabel_2")
        self.TasiyiciHiziLabel_2.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout.addWidget(self.TasiyiciHiziLabel_2)

        self.PilGerilimiLabel = QLabel(self.frm_top)
        self.PilGerilimiLabel.setObjectName(u"PilGerilimiLabel")
        self.PilGerilimiLabel.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout.addWidget(self.PilGerilimiLabel)

        self.PilGerilimiLabel_2 = QLabel(self.frm_top)
        self.PilGerilimiLabel_2.setObjectName(u"PilGerilimiLabel_2")
        self.PilGerilimiLabel_2.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout.addWidget(self.PilGerilimiLabel_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


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
        self.frm_middle_left.setMinimumSize(QSize(250, 0))
        self.frm_middle_left.setMaximumSize(QSize(250, 16777215))
        self.frm_middle_left.setStyleSheet(u"background-color: rgb(118, 152, 194);\n"
"/*rgb(155, 195, 244)")
        self.frm_middle_left.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_middle_left.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton = QPushButton(self.frm_middle_left)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(70, 440, 100, 32))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(156, 164, 172, 255), /* A\u00e7\u0131k gri-mavi */\n"
"        stop:0.5 rgba(120, 130, 140, 255), /* Orta ton */\n"
"        stop:1 rgba(90, 100, 110, 255) /* Daha koyu g\u00f6lge */\n"
"    );\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"/* Butona bas\u0131ld\u0131\u011f\u0131nda (t\u0131klama efekti) */\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 rgba(120, 130, 140, 255),\n"
"        stop:1 rgba(90, 100, 110, 255)\n"
"    );\n"
"}\n"
"\n"
"\n"
"/*background-color:rgb(156, 164, 172);\n"
" border-radius: 10px;*/")

        self.horizontalLayout_3.addWidget(self.frm_middle_left)

        self.frm_middle_middle = QFrame(self.frm_middle)
        self.frm_middle_middle.setObjectName(u"frm_middle_middle")
        self.frm_middle_middle.setStyleSheet(u"background-color: rgb(5, 69, 105);\n"
"")
        self.frm_middle_middle.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_middle_middle.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_3.addWidget(self.frm_middle_middle)

        self.frm_middle_right = QFrame(self.frm_middle)
        self.frm_middle_right.setObjectName(u"frm_middle_right")
        self.frm_middle_right.setMinimumSize(QSize(250, 0))
        self.frm_middle_right.setMaximumSize(QSize(250, 500))
        self.frm_middle_right.setStyleSheet(u"background-color: rgb(118, 152, 194);")
        self.frm_middle_right.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_middle_right.setFrameShadow(QFrame.Shadow.Raised)

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
        self.BasincLabel_2.setText(QCoreApplication.translate("MainWindow", u"20 C", None))
        self.BasincLabel.setText(QCoreApplication.translate("MainWindow", u"Basinc:", None))
        self.BasincLabel_3.setText(QCoreApplication.translate("MainWindow", u"0.9 ATM", None))
        self.GorevYukuYukseklikLabel.setText(QCoreApplication.translate("MainWindow", u"G\u00f6rev Y\u00fck\u00fc Y\u00fckseklik:", None))
        self.GorevYukuYukseklikLabel_2.setText(QCoreApplication.translate("MainWindow", u"300 m", None))
        self.TasiyiciYukseklikLabel.setText(QCoreApplication.translate("MainWindow", u"Ta\u015f\u0131y\u0131c\u0131 Y\u00fckseklik:", None))
        self.TasiyiciYukseklikLabel_2.setText(QCoreApplication.translate("MainWindow", u"250 m", None))
        self.IrtifaFarkiLabel.setText(QCoreApplication.translate("MainWindow", u"\u0130rtifa Fark\u0131:", None))
        self.IrtifaFarkiLabel_2.setText(QCoreApplication.translate("MainWindow", u"50 m", None))
        self.GorevYukuHizLabel.setText(QCoreApplication.translate("MainWindow", u"G\u00f6rev Y\u00fck\u00fc H\u0131z\u0131:", None))
        self.GorevYukuHizLabel_2.setText(QCoreApplication.translate("MainWindow", u"10 m/s", None))
        self.TasiyiciHiziLabel.setText(QCoreApplication.translate("MainWindow", u"Ta\u015f\u0131y\u0131c\u0131 H\u0131z\u0131:", None))
        self.TasiyiciHiziLabel_2.setText(QCoreApplication.translate("MainWindow", u"12 m/s", None))
        self.PilGerilimiLabel.setText(QCoreApplication.translate("MainWindow", u"Pil Gerilimi:", None))
        self.PilGerilimiLabel_2.setText(QCoreApplication.translate("MainWindow", u"7 V", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

