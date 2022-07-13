import pandas as pd
from matplotlib import pyplot as plt

from sklearn.linear_model import LinearRegression

from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
#import matplotlib.pyplot as plt

import seaborn as sns

import webS_prox_saba_domi

vi= pd.read_csv('Lista de productos.csv')

#vi=vi.drop(['precio'], axis=1, inplace=True))

cait= pd.read_csv('ResumenVentas_1.csv')

kiraman= pd.read_csv('ResumenVentas_2.csv')

cait= pd.concat([cait, kiraman], axis=0, ignore_index=True)
datos_hora= pd.read_csv('ResumenVentas_3.csv')
#datos_hora= datos_hora.iloc[:, :-1]
cait= pd.concat([cait, datos_hora.iloc[:, :-1]], axis=0, ignore_index=True)


#pd.to_datetime(df["date"].dt.strftime('%Y-%m'))
#cait['fecha']= pd.to_datetime(cait['fecha'].dt.strftime('%Y-%m-%d'))
cait['fecha']=  pd.to_datetime(cait.fecha, format='%d/%m/%Y')
cait['fecha']= pd.to_datetime(cait['fecha'].dt.strftime('%Y-%m-%d'))
cait['fecha']= cait['fecha'].dt.date
#cait['fecha']= pd.to_datetime(cait['fecha'].dt.strftime('%Y-%m-%d'))


#cait= cait.dropna(subset=['fecha'])
cait= cait.dropna()
datos_hora= datos_hora.dropna()

#record_clima= pd.concat([pd.read_csv('record_clima_2020_domingo.csv'), pd.read_csv('record_clima_2020_sabado.csv')], axis=0, ignore_index=True)
#record_clima= pd.read_csv('record_clima_2021.csv')
record_clima= pd.concat([pd.read_csv('record_clima_2020.csv'), pd.read_csv('record_clima_2021.csv')], axis=0, ignore_index=True)


record_clima['fecha']=  pd.to_datetime(record_clima.fecha, format='%Y-%m-%d')
record_clima['fecha']= pd.to_datetime(record_clima['fecha'].dt.strftime('%Y-%m-%d'))
#record_clima['fecha']= record_clima['fecha'].dt.date
#record_clima['mes'] = record_clima['fecha'].dt.strftime('%b')
record_clima['mes'] = record_clima['fecha'].dt.month
record_clima['fecha']= record_clima['fecha'].dt.date

record_clima['temperatura']= record_clima['temperatura'].str[:2].apply(pd.to_numeric)
record_clima['Punto de rocio']= record_clima['Punto de rocio'].str[:2].apply(pd.to_numeric)
record_clima['Humedad']= record_clima['Humedad'].str[:2].apply(pd.to_numeric)
record_clima['nudos de viento']= record_clima['nudos de viento'].str[:2].apply(pd.to_numeric)
record_clima['Rafaga']= record_clima['Rafaga'].str[:2].apply(pd.to_numeric)

record_clima['Presion']= record_clima['Presion'].str[:5].apply(pd.to_numeric)
#datf['Max']= datf['Max'].str[:2].apply(pd.to_numeric)
traducto_condicion= pd.read_csv('Condicion convertido -condicion.csv')
traductor_veinto  = pd.read_csv('Condicion convertido -viento.csv')
#tabla_ventas= pd.merge(cait, vi, on='IdProducto')
record_clima= pd.merge(record_clima, traducto_condicion, on='Condicion')
record_clima= pd.merge(record_clima, traductor_veinto, on='viento')

record_clima['hora']= record_clima['hora'].str[:2]+ record_clima['hora'].str[-3:]

akko=[['10 AM', '11 AM'], ['12 PM', '1: PM'], ['2: PM', '3: PM', '4: PM']]
dian=['12:00', '2:00' , '5:00']

#record_clima= record_clima.loc[record_clima['hora'].isin(valo[1])]
#record_clima['hora']= 'raa'

record_clima_agrupado_horas= pd.DataFrame()
for ak, di in zip(akko, dian):
    act4= record_clima.loc[record_clima['hora'].isin(ak)]
    act4['hora']= di
    record_clima_agrupado_horas= pd.concat([record_clima_agrupado_horas, act4], ignore_index= True)

record_clima_agrupado= record_clima.groupby('fecha', as_index=False).agg(temperatura_max=('temperatura', 'max'), temperatura_min= ('temperatura', 'min'),
                                                                Punto_de_rocio_max=('Punto de rocio', 'max'), Punto_de_rocio_min=('Punto de rocio', 'min'),
                                                                Humedad_max=('Humedad', 'max'), Humedad_min=('Humedad', 'min'),
                                                                nudos_de_viento_max=('nudos de viento', 'max'), nudos_de_viento_min=('nudos de viento', 'min'),
                                                                #Rafaga_max=('Rafaga', 'max'), Rafaga_min=('Rafaga', 'min'),
                                                                Presion_max=('Presion', 'max'), Presion_min=('Presion', 'min'),
                                                                Condicion_max=('valor_Condicion', 'max'), Condicion_min=('valor_Condicion', 'min'),
                                                                #viento_max=('valor_veinto', 'max'), viento_min=('valor_veinto', 'min')
                                                                )

revison_horas= record_clima_agrupado_horas.groupby(['fecha', 'hora'], as_index=False).agg(temperatura_max=('temperatura', 'max'), temperatura_min= ('temperatura', 'min'),
                                                                Punto_de_rocio_max=('Punto de rocio', 'max'), Punto_de_rocio_min=('Punto de rocio', 'min'),
                                                                Humedad_max=('Humedad', 'max'), Humedad_min=('Humedad', 'min'),
                                                                nudos_de_viento_max=('nudos de viento', 'max'), nudos_de_viento_min=('nudos de viento', 'min'),
                                                                #Rafaga_max=('Rafaga', 'max'), Rafaga_min=('Rafaga', 'min'),
                                                                Presion_max=('Presion', 'max'), Presion_min=('Presion', 'min'),
                                                                Condicion_max=('valor_Condicion', 'max'), Condicion_min=('valor_Condicion', 'min'),
                                                                #viento_max=('valor_veinto', 'max'), viento_min=('valor_veinto', 'min')
                                                                )


record_clima_agrupado_horas= record_clima_agrupado_horas.groupby(['fecha', 'hora'], as_index=False).agg(temperatura_max=('temperatura', 'max'), temperatura_min= ('temperatura', 'min'),
                                                                Punto_de_rocio_max=('Punto de rocio', 'max'), Punto_de_rocio_min=('Punto de rocio', 'min'),
                                                                Humedad_max=('Humedad', 'max'), Humedad_min=('Humedad', 'min'),
                                                                nudos_de_viento_max=('nudos de viento', 'max'), nudos_de_viento_min=('nudos de viento', 'min'),
                                                                #Rafaga_max=('Rafaga', 'max'), Rafaga_min=('Rafaga', 'min'),
                                                                Presion_max=('Presion', 'max'), Presion_min=('Presion', 'min'),
                                                                Condicion_max=('valor_Condicion', 'max'), Condicion_min=('valor_Condicion', 'min'),
                                                                #viento_max=('valor_veinto', 'max'), viento_min=('valor_veinto', 'min')
                                                                )



record_clima_agrupado['temperatura']= (record_clima_agrupado['temperatura_max']+ record_clima_agrupado['temperatura_min'])/2
record_clima_agrupado['Punto de rocio']= (record_clima_agrupado['Punto_de_rocio_max']+ record_clima_agrupado['Punto_de_rocio_min'])/2
record_clima_agrupado['Humedad']= (record_clima_agrupado['Humedad_max']+ record_clima_agrupado['Humedad_min'])/2
record_clima_agrupado['nudos de viento']= (record_clima_agrupado['nudos_de_viento_max']+ record_clima_agrupado['nudos_de_viento_min'])/2
record_clima_agrupado['Presion']= (record_clima_agrupado['Presion_max']+ record_clima_agrupado['Presion_min'])/2
record_clima_agrupado['Condicion']= (record_clima_agrupado['Condicion_max']+ record_clima_agrupado['Condicion_min'])/2

record_clima_agrupado.drop(['temperatura_max', 'temperatura_min'], axis = 1, inplace=True)
record_clima_agrupado.drop(['Punto_de_rocio_max', 'Punto_de_rocio_min'], axis = 1, inplace=True)
record_clima_agrupado.drop(['Humedad_max', 'Humedad_min'], axis = 1, inplace=True)
record_clima_agrupado.drop(['nudos_de_viento_max', 'nudos_de_viento_min'], axis = 1, inplace=True)
record_clima_agrupado.drop(['Presion_max', 'Presion_min'], axis = 1, inplace=True)
record_clima_agrupado.drop(['Condicion_max', 'Condicion_min'], axis = 1, inplace=True)

record_clima_agrupado_horas['temperatura']= (record_clima_agrupado_horas['temperatura_max']+ record_clima_agrupado_horas['temperatura_min'])/2
record_clima_agrupado_horas['Punto de rocio']= (record_clima_agrupado_horas['Punto_de_rocio_max']+ record_clima_agrupado_horas['Punto_de_rocio_min'])/2
record_clima_agrupado_horas['Humedad']= (record_clima_agrupado_horas['Humedad_max']+ record_clima_agrupado_horas['Humedad_min'])/2
record_clima_agrupado_horas['nudos de viento']= (record_clima_agrupado_horas['nudos_de_viento_max']+ record_clima_agrupado_horas['nudos_de_viento_min'])/2
record_clima_agrupado_horas['Presion']= (record_clima_agrupado_horas['Presion_max']+ record_clima_agrupado_horas['Presion_min'])/2
record_clima_agrupado_horas['Condicion']= (record_clima_agrupado_horas['Condicion_max']+ record_clima_agrupado_horas['Condicion_min'])/2

record_clima_agrupado_horas.drop(['temperatura_max', 'temperatura_min'], axis = 1, inplace=True)
record_clima_agrupado_horas.drop(['Punto_de_rocio_max', 'Punto_de_rocio_min'], axis = 1, inplace=True)
record_clima_agrupado_horas.drop(['Humedad_max', 'Humedad_min'], axis = 1, inplace=True)
record_clima_agrupado_horas.drop(['nudos_de_viento_max', 'nudos_de_viento_min'], axis = 1, inplace=True)
record_clima_agrupado_horas.drop(['Presion_max', 'Presion_min'], axis = 1, inplace=True)
record_clima_agrupado_horas.drop(['Condicion_max', 'Condicion_min'], axis = 1, inplace=True)
#print(cait)
#	Unnamed: 0	hora	temperatura	Punto de rocio	Humedad	viento	nudos de viento	Rafaga	Presion	Precipitacion	Condicion	fecha	mes	valor_Condicion	valor_veinto

#sicc= pd.concat([cait, vi.reindex(cait.index)])
#sicc= pd.concat([cait, vi.reindex(cait.index)], axis=1)
#pd.merge(clients, invoices, on='client_id')

#tabla_ventas= pd.merge(cait, vi, on='IdProducto').drop(['mozo', 'fecha','Nombre','IdProducto','Precio'], axis=1)
tabla_ventas= pd.merge(cait, vi, on='IdProducto')
tabla_ventas['Total']= tabla_ventas['Precio']*tabla_ventas['cantidad']

datos_hora= pd.merge(datos_hora, vi, on='IdProducto')
datos_hora['Total']= datos_hora['Precio']*datos_hora['cantidad']
#df.groupby('Company Name').agg(MySum=('Amount', 'sum'), MyCount=('Amount', 'count'))

#dat1= tabla_ventas.groupby('Tipo').agg(MySum=('cantidad', 'sum'), MyCount=('Tipo', 'count'))

def obtenerProductos_CU_Tipo_TotalCantidad():
    cup= tabla_ventas.groupby('Nombre').agg(TotalxProducto=('cantidad', 'sum'))
    cup= pd.merge(cup, vi[['Nombre', 'Tipo', 'Precio']] , on='Nombre')
    cup['Total']= cup['Precio']*cup['TotalxProducto']
    
    
    cake= cup.groupby('Tipo',  as_index = False).agg(Total=('Total', 'sum'))
    #Nombre	TotalxProducto	Tipo	Precio	Total
    vio= cup[['Nombre', 'TotalxProducto']]
    vio= vio.nlargest(16, ['TotalxProducto']).reset_index(drop=True)
    let= cup[['Nombre', 'Total']]
    let= let.nlargest(16, ['Total']).reset_index(drop=True)
    return [vio, let, cake]

    

def obtenerVentaMesero_CC_PT_Ce():
    cup= pd.merge(cait, vi, on='IdProducto')
    #precio y cantidad
    cup['Total']= cup['Precio']*cup['cantidad']
    #cup= cup.groupby('mozo', as_index = False)
    #cup= cup.groupby(['mozo', 'Tipo'],  as_index = False)
    cup= cup.groupby(['mozo', 'Tipo'],  as_index = False).agg(Productos_Vendidos=('cantidad', 'sum'), Total_vendido=('Total', 'sum'))
    #cup= cup['Plato Típico']
    valo= ['Plato Típico', 'Caja China', 'Cervezas']
    violet= cup.groupby('mozo', as_index = False).agg(Contador=('Productos_Vendidos', 'sum'), Total=('Total_vendido', 'sum'))
    #vio= cup['mozo']
    #vio= pd.DataFrame()
    for i in valo:
        cake= cup.loc[cup['Tipo']==i]
        cake.rename({'Productos_Vendidos': 'Productos_Vendidos_'+i, 'Total_vendido': 'Total_vendido_'+i}, axis=1, inplace=True)
        cake.drop('Tipo', axis=1, inplace=True)
         
        #vio= pd.concat([vio, cake], ignore_index=True)
        violet= violet.merge(cake, on='mozo')
        
    #violet.drop('Contador', axis=1, inplace=True)
        
    #mozo	Contador	Productos_Vendidos_Plato Típico	Total_vendido_Plato Típico	Productos_Vendidos_Caja China	Total_vendido_Caja China	Productos_Vendidos_Cervezas	Total_vendido_Cervezas
    vio= violet[['mozo', 'Contador','Productos_Vendidos_Plato Típico', 'Productos_Vendidos_Caja China', 'Productos_Vendidos_Cervezas']]
    let= violet[['mozo', 'Total' ,'Total_vendido_Plato Típico', 'Total_vendido_Caja China', 'Total_vendido_Cervezas']]
    #mozo	Tipo	Productos_Vendidos	Total_vendido
    #cup= cup.loc[cup['Tipo'].isin(valu)]
    
    return [vio, let, valo]
        
    #violet.drop('Contador', axis=1, inplace=True)
        

def obtenerVentas_Fecha():
    cup= tabla_ventas.groupby(['fecha', 'Nombre'],  as_index = False).agg(Productos_Vendidos=('cantidad', 'sum'))
    cup= pd.merge(cup, vi[['Nombre', 'Tipo', 'Precio']] , on='Nombre')
    cup['Total']= cup['Precio']*cup['Productos_Vendidos']
    
    cup= cup.groupby(['fecha', 'Tipo'], as_index= False).agg(Total_vendido=('Total','sum'))
    #vio= cup
    #cup= cup.nlargest(16, ['Total']).reset_index(drop=True)
    valo= ['Plato Típico', 'Caja China', 'Cervezas']
    #cake= cake.loc[cake['Tipo'].isin(valo)]
    vio= cup['Total_vendido'].sum()
    violet= cup.groupby('fecha', as_index = False).agg(Contador=('fecha', 'count'))
    
    for i in valo:
        cake= cup.loc[cup['Tipo']==i]
        cake.rename({'Total_vendido': 'Total_vendido_'+i}, axis=1, inplace=True)
        cake.drop('Tipo', axis=1, inplace=True)
        #vio= pd.concat([vio, cake], ignore_index=True)
        violet= violet.merge(cake, on='fecha')
    violet.drop('Contador', axis=1, inplace=True)
    #violet= let.nlargest(16, ['Total']).reset_index(drop=True)
    #vio= cake.groupby('fecha', as_index= False).agg(Total=('Total_vendido', 'sum'))
    #fecha	Tipo	Total_vendido
    return [ violet, vio, valo]

def obtenerVentasTotal_fecha():
    cup= tabla_ventas.groupby(['fecha', 'Nombre'],  as_index = False).agg(Productos_Vendidos=('cantidad', 'sum'))
    cup= pd.merge(cup, vi[['Nombre', 'Tipo', 'Precio']] , on='Nombre')
    cup['Total']= cup['Precio']*cup['Productos_Vendidos']
    
    cup= cup.groupby(['fecha', 'Tipo'], as_index= False).agg(Total_vendido=('Total','sum'))
    #vio= cup
    valo= list(cup.groupby(['Tipo'], as_index= False).agg(Total_vendido=('Tipo','count')).iloc[:, 0])
    #cake= cake.loc[cake['Tipo'].isin(valo)]
    vio= cup['Total_vendido'].sum()
    violet= cup.groupby('fecha', as_index = False).agg(Contador=('fecha', 'count'))
    for i in valo:
        cake= cup.loc[cup['Tipo']==i]
        cake.rename({'Total_vendido': 'Total_vendido_'+i}, axis=1, inplace=True)
        cake.drop('Tipo', axis=1, inplace=True)
        #vio= pd.concat([vio, cake], ignore_index=True)
        violet= violet.merge(cake, on='fecha', how = 'outer').fillna(0)
    violet.drop('Contador', axis=1, inplace=True)
    cup= cup.groupby('fecha', as_index= False).agg(contador=('fecha','count'))
    #vio= cake.groupby('fecha', as_index= False).agg(Total=('Total_vendido', 'sum'))
    #fecha	Tipo	Total_vendido
    #ejem= list(violet.iloc[0:1,0:-1])
    #ejem= violet.iloc[:,1:-1].to_numpy()
    #ejem = (violet.iloc[:,1:-1]).to_numpy()
    #ejem= list(violet.columns)
    return [violet, vio, valo]

def obtenerTOP_3_fecha():
    cup= tabla_ventas.groupby(['fecha', 'Nombre'],  as_index = False).agg(Productos_Vendidos=('cantidad', 'sum'))
    cup= pd.merge(cup, vi[['Nombre', 'Tipo', 'Precio']] , on='Nombre')
    cup['Total']= cup['Precio']*cup['Productos_Vendidos']
    
    cup= cup.groupby(['fecha', 'Tipo'], as_index= False).agg(Total_vendido=('Total','sum'))
    
    sweet= cup.groupby(['Tipo'], as_index= False).agg(Total_vendido=('Total_vendido','sum'))
    sweet= sweet.nlargest(3, ['Total_vendido']).reset_index(drop=True)
    #vio= cup
    #cup= cup.nlargest(4, ['Total_vendido']).reset_index(drop=True)
    #valo= list(cup.groupby(['Tipo'], as_index= False).agg(Total_vendido=('Tipo','count')).iloc[:, 0])
    valo= list(sweet.groupby(['Tipo'], as_index= False).agg(Total_vendido=('Tipo','count')).iloc[:, 0])
    #cake= cake.loc[cake['Tipo'].isin(valo)]
    vio= cup['Total_vendido'].sum()
    violet= cup.groupby('fecha', as_index = False).agg(Contador=('fecha', 'count'))
    for i in valo:
        cake= cup.loc[cup['Tipo']==i]
        cake.rename({'Total_vendido': 'Total_vendido_'+i}, axis=1, inplace=True)
        cake.drop('Tipo', axis=1, inplace=True)
        #vio= pd.concat([vio, cake], ignore_index=True)
        violet= violet.merge(cake, on='fecha')
    violet.drop('Contador', axis=1, inplace=True)
    #vio= cake.groupby('fecha', as_index= False).agg(Total=('Total_vendido', 'sum'))
    #fecha	Tipo	Total_vendido
    #ejem= list(violet.iloc[0:1,0:-1])
    #ejem= violet.iloc[:,1:-1].to_numpy()
    #ejem = (violet.iloc[:,1:-1]).to_numpy()
    #ejem= list(violet.columns)
    return [violet, vio, valo]

def obtenerHeatMap():
    cupcake= cait
    cupcake= pd.merge(cupcake, vi, on='IdProducto')
    
    cupcake= cupcake.groupby(['fecha', 'Nombre'], as_index = False).agg(Cantidad_plati=('cantidad', 'sum'))
    
    #nilfgard= conquer
    cupcake= cupcake.pivot(index= 'Nombre', columns='fecha', values= 'Cantidad_plati').fillna(0)#.reset_index()
    
    return cupcake


def obtenerHeatMap_1(): 
    #cupcake= tabla_ventas.groupby(['fecha', 'Nombre'],  as_index = False).agg(Productos_Vendidos=('cantidad', 'sum'))
    #cupcake= pd.merge(cupcake, vi[['Nombre', 'Tipo', 'Precio']] , on='Nombre')
    #cupcake['Total']= cupcake['Precio']*cupcake['Productos_Vendidos']
    
    cupcake= tabla_ventas.groupby(['fecha', 'Nombre'], as_index = False).agg(Total_vendido=('Total', 'sum'))
    #cupcake= cait
    #cupcake= pd.merge(cupcake, vi, on='IdProducto')
    
    #cupcake= cupcake.groupby(['fecha', 'Nombre'], as_index = False).agg(Total_vendido=('Total', 'sum'))
    #cupcake['Total']= cupcake['Precio']*cupcake['Cantidad_plati']
    #nilfgard= conquer
    cupcake= cupcake.pivot(index= 'Nombre', columns='fecha', values= 'Total_vendido').fillna(0)#.reset_index()
    
    return cupcake

    

def obtenerHeatMap_2(): 
    #cupcake= tabla_ventas.groupby(['fecha', 'Nombre'],  as_index = False).agg(Productos_Vendidos=('cantidad', 'sum'))
    #cupcake= pd.merge(cupcake, vi[['Nombre', 'Tipo', 'Precio']] , on='Nombre')
    #cupcake['Total']= cupcake['Precio']*cupcake['Productos_Vendidos']
    
    cupcake= tabla_ventas.groupby(['fecha', 'Tipo'], as_index = False).agg(Total_vendido=('Total', 'sum'))
    #cupcake= cait
    #cupcake= pd.merge(cupcake, vi, on='IdProducto')
    
    #cupcake= cupcake.groupby(['fecha', 'Nombre'], as_index = False).agg(Total_vendido=('Total', 'sum'))
    #cupcake['Total']= cupcake['Precio']*cupcake['Cantidad_plati']
    #nilfgard= conquer
    cupcake= cupcake.pivot(index= 'Tipo', columns='fecha', values= 'Total_vendido').fillna(0)#.reset_index()
    
    return cupcake


def obtenerHeatMap_3(): 
    #cupcake= tabla_ventas.groupby(['fecha', 'Nombre'],  as_index = False).agg(Productos_Vendidos=('cantidad', 'sum'))
    #cupcake= pd.merge(cupcake, vi[['Nombre', 'Tipo', 'Precio']] , on='Nombre')
    #cupcake['Total']= cupcake['Precio']*cupcake['Productos_Vendidos']
    
    cupcake= tabla_ventas.groupby(['fecha', 'Nombre'], as_index = False).agg(Total_vendido=('cantidad', 'sum'))
    #cupcake= cait
    #cupcake= pd.merge(cupcake, vi, on='IdProducto')
    
    #cupcake= cupcake.groupby(['fecha', 'Nombre'], as_index = False).agg(Total_vendido=('Total', 'sum'))
    #cupcake['Total']= cupcake['Precio']*cupcake['Cantidad_plati']
    #nilfgard= conquer
    cupcake= cupcake.pivot(index= 'Nombre', columns='fecha', values= 'Total_vendido').fillna(0)#.reset_index()
    
    
    return cupcake

def obtenerHeatMap_4(): 
    #cupcake= tabla_ventas.groupby(['fecha', 'Nombre'],  as_index = False).agg(Productos_Vendidos=('cantidad', 'sum'))
    #cupcake= pd.merge(cupcake, vi[['Nombre', 'Tipo', 'Precio']] , on='Nombre')
    #cupcake['Total']= cupcake['Precio']*cupcake['Productos_Vendidos']
    
    cupcake= tabla_ventas.groupby(['fecha', 'Tipo'], as_index = False).agg(Total_vendido=('cantidad', 'sum'))
    #cupcake= cait
    #cupcake= pd.merge(cupcake, vi, on='IdProducto')
    
    #cupcake= cupcake.groupby(['fecha', 'Nombre'], as_index = False).agg(Total_vendido=('Total', 'sum'))
    #cupcake['Total']= cupcake['Precio']*cupcake['Cantidad_plati']
    #nilfgard= conquer
    cupcake= cupcake.pivot(index= 'Tipo', columns='fecha', values= 'Total_vendido').fillna(0)#.reset_index()
    #cupcake= cupcake.drop('fecha', axis=1)
    
    return cupcake

def obtenerHeatMap_5():
    cuervo= pd.merge(tabla_ventas, record_clima_agrupado_horas , on='fecha')
    
    cupcake= cuervo.groupby(['fecha', 'temperatura'], as_index = False).agg(Total_vendido=('Total', 'sum'))
    violet= cuervo.groupby(['fecha', 'Condicion'], as_index = False).agg(Total_vendido=('Total', 'sum'))
    
    cupcake= cupcake.pivot(index= 'temperatura', columns='fecha', values= 'Total_vendido').fillna(0)#.reset_index()
    violet= violet.pivot(index= 'Condicion', columns='fecha', values= 'Total_vendido').fillna(0)#.reset_index()
    return [cupcake, violet]

def obtenerHeatMap_horas_productos():
    #cuervo= pd.merge(tabla_ventas, record_clima_agrupado_horas , on='fecha')
    
    cupcake= datos_hora.groupby(['fecha', 'Hora'], as_index = False).agg(Total_vendido=('cantidad', 'sum'))
    
    cupcake= cupcake.pivot(index= 'Hora', columns='fecha', values= 'Total_vendido').fillna(0)#.reset_index()
    
    sweet= datos_hora.groupby(['Tipo'], as_index= False).agg(Total_vendido=('cantidad','sum'))
    sweet= sweet.nlargest(3, ['Total_vendido']).reset_index(drop=True)
    #vio= cup
    #cup= cup.nlargest(4, ['Total_vendido']).reset_index(drop=True)
    #valo= list(cup.groupby(['Tipo'], as_index= False).agg(Total_vendido=('Tipo','count')).iloc[:, 0])
    valo= list(sweet.groupby(['Tipo'], as_index= False).agg(Total_vendido=('Tipo','count')).iloc[:, 0])
    
    violet=[]
    
    for i in valo:
        cake= datos_hora.loc[datos_hora['Tipo']==i]
        cake= cake.groupby(['fecha', 'Hora'], as_index = False).agg(Total_vendido=('cantidad', 'sum'))
        cake.rename({'Hora': i}, axis=1, inplace=True)
        cake= cake.pivot(index= i, columns='fecha', values= 'Total_vendido').fillna(0)
        violet.append(cake)
    
    
    return [cupcake, violet]


def obtener_regresion_ventas_clima(reqq):
    cup = tabla_ventas.groupby('fecha', as_index= False).agg(Total_vendido=('Total', 'sum'))
    #cup = tabla_ventas.groupby('fecha').agg(Total_vendido=('Total', 'sum'))
    
    #record_clima['normali']= record_clima.apply(lambda row: normailizar_dato_clim( maxc, minc, row['temperatura']), axis=1)
    cup= pd.merge(cup, record_clima_agrupado, on='fecha')
    cup.drop('fecha', axis=1, inplace=True)
    
    
    violet=[]
    for column in cup.iloc[:, 1:]:
        violet.append([cup[column].max(), cup[column].min()])
        #(cup[column]) 
        #cup[column]= cup.apply(lambda  row: normailizar_dato_clim(cup[column].max(), cup[column].min(), cup[column]), axis=1)
        
    for column, vio in zip(cup.iloc[:, 1:], violet):
        cup[column]= cup.apply(lambda  row: normailizar_dato_clim(vio[0], vio[1], row[column]), axis=1)
    print(violet)
    
    X_multiple = cup.iloc[:, 1:].values
    y_multiple = cup.iloc[:, 0].values 
     
    #modelo =cup.iloc[1:2, 1:].values
    
    #Y_pred_multiple.predict

    sa_do= webS_prox_saba_domi.obtener_dia_actual()
    
    sa_do['fecha']=  pd.to_datetime(sa_do.fecha, format='%Y-%m-%d')
    sa_do['fecha']= pd.to_datetime(sa_do['fecha'].dt.strftime('%Y-%m-%d'))
    #record_clima['fecha']= record_clima['fecha'].dt.date
    #record_clima['mes'] = record_clima['fecha'].dt.strftime('%b')
    #sa_do['mes'] = sa_do['fecha'].dt.month
    sa_do['fecha']= sa_do['fecha'].dt.date
    
    sa_do['temperatura']= sa_do['temperatura'].str[:2].apply(pd.to_numeric)
    sa_do['Punto de rocio']= sa_do['Punto de rocio'].str[:2].apply(pd.to_numeric)
    sa_do['Humedad']= sa_do['Humedad'].str[:2].apply(pd.to_numeric)
    sa_do['nudos de viento']= sa_do['nudos de viento'].str[:2].apply(pd.to_numeric)
    sa_do['Rafaga']= sa_do['Rafaga'].str[:2].apply(pd.to_numeric)
    
    sa_do['Presion']= sa_do['Presion'].str[:5].apply(pd.to_numeric)
    #datf['Max']= datf['Max'].str[:2].apply(pd.to_numeric)
    traducto_condicion= pd.read_csv('Condicion convertido -condicion.csv')
    traductor_veinto  = pd.read_csv('Condicion convertido -viento.csv')
    #tabla_ventas= pd.merge(cait, vi, on='IdProducto')
    sa_do= pd.merge(sa_do, traducto_condicion, on='Condicion')
    sa_do= pd.merge(sa_do, traductor_veinto, on='viento')
    
    sa_do= sa_do.groupby('fecha', as_index=False).agg(temperatura_max=('temperatura', 'max'), temperatura_min= ('temperatura', 'min'),
                                                                Punto_de_rocio_max=('Punto de rocio', 'max'), Punto_de_rocio_min=('Punto de rocio', 'min'),
                                                                Humedad_max=('Humedad', 'max'), Humedad_min=('Humedad', 'min'),
                                                                nudos_de_viento_max=('nudos de viento', 'max'), nudos_de_viento_min=('nudos de viento', 'min'),
                                                                #Rafaga_max=('Rafaga', 'max'), Rafaga_min=('Rafaga', 'min'),
                                                                Presion_max=('Presion', 'max'), Presion_min=('Presion', 'min'),
                                                                Condicion_max=('valor_Condicion', 'max'), Condicion_min=('valor_Condicion', 'min'),
                                                                #viento_max=('valor_veinto', 'max'), viento_min=('valor_veinto', 'min')
                                                                )
    
    sa_do['temperatura']= (sa_do['temperatura_max']+ sa_do['temperatura_min'])/2
    sa_do['Punto de rocio']= (sa_do['Punto_de_rocio_max']+ sa_do['Punto_de_rocio_min'])/2
    sa_do['Humedad']= (sa_do['Humedad_max']+ sa_do['Humedad_min'])/2
    sa_do['nudos de viento']= (sa_do['nudos_de_viento_max']+ sa_do['nudos_de_viento_min'])/2
    sa_do['Presion']= (sa_do['Presion_max']+ sa_do['Presion_min'])/2
    sa_do['Condicion']= (sa_do['Condicion_max']+ sa_do['Condicion_min'])/2
    
    
    sa_do.drop(['temperatura_max', 'temperatura_min'], axis = 1, inplace=True)
    sa_do.drop(['Punto_de_rocio_max', 'Punto_de_rocio_min'], axis = 1, inplace=True)
    sa_do.drop(['Humedad_max', 'Humedad_min'], axis = 1, inplace=True)
    sa_do.drop(['nudos_de_viento_max', 'nudos_de_viento_min'], axis = 1, inplace=True)
    sa_do.drop(['Presion_max', 'Presion_min'], axis = 1, inplace=True)
    sa_do.drop(['Condicion_max', 'Condicion_min'], axis = 1, inplace=True)
    
    for column, vio in zip(sa_do.iloc[:, 1:], violet):
        sa_do[column]= sa_do.apply(lambda  row: normailizar_dato_clim(vio[0], vio[1], row[column]), axis=1)
        
    
    
    alle= []
    for i in range (0, reqq):
        X_train, X_test, y_train, y_test = train_test_split(X_multiple, y_multiple, test_size=0.6)
        
        lr_multiple = linear_model.LinearRegression()
        lr_multiple.fit(X_train, y_train)
        #lr_multiple.fit()
        Y_pred_multiple = lr_multiple.predict(X_test)
        
        predi = sa_do.iloc[:,1:].values 
        
        print('DATOS DEL MODELO REGRESIÓN LINEAL MULTIPLE')
        print()
        print('Valor de las pendientes o coeficientes "a":')
        print(lr_multiple.coef_)
        print('Valor de la intersección o coeficiente "b":')
        print(lr_multiple.intercept_)
        print('Precisión del modelo:')
        print(lr_multiple.score(X_train, y_train))
        
        print(lr_multiple.predict(predi))
        alle.append([lr_multiple.coef_, lr_multiple.intercept_, lr_multiple.score(X_train, y_train), lr_multiple.predict(predi)])
    #testy= array([0.638889,0.555556,0.304,0.1,0.516129, 0.722222])
    ra=0
    cupcake=[]
    for i in alle:
        if (i[2]> ra) and i[-1][0] >0 and i[-1][1] >0:
            ra= i[2]
            cupcake= i
    
    #print(lr_multiple.predict([0.7, 0, 0.04, 0.0833333,	0.0322581, 0]))
    
    for index, feature_name in enumerate(cup.iloc[:,0:]):
        plt.figure(figsize=(5, 4))
        plt.scatter(cup.iloc[:, index], cup.iloc[:, 0])
        plt.ylabel('Venta', size=12)
        plt.xlabel(feature_name, size=12)
        plt.show()
    
    
    return cupcake
def normailizar_dato_clim(xmax, xmin, xnor):
    return (xnor- xmin)/(xmax-xmin)
    
    
'''
get1= obtenerProductos_CU_Tipo_TotalCantidad()
get2= obtenerVentaMesero_CC_PT_Ce()
get3= obtenerVentas_Fecha()
get4= obtenerVentasTotal_fecha()

get5= obtenerTOP_3_fecha()

get6= obtenerHeatMap()
get7= obtenerHeatMap_1()

get7= obtenerHeatMap_3()

get8= obtener_regresion_ventas_clima()
'''

'''  
dat1= Anabell.groupby('Nombre').agg(TotalxProducto=('cantidad', 'sum'), MyCount=('Tipo', 'count'))
dat1= pd.merge(dat1, vi[['Nombre', 'Tipo', 'Precio']] , on='Nombre')
dat1['Total']= dat1['Precio']*dat1['TotalxProducto']
#print(dat1['Tipo'])
#dat1= Anabell.groupby('Tipo').agg( MiCuenta=('tipo','count'))
#dat1= Anabell.groupby('Tipo').sum()
dat2= dat1.groupby('Tipo').agg(Total=('Total', 'sum'), MyCount=('Total', 'count'))
#dat2= pd.merge(dat2, vi[['Nombre', 'Tipo', 'Precio']], on='Nombre')

#dat3= Anabell.groupby('mozo').agg(TotalxProducto=('cantidad', 'sum'), MyCount=('Tipo', 'count'))
dat3= pd.merge(cait, vi, on='IdProducto')
#precio y cantidad
dat3['Total']= dat3['Precio']*dat3['cantidad']
#dat3= dat3.groupby(['mozo', 'Tipo']).agg(Productos_Vendidos=('cantidad', lambda x: x.sum()), Total_vendido=('Total', lambda x: x.sum()))

dat3= dat3.groupby(['mozo', 'Tipo'],  as_index = False).agg(Productos_Vendidos=('cantidad', 'sum'), Total_vendido=('Total', 'sum'))

#dat3= dat3.groupby(['mozo', 'Tipo']).agg({'cantidad': lambda x: x.sum(), 'Total': lambda x: x.sum()})

valu= ['Plato Típico', 'Caja China']

for col in dat3.columns:
    print(col)
#d1['A'].values
#dat3= dat3['Tipo'].values
dat3= dat3.loc[dat3['Tipo'].isin(valu)]


#print(dat3)
#print(dat3['Productos_Vendidos'])
#dat3= dat3.loc[dat3['TotalxProducto']> 1000000]

dat4= Anabell.groupby(['fecha', 'Nombre'],  as_index = False).agg(Productos_Vendidos=('cantidad', 'sum'))
dat4= pd.merge(dat4, vi[['Nombre', 'Tipo', 'Precio']] , on='Nombre')
dat4['Total']= dat4['Precio']*dat4['Productos_Vendidos']

dat5= dat4.groupby(['fecha', 'Tipo'], as_index = False).agg(Total_vendido=('Total', 'sum'))
dat6=dat5
#dat5= dat5.loc[dat5['Tipo'].isin(valu)]

dat6= dat5.groupby('fecha', as_index= False).agg(Total=('Total_vendido', 'sum'))

dat5= dat5.loc[dat5['Tipo'].isin(valu)]

dat7= dat6['Total'].sum()


dat8= Anabell.groupby(['fecha', 'mozo'],  as_index = False).agg(Productos_Vendidos=('cantidad', 'sum'))

dias_trabajados= dat6['fecha'].tolist()

#a = df[df['newest_date_available'] < date_before]

#print(record_clima['fecha'])
dias_trab= record_clima[record_clima['fecha'].isin(dat6['fecha'].tolist())]

dias_trab_minmax= dias_trab.groupby('fecha', as_index= False).agg(Min=('temperatura', 'min'), Max=('temperatura', 'max'))


num_mozos= cait.groupby(['fecha'],  as_index = False).agg(Num_mozos=('mozo', 'nunique'))
datf= pd.merge(dat6,dias_trab_minmax, on='fecha')
#datf= pd.merge(datf,dias_trab[['fecha','nudos de viento']], on='fecha')

datf= pd.merge(datf,num_mozos, on='fecha')
#df[["a", "b"]] = df[["a", "b"]].apply(pd.to_numeric)
#datf[['Min', 'Max']]= datf[['Min', 'Max'].str[:2]].apply(pd.to_numeric)
#datf['Min']= datf['Min'].str[:2].apply(pd.to_numeric)
#datf['Max']= datf['Max'].str[:2].apply(pd.to_numeric)
#datf['Max']= datf['Max'].str[:2].apply(pd.to_numeric)
#datf= pd.merge(datf,dias_trab[['fecha','nudos de viento']], on='fecha')
viento_minmax= dias_trab.groupby('fecha', as_index= False).agg(MinV=('nudos de viento', 'min'), MaxV=('nudos de viento', 'max'))
#viento_minmax['MinV']= viento_minmax['MinV'].str[:2].apply(pd.to_numeric)
#viento_minmax['MaxV']= viento_minmax['MaxV'].str[:2].apply(pd.to_numeric)

datf= pd.merge(datf,viento_minmax, on='fecha')


X = datf.iloc[:, 2].values.reshape(-1, 1) 
Y = datf.iloc[:, 1].values.reshape(-1, 1) 

linear_regressor = LinearRegression()  # Crear modelo
linear_regressor.fit(X, Y)  # Ejecutar la regresión lineal
Y_pred = linear_regressor.predict(X)  # Predecir

print(f'Termino independiente= {linear_regressor.intercept_[0]}')
print(f'Coeficiente lineal simple = {linear_regressor.coef_[0][0]}')
print(f'Ecuacion lineal simple= {linear_regressor.intercept_[0]} + {linear_regressor.coef_[0][0]}*x' )
print(f'R cuadrado lineal simple = {linear_regressor.score(X, Y)}')



#X_multiple = datf.iloc[:, 2:5].values 

X_multiple = datf.iloc[:, 2:7].values
 
y_multiple = datf.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(X_multiple, y_multiple, test_size=0.2)

lr_multiple = linear_model.LinearRegression()
lr_multiple.fit(X_train, y_train)
Y_pred_multiple = lr_multiple.predict(X_test)

print('DATOS DEL MODELO REGRESIÓN LINEAL MULTIPLE')
print()
print('Valor de las pendientes o coeficientes "a":')
print(lr_multiple.coef_)
print('Valor de la intersección o coeficiente "b":')
print(lr_multiple.intercept_)
print('Precisión del modelo:')
print(lr_multiple.score(X_train, y_train))


plt.figure(figsize=(5, 4))
#plt.scatter(datf.iloc[:, 2:4].values, datf.iloc[:, 1])
plt.scatter(datf.iloc[:, 1].values, datf.iloc[:, 1])
plt.ylabel('Percio', size=12)
plt.xlabel('Total', size=12)
plt.show()

#>> widened = long.pivot(index='year', columns='party', values='seats').reset_index()

#conquer= datf.pivot(index= 'fecha', columns='Num_mozos', values= 'Total')#.reset_index()

#conquer= pd.merge(cait, dias_trab.groupby(['fecha']) , on='fecha')

conquer= cait
#conquer= pd.merge(cait, dias_trab_minmax , on='fecha')
#conquer['Min']= conquer['Min'].str[:2].apply(pd.to_numeric)
#conquer['Max']= conquer['Max'].str[:2].apply(pd.to_numeric)
conquer= pd.merge(conquer, vi, on='IdProducto')

conquer= conquer.groupby(['fecha', 'Nombre'], as_index = False).agg(Cantidad_plati=('Nombre', 'count'))

nilfgard= conquer
conquer= conquer.pivot(index= 'Nombre', columns='fecha', values= 'Cantidad_plati').fillna(0)#.reset_index()


sns.heatmap(conquer, cmap="viridis",  # Choose a squential colormap
                #annot=jb_labels, # Label the maximum value
                annot_kws={'fontsize':11},  # Reduce size of label to fit
                fmt='',          # Interpret labels as strings
                #square=True,     # Force square cells
                vmax=40,         # Ensure same 
                vmin=0,          # color scale
                linewidth=0.01,  # Add gridlines
                linecolor="#222",# Adjust gridline color
                #ax=ax[i],        # Arrange in subplot
               )
plt.show()

###########################

caitlyn= Anabell.groupby(['fecha', 'Tipo'], as_index = False).agg(Total_vendido_caja=('Tipo', 'count'))

tipos_platillo= ['Caja China']

caitlyn= caitlyn.loc[caitlyn['Tipo'].isin(tipos_platillo)]

caitlyn= caitlyn.drop(['Tipo'], axis=1)

fechas= ['2020-11-29']
#caitlyn= caitlyn.loc[caitlyn['fecha'].ne(fechas)]

#violet= datf

violet= violet= pd.merge(caitlyn, datf.drop(['Total'], axis=1), on='fecha')

#violet= violet.drop(7)

#violet= violet.drop(1)

###################
print('Caja china')
X_multiple = violet.iloc[:, 2:7].values
 
y_multiple = violet.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(X_multiple, y_multiple, test_size=0.2)

lr_multiple = linear_model.LinearRegression()
lr_multiple.fit(X_train, y_train)
Y_pred_multiple = lr_multiple.predict(X_test)

print('Valor de las pendientes o coeficientes "a":')
print(lr_multiple.coef_)
print('Valor de la intersección o coeficiente "b":')
print(lr_multiple.intercept_)
print('Precisión del modelo:')
print(lr_multiple.score(X_train, y_train))

################################

caitlyn= Anabell.groupby(['fecha', 'Tipo'], as_index = False).agg(Total_vendido_caja=('Tipo', 'count'))

tipos_platillo= ['Cervezas']

caitlyn= caitlyn.loc[caitlyn['Tipo'].isin(tipos_platillo)]

caitlyn= caitlyn.drop(['Tipo'], axis=1)

fechas= ['2020-11-29']
#caitlyn= caitlyn.loc[caitlyn['fecha'].ne(fechas)]

#violet= datf

violet= violet= pd.merge(caitlyn, datf.drop(['Total'], axis=1), on='fecha')

#violet= violet.drop(7)

#violet= violet.drop(1)

###################
print('Cervezas')
X_multiple = violet.iloc[:, 2:7].values
 
y_multiple = violet.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(X_multiple, y_multiple, test_size=0.2)

lr_multiple = linear_model.LinearRegression()
lr_multiple.fit(X_train, y_train)
Y_pred_multiple = lr_multiple.predict(X_test)

print('Valor de las pendientes o coeficientes "a":')
print(lr_multiple.coef_)
print('Valor de la intersección o coeficiente "b":')
print(lr_multiple.intercept_)
print('Precisión del modelo:')
print(lr_multiple.score(X_train, y_train))

#########################################################
caitlyn= Anabell.groupby(['fecha', 'Tipo'], as_index = False).agg(Total_vendido_caja=('Tipo', 'count'))

tipos_platillo= ['Plato Típico']

caitlyn= caitlyn.loc[caitlyn['Tipo'].isin(tipos_platillo)]

caitlyn= caitlyn.drop(['Tipo'], axis=1)

fechas= ['2020-11-29']
#caitlyn= caitlyn.loc[caitlyn['fecha'].ne(fechas)]

#violet= datf

violet= violet= pd.merge(caitlyn, datf.drop(['Total'], axis=1), on='fecha')

#violet= violet.drop(7)

#violet= violet.drop(1)

###################
print('Plato Tipico')
X_multiple = violet.iloc[:, 2:7].values
 
y_multiple = violet.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(X_multiple, y_multiple, test_size=0.2)

lr_multiple = linear_model.LinearRegression()
lr_multiple.fit(X_train, y_train)
Y_pred_multiple = lr_multiple.predict(X_test)

print('Valor de las pendientes o coeficientes "a":')
print(lr_multiple.coef_)
print('Valor de la intersección o coeficiente "b":')
print(lr_multiple.intercept_)
print('Precisión del modelo:')
print(lr_multiple.score(X_train, y_train))


get1= obtenerProductos_CU_Tipo_TotalCantidad()
get2= obtenerVentaMesero_CC_PT_Ce()
get3= obtenerVentas_Fecha()
get4= obtenerVentasTotal_fecha()

get5= obtenerTOP_3_fecha()

get6= obtenerHeatMap()
get7= obtenerHeatMap_1()

get7= obtenerHeatMap_3()

df = pd.DataFrame({'x': [1, 2, 3, 4],
                   'y1': [10, 20, 10, 30],
                   'y2': [20, 25, 15, 25],
                   'y3': [5, 10, 5, 20]})





'''




