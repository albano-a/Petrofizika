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
        MainWindow.resize(959, 784)
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
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setTabBarAutoHide(True)
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
        self.porosityTabWidget.setTabPosition(QTabWidget.North)
        self.porosityTabWidget.setTabShape(QTabWidget.Triangular)
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
        self.gridLayout_5 = QGridLayout(self.densityPorosity)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_3 = QGroupBox(self.densityPorosity)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.matrixDensityInput = QLineEdit(self.groupBox_3)
        self.matrixDensityInput.setObjectName(u"matrixDensityInput")
        self.matrixDensityInput.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.matrixDensityInput, 1, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        font2 = QFont()
        font2.setBold(False)
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_7, 0, 1, 1, 1)

        self.bulkFormationDensityInput = QLineEdit(self.groupBox_3)
        self.bulkFormationDensityInput.setObjectName(u"bulkFormationDensityInput")
        self.bulkFormationDensityInput.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.bulkFormationDensityInput, 1, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_8, 2, 0, 1, 2)

        self.fluidDensityInput = QLineEdit(self.groupBox_3)
        self.fluidDensityInput.setObjectName(u"fluidDensityInput")
        self.fluidDensityInput.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.fluidDensityInput, 3, 0, 1, 2)

        self.calculateDensityLogPorosity = QPushButton(self.groupBox_3)
        self.calculateDensityLogPorosity.setObjectName(u"calculateDensityLogPorosity")

        self.gridLayout_10.addWidget(self.calculateDensityLogPorosity, 4, 0, 1, 2)

        self.resultDensityPorosityPerc = QLineEdit(self.groupBox_3)
        self.resultDensityPorosityPerc.setObjectName(u"resultDensityPorosityPerc")
        self.resultDensityPorosityPerc.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.resultDensityPorosityPerc, 6, 1, 1, 1)

        self.resultDensityPorosityDec = QLineEdit(self.groupBox_3)
        self.resultDensityPorosityDec.setObjectName(u"resultDensityPorosityDec")
        self.resultDensityPorosityDec.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.resultDensityPorosityDec, 6, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_3, 5, 0, 1, 2)


        self.verticalLayout_6.addLayout(self.gridLayout_10)


        self.gridLayout_5.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.densityPorosity)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.chooseNeutronDensityModel = QComboBox(self.groupBox_4)
        self.chooseNeutronDensityModel.addItem("")
        self.chooseNeutronDensityModel.addItem("")
        self.chooseNeutronDensityModel.setObjectName(u"chooseNeutronDensityModel")

        self.gridLayout_11.addWidget(self.chooseNeutronDensityModel, 0, 0, 1, 2)

        self.resultNeutronDensityPorositPerc = QLineEdit(self.groupBox_4)
        self.resultNeutronDensityPorositPerc.setObjectName(u"resultNeutronDensityPorositPerc")
        self.resultNeutronDensityPorositPerc.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.resultNeutronDensityPorositPerc, 6, 1, 1, 1)

        self.resultNeutronDensityPorosityDec = QLineEdit(self.groupBox_4)
        self.resultNeutronDensityPorosityDec.setObjectName(u"resultNeutronDensityPorosityDec")
        self.resultNeutronDensityPorosityDec.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.resultNeutronDensityPorosityDec, 6, 0, 1, 1)

        self.calculateNeutronDensityGas = QPushButton(self.groupBox_4)
        self.calculateNeutronDensityGas.setObjectName(u"calculateNeutronDensityGas")

        self.gridLayout_11.addWidget(self.calculateNeutronDensityGas, 4, 0, 1, 2)

        self.spacer = QSpacerItem(20, 70, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.spacer, 5, 0, 1, 2)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setOpenExternalLinks(False)

        self.gridLayout_11.addWidget(self.label_10, 2, 1, 1, 1)

        self.neutronLogPorosityInput = QLineEdit(self.groupBox_4)
        self.neutronLogPorosityInput.setObjectName(u"neutronLogPorosityInput")
        self.neutronLogPorosityInput.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.neutronLogPorosityInput, 3, 0, 1, 1)

        self.densityLogPorosityInput = QLineEdit(self.groupBox_4)
        self.densityLogPorosityInput.setObjectName(u"densityLogPorosityInput")
        self.densityLogPorosityInput.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.densityLogPorosityInput, 3, 1, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_11)


        self.gridLayout_5.addWidget(self.groupBox_4, 0, 1, 1, 1)

        self.addTableDensityPorosity = QPushButton(self.densityPorosity)
        self.addTableDensityPorosity.setObjectName(u"addTableDensityPorosity")

        self.gridLayout_5.addWidget(self.addTableDensityPorosity, 1, 0, 1, 2)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 915, 300))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.outputTableSonicPorosity = QTableWidget(self.scrollAreaWidgetContents)
        self.outputTableSonicPorosity.setObjectName(u"outputTableSonicPorosity")

        self.verticalLayout_3.addWidget(self.outputTableSonicPorosity)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.exportPorosityTable = QPushButton(self.tabPorosity)
        self.exportPorosityTable.setObjectName(u"exportPorosityTable")

        self.verticalLayout_2.addWidget(self.exportPorosityTable)

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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 915, 679))
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

        self.fromDistanceUnitInput = QComboBox(self.scrollAreaWidgetContents_2)
        self.fromDistanceUnitInput.addItem("")
        self.fromDistanceUnitInput.addItem("")
        self.fromDistanceUnitInput.addItem("")
        self.fromDistanceUnitInput.addItem("")
        self.fromDistanceUnitInput.setObjectName(u"fromDistanceUnitInput")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.fromDistanceUnitInput.sizePolicy().hasHeightForWidth())
        self.fromDistanceUnitInput.setSizePolicy(sizePolicy2)

        self.gridLayout_7.addWidget(self.fromDistanceUnitInput, 1, 0, 1, 1)

        self.label_17 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_7.addWidget(self.label_17, 1, 2, 1, 1)

        self.toDistanceUnitOutput = QComboBox(self.scrollAreaWidgetContents_2)
        self.toDistanceUnitOutput.addItem("")
        self.toDistanceUnitOutput.addItem("")
        self.toDistanceUnitOutput.addItem("")
        self.toDistanceUnitOutput.addItem("")
        self.toDistanceUnitOutput.setObjectName(u"toDistanceUnitOutput")
        sizePolicy2.setHeightForWidth(self.toDistanceUnitOutput.sizePolicy().hasHeightForWidth())
        self.toDistanceUnitOutput.setSizePolicy(sizePolicy2)

        self.gridLayout_7.addWidget(self.toDistanceUnitOutput, 1, 3, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_7)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_12 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_6.addWidget(self.label_12, 0, 0, 1, 6)

        self.fromAreaUnitInput = QComboBox(self.scrollAreaWidgetContents_2)
        self.fromAreaUnitInput.addItem("")
        self.fromAreaUnitInput.addItem("")
        self.fromAreaUnitInput.addItem("")
        self.fromAreaUnitInput.addItem("")
        self.fromAreaUnitInput.setObjectName(u"fromAreaUnitInput")
        sizePolicy2.setHeightForWidth(self.fromAreaUnitInput.sizePolicy().hasHeightForWidth())
        self.fromAreaUnitInput.setSizePolicy(sizePolicy2)

        self.gridLayout_6.addWidget(self.fromAreaUnitInput, 1, 0, 1, 1)

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

        self.toAreaUnitOutput = QComboBox(self.scrollAreaWidgetContents_2)
        self.toAreaUnitOutput.addItem("")
        self.toAreaUnitOutput.addItem("")
        self.toAreaUnitOutput.addItem("")
        self.toAreaUnitOutput.addItem("")
        self.toAreaUnitOutput.setObjectName(u"toAreaUnitOutput")
        sizePolicy2.setHeightForWidth(self.toAreaUnitOutput.sizePolicy().hasHeightForWidth())
        self.toAreaUnitOutput.setSizePolicy(sizePolicy2)

        self.gridLayout_6.addWidget(self.toAreaUnitOutput, 1, 3, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_6)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.fromVolumeUnitInput = QComboBox(self.scrollAreaWidgetContents_2)
        self.fromVolumeUnitInput.addItem("")
        self.fromVolumeUnitInput.addItem("")
        self.fromVolumeUnitInput.addItem("")
        self.fromVolumeUnitInput.addItem("")
        self.fromVolumeUnitInput.addItem("")
        self.fromVolumeUnitInput.addItem("")
        self.fromVolumeUnitInput.setObjectName(u"fromVolumeUnitInput")
        sizePolicy2.setHeightForWidth(self.fromVolumeUnitInput.sizePolicy().hasHeightForWidth())
        self.fromVolumeUnitInput.setSizePolicy(sizePolicy2)

        self.gridLayout_8.addWidget(self.fromVolumeUnitInput, 1, 0, 1, 1)

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

        self.toVolumeUnitOuput = QComboBox(self.scrollAreaWidgetContents_2)
        self.toVolumeUnitOuput.addItem("")
        self.toVolumeUnitOuput.addItem("")
        self.toVolumeUnitOuput.addItem("")
        self.toVolumeUnitOuput.addItem("")
        self.toVolumeUnitOuput.addItem("")
        self.toVolumeUnitOuput.addItem("")
        self.toVolumeUnitOuput.setObjectName(u"toVolumeUnitOuput")
        sizePolicy2.setHeightForWidth(self.toVolumeUnitOuput.sizePolicy().hasHeightForWidth())
        self.toVolumeUnitOuput.setSizePolicy(sizePolicy2)

        self.gridLayout_8.addWidget(self.toVolumeUnitOuput, 1, 3, 1, 1)


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

        self.fromPressureUnitInput = QComboBox(self.scrollAreaWidgetContents_2)
        self.fromPressureUnitInput.addItem("")
        self.fromPressureUnitInput.addItem("")
        self.fromPressureUnitInput.addItem("")
        self.fromPressureUnitInput.addItem("")
        self.fromPressureUnitInput.addItem("")
        self.fromPressureUnitInput.setObjectName(u"fromPressureUnitInput")

        self.gridLayout_9.addWidget(self.fromPressureUnitInput, 1, 0, 1, 1, Qt.AlignHCenter)

        self.toPressureUnitOutput = QComboBox(self.scrollAreaWidgetContents_2)
        self.toPressureUnitOutput.addItem("")
        self.toPressureUnitOutput.addItem("")
        self.toPressureUnitOutput.addItem("")
        self.toPressureUnitOutput.addItem("")
        self.toPressureUnitOutput.addItem("")
        self.toPressureUnitOutput.setObjectName(u"toPressureUnitOutput")

        self.gridLayout_9.addWidget(self.toPressureUnitOutput, 1, 3, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_9)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_2)

        self.conversionScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_5.addWidget(self.conversionScrollArea)

        self.tabWidget.addTab(self.tab_7, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 959, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.inputDeltaTfl_wyllie)
        self.label.setBuddy(self.inputDeltaTlog_wyllie)
        self.label_2.setBuddy(self.inputDeltaTma_wyllie)
        self.label_6.setBuddy(self.inputDeltaTma_raymer)
        self.label_5.setBuddy(self.inputDeltaTlog_raymer)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.tabWidget, self.porosityTabWidget)
        QWidget.setTabOrder(self.porosityTabWidget, self.inputDeltaTlog_wyllie)
        QWidget.setTabOrder(self.inputDeltaTlog_wyllie, self.inputDeltaTma_wyllie)
        QWidget.setTabOrder(self.inputDeltaTma_wyllie, self.inputDeltaTfl_wyllie)
        QWidget.setTabOrder(self.inputDeltaTfl_wyllie, self.calculateWylliePorosity)
        QWidget.setTabOrder(self.calculateWylliePorosity, self.resultWylliePerc)
        QWidget.setTabOrder(self.resultWylliePerc, self.resultWyllieDec)
        QWidget.setTabOrder(self.resultWyllieDec, self.addTableWyllie)
        QWidget.setTabOrder(self.addTableWyllie, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.inputDeltaTlog_raymer)
        QWidget.setTabOrder(self.inputDeltaTlog_raymer, self.inputDeltaTma_raymer)
        QWidget.setTabOrder(self.inputDeltaTma_raymer, self.calculateRaymerPorosity)
        QWidget.setTabOrder(self.calculateRaymerPorosity, self.resultRaymerPerc)
        QWidget.setTabOrder(self.resultRaymerPerc, self.resultRaymerDec)
        QWidget.setTabOrder(self.resultRaymerDec, self.addTableRaymer)
        QWidget.setTabOrder(self.addTableRaymer, self.outputTableSonicPorosity)
        QWidget.setTabOrder(self.outputTableSonicPorosity, self.exportPorosityTable)
        QWidget.setTabOrder(self.exportPorosityTable, self.conversionScrollArea)
        QWidget.setTabOrder(self.conversionScrollArea, self.fromDistanceInput)
        QWidget.setTabOrder(self.fromDistanceInput, self.toDistanceOutput)
        QWidget.setTabOrder(self.toDistanceOutput, self.fromDistanceUnitInput)
        QWidget.setTabOrder(self.fromDistanceUnitInput, self.toDistanceUnitOutput)
        QWidget.setTabOrder(self.toDistanceUnitOutput, self.fromAreaUnitInput)
        QWidget.setTabOrder(self.fromAreaUnitInput, self.fromAreaInput)
        QWidget.setTabOrder(self.fromAreaInput, self.toAreaOutput)
        QWidget.setTabOrder(self.toAreaOutput, self.toAreaUnitOutput)
        QWidget.setTabOrder(self.toAreaUnitOutput, self.fromVolumeUnitInput)
        QWidget.setTabOrder(self.fromVolumeUnitInput, self.fromVolumeInput)
        QWidget.setTabOrder(self.fromVolumeInput, self.toVolumeOutput)
        QWidget.setTabOrder(self.toVolumeOutput, self.toVolumeUnitOuput)
        QWidget.setTabOrder(self.toVolumeUnitOuput, self.toPressureOutput)
        QWidget.setTabOrder(self.toPressureOutput, self.fromPressureInput)
        QWidget.setTabOrder(self.fromPressureInput, self.fromPressureUnitInput)
        QWidget.setTabOrder(self.fromPressureUnitInput, self.toPressureUnitOutput)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.porosityTabWidget.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Petrofizika", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Wyllie et al., 1958", None))
        self.resultWyllieDec.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result (dec)", None))
        self.resultWylliePerc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result (%)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u0394tfl</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u0394tlog</span></p></body></html>", None))
        self.inputDeltaTlog_wyllie.setText("")
        self.inputDeltaTlog_wyllie.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u00b5s/ft", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u0394tma</span></p></body></html>", None))
        self.inputDeltaTma_wyllie.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u00b5s/ft", None))
        self.calculateWylliePorosity.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.addTableWyllie.setText(QCoreApplication.translate("MainWindow", u"Add to the table", None))
        self.inputDeltaTfl_wyllie.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u00b5s/ft", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Raymer et al., 1980", None))
        self.resultRaymerPerc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result (%)", None))
        self.resultRaymerDec.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result (dec)", None))
        self.inputDeltaTlog_raymer.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u00b5s/ft", None))
        self.calculateRaymerPorosity.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u0394tma</span></p></body></html>", None))
        self.inputDeltaTma_raymer.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u00b5s/ft", None))
        self.addTableRaymer.setText(QCoreApplication.translate("MainWindow", u"Add to the table", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u0394tlog</span></p></body></html>", None))
        self.porosityTabWidget.setTabText(self.porosityTabWidget.indexOf(self.sonicPorosity), QCoreApplication.translate("MainWindow", u"Sonic", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Density Log", None))
        self.matrixDensityInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u03c1ma", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Bulk formation density", None))
        self.bulkFormationDensityInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u03c1b", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Matrix density", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Fluid Density", None))
        self.fluidDensityInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u03c1fl", None))
        self.calculateDensityLogPorosity.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.resultDensityPorosityPerc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result (%)", None))
        self.resultDensityPorosityDec.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result (dec)", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Neutron-Density Combination", None))
        self.chooseNeutronDensityModel.setItemText(0, QCoreApplication.translate("MainWindow", u"Standard Model", None))
        self.chooseNeutronDensityModel.setItemText(1, QCoreApplication.translate("MainWindow", u"Alternative Model", None))

        self.resultNeutronDensityPorositPerc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result (%)", None))
        self.resultNeutronDensityPorosityDec.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result (dec)", None))
        self.calculateNeutronDensityGas.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Neutron Log Porosity", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Density Log Porosity", None))
        self.neutronLogPorosityInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0278n", None))
        self.densityLogPorosityInput.setText("")
        self.densityLogPorosityInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0278d", None))
        self.addTableDensityPorosity.setText(QCoreApplication.translate("MainWindow", u"Add to the Table", None))
        self.porosityTabWidget.setTabText(self.porosityTabWidget.indexOf(self.densityPorosity), QCoreApplication.translate("MainWindow", u"Density", None))
        self.porosityTabWidget.setTabText(self.porosityTabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Resistivity", None))
        self.porosityTabWidget.setTabText(self.porosityTabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Shale Correction", None))
        self.exportPorosityTable.setText(QCoreApplication.translate("MainWindow", u"Export data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPorosity), QCoreApplication.translate("MainWindow", u"Porosity", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPermeability), QCoreApplication.translate("MainWindow", u"Permeability", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Resistivity", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Water Saturation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Shale Volume", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Reserves", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Distance</span></p></body></html>", None))
        self.fromDistanceUnitInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Feet", None))
        self.fromDistanceUnitInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Meters", None))
        self.fromDistanceUnitInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Miles", None))
        self.fromDistanceUnitInput.setItemText(3, QCoreApplication.translate("MainWindow", u"Kilometers", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">TO</span></p></body></html>", None))
        self.toDistanceUnitOutput.setItemText(0, QCoreApplication.translate("MainWindow", u"Feet", None))
        self.toDistanceUnitOutput.setItemText(1, QCoreApplication.translate("MainWindow", u"Meters", None))
        self.toDistanceUnitOutput.setItemText(2, QCoreApplication.translate("MainWindow", u"Miles", None))
        self.toDistanceUnitOutput.setItemText(3, QCoreApplication.translate("MainWindow", u"Kilometers", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Area</span></p></body></html>", None))
        self.fromAreaUnitInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Acres", None))
        self.fromAreaUnitInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Square feet", None))
        self.fromAreaUnitInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Square meters", None))
        self.fromAreaUnitInput.setItemText(3, QCoreApplication.translate("MainWindow", u"Square kilometers", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">TO</span></p></body></html>", None))
        self.toAreaUnitOutput.setItemText(0, QCoreApplication.translate("MainWindow", u"Acres", None))
        self.toAreaUnitOutput.setItemText(1, QCoreApplication.translate("MainWindow", u"Square feet", None))
        self.toAreaUnitOutput.setItemText(2, QCoreApplication.translate("MainWindow", u"Square meters", None))
        self.toAreaUnitOutput.setItemText(3, QCoreApplication.translate("MainWindow", u"Square kilometers", None))

        self.fromVolumeUnitInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Acre-feet", None))
        self.fromVolumeUnitInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Barrels", None))
        self.fromVolumeUnitInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Cubic feet", None))
        self.fromVolumeUnitInput.setItemText(3, QCoreApplication.translate("MainWindow", u"Cubic meters", None))
        self.fromVolumeUnitInput.setItemText(4, QCoreApplication.translate("MainWindow", u"Gallons", None))
        self.fromVolumeUnitInput.setItemText(5, QCoreApplication.translate("MainWindow", u"Metric tons", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Volume</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">TO</span></p></body></html>", None))
        self.toVolumeUnitOuput.setItemText(0, QCoreApplication.translate("MainWindow", u"Acre-feet", None))
        self.toVolumeUnitOuput.setItemText(1, QCoreApplication.translate("MainWindow", u"Barrels", None))
        self.toVolumeUnitOuput.setItemText(2, QCoreApplication.translate("MainWindow", u"Cubic feet", None))
        self.toVolumeUnitOuput.setItemText(3, QCoreApplication.translate("MainWindow", u"Cubic meters", None))
        self.toVolumeUnitOuput.setItemText(4, QCoreApplication.translate("MainWindow", u"Gallons", None))
        self.toVolumeUnitOuput.setItemText(5, QCoreApplication.translate("MainWindow", u"Metric tons", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">TO</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Pressure</span></p></body></html>", None))
        self.fromPressureUnitInput.setItemText(0, QCoreApplication.translate("MainWindow", u"PSIA", None))
        self.fromPressureUnitInput.setItemText(1, QCoreApplication.translate("MainWindow", u"kPa", None))
        self.fromPressureUnitInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Bar", None))
        self.fromPressureUnitInput.setItemText(3, QCoreApplication.translate("MainWindow", u"BTU", None))
        self.fromPressureUnitInput.setItemText(4, QCoreApplication.translate("MainWindow", u"Joules", None))

        self.toPressureUnitOutput.setItemText(0, QCoreApplication.translate("MainWindow", u"PSIA", None))
        self.toPressureUnitOutput.setItemText(1, QCoreApplication.translate("MainWindow", u"kPa", None))
        self.toPressureUnitOutput.setItemText(2, QCoreApplication.translate("MainWindow", u"Bar", None))
        self.toPressureUnitOutput.setItemText(3, QCoreApplication.translate("MainWindow", u"BTU", None))
        self.toPressureUnitOutput.setItemText(4, QCoreApplication.translate("MainWindow", u"Joules", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Conversions", None))
    # retranslateUi

