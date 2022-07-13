# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 09:53:28 2022

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
    vi= pd.DataFrame()
    

    for juicio in dates:
        print(juicio)
        url= 'https://www.wunderground.com/history/daily/pe/ayacucho/SPHO/date/'+juicio
        
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
            faraon=[]
            for row in table.find_elements_by_xpath('./tr'):
                #print(row)
                r+=1
                #print(r)
                faraon.append([])
                c=0
                for i in row.find_elements_by_xpath('./td'):
                    c+=1
                    #print(c)
                    if c==1 or c==5 or c==10:
                        ga= i.find_elements_by_xpath('./span')
                        faraon[r-1].append(ga[0].text)
                        #print(ga[0].text)
                    else:
                        ga= i.find_elements_by_xpath('./lib-display-unit')
                        faraon[-1].append(ga[0].text)
                        #print(ga[0].text)
                        
            #for raa in faraon:
            #    print(raa)
                
            driver.quit()
            
            
            dataf= pd.DataFrame(faraon, columns=['hora', 'temperatura', 'Punto de rocio','Humedad', 'viento', 'nudos de viento', 'Rafaga', 'Presion', 'Precipitacion', 'Condicion'])
            dataf.loc[:, 'fecha'] = juicio
            vi= pd.concat([vi, dataf], ignore_index=True)
        except:
            error.append(juicio)
            
        print(error)
        #vi.append(dataf, ignore_index=True)
        #print(dataf)
        #print('/////////////////////////////////////////////////')
        #print(vi)
        
        
        #vi.join(dataf, on='mukey', how='left')
        #vi.append(dataf, ignore_index=True)
        #vi=dataf
        #dat= pd.concat([dat,dataf])
    return vi
        

import datetime
yy=2021

# display the calendar
#sun=pd.date_range(start=str(yy), end=str(yy+1), freq='W-SUN').strftime('%m/%d/%Y').tolist()
#sun=pd.date_range(start=str(yy), end=str(yy+1), freq='W-SUN').strftime('%Y-%m-%d').tolist()
today= pd.to_datetime("today")
today= pd.Timestamp(today).date()

tod1= datetime.timedelta(today.weekday()-6)+ today
tod2= datetime.timedelta(today.weekday()-5)+ today


tod1= tod1.strftime(('%Y-%m-%d'))
tod2= tod2.strftime(('%Y-%m-%d'))

print(tod1, tod2)
print(today.weekday())
#sat=pd.date_range(start=str(yy), end=str(yy+1), freq='D').strftime('%Y-%m-%d').tolist()

sat=[tod1, tod2]

clima=obtenerFechas(sat)



print(clima)

#vi.to_csv('record_clima_2021.csv')




    


