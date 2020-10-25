#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:21:34 2019

@author: robot
"""


import pandas as pd

import matplotlib.pyplot as plt

import time

from functools import wraps

def controler_temps():
    """El decorador controla el tiempo que toma una función.
        """
    
    def decorateur(fonction_a_executer):
        
        @wraps(fonction_a_executer)
        def fonction_modifiee(*parametres_non_nommes, **parametres_nommes):
            
            tps_avant = time.time() 
            valeur_renvoyee = fonction_a_executer(*parametres_non_nommes, **parametres_nommes) 
            tps_apres = time.time()
            tps_execution = tps_apres - tps_avant
            print("La funcion {0} tomó {1} segundas.".format( \
                  fonction_a_executer, round(tps_execution, 3)))
            return valeur_renvoyee
        return fonction_modifiee
    return decorateur

@controler_temps()
def variablesNlVm(logs, m=0):
    """ La función calcula y devuelve las variables Vm y Nl.
        Vm = numero de visitas al curso
        Nl = numero de logs del estudiante"""
        
    Nl = [[],[]]
    
    dfUser = pd.DataFrame(logs.groupby('User full name')['Dayofweek'].count())
    Vm = dfUser['Dayofweek'].sum()
    Nl[0]=dfUser.index
    dfUser = dfUser.set_index('Dayofweek')
    Nl[1]=dfUser.index    
    
    return(Nl[0], Nl[1], Vm)
    
@controler_temps()
def boxplotStud(logs, m=0):
    """La función hace una boxplot de los accesos de los estudiantes.
        """
    
    dfStud = pd.DataFrame(logs.groupby('User full name').size())
    
    #Boxplot de los logs de los estudiantes
    fig, ax = plt.subplots()
    plt.boxplot([dfStud[x] for x in dfStud.keys()], labels = dfStud.keys())
    fig.suptitle('Boxplot de los accesos de los estudiantes', fontsize=16)
    plt.subplots_adjust(top=0.88)
    fig.savefig('Boxplot_students{0}.png' .format(m), dpi=fig.dpi, bbox_inches='tight')
