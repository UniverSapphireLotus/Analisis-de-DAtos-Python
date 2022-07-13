import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice

import pyqtgraph as pg
from pyqtgraph.graphicsItems.PlotDataItem import dataType
import seaborn as sns
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib.pyplot as plt
# from PySide2 import QtWidgets
# from PyQt5 import QtWidgets
from qt_material import apply_stylesheet

from dash_bo import Ui_MainWindow

import pandas as pd
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
import numpy as np
from matplotlib import cm
#import seabornplot


import data_ventas
class MainWindow(QMainWindow):
    siz1= 0
    siz2= 0

    sizx= 0
    sizy= 0
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

        #self.setWindowFlag(Qt.FramelessWindowHint)
        #self.setAttribute(Qt.WA_TranslucentBackground)

        ####MOVE####
        #siz1=self.ui.frame_barra_menu.size().width()
        #siz2=self.ui.frame_barra_tool.size().width()
        #print(siz1, siz1)
        self.ui.boto_menu.clicked.connect(lambda: self.move_menu(self.ui.frame_barra_menu, self.siz1, self.sizx))
        self.ui.boto_tool.clicked.connect(lambda: self.move_menu(self.ui.frame_barra_tool, self.siz2, self.sizy))
        self.ui.boto_tool.setMaximumSize(0,0)
        ####----####

        self.ui.boto_men1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.boto_men2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.boto_men3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.boto_men4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))


        self.ui.boto_heat_1.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_5))
        self.ui.boto_heat_2.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_6))
        self.ui.boto_heat_3.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_7))
        self.ui.boto_heat_4.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_8))
        self.ui.boto_heat_5.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_9))
        self.ui.boto_heat_6.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_10))
        self.ui.boto_heat_7.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_11))
        #self.ui.frame_7= pg.PlotWidget()
        #self.centralWidget(self.ui.frame_7)
        self.ui.boto_max.hide()
        
        ####BOTO####
        self.ui.boto_cerrar.clicked.connect(lambda: self.close())
        self.ui.boto_max.clicked.connect(lambda: self.maxi_window())
        self.ui.boto_restaurar.clicked.connect(self.rest_window)
        self.ui.boto_min.clicked.connect(self.showMinimized)
        ####----####
        #self.ui.bt_menu.clicked.connect(self.mover_menu)
        #self.ui.frame_tool.clicked.connect(self.mover_menu)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        #self.graphWidget.plot(hour, temperature)
        y1 = [5, 5, 7, 10, 3, 8, 9, 1, 6, 2]
        # create horizontal list i.e x-axis
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        #self.ui.frame_7.plot(hour, temperature)
        #self.ui.widget.graphWidget.plot(hour, temperature)
        self.ui.widget.setBackground('31363b')
        self.ui.widget_1.setBackground('31363b')
        self.ui.widget_2.setBackground('31363b')
        self.ui.widget_3.setBackground('31363b')
        self.ui.widget_4.setBackground('31363b')
        self.ui.widget_5.setBackground('31363b')
        self.ui.widget_6.setBackground('31363b')
        self.ui.widget_7.setBackground('31363b')
        #self.ui.widgetGraficoBarra.plot(hour, temperature)
        #self.ui.widget.plot(hour, temperature)
        #self.ui.widget_2.plot(hour, temperature)
        #self.ui.widget_3.plot(hour, temperature)
        
        self.ui.widget_4.plot(hour, temperature)
        #self.ui.widget_5.plot(y1, x)
        #self.ui.widget_5.addItem(pg.BarGraphItem(x = x, height = y1, width = 0.6, brush ='w'))
        #self.ui.widget_5.addItem()
        #self.ui.widget_5= pg.BarGraphItem(x = x, height = y1, width = 0.6, brush ='g')
        
        ##pie chart
        #self.create_piechart()

        #self.ui.widget_6.plot(hour, temperature)
        #self.ui.widget_6.plot(y1, x)
        #self.ui.widget_7.plot(hour, temperature)

        alle= data_ventas.obtenerVentaMesero_CC_PT_Ce()
        self.draw_graf_barr_stac(self.ui.widget_2, alle[0], alle[-1], 2)
        self.draw_graf_barr_stac(self.ui.widget_1, alle[1], alle[-1], 2)
        #self.ui.widget_7.addItem(pg.BarGraphItem(x = x, height = y1, width = 0.6, brush ='b'))
        #self.create_stacked_barra()
        xand= data_ventas.obtenerProductos_CU_Tipo_TotalCantidad()
        self.draw_graf_pie(self.ui.widget_8, xand[2])
        self.draw_graf_barr_stac(self.ui.widget_3, xand[0],[''], 1)
        self.draw_graf_barr_stac(self.ui.widget, xand[1],[''], 1)
        
        self.draw_graf_line_top3([self.ui.widget_4, self.ui.widget_5, self.ui.widget_6], data_ventas.obtenerTOP_3_fecha()[0])
        self.draw_graf_line_mult(self.ui.widget_7, data_ventas.obtenerVentasTotal_fecha()[0])

        #self.draw_graf_heat_mapi(self.ui.frame_8, pucci.obtenerHeatMap())
        #self.draw_graf_heat_matp(self.ui.frame_8, pucci.obtenerHeatMap_4())
        self.draw_graf_heat_matp(self.ui.page_5, data_ventas.obtenerHeatMap_1())
        self.draw_graf_heat_matp(self.ui.page_6, data_ventas.obtenerHeatMap_2())
        self.draw_graf_heat_matp(self.ui.page_7, data_ventas.obtenerHeatMap_3())
        self.draw_graf_heat_matp(self.ui.page_8, data_ventas.obtenerHeatMap_4())
        clima_condicion= data_ventas.obtenerHeatMap_5()
        self.draw_graf_heat_matp(self.ui.page_9, clima_condicion[0])
        self.draw_graf_heat_matp(self.ui.page_10, clima_condicion[1])

        hora_heat_map = data_ventas.obtenerHeatMap_horas_productos()
        self.draw_graf_heat_matp(self.ui.fram_hora_1, hora_heat_map[0])
        self.draw_graf_heat_matp(self.ui.fram_hora_2, hora_heat_map[1][0])
        self.draw_graf_heat_matp(self.ui.fram_hora_3, hora_heat_map[1][1])
        self.draw_graf_heat_matp(self.ui.fram_hora_4, hora_heat_map[1][2])

        
        #self.draw_graf_heat_mapi()
        self.ui.boto_pred.clicked.connect(lambda: self.predecir())


        self.showMaximized()
        self.show()
    def predecir(self):
    
        try:
            iter= int(self.ui.lineEdit.text())
            valo= data_ventas.obtener_regresion_ventas_clima(iter)
            self.ui.labe_conf.setText(str(valo[2]))
            self.ui.labe_coef.setText(str(valo[0]))
            self.ui.labe_pend.setText(str(valo[1]))
            self.ui.labe_saba.setText(str(valo[-1][0]))
            self.ui.labe_domi.setText(str(valo[-1][1]))


        except:
            print('nop')

    def seabornplot(self, sweet):
        #tips = sns.load_dataset("tips")
        #uniform_data = np.random.rand(10, 12)
        #g = sns.FacetGrid(tips, col="sex", hue="time", palette="Set1", hue_order=["Dinner", "Lunch"])
        g = sns.FacetGrid(sweet, legend_out= False)#, palette="Set1")
        #sns.set_color_codes
        #g.map(plt.scatter, "total_bill", "tip", edgecolor="w")
        #uniform_data = np.random.rand(10, 12)
        ax = sns.heatmap(sweet, cmap="viridis",  # Choose a squential colormap
                #annot=jb_labels, # Label the maximum value
                annot_kws={'fontsize':11},  # Reduce size of label to fit
                fmt='',          # Interpret labels as strings
                #square=True,     # Force square cells
                #vmax=40,         # Ensure same 
                vmin=0,          # color scale
                linewidth=0.01,  # Add gridlines
                linecolor="#222",# Adjust gridline color
                #ax=ax[i],        # Arrange in subplot
                robust=True,
                xticklabels=1,
                yticklabels=1
                #annot=True
               )
        #g.map(ax)
        
        return g.fig

    def draw_graf_heat_matp(self, cake, cup):
        sweet= self.seabornplot(cup)
        canva= FigureCanvas(sweet)
        #canva.autoFillBackground()
        canva.setStyleSheet("background-color:transparent;")
        #self.ui.frame_8.layout().addWidget(canva)
        cake.layout().addWidget(canva)
        

    def draw_graf_line_top3(self, cake, cup):
        #cup= list(cup.columns)
        let= list(cup.index.values)
        cup= cup.iloc[:, 1:]
        cmap = cm.get_cmap('tab10')
        colors = [tuple(255*x for x in cmap(i/10))[:-1] for i in range(len(cup.columns))]
        zelda= list(cup.columns)
        #cake.addLegend()
        for col, color, link,sweet in zip(cup.columns, colors, zelda, cake):
            #print('raa' , list(cup[link]),col, color)
            #cake.plot(let, list(cup[link]),  fillLevel=0.1, fillBrush=pg.mkBrush(color = color), name= link)
            sweet.addLegend()
            sweet.plot(let, list(cup[link]),  fillLevel=0.1, pen= pg.mkPen(color = color), name= link)

    def draw_graf_line_mult(self, cake, cup):
        #cup= list(cup.columns)
        let= list(cup.index.values)
        cup= cup.iloc[:, 1:]
        cmap = cm.get_cmap('tab10')
        colors = [tuple(255*x for x in cmap(i/10))[:-1] for i in range(len(cup.columns))]
        zelda= list(cup.columns)
        cake.addLegend()
        for col, color, link in zip(cup.columns, colors, zelda):
            #print('raa' , list(cup[link]),col, color)
            #cake.plot(let, list(cup[link]),  fillLevel=0.1, fillBrush=pg.mkBrush(color = color), name= link)
            cake.plot(let, list(cup[link]),  fillLevel=0.1, pen= pg.mkPen(color = color), name= link)

    def draw_graf_barr_stac(self, cake, cup, valo ,ind):
        #df= pucci.obtenerVentaMesero_CC_PT_Ce()[2]
        #df.drop('mozo', axis=1, inplace=True)
        cup= cup.reindex()
        vio= list(cup.iloc[:, 1])
        let= list(cup.index.values)
        
        axi= dict(zip(list(cup.index.values), list(cup.iloc[:, 0])))
        print(axi)

        axy = pg.GraphicsWindow()
        stringaxis = pg.AxisItem(orientation='right')
        stringaxis.setTicks([axi.items()])
        cake.plotItem.setAxisItems(axisItems={'left': stringaxis})
        
        cake.addLegend(offset=-1)
        cake.plot(vio, let, fillLevel=1, name='total')#, orientation='bottom',fillBrush=(255,255,255,30), name='total')
        cup= cup.iloc[:, ind:]
        
        bottom = np.zeros(len(cup))
        cmap = cm.get_cmap('tab10')
        colors = [tuple(255*x for x in cmap(i/10))[:-1] for i in range(len(cup.columns))]
        #color2 = [tuple(255*x for x in cmap(i/10))[:-1] for i in range(len(df.columns))]
        #valu= ['Plato Típico', 'Caja China', 'Cervezas']
        for col, color, val in zip(cup.columns, colors, valo):
            #bargraph = pg.BarGraphItem(x = cup.index, height = cup[col], y0 = bottom, width = 0.6, brush = pg.mkBrush(color = color), pen = pg.mkPen(color = color), name=val)
            bargraph = pg.BarGraphItem(y = cup.index, width = cup[col], x0 = bottom, height = 0.6, brush = pg.mkBrush(color = color), pen = pg.mkPen(color = color), name=val)
            #bargraph2 = pg.BarGraphItem(x = cup.index, height = cup[col], y0 = bottom, width = 0.6, brush = pg.mkBrush(color = color), pen = pg.mkPen(color = color))    
            cake.addItem(bargraph)
            bottom += cup[col]
        #QtGui.QApplication.instance().exec_()

    def draw_graf_pie(self, cake, cup):
        
        vio= list(cup.iloc[:, 0])
        let= list(cup.iloc[:, 1])
        pie = QPieSeries()
        print(vio)
        for vi, le in zip(vio, let):
            pie.append(vi ,le)
        
        chart = QChart()
        chart.legend().hide()
        chart.addSeries(pie)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Pie Chart Example")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        pirchart = QChartView(chart)
        pirchart.setRenderHint(QPainter.Antialiasing)
        cake.setChart(chart)
        


    def move_menu(self, menu, lonx, lony):
        #self.clickPosition = event.globalPos()
        vi= menu.width()
        print('vi: ', vi)
        #cait= self.ui.frame_barra_menu.size()
        #print(menu.size().width())
        #print(menu.size())
        #print(size)
        #print(cait)
        extend=0
        
        #self.ui.frame_barra_menu
        
        if vi==0:
            extend= lonx
            menu.setMinimumSize(extend,lony)
            #menu.setMaximumWidth(extend)
            #self.ui.frame_barra_menu.setMaximumWidth
        else:
            #self.siz1= menu.size().width()
            self.update_data()
            menu.setMaximumSize(extend,lony)
            print('oh me ejecuto')
            #self.ui.frame_barra_menu.resize(extend,844)
            #self.ui.frame_barra_menu.setGeometry()

        self.animacion = QPropertyAnimation(menu, b'minimumWidth')
        self.animacion.setDuration(400)
        self.animacion.setStartValue(vi)
        self.animacion.setEndValue(extend)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacion.start()

        print( vi, ' <> ',extend)
        print('ra: ',self.siz1, ' & ',self.sizx)
        print('ga: ',self.siz2, ' & ',self.sizy)
        #print(vi)

    def update_data(self):
        if(self.ui.frame_barra_menu.size().width()!=0):
            self.siz1=self.ui.frame_barra_menu.size().width()
        if(self.ui.frame_barra_tool.size().width()!=0):
            self.siz2=self.ui.frame_barra_tool.size().width()
        if(self.ui.frame_barra_menu.size().height()!=0):
            self.sizx=self.ui.frame_barra_menu.size().height()
        if(self.ui.frame_barra_tool.size().height()!=0):
            self.sizy=self.ui.frame_barra_tool.size().height()
	

    def rest_window(self): 
        self.showNormal()		
        self.ui.boto_restaurar.hide()
        self.ui.boto_max.show()
        self.update_data()


    def maxi_window(self): 
        self.showMaximized()
        self.ui.boto_max.hide()
        self.ui.boto_restaurar.show()
        self.update_data()

    def desplegar_ventana(self, event):
        pass

    

        


if __name__== '__main__':
    print('raaaa')
    app= QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_cyan.xml')
    window= MainWindow()
    sys.exit(app.exec_())

data_ventas.obtenerVentas_Fecha()
#pucci.obtenerVentas_Fecha()
#pyside6-uic dasdh_bo.ui -o dash_bo.py