#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 13:13:37 2019

@author: robot
"""


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from Package.otros import controler_temps


path = '/home/robot/Desktop/Package'


"""
                Histogramas para analizar cuando se registran los accesos
"""

@controler_temps()
def histFranjas(logs, m=0):
    """La función hace un histograma de los numeros de acceso en función de franjas de tiempo.
        """
    
    inter = ['0-7','7-9','9-11','11-13','13-15','15-17','17-19','19-21','21-24']
    
    dfFranja = pd.DataFrame({'Value': logs.groupby('Franja').size(), 'inter': inter})
    
    dfFranja = dfFranja.set_index('inter')
    
    # Histograma de accesos por franja
    fig, ax = plt.subplots()
    dfFranja['Value'].plot(kind='bar')
    fig.suptitle('Accesos por franja', fontsize=16)
    plt.subplots_adjust(top=0.88)
    fig.savefig('Hist_Franjas{0}.png' .format(m), dpi=fig.dpi, bbox_inches='tight')
    
@controler_temps()
def histDayofweek(logs, m=0):
    """Histograma de los numeros de acceso en función del día de la semana.
        """
    
    sem = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
    if len(logs['Dayofweek'].unique().tolist()) == 7:
        dfSem = pd.DataFrame({'sem': sem, 'Value': logs.groupby('Dayofweek').size()})
        dfSem = dfSem.set_index(dfSem['sem'])
    else:
        dfSem = pd.DataFrame({'Value':logs.groupby('Dayofweek').size()})
    # Histograma de los accesos por día
    fig, ax = plt.subplots()
    dfSem['Value'].plot(kind = 'bar')
    fig.suptitle('Accesos por dia', fontsize=16)
    plt.subplots_adjust(top=0.88)
    fig.savefig('Hist_Dayofweek{0}.png' .format(m), dpi=fig.dpi, bbox_inches='tight')


"""
            Histogramas para analizar las actividades que registran los accesos
"""

@controler_temps()
def histComp(logs, m=0):
    """La función hace un histograma de los accesos en funcion de los componentes.
        La función devuelve mayorComp y mayorComp2.
        porcComp: porciento de accesos que registraron los 10 principales componentes
        mayorComp: numero de componente(s) que registraron más de un 50% de los accesos
        mayorComp2: numero de componente(s) que registraron más de un 90% de los accesos"""
    
    dfComp = pd.DataFrame({'Value':logs.groupby('Component').size()})  
    
    # Para ordenar el dataframe
    dfCompSort=dfComp['Value'].sort_values(ascending=False)
    
    # Cuanto es el porcentaje
    porcComp=np.sum(dfCompSort[:10])/np.sum(dfCompSort)
    
    # Para encontrar la importancia de los eventos
    porcComp2 = 0
    i = 0
    while porcComp2 < 0.5:
        i += 1
        porcComp2 = np.sum(dfCompSort[:i])/np.sum(dfCompSort)
    mayorComp = i
    
    porcComp3 = 0
    i = 0
    while porcComp3 < 0.9:
        i += 1
        porcComp3 = np.sum(dfCompSort[:i])/np.sum(dfCompSort)
    mayorComp2 = i
    
    # Para guardar solo los 10 principales componentes
    dfCompMax = pd.DataFrame(dfCompSort[:10], columns = ['Value'])
    
    # Histograma de los principales componentes
    fig, ax = plt.subplots()
    dfCompMax['Value'].plot(kind='bar',facecolor='#AA0000') # Para hacer el histograma
    fig.suptitle('Accesos para los 10 principales componentes', fontsize=16)    # Para poner un titulo
    plt.subplots_adjust(top=0.88)
    fig.savefig('Hist_10_principales_componentes{0}.png' .format(m), dpi=fig.dpi, bbox_inches='tight')  # Para guardar el histograma
    
    return(mayorComp, mayorComp2)
    
@controler_temps()
def histEvent(logs, m=0):
    """La función hace un histograma de los numeros de acceso en funcion de los eventos.
        La función devuelve porcEvent, mayorEvent y mayorEvent2.
        porcEvent: porciento de accesos que registraron los 10 principales eventos
        mayorEvent: numero de evento(s) que registraron más de un 50% de los accesos
        mayorEvent2: numero de evento(s) que registraron más de un 90% de los accesos"""
    
    dfEvent = pd.DataFrame({'Value': logs.groupby('Event context').size()})

    # Para ordenar el dataframe
    dfEventSort=dfEvent['Value'].sort_values(ascending=False)
    
    # Cuanto es el porcentaje
    porcEvent=np.sum(dfEventSort[:10])/np.sum(dfEventSort)
    
    # Para encontrar la importancia de los eventos
    porcEvent2 = 0
    i = 0
    while porcEvent2 < 0.5:
        i += 1
        porcEvent2 = np.sum(dfEventSort[:i])/np.sum(dfEventSort)
    mayorEvent = i
    
    porcEvent3 = 0
    i = 0
    while porcEvent3 < 0.9:
        i += 1
        porcEvent3 = np.sum(dfEventSort[:i])/np.sum(dfEventSort)
    mayorEvent2 = i
    
    # Para guardar solo los 10 principales eventos
    dfEventMax = pd.DataFrame(dfEventSort[:10])
    
    # Histograma de los principales eventos
    fig, ax = plt.subplots()
    dfEventMax['Value'].plot(kind='bar',facecolor='#AA0000')
    fig.suptitle('Accesos para los 10 principales eventos', fontsize=16)
    plt.subplots_adjust(top=0.88)
    fig.savefig('Hist_10_principales_eventos{0}.png' .format(m), dpi=fig.dpi, bbox_inches='tight')
    
    return(porcEvent, mayorEvent, mayorEvent2)
    
@controler_temps()
def histStud(logs, tabUsername=[], m=0):
    """La función hace un histograma de los numeros de accesos en función de los estudiantes.
        """
        
    if tabUsername == []:
        tabUsername = logs['User full name'].unique().tolist()
        
    dfStud = pd.DataFrame({'Value': logs.groupby('User full name').size(),
                           'Nombres': tabUsername})
    
    dfStud = dfStud.set_index('Nombres')
    
    # Para ordenar el dataframe
    dfStudSort=dfStud['Value'].sort_values(ascending=False)
    
    # Para poner un nombre a la columna
    dfStud2=pd.DataFrame(dfStudSort, columns = ['Value'])
    
    #Histograma de los accesos por estudiante
    fig, ax = plt.subplots(figsize=(20,10))
    dfStud2['Value'].plot(kind='bar')
    fig.suptitle('Accesos por estudiante', fontsize=16)
    plt.subplots_adjust(top=0.88)
    fig.savefig('Hist_Students{0}.png' .format(m), dpi=fig.dpi, bbox_inches='tight')
    
@controler_temps()
def histDistStud(logs, m=0):
    """La función hace una histograma de la distribución de los accesos por estudiante. 
        """
    
    dfStud = pd.DataFrame({'Value': logs.groupby('User full name').size()})
    
    # Distribución de los numeros de accesos por estudiante
    fig, ax = plt.subplots()
    fig.suptitle('Distribucion de los accesos por estudiante', fontsize=16)
    dfStud['Value'].hist(bins=10)
    plt.subplots_adjust(top=0.88)
    fig.savefig('Hist_Distribucion{0}.png' .format(m), dpi=fig.dpi, bbox_inches='tight')
    
@controler_temps()
def histCourse(logs, cursor,  m=0):
    """La función hace un histograma de los numeros de accesos en función de los cursos para los 10 principales.
        """
    
    dfCourse = pd.DataFrame({'Value': logs.groupby('courseid').size()})
    
    # Para ordenar el dataframe
    dfCourseSort=dfCourse['Value'].sort_values(ascending=False)
    
    # Para guardar solo los 10 principales cursos
    dfCourseMax = pd.DataFrame(dfCourseSort[:10])
    
    # Para cambiar los ids de los cursos por su nombre
    tabCourse = []
    for i in dfCourseMax.index.unique().tolist(): 
        cursor.execute("""SELECT DISTINCT fullname 
                           FROM avatapre.moodle_course
                           INNER JOIN avatapre.moodle_logstore_standard_log 
                           ON avatapre.moodle_course.id = avatapre.moodle_logstore_standard_log.courseid
                           WHERE avatapre.moodle_logstore_standard_log.courseid = {};""".format(i))
        rows = cursor.fetchall()
        tabCourse.append(rows[0][0])
    dfTab = pd.DataFrame(tabCourse, columns = ['name'])
    dfTab['name'] = dfTab['name'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfCourseMax = dfCourseMax.set_index(dfTab['name'])
    
    # Histograma de los accesos por curso
    fig, ax = plt.subplots()
    dfCourseMax['Value'].plot(kind='bar',facecolor='#AA0000')
    fig.suptitle('Accesos para los 10 principales cursos', fontsize=16)
    plt.subplots_adjust(top=0.88)
    fig.savefig('Hist_10_principales_cursos{0}.png' .format(m), dpi=fig.dpi, bbox_inches='tight')
    
@controler_temps()
def histDistCourse(logs, m=0):
    """La funcion hace el histograma de la distribución de accesos por curso.
        """
    
    dfCourse = pd.DataFrame({'Value': logs.groupby('courseid').size()})
    
    # Histograma de la distribución de accesos por curso
    fig, ax = plt.subplots()
    fig.suptitle('Distribucion de accesos a los cursos', fontsize=16)
    dfCourse['Value'].hist(bins=10)
    plt.subplots_adjust(top=0.88)
    fig.savefig('Hist_Distribucion_Cursos{0}.png' .format(m), dpi=fig.dpi, bbox_inches='tight')


"""
                Bar graphicos para analizar cuando los accesos se registran  
"""

@controler_temps()
def histNocheDia(logs, m=0):
    """Bar graphico de las medias de numeros de accesos durante el dia y la noche.
        La función devuelve porcDH y porcNH.
        porcDH: porciento de accesos por hora durante el día
        porcNH: porciento de accesos por hora durante la noche"""
    
    dfDiurNoct = pd.DataFrame({'Value': logs.groupby(['DiurnoNoct']).size()})
    
    tpN = dfDiurNoct.loc['N'][0] # Numero total de accesos durante la noche
    tpD = dfDiurNoct.loc['D'][0] # Numero total de accesos durante el día
    
    tot = dfDiurNoct.sum()[0]    # Numero total de accesos
    
    # Porcientos de accesos durante el día y la noche
    porcN = tpN/tot
    porcD = tpD/tot
    
    # Values por hora
    tpNH = (tpN/6)*24
    tpDH = (tpD/18)*24
    totH = tpNH+tpDH
    
    # Porcientos por hora
    porcNH = tpNH/totH
    porcDH = tpDH/totH
    
    # Medias por hora
    MN = tpN/6
    MD = tpD/18
    
    l = [MD,MN]
    
    # Bar graphico de las medias de logs durante la noche y el día
    fig, ax = plt.subplots()
    plt.bar(range(2),l)
    fig.suptitle('Media de los numeros de acceso por hora durante el dia y la noche', fontsize=16)
    plt.subplots_adjust(top=0.88)
    fig.savefig('Hist_Noche-Dia{0}.png' .format(m), dpi=fig.dpi, bbox_inches='tight')
    
    return porcDH, porcNH

@controler_temps()
def histSemWE(logs, diasDeClase=[[]], m=0, m2=0):
    """La función hace un histograma de las medias de accesos durante la semana y el weekend.
        La función devuelve difClase, porcSD y porcWD.
        difClase: diferencia de accesos entre los días de clase y los otros
        porcSD: porciento de accesos por día durante la semana
        porcWD: porciento de accesos por día durante el weekend"""
    
    nbDia = np.zeros(7)
    tot = 0
    totS = 0
    totW = 0
    
    i = 0
    for i in range(7):
        counter = logs[logs['Dayofweek']==i]
        nbDia[i] = counter['User full name'].count()
        if len(diasDeClase[m])==2:
            if ((i!=diasDeClase[m][0]) and (i!=diasDeClase[m][1])):
                tot += nbDia[i]
                if i<5:
                    totS += nbDia[i]    # Ls = numero de logs mientras la semana
                else:
                    totW += nbDia[i]    # Lf = numero de logs mientras el fin de semana
        if len(diasDeClase[m])==1:
            if i!=diasDeClase[m][0]:
                tot += nbDia[i]
                if i<5:
                    totS += nbDia[i]    # Ls
                else:
                    totW += nbDia[i]    # Lf
        if len(diasDeClase[m])==0:
            tot += nbDia[i]
            if i<5:
                totS += nbDia[i]    # Ls
            else:
                totW += nbDia[i]    # Lf
    
    # Para conocer la diferencia de accesos durante los dias de curso y los otros
    logsClase = 0
    for i in range(len(diasDeClase[m])):      
        logsClase += nbDia[diasDeClase[m][i]]
    
    if len(diasDeClase[m])!=0:
        mediaClase = logsClase/len(diasDeClase[m])
        mediaFuera = tot/(7-len(diasDeClase[m]))
        difClase = mediaClase/mediaFuera
    else:
        difClase = 0
      
    # Porcientos de accesos durante la semana y el weekend
    if m!=0:
        porcS = totS/tot
        porcW = totW/tot
    
    # Valores por dia
    totSD = (totS/3)*5
    totWD = (totW/2)*5
    totD = totSD+totWD
    
    # Porcientos por día
    porcSD = totSD/totD
    porcWD = totWD/totD
    
    # Medias por dia
    MS = totS/(5-len(diasDeClase[m]))
    MW = totW/2
    
    t = [MS,MW]
    
    #Bar graphico de las medias de logs durante la semana y el weekend
    fig, ax = plt.subplots()
    plt.bar(range(2),t)
    fig.suptitle('Media de los logs por día durante la semana y el fin de semana', fontsize=16)
    plt.subplots_adjust(top=0.88)
    fig.savefig('Hist_Semana-Weekend{0}.png' .format(m2), dpi=fig.dpi, bbox_inches='tight')
    
    return difClase, porcSD, porcWD
    
    