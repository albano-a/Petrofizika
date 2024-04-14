# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1116, 877)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabPorosity = QWidget()
        self.tabPorosity.setObjectName(u"tabPorosity")
        self.verticalLayout_2 = QVBoxLayout(self.tabPorosity)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.porosityTabWidget = QTabWidget(self.tabPorosity)
        self.porosityTabWidget.setObjectName(u"porosityTabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.porosityTabWidget.sizePolicy().hasHeightForWidth())
        self.porosityTabWidget.setSizePolicy(sizePolicy)
        self.sonicPorosity = QWidget()
        self.sonicPorosity.setObjectName(u"sonicPorosity")
        self.horizontalLayout_2 = QHBoxLayout(self.sonicPorosity)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.sonicPorosity)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 2)

        self.groupBox = QGroupBox(self.sonicPorosity)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(10)
        self.label.setFont(font1)

        self.verticalLayout_4.addWidget(self.label)

        self.inputDeltaTlog_wyllie = QLineEdit(self.groupBox)
        self.inputDeltaTlog_wyllie.setObjectName(u"inputDeltaTlog_wyllie")
        self.inputDeltaTlog_wyllie.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.inputDeltaTlog_wyllie)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.inputDeltaTma_wyllie = QLineEdit(self.groupBox)
        self.inputDeltaTma_wyllie.setObjectName(u"inputDeltaTma_wyllie")

        self.verticalLayout_4.addWidget(self.inputDeltaTma_wyllie)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_3)

        self.inputDeltaTfl_wyllie = QLineEdit(self.groupBox)
        self.inputDeltaTfl_wyllie.setObjectName(u"inputDeltaTfl_wyllie")

        self.verticalLayout_4.addWidget(self.inputDeltaTfl_wyllie)

        self.calculateWylliePorosity = QPushButton(self.groupBox)
        self.calculateWylliePorosity.setObjectName(u"calculateWylliePorosity")

        self.verticalLayout_4.addWidget(self.calculateWylliePorosity)

        self.resultWylliePerc = QTextEdit(self.groupBox)
        self.resultWylliePerc.setObjectName(u"resultWylliePerc")
        self.resultWylliePerc.setMaximumSize(QSize(16777215, 30))
        self.resultWylliePerc.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.resultWylliePerc)

        self.resultWyllieDec = QTextEdit(self.groupBox)
        self.resultWyllieDec.setObjectName(u"resultWyllieDec")
        self.resultWyllieDec.setMaximumSize(QSize(16777215, 30))
        self.resultWyllieDec.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.resultWyllieDec)

        self.addTableWyllie = QPushButton(self.groupBox)
        self.addTableWyllie.setObjectName(u"addTableWyllie")

        self.verticalLayout_4.addWidget(self.addTableWyllie)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.sonicPorosity)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_5)

        self.inputDeltaTlog_raymer = QLineEdit(self.groupBox_2)
        self.inputDeltaTlog_raymer.setObjectName(u"inputDeltaTlog_raymer")

        self.verticalLayout_5.addWidget(self.inputDeltaTlog_raymer)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.inputDeltaTma_raymer = QLineEdit(self.groupBox_2)
        self.inputDeltaTma_raymer.setObjectName(u"inputDeltaTma_raymer")

        self.verticalLayout_5.addWidget(self.inputDeltaTma_raymer)

        self.calculateRaymerPorosity = QPushButton(self.groupBox_2)
        self.calculateRaymerPorosity.setObjectName(u"calculateRaymerPorosity")

        self.verticalLayout_5.addWidget(self.calculateRaymerPorosity)

        self.resultRaymerPerc = QTextEdit(self.groupBox_2)
        self.resultRaymerPerc.setObjectName(u"resultRaymerPerc")
        self.resultRaymerPerc.setMaximumSize(QSize(16777215, 30))
        self.resultRaymerPerc.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.resultRaymerPerc)

        self.resultRaymerDec = QTextEdit(self.groupBox_2)
        self.resultRaymerDec.setObjectName(u"resultRaymerDec")
        self.resultRaymerDec.setMaximumSize(QSize(16777215, 30))
        self.resultRaymerDec.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.resultRaymerDec)

        self.addTableRaymer = QPushButton(self.groupBox_2)
        self.addTableRaymer.setObjectName(u"addTableRaymer")

        self.verticalLayout_5.addWidget(self.addTableRaymer)


        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_2)

        self.porosityTabWidget.addTab(self.sonicPorosity, "")
        self.densityPorosity = QWidget()
        self.densityPorosity.setObjectName(u"densityPorosity")
        self.porosityTabWidget.addTab(self.densityPorosity, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout = QGridLayout(self.tab_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.porosityTabWidget.addTab(self.tab_3, "")

        self.verticalLayout_2.addWidget(self.porosityTabWidget)

        self.scrollArea = QScrollArea(self.tabPorosity)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1072, 362))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.outputTableSonicPorosity = QTableWidget(self.scrollAreaWidgetContents)
        self.outputTableSonicPorosity.setObjectName(u"outputTableSonicPorosity")

        self.verticalLayout_3.addWidget(self.outputTableSonicPorosity)

        self.exportSonicPorosityTable = QPushButton(self.scrollAreaWidgetContents)
        self.exportSonicPorosityTable.setObjectName(u"exportSonicPorosityTable")

        self.verticalLayout_3.addWidget(self.exportSonicPorosityTable)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tabPorosity, "")
        self.tabPermeability = QWidget()
        self.tabPermeability.setObjectName(u"tabPermeability")
        self.verticalLayout = QVBoxLayout(self.tabPermeability)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget.addTab(self.tabPermeability, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1116, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.porosityTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Wyllie et al., 1958", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u0394tlog</span></p></body></html>", None))
        self.inputDeltaTlog_wyllie.setText("")
        self.inputDeltaTlog_wyllie.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u00b5s/ft", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u0394tma</span></p></body></html>", None))
        self.inputDeltaTma_wyllie.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u00b5s/ft", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u0394tfl</span></p></body></html>", None))
        self.inputDeltaTfl_wyllie.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u00b5s/ft", None))
        self.calculateWylliePorosity.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.resultWylliePerc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result (%)", None))
        self.resultWyllieDec.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result (dec)", None))
        self.addTableWyllie.setText(QCoreApplication.translate("MainWindow", u"Adicionar a tabela", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Raymer et al., 1980", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u0394tlog</span></p></body></html>", None))
        self.inputDeltaTlog_raymer.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u00b5s/ft", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u0394tma</span></p></body></html>", None))
        self.inputDeltaTma_raymer.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u00b5s/ft", None))
        self.calculateRaymerPorosity.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.resultRaymerPerc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result (%)", None))
        self.resultRaymerDec.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result (dec)", None))
        self.addTableRaymer.setText(QCoreApplication.translate("MainWindow", u"Adicionar a tabela", None))
        self.porosityTabWidget.setTabText(self.porosityTabWidget.indexOf(self.sonicPorosity), QCoreApplication.translate("MainWindow", u"S\u00f4nico", None))
        self.porosityTabWidget.setTabText(self.porosityTabWidget.indexOf(self.densityPorosity), QCoreApplication.translate("MainWindow", u"Densidade", None))
        self.porosityTabWidget.setTabText(self.porosityTabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Resistividade", None))
        self.exportSonicPorosityTable.setText(QCoreApplication.translate("MainWindow", u"Exportar dados", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPorosity), QCoreApplication.translate("MainWindow", u"Porosidade", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPermeability), QCoreApplication.translate("MainWindow", u"Permeabilidade", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Resistividade", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Satura\u00e7\u00e3o de \u00c1gua", None))
    # retranslateUi

