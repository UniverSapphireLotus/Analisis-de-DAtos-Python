# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dasdh_bo.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QToolButton, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1489, 883)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_tool = QFrame(self.centralwidget)
        self.frame_tool.setObjectName(u"frame_tool")
        self.frame_tool.setFrameShape(QFrame.StyledPanel)
        self.frame_tool.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_tool)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.boto_menu = QToolButton(self.frame_tool)
        self.boto_menu.setObjectName(u"boto_menu")
        self.boto_menu.setMinimumSize(QSize(40, 40))
        self.boto_menu.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.boto_menu)

        self.boto_tool = QToolButton(self.frame_tool)
        self.boto_tool.setObjectName(u"boto_tool")
        self.boto_tool.setMinimumSize(QSize(40, 40))
        self.boto_tool.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.boto_tool)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.boto_min = QToolButton(self.frame_tool)
        self.boto_min.setObjectName(u"boto_min")
        self.boto_min.setMinimumSize(QSize(40, 40))
        self.boto_min.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.boto_min)

        self.boto_restaurar = QToolButton(self.frame_tool)
        self.boto_restaurar.setObjectName(u"boto_restaurar")
        self.boto_restaurar.setMinimumSize(QSize(40, 40))
        self.boto_restaurar.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.boto_restaurar)

        self.boto_max = QToolButton(self.frame_tool)
        self.boto_max.setObjectName(u"boto_max")
        self.boto_max.setMinimumSize(QSize(40, 40))
        self.boto_max.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.boto_max)

        self.boto_cerrar = QToolButton(self.frame_tool)
        self.boto_cerrar.setObjectName(u"boto_cerrar")
        self.boto_cerrar.setMinimumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.boto_cerrar)


        self.gridLayout.addWidget(self.frame_tool, 0, 1, 1, 2)

        self.frame_barra_menu = QFrame(self.centralwidget)
        self.frame_barra_menu.setObjectName(u"frame_barra_menu")
        self.frame_barra_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_barra_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_barra_menu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_13 = QFrame(self.frame_barra_menu)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_13)

        self.frame_5 = QFrame(self.frame_barra_menu)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.boto_men1 = QPushButton(self.frame_5)
        self.boto_men1.setObjectName(u"boto_men1")

        self.verticalLayout_2.addWidget(self.boto_men1)

        self.boto_men2 = QPushButton(self.frame_5)
        self.boto_men2.setObjectName(u"boto_men2")

        self.verticalLayout_2.addWidget(self.boto_men2)

        self.boto_men3 = QPushButton(self.frame_5)
        self.boto_men3.setObjectName(u"boto_men3")

        self.verticalLayout_2.addWidget(self.boto_men3)

        self.boto_men4 = QPushButton(self.frame_5)
        self.boto_men4.setObjectName(u"boto_men4")

        self.verticalLayout_2.addWidget(self.boto_men4)


        self.verticalLayout.addWidget(self.frame_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.frame_barra_menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon = QIcon()
        icon.addFile(u"gif/cait.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(120, 120))

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_4)


        self.gridLayout.addWidget(self.frame_barra_menu, 0, 0, 2, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_7 = QFrame(self.page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_1 = PlotWidget(self.frame_7)
        self.widget_1.setObjectName(u"widget_1")

        self.verticalLayout_6.addWidget(self.widget_1)


        self.gridLayout_2.addWidget(self.frame_7, 0, 0, 2, 1)

        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_2 = PlotWidget(self.frame_6)
        self.widget_2.setObjectName(u"widget_2")

        self.verticalLayout_7.addWidget(self.widget_2)


        self.gridLayout_2.addWidget(self.frame_6, 0, 1, 2, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_12 = QVBoxLayout(self.page_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame = QFrame(self.page_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget = PlotWidget(self.frame)
        self.widget.setObjectName(u"widget")

        self.gridLayout_4.addWidget(self.widget, 0, 1, 1, 1)

        self.widget_3 = PlotWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")

        self.gridLayout_4.addWidget(self.widget_3, 1, 1, 1, 1)

        self.widget_8 = QChartView(self.frame)
        self.widget_8.setObjectName(u"widget_8")

        self.gridLayout_4.addWidget(self.widget_8, 0, 0, 2, 1)


        self.verticalLayout_12.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_4 = QHBoxLayout(self.page_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_3 = QFrame(self.page_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_17 = QFrame(self.frame_3)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_17)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_5 = PlotWidget(self.frame_17)
        self.widget_5.setObjectName(u"widget_5")

        self.verticalLayout_9.addWidget(self.widget_5)


        self.gridLayout_6.addWidget(self.frame_17, 0, 1, 1, 1)

        self.frame_16 = QFrame(self.frame_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_16)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_7 = PlotWidget(self.frame_16)
        self.widget_7.setObjectName(u"widget_7")

        self.verticalLayout_11.addWidget(self.widget_7)


        self.gridLayout_6.addWidget(self.frame_16, 1, 0, 1, 3)

        self.frame_15 = QFrame(self.frame_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_6 = PlotWidget(self.frame_15)
        self.widget_6.setObjectName(u"widget_6")

        self.verticalLayout_10.addWidget(self.widget_6)


        self.gridLayout_6.addWidget(self.frame_15, 0, 2, 1, 1)

        self.frame_14 = QFrame(self.frame_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_14)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_4 = PlotWidget(self.frame_14)
        self.widget_4.setObjectName(u"widget_4")

        self.verticalLayout_8.addWidget(self.widget_4)


        self.gridLayout_6.addWidget(self.frame_14, 0, 0, 1, 1)

        self.gridLayout_6.setRowStretch(0, 2)
        self.gridLayout_6.setRowStretch(1, 6)

        self.horizontalLayout_4.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_13 = QVBoxLayout(self.page_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_9 = QFrame(self.page_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.boto_heat_1 = QPushButton(self.frame_9)
        self.boto_heat_1.setObjectName(u"boto_heat_1")

        self.horizontalLayout.addWidget(self.boto_heat_1)

        self.boto_heat_2 = QPushButton(self.frame_9)
        self.boto_heat_2.setObjectName(u"boto_heat_2")

        self.horizontalLayout.addWidget(self.boto_heat_2)

        self.boto_heat_3 = QPushButton(self.frame_9)
        self.boto_heat_3.setObjectName(u"boto_heat_3")

        self.horizontalLayout.addWidget(self.boto_heat_3)

        self.boto_heat_4 = QPushButton(self.frame_9)
        self.boto_heat_4.setObjectName(u"boto_heat_4")

        self.horizontalLayout.addWidget(self.boto_heat_4)

        self.boto_heat_5 = QPushButton(self.frame_9)
        self.boto_heat_5.setObjectName(u"boto_heat_5")

        self.horizontalLayout.addWidget(self.boto_heat_5)

        self.boto_heat_6 = QPushButton(self.frame_9)
        self.boto_heat_6.setObjectName(u"boto_heat_6")

        self.horizontalLayout.addWidget(self.boto_heat_6)

        self.boto_heat_7 = QPushButton(self.frame_9)
        self.boto_heat_7.setObjectName(u"boto_heat_7")

        self.horizontalLayout.addWidget(self.boto_heat_7)


        self.verticalLayout_13.addWidget(self.frame_9)

        self.frame_8 = QFrame(self.page_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_8)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.stackedWidget_2 = QStackedWidget(self.frame_8)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_15 = QVBoxLayout(self.page_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.stackedWidget_2.addWidget(self.page_5)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.gridLayout_7 = QGridLayout(self.page_10)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.stackedWidget_2.addWidget(self.page_10)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_16 = QVBoxLayout(self.page_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.stackedWidget_2.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_17 = QVBoxLayout(self.page_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.stackedWidget_2.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_18 = QVBoxLayout(self.page_8)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.stackedWidget_2.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_19 = QVBoxLayout(self.page_9)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.stackedWidget_2.addWidget(self.page_9)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.gridLayout_8 = QGridLayout(self.page_11)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.fram_hora_3 = QWidget(self.page_11)
        self.fram_hora_3.setObjectName(u"fram_hora_3")
        self.verticalLayout_22 = QVBoxLayout(self.fram_hora_3)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")

        self.gridLayout_8.addWidget(self.fram_hora_3, 0, 1, 1, 1)

        self.fram_hora_1 = QWidget(self.page_11)
        self.fram_hora_1.setObjectName(u"fram_hora_1")
        self.verticalLayout_20 = QVBoxLayout(self.fram_hora_1)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")

        self.gridLayout_8.addWidget(self.fram_hora_1, 0, 0, 1, 1)

        self.fram_hora_4 = QWidget(self.page_11)
        self.fram_hora_4.setObjectName(u"fram_hora_4")
        self.verticalLayout_23 = QVBoxLayout(self.fram_hora_4)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")

        self.gridLayout_8.addWidget(self.fram_hora_4, 1, 1, 1, 1)

        self.fram_hora_2 = QWidget(self.page_11)
        self.fram_hora_2.setObjectName(u"fram_hora_2")
        self.verticalLayout_21 = QVBoxLayout(self.fram_hora_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")

        self.gridLayout_8.addWidget(self.fram_hora_2, 1, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_11)

        self.verticalLayout_14.addWidget(self.stackedWidget_2)


        self.verticalLayout_13.addWidget(self.frame_8)

        self.verticalLayout_13.setStretch(1, 9)
        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.frame_2, 1, 2, 1, 1)

        self.frame_barra_tool = QFrame(self.centralwidget)
        self.frame_barra_tool.setObjectName(u"frame_barra_tool")
        self.frame_barra_tool.setFrameShape(QFrame.StyledPanel)
        self.frame_barra_tool.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_barra_tool)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_11 = QFrame(self.frame_barra_tool)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 5, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame_11)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_7 = QLabel(self.frame_11)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 6, 0, 1, 1)

        self.labe_conf = QLabel(self.frame_11)
        self.labe_conf.setObjectName(u"labe_conf")

        self.gridLayout_3.addWidget(self.labe_conf, 2, 1, 1, 1)

        self.labe_coef = QLabel(self.frame_11)
        self.labe_coef.setObjectName(u"labe_coef")

        self.gridLayout_3.addWidget(self.labe_coef, 3, 1, 1, 1)

        self.labe_pend = QLabel(self.frame_11)
        self.labe_pend.setObjectName(u"labe_pend")

        self.gridLayout_3.addWidget(self.labe_pend, 4, 1, 1, 1)

        self.labe_saba = QLabel(self.frame_11)
        self.labe_saba.setObjectName(u"labe_saba")

        self.gridLayout_3.addWidget(self.labe_saba, 5, 1, 1, 1)

        self.labe_domi = QLabel(self.frame_11)
        self.labe_domi.setObjectName(u"labe_domi")

        self.gridLayout_3.addWidget(self.labe_domi, 6, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_barra_tool)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_12)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.boto_pred = QPushButton(self.frame_12)
        self.boto_pred.setObjectName(u"boto_pred")
        self.boto_pred.setMinimumSize(QSize(80, 80))
        self.boto_pred.setMaximumSize(QSize(16777215, 16777215))
        self.boto_pred.setSizeIncrement(QSize(80, 80))
        icon1 = QIcon()
        icon1.addFile(u"gif/vi.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.boto_pred.setIcon(icon1)
        self.boto_pred.setIconSize(QSize(120, 120))

        self.gridLayout_5.addWidget(self.boto_pred, 3, 0, 1, 2)


        self.verticalLayout_5.addWidget(self.frame_12)


        self.gridLayout.addWidget(self.frame_barra_tool, 1, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 19)
        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 8)
        self.gridLayout.setColumnStretch(2, 21)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.boto_menu.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.boto_tool.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.boto_min.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.boto_restaurar.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.boto_max.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.boto_cerrar.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.boto_men1.setText(QCoreApplication.translate("MainWindow", u"Venta de empleados total y cantidad", None))
        self.boto_men2.setText(QCoreApplication.translate("MainWindow", u"Linea de ventas por tipo", None))
        self.boto_men3.setText(QCoreApplication.translate("MainWindow", u"Pie de ventas por tipo", None))
        self.boto_men4.setText(QCoreApplication.translate("MainWindow", u"Mapa de calor", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PIN", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Mapa de calor", None))
        self.boto_heat_1.setText(QCoreApplication.translate("MainWindow", u"Venta total por producto", None))
        self.boto_heat_2.setText(QCoreApplication.translate("MainWindow", u"Venta total por tipo", None))
        self.boto_heat_3.setText(QCoreApplication.translate("MainWindow", u"Cantidad de producto", None))
        self.boto_heat_4.setText(QCoreApplication.translate("MainWindow", u"Cantidad por tipo", None))
        self.boto_heat_5.setText(QCoreApplication.translate("MainWindow", u"Ventas x temperatura", None))
        self.boto_heat_6.setText(QCoreApplication.translate("MainWindow", u"Ventas x condicion", None))
        self.boto_heat_7.setText(QCoreApplication.translate("MainWindow", u"Ventas x hora", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Confiabilidad", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Coeficiente a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Prediccion sabado", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Numero de iteraciones", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Coeficientes b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Modelo prediccion", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Prediccion domingo", None))
        self.labe_conf.setText("")
        self.labe_coef.setText("")
        self.labe_pend.setText("")
        self.labe_saba.setText("")
        self.labe_domi.setText("")
        self.boto_pred.setText(QCoreApplication.translate("MainWindow", u"PREDECIR", None))
    # retranslateUi

