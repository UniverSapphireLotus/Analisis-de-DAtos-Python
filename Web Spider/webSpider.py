# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 05:27:17 2021

@author: UniverSapphireLotus
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import time

from pandas.io.json import json_normalize

#url= 'https://www.wunderground.com/history/daily/pe/ayacucho/SPHO/date/2021-10-21'
def obtenerFechas(dates):
    
    #vi= pd.DataFrame(columns=['hora', 'temperatura', 'Punto de rocio','Humedad', 'viento', 'nudos de viento', 'Rafaga', 'Presion', 'Precipitacion', 'Condicion'])
    vi = pd.DataFrame()


    for dia in dates:
        print(dia)
        url= 'https://www.wunderground.com/history/daily/pe/ayacucho/SPHO/date/'+dia
        
        driver = webdriver.Firefox()
        driver.implicitly_wait(30)
        time.sleep(2)
        driver.get(url)
        time.sleep(2)
        
        error=[]
        
        #item = driver.find_element_by_xpath('//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table')
        try:
            table = driver.find_element_by_xpath('//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table/tbody')
            
            #soup = BeautifulSoup(driver.page_source)
            #soup_table = soup.find_all('//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table/tbody')
            #print(str(table))
            #print(soup_table)
            #time.sleep(2)
            #req= requests.get(call)
            
            r=0
            temporal_dia=[]
            for row in table.find_elements_by_xpath('./tr'):
                #print(row)
                r+=1
                #print(r)
                temporal_dia.append([])
                c=0
                for i in row.find_elements_by_xpath('./td'):
                    c+=1
                    #print(c)
                    if c==1 or c==5 or c==10:
                        ga= i.find_elements_by_xpath('./span')
                        temporal_dia[r-1].append(ga[0].text)
                        #print(ga[0].text)
                    else:
                        ga= i.find_elements_by_xpath('./lib-display-unit')
                        temporal_dia[-1].append(ga[0].text)
                        #print(ga[0].text)
                        
            #for raa in temporal_dia:
            #    print(raa)
                
            driver.quit()
            
            
            dataf= pd.DataFrame(temporal_dia, columns=['hora', 'temperatura', 'Punto de rocio','Humedad', 'viento', 'nudos de viento', 'Rafaga', 'Presion', 'Precipitacion', 'Condicion'])
            dataf.loc[:, 'fecha'] = dia
        except:
            error.append(dia)
            
        print(error)
        #vi.append(dataf, ignore_index=True)
        #print(dataf)
        #print('/////////////////////////////////////////////////')
        #print(vi)
        vi= pd.concat([vi, dataf], ignore_index=True)
        
        #vi.join(dataf, on='mukey', how='left')
        #vi.append(dataf, ignore_index=True)
        #vi=dataf
        #dat= pd.concat([dat,dataf])
    return vi
        


yy=2021

# display the calendar
#sun=pd.date_range(start=str(yy), end=str(yy+1), freq='W-SUN').strftime('%m/%d/%Y').tolist()
#sun=pd.date_range(start=str(yy), end=str(yy+1), freq='W-SUN').strftime('%Y-%m-%d').tolist()

sat=pd.date_range(start=str(yy), end=str(yy+1), freq='D').strftime('%Y-%m-%d').tolist()

#sat=['2021-10-16','2021-10-16']

clima=obtenerFechas(sat)



print(clima)

clima.to_csv('record_clima_2021.csv')




    


