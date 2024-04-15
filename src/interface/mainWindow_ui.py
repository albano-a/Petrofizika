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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(994, 805)
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
        self.porosityTabWidget.setDocumentMode(True)
        self.sonicPorosity = QWidget()
        self.sonicPorosity.setObjectName(u"sonicPorosity")
        self.horizontalLayout_2 = QHBoxLayout(self.sonicPorosity)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(self.sonicPorosity)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.resultWyllieDec = QTextEdit(self.groupBox)
        self.resultWyllieDec.setObjectName(u"resultWyllieDec")
        self.resultWyllieDec.setMaximumSize(QSize(16777215, 35))
        self.resultWyllieDec.setReadOnly(True)

        self.gridLayout_3.addWidget(self.resultWyllieDec, 5, 1, 1, 1)

        self.resultWylliePerc = QTextEdit(self.groupBox)
        self.resultWylliePerc.setObjectName(u"resultWylliePerc")
        self.resultWylliePerc.setMaximumSize(QSize(16777215, 35))
        self.resultWylliePerc.setReadOnly(True)

        self.gridLayout_3.addWidget(self.resultWylliePerc, 5, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_3.setFont(font1)

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.inputDeltaTlog_wyllie = QLineEdit(self.groupBox)
        self.inputDeltaTlog_wyllie.setObjectName(u"inputDeltaTlog_wyllie")
        self.inputDeltaTlog_wyllie.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.inputDeltaTlog_wyllie, 1, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setFont(font1)

        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)

        self.inputDeltaTma_wyllie = QLineEdit(self.groupBox)
        self.inputDeltaTma_wyllie.setObjectName(u"inputDeltaTma_wyllie")

        self.gridLayout_3.addWidget(self.inputDeltaTma_wyllie, 1, 1, 1, 1)

        self.calculateWylliePorosity = QPushButton(self.groupBox)
        self.calculateWylliePorosity.setObjectName(u"calculateWylliePorosity")

        self.gridLayout_3.addWidget(self.calculateWylliePorosity, 4, 0, 1, 2)

        self.addTableWyllie = QPushButton(self.groupBox)
        self.addTableWyllie.setObjectName(u"addTableWyllie")

        self.gridLayout_3.addWidget(self.addTableWyllie, 6, 0, 1, 2)

        self.inputDeltaTfl_wyllie = QLineEdit(self.groupBox)
        self.inputDeltaTfl_wyllie.setObjectName(u"inputDeltaTfl_wyllie")

        self.gridLayout_3.addWidget(self.inputDeltaTfl_wyllie, 3, 0, 1, 2)


        self.verticalLayout_4.addLayout(self.gridLayout_3)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.frame = QFrame(self.sonicPorosity)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame)

        self.groupBox_2 = QGroupBox(self.sonicPorosity)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.groupBox_2.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.resultRaymerPerc = QTextEdit(self.groupBox_2)
        self.resultRaymerPerc.setObjectName(u"resultRaymerPerc")
        self.resultRaymerPerc.setMaximumSize(QSize(16777215, 35))
        self.resultRaymerPerc.setReadOnly(True)

        self.gridLayout_2.addWidget(self.resultRaymerPerc, 4, 0, 1, 1)

        self.resultRaymerDec = QTextEdit(self.groupBox_2)
        self.resultRaymerDec.setObjectName(u"resultRaymerDec")
        self.resultRaymerDec.setMaximumSize(QSize(16777215, 35))
        self.resultRaymerDec.setReadOnly(True)

        self.gridLayout_2.addWidget(self.resultRaymerDec, 4, 1, 1, 1)

        self.inputDeltaTlog_raymer = QLineEdit(self.groupBox_2)
        self.inputDeltaTlog_raymer.setObjectName(u"inputDeltaTlog_raymer")

        self.gridLayout_2.addWidget(self.inputDeltaTlog_raymer, 1, 0, 1, 1)

        self.calculateRaymerPorosity = QPushButton(self.groupBox_2)
        self.calculateRaymerPorosity.setObjectName(u"calculateRaymerPorosity")

        self.gridLayout_2.addWidget(self.calculateRaymerPorosity, 3, 0, 1, 2)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setMaximumSize(QSize(16777215, 30))
        self.label_6.setFont(font1)

        self.gridLayout_2.addWidget(self.label_6, 0, 1, 1, 1)

        self.inputDeltaTma_raymer = QLineEdit(self.groupBox_2)
        self.inputDeltaTma_raymer.setObjectName(u"inputDeltaTma_raymer")

        self.gridLayout_2.addWidget(self.inputDeltaTma_raymer, 1, 1, 1, 1)

        self.addTableRaymer = QPushButton(self.groupBox_2)
        self.addTableRaymer.setObjectName(u"addTableRaymer")

        self.gridLayout_2.addWidget(self.addTableRaymer, 5, 0, 1, 2)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(0, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 2)


        self.verticalLayout_5.addLayout(self.gridLayout_2)


        self.horizontalLayout_3.addWidget(self.groupBox_2)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)

        self.porosityTabWidget.addTab(self.sonicPorosity, "")
        self.densityPorosity = QWidget()
        self.densityPorosity.setObjectName(u"densityPorosity")
        self.porosityTabWidget.addTab(self.densityPorosity, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout = QGridLayout(self.tab_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.tab_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setFrameShape(QFrame.Box)
        self.stackedWidget.setLineWidth(1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.porosityTabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.porosityTabWidget.addTab(self.tab_4, "")

        self.verticalLayout_2.addWidget(self.porosityTabWidget)

        self.scrollArea = QScrollArea(self.tabPorosity)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 950, 343))
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
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.conversionScrollArea = QScrollArea(self.tab_7)
        self.conversionScrollArea.setObjectName(u"conversionScrollArea")
        self.conversionScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 950, 694))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_16 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_7.addWidget(self.label_16, 0, 0, 1, 6)

        self.fromDistanceInput = QLineEdit(self.scrollAreaWidgetContents_2)
        self.fromDistanceInput.setObjectName(u"fromDistanceInput")

        self.gridLayout_7.addWidget(self.fromDistanceInput, 1, 1, 1, 1)

        self.toDistanceOutput = QLineEdit(self.scrollAreaWidgetContents_2)
        self.toDistanceOutput.setObjectName(u"toDistanceOutput")
        self.toDistanceOutput.setReadOnly(True)

        self.gridLayout_7.addWidget(self.toDistanceOutput, 1, 4, 1, 1)

        self.distanceSelector1 = QComboBox(self.scrollAreaWidgetContents_2)
        self.distanceSelector1.addItem("")
        self.distanceSelector1.addItem("")
        self.distanceSelector1.addItem("")
        self.distanceSelector1.addItem("")
        self.distanceSelector1.setObjectName(u"distanceSelector1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.distanceSelector1.sizePolicy().hasHeightForWidth())
        self.distanceSelector1.setSizePolicy(sizePolicy2)

        self.gridLayout_7.addWidget(self.distanceSelector1, 1, 0, 1, 1)

        self.label_17 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_7.addWidget(self.label_17, 1, 2, 1, 1)

        self.distanceSelector2 = QComboBox(self.scrollAreaWidgetContents_2)
        self.distanceSelector2.addItem("")
        self.distanceSelector2.addItem("")
        self.distanceSelector2.addItem("")
        self.distanceSelector2.addItem("")
        self.distanceSelector2.setObjectName(u"distanceSelector2")
        sizePolicy2.setHeightForWidth(self.distanceSelector2.sizePolicy().hasHeightForWidth())
        self.distanceSelector2.setSizePolicy(sizePolicy2)

        self.gridLayout_7.addWidget(self.distanceSelector2, 1, 3, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_7)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_12 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_6.addWidget(self.label_12, 0, 0, 1, 6)

        self.areaSelector1 = QComboBox(self.scrollAreaWidgetContents_2)
        self.areaSelector1.addItem("")
        self.areaSelector1.addItem("")
        self.areaSelector1.addItem("")
        self.areaSelector1.addItem("")
        self.areaSelector1.setObjectName(u"areaSelector1")
        sizePolicy2.setHeightForWidth(self.areaSelector1.sizePolicy().hasHeightForWidth())
        self.areaSelector1.setSizePolicy(sizePolicy2)

        self.gridLayout_6.addWidget(self.areaSelector1, 1, 0, 1, 1)

        self.label_15 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_6.addWidget(self.label_15, 1, 2, 1, 1)

        self.fromAreaInput = QLineEdit(self.scrollAreaWidgetContents_2)
        self.fromAreaInput.setObjectName(u"fromAreaInput")

        self.gridLayout_6.addWidget(self.fromAreaInput, 1, 1, 1, 1)

        self.toAreaOutput = QLineEdit(self.scrollAreaWidgetContents_2)
        self.toAreaOutput.setObjectName(u"toAreaOutput")
        self.toAreaOutput.setReadOnly(True)

        self.gridLayout_6.addWidget(self.toAreaOutput, 1, 4, 1, 1)

        self.areaSelector2 = QComboBox(self.scrollAreaWidgetContents_2)
        self.areaSelector2.addItem("")
        self.areaSelector2.addItem("")
        self.areaSelector2.addItem("")
        self.areaSelector2.addItem("")
        self.areaSelector2.setObjectName(u"areaSelector2")
        sizePolicy2.setHeightForWidth(self.areaSelector2.sizePolicy().hasHeightForWidth())
        self.areaSelector2.setSizePolicy(sizePolicy2)

        self.gridLayout_6.addWidget(self.areaSelector2, 1, 3, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_6)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.volumeSelector1 = QComboBox(self.scrollAreaWidgetContents_2)
        self.volumeSelector1.addItem("")
        self.volumeSelector1.addItem("")
        self.volumeSelector1.addItem("")
        self.volumeSelector1.addItem("")
        self.volumeSelector1.addItem("")
        self.volumeSelector1.addItem("")
        self.volumeSelector1.setObjectName(u"volumeSelector1")
        sizePolicy2.setHeightForWidth(self.volumeSelector1.sizePolicy().hasHeightForWidth())
        self.volumeSelector1.setSizePolicy(sizePolicy2)

        self.gridLayout_8.addWidget(self.volumeSelector1, 1, 0, 1, 1)

        self.label_18 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_8.addWidget(self.label_18, 0, 0, 1, 6)

        self.label_19 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_8.addWidget(self.label_19, 1, 2, 1, 1)

        self.fromVolumeInput = QLineEdit(self.scrollAreaWidgetContents_2)
        self.fromVolumeInput.setObjectName(u"fromVolumeInput")

        self.gridLayout_8.addWidget(self.fromVolumeInput, 1, 1, 1, 1)

        self.toVolumeOutput = QLineEdit(self.scrollAreaWidgetContents_2)
        self.toVolumeOutput.setObjectName(u"toVolumeOutput")
        self.toVolumeOutput.setMinimumSize(QSize(0, 0))
        self.toVolumeOutput.setReadOnly(True)

        self.gridLayout_8.addWidget(self.toVolumeOutput, 1, 4, 1, 1)

        self.volumeSelector2 = QComboBox(self.scrollAreaWidgetContents_2)
        self.volumeSelector2.addItem("")
        self.volumeSelector2.addItem("")
        self.volumeSelector2.addItem("")
        self.volumeSelector2.addItem("")
        self.volumeSelector2.addItem("")
        self.volumeSelector2.addItem("")
        self.volumeSelector2.setObjectName(u"volumeSelector2")
        sizePolicy2.setHeightForWidth(self.volumeSelector2.sizePolicy().hasHeightForWidth())
        self.volumeSelector2.setSizePolicy(sizePolicy2)

        self.gridLayout_8.addWidget(self.volumeSelector2, 1, 3, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_8)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_20 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_9.addWidget(self.label_20, 1, 2, 1, 1)

        self.toPressureOutput = QLineEdit(self.scrollAreaWidgetContents_2)
        self.toPressureOutput.setObjectName(u"toPressureOutput")
        self.toPressureOutput.setReadOnly(True)

        self.gridLayout_9.addWidget(self.toPressureOutput, 1, 4, 1, 1)

        self.fromPressureInput = QLineEdit(self.scrollAreaWidgetContents_2)
        self.fromPressureInput.setObjectName(u"fromPressureInput")

        self.gridLayout_9.addWidget(self.fromPressureInput, 1, 1, 1, 1)

        self.label_21 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_9.addWidget(self.label_21, 0, 0, 1, 6)

        self.pressureSelector1 = QComboBox(self.scrollAreaWidgetContents_2)
        self.pressureSelector1.addItem("")
        self.pressureSelector1.addItem("")
        self.pressureSelector1.addItem("")
        self.pressureSelector1.addItem("")
        self.pressureSelector1.addItem("")
        self.pressureSelector1.setObjectName(u"pressureSelector1")
        sizePolicy2.setHeightForWidth(self.pressureSelector1.sizePolicy().hasHeightForWidth())
        self.pressureSelector1.setSizePolicy(sizePolicy2)

        self.gridLayout_9.addWidget(self.pressureSelector1, 1, 0, 1, 1)

        self.pressureSelector2 = QComboBox(self.scrollAreaWidgetContents_2)
        self.pressureSelector2.addItem("")
        self.pressureSelector2.addItem("")
        self.pressureSelector2.addItem("")
        self.pressureSelector2.addItem("")
        self.pressureSelector2.addItem("")
        self.pressureSelector2.setObjectName(u"pressureSelector2")
        sizePolicy2.setHeightForWidth(self.pressureSelector2.sizePolicy().hasHeightForWidth())
        self.pressureSelector2.setSizePolicy(sizePolicy2)

        self.gridLayout_9.addWidget(self.pressureSelector2, 1, 3, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_9)

        self.conversionScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_5.addWidget(self.conversionScrollArea)

        self.tabWidget.addTab(self.tab_7, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 994, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(6)
        self.porosityTabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Wyllie et al., 1958", None))
        self.resultWyllieDec.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result (dec)", None))
        self.resultWylliePerc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result (%)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u0394tfl</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u0394tlog</span></p></body></html>", None))
        self.inputDeltaTlog_wyllie.setText("")
        self.inputDeltaTlog_wyllie.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u00b5s/ft", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u0394tma</span></p></body></html>", None))
        self.inputDeltaTma_wyllie.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u00b5s/ft", None))
        self.calculateWylliePorosity.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.addTableWyllie.setText(QCoreApplication.translate("MainWindow", u"Adicionar a tabela", None))
        self.inputDeltaTfl_wyllie.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u00b5s/ft", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Raymer et al., 1980", None))
        self.resultRaymerPerc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result (%)", None))
        self.resultRaymerDec.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result (dec)", None))
        self.inputDeltaTlog_raymer.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u00b5s/ft", None))
        self.calculateRaymerPorosity.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u0394tma</span></p></body></html>", None))
        self.inputDeltaTma_raymer.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u00b5s/ft", None))
        self.addTableRaymer.setText(QCoreApplication.translate("MainWindow", u"Adicionar a tabela", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u0394tlog</span></p></body></html>", None))
        self.porosityTabWidget.setTabText(self.porosityTabWidget.indexOf(self.sonicPorosity), QCoreApplication.translate("MainWindow", u"S\u00f4nico", None))
        self.porosityTabWidget.setTabText(self.porosityTabWidget.indexOf(self.densityPorosity), QCoreApplication.translate("MainWindow", u"Densidade", None))
        self.porosityTabWidget.setTabText(self.porosityTabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Resistividade", None))
        self.porosityTabWidget.setTabText(self.porosityTabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Corre\u00e7\u00e3o para Folhelho", None))
        self.exportSonicPorosityTable.setText(QCoreApplication.translate("MainWindow", u"Exportar dados", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPorosity), QCoreApplication.translate("MainWindow", u"Porosidade", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPermeability), QCoreApplication.translate("MainWindow", u"Permeabilidade", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Resistividade", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Satura\u00e7\u00e3o de \u00c1gua", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Volume de Shale", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Reservas", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Dist\u00e2ncia</span></p></body></html>", None))
        self.distanceSelector1.setItemText(0, QCoreApplication.translate("MainWindow", u"P\u00e9s", None))
        self.distanceSelector1.setItemText(1, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.distanceSelector1.setItemText(2, QCoreApplication.translate("MainWindow", u"Milhas", None))
        self.distanceSelector1.setItemText(3, QCoreApplication.translate("MainWindow", u"Quil\u00f4metros", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">PARA</span></p></body></html>", None))
        self.distanceSelector2.setItemText(0, QCoreApplication.translate("MainWindow", u"P\u00e9s", None))
        self.distanceSelector2.setItemText(1, QCoreApplication.translate("MainWindow", u"Metros", None))
        self.distanceSelector2.setItemText(2, QCoreApplication.translate("MainWindow", u"Milhas", None))
        self.distanceSelector2.setItemText(3, QCoreApplication.translate("MainWindow", u"Quil\u00f4metros", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">\u00c1rea</span></p></body></html>", None))
        self.areaSelector1.setItemText(0, QCoreApplication.translate("MainWindow", u"Acres", None))
        self.areaSelector1.setItemText(1, QCoreApplication.translate("MainWindow", u"P\u00e9s quadrados", None))
        self.areaSelector1.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros quadrados", None))
        self.areaSelector1.setItemText(3, QCoreApplication.translate("MainWindow", u"Quil\u00f4metros quadrados", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">PARA</span></p></body></html>", None))
        self.areaSelector2.setItemText(0, QCoreApplication.translate("MainWindow", u"Acres", None))
        self.areaSelector2.setItemText(1, QCoreApplication.translate("MainWindow", u"P\u00e9s quadrados", None))
        self.areaSelector2.setItemText(2, QCoreApplication.translate("MainWindow", u"Metros quadrados", None))
        self.areaSelector2.setItemText(3, QCoreApplication.translate("MainWindow", u"Quil\u00f4metros quadrados", None))

        self.volumeSelector1.setItemText(0, QCoreApplication.translate("MainWindow", u"P\u00e9s c\u00fabicos por Acre", None))
        self.volumeSelector1.setItemText(1, QCoreApplication.translate("MainWindow", u"Barris", None))
        self.volumeSelector1.setItemText(2, QCoreApplication.translate("MainWindow", u"P\u00e9s c\u00fabicos", None))
        self.volumeSelector1.setItemText(3, QCoreApplication.translate("MainWindow", u"Metros c\u00fabicos", None))
        self.volumeSelector1.setItemText(4, QCoreApplication.translate("MainWindow", u"Gal\u00f5es", None))
        self.volumeSelector1.setItemText(5, QCoreApplication.translate("MainWindow", u"Toneladas m\u00e9tricas", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Volume</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">PARA</span></p></body></html>", None))
        self.volumeSelector2.setItemText(0, QCoreApplication.translate("MainWindow", u"P\u00e9s c\u00fabicos por Acre", None))
        self.volumeSelector2.setItemText(1, QCoreApplication.translate("MainWindow", u"Barris", None))
        self.volumeSelector2.setItemText(2, QCoreApplication.translate("MainWindow", u"P\u00e9s c\u00fabicos", None))
        self.volumeSelector2.setItemText(3, QCoreApplication.translate("MainWindow", u"Metros c\u00fabicos", None))
        self.volumeSelector2.setItemText(4, QCoreApplication.translate("MainWindow", u"Gal\u00f5es", None))
        self.volumeSelector2.setItemText(5, QCoreApplication.translate("MainWindow", u"Toneladas m\u00e9tricas", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">PARA</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Press\u00e3o</span></p></body></html>", None))
        self.pressureSelector1.setItemText(0, QCoreApplication.translate("MainWindow", u"PSIA", None))
        self.pressureSelector1.setItemText(1, QCoreApplication.translate("MainWindow", u"kPa - Kilopascal", None))
        self.pressureSelector1.setItemText(2, QCoreApplication.translate("MainWindow", u"Bar", None))
        self.pressureSelector1.setItemText(3, QCoreApplication.translate("MainWindow", u"BTU - Unidade T\u00e9rmica Brit\u00e2nica", None))
        self.pressureSelector1.setItemText(4, QCoreApplication.translate("MainWindow", u"Joules", None))

        self.pressureSelector2.setItemText(0, QCoreApplication.translate("MainWindow", u"PSIA", None))
        self.pressureSelector2.setItemText(1, QCoreApplication.translate("MainWindow", u"kPa - Kilopascal", None))
        self.pressureSelector2.setItemText(2, QCoreApplication.translate("MainWindow", u"Bar", None))
        self.pressureSelector2.setItemText(3, QCoreApplication.translate("MainWindow", u"BTU - Unidade T\u00e9rmica Brit\u00e2nica", None))
        self.pressureSelector2.setItemText(4, QCoreApplication.translate("MainWindow", u"Joules", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Convers\u00f5es", None))
    # retranslateUi

