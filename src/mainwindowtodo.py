# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowtodo.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(698, 502)
        self.actionSobre = QAction(MainWindow)
        self.actionSobre.setObjectName(u"actionSobre")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 671, 451))
        self.verticalLayoutMain = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayoutMain.setObjectName(u"verticalLayoutMain")
        self.verticalLayoutMain.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QHBoxLayout()
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setContentsMargins(10, 10, 10, 10)
        self.nomeListaTarefas = QLabel(self.verticalLayoutWidget)
        self.nomeListaTarefas.setObjectName(u"nomeListaTarefas")

        self.topMenu.addWidget(self.nomeListaTarefas)

        self.botDesfazer = QPushButton(self.verticalLayoutWidget)
        self.botDesfazer.setObjectName(u"botDesfazer")
        self.botDesfazer.setMaximumSize(QSize(125, 16777215))

        self.topMenu.addWidget(self.botDesfazer)

        self.botApagarTudo = QPushButton(self.verticalLayoutWidget)
        self.botApagarTudo.setObjectName(u"botApagarTudo")
        self.botApagarTudo.setMaximumSize(QSize(125, 16777215))

        self.topMenu.addWidget(self.botApagarTudo)

        self.botRecuperarTudo = QPushButton(self.verticalLayoutWidget)
        self.botRecuperarTudo.setObjectName(u"botRecuperarTudo")
        self.botRecuperarTudo.setMaximumSize(QSize(125, 16777215))

        self.topMenu.addWidget(self.botRecuperarTudo)


        self.verticalLayoutMain.addLayout(self.topMenu)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMouseTracking(False)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreWidContents = QWidget()
        self.scrollAreWidContents.setObjectName(u"scrollAreWidContents")
        self.scrollAreWidContents.setGeometry(QRect(0, 0, 665, 343))
        self.scrollArea.setWidget(self.scrollAreWidContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayoutMain.addLayout(self.verticalLayout_2)

        self.bottonMenu = QHBoxLayout()
        self.bottonMenu.setObjectName(u"bottonMenu")
        self.bottonMenu.setContentsMargins(10, 10, 10, 10)
        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.bottonMenu.addWidget(self.lineEdit)

        self.botAdd = QPushButton(self.verticalLayoutWidget)
        self.botAdd.setObjectName(u"botAdd")

        self.bottonMenu.addWidget(self.botAdd)


        self.verticalLayoutMain.addLayout(self.bottonMenu)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 698, 22))
        self.menuArquivo = QMenu(self.menubar)
        self.menuArquivo.setObjectName(u"menuArquivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menuArquivo.addAction(self.actionSobre)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.nomeListaTarefas.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.botDesfazer.setText(QCoreApplication.translate("MainWindow", u"Desfazer", None))
#if QT_CONFIG(statustip)
        self.botApagarTudo.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.botApagarTudo.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.botApagarTudo.setText(QCoreApplication.translate("MainWindow", u"Apagar Tudo", None))
        self.botRecuperarTudo.setText(QCoreApplication.translate("MainWindow", u"Recuperar Tudo", None))
#if QT_CONFIG(statustip)
        self.scrollArea.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.scrollArea.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.scrollArea.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.botAdd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.menuArquivo.setTitle(QCoreApplication.translate("MainWindow", u"Arquivo", None))
    # retranslateUi

