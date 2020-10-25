# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 09:45:41 2019

@author: olmer.garciab
"""



from Package.hist import histFranjas, histDayofweek, histComp, histEvent, histNocheDia, histSemWE, histStud, histDistStud
from Package.heatmap import heatmapDayofweekStud, heatmapFranjasDayofweek, heatmapFranjasStud
from Package.otros import boxplotStud
from Package.informe import informeCurso

import datetime

import numpy as np
import pandas as pd

import os 


path = '/home/robot/Desktop/'

if not os.path.exists('/home/robot/Desktop/Test'):
    os.makedirs('/home/robot/Desktop/Test')
os.chdir('/home/robot/Desktop/Test')

logs = pd.read_csv('/home/robot/Desktop/estudiantes_antioquia_474.csv',encoding='utf8')


    #Remove special characters
#logs['User full name'] = logs['Nombre completo del usuario'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
#logs['Event context'] = logs['Nombre evento'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
#logs['Time2'] = pd.to_datetime(logs.Hora, format='%d/%m/%Y %H:%M')  #Convert date to special datetime format
#logs['Fecha'] = logs.Time2.dt.date  
#logs['Dayofweek'] = logs.Time2.dt.dayofweek
#logs['DiurnoNoct'] = np.where(logs.Time2.dt.time>datetime.time(18),"N","D") #D=Diurno, N=Nocturno
#logs['Weekend'] = np.where(logs['Dayofweek']>4,"S","N") #S=Si, N=No
#logs['Component'] = logs['Componente'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
#
#logs.drop(['Hora','Nombre completo del usuario','Usuario afectado','Nombre evento','Componente','Contexto del evento','Origen'],axis=1,inplace=True)
#
#logs['Franja']=np.zeros(len(logs))
#logs['Franja'] = np.where(logs.Time2.dt.time>datetime.time(0), 0, logs['Franja'])
#logs['Franja'] = np.where(logs.Time2.dt.time>datetime.time(7), 1, logs['Franja'])
#logs['Franja'] = np.where(logs.Time2.dt.time>datetime.time(9), 2, logs['Franja'])
#logs['Franja'] = np.where(logs.Time2.dt.time>datetime.time(11), 3, logs['Franja'])
#logs['Franja'] = np.where(logs.Time2.dt.time>datetime.time(13), 4, logs['Franja'])
#logs['Franja'] = np.where(logs.Time2.dt.time>datetime.time(15), 5, logs['Franja'])
#logs['Franja'] = np.where(logs.Time2.dt.time>datetime.time(17), 6, logs['Franja'])
#logs['Franja'] = np.where(logs.Time2.dt.time>datetime.time(19), 7, logs['Franja'])
#logs['Franja'] = np.where(logs.Time2.dt.time>datetime.time(21), 8, logs['Franja'])

        #Remove special characters
logs['User full name'] = logs['userid']
logs['Event context'] = logs['eventname'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        
    #Covert timestamp to datetim
tabTime=[]
i=0
for t in range(len(logs['timecreated'])):
    tabTime.append(t)
    tabTime[i]=datetime.datetime.fromtimestamp(logs['timecreated'][i])
    i+=1
        
logs['Time2'] = pd.to_datetime(tabTime, format='%d/%m/%Y %H:%M')

#logs['Time2'] = pd.to_datetime(logs['timecreated'], unit = 's')  #Convert date to special datetime format
logs['Fecha'] = logs.Time2.dt.date  
logs['Dayofweek'] = logs.Time2.dt.dayofweek
logs['Hora']=logs['Time2'].dt.time
logs['DiurnoNoct'] = np.where(logs.Time2.dt.time>datetime.time(18, 0),"N","D") #D=Diurno, N=Nocturno
logs['Weekend'] = np.where(logs['Dayofweek']>4,"S","N") #S=Si, N=No
logs['Component'] = logs['component'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8') 
    
logs['Franja']=np.zeros(len(logs))
logs['Franja'] = np.where(logs['Hora']>datetime.time(0), 1, logs['Franja'])
logs['Franja'] = np.where(logs['Hora']>datetime.time(7), 2, logs['Franja'])
logs['Franja'] = np.where(logs['Hora']>datetime.time(9), 3, logs['Franja'])
logs['Franja'] = np.where(logs['Hora']>datetime.time(11), 4, logs['Franja'])
logs['Franja'] = np.where(logs['Hora']>datetime.time(13), 5, logs['Franja'])
logs['Franja'] = np.where(logs['Hora']>datetime.time(15), 6, logs['Franja'])
logs['Franja'] = np.where(logs['Hora']>datetime.time(17), 7, logs['Franja'])
logs['Franja'] = np.where(logs['Hora']>datetime.time(19), 8, logs['Franja'])
logs['Franja'] = np.where(logs['Hora']>datetime.time(21), 9, logs['Franja'])

heatmapDayofweekStud(logs)
mayorComp, mayorComp2 = histComp(logs)
porcEvent, mayorEvent, mayorEvent2 = histEvent(logs)
histDayofweek(logs)
difClase, porcSD, porcWD = histSemWE(logs)
porcDH, porcNH = histNocheDia(logs)
histStud(logs)
histDistStud(logs)
boxplotStud(logs)
histFranjas(logs)
heatmapFranjasDayofweek(logs)
heatmapFranjasStud(logs) 
informeCurso(logs, mayorEvent, mayorEvent2, mayorComp, mayorComp2, porcSD, porcWD, porcDH, porcNH, diasDeClase=[], m=0, nameCurso=0, difClase=0)





