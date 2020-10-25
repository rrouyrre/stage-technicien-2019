#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:06:07 2019

@author: robot
"""


import numpy.random as rs

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from Package.otros import controler_temps


@controler_temps()
def heatmapDayofweekStud(logs, m=0):
    """La función hace una mapa de calor de los numeros de acceso por estudiante en función del día de la semana.
        """
    
    dfUser = pd.DataFrame(data=rs.normal(size=(7, len(logs['User full name'].unique().tolist()))),
                     columns=logs['User full name'].unique().tolist())  
    
    # Para sacar los datos
    for name in logs['User full name'].unique().tolist():
        l = (logs['User full name']==name)
        l2 = logs[l]
        dfUser[name] = np.histogram(l2['Dayofweek'],bins=7)[0]
    
    # Mapa de calor de los accesos en función del día y de los estudiantes
    plt.figure()
    fig, ax = plt.subplots(figsize=(11, 9))
    fig.suptitle('Accesos por día en función de los estudiantes', fontsize=16) # Para poner un título
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(dfUser, cmap=cmap, vmax=1000, center=0,
                square=True, linewidths=.5)
    plt.subplots_adjust(top=0.88)
    fig.savefig('Heatmap_Dayofweek{0}.png' .format(m), dpi=fig.dpi, bbox_inches='tight')    # Para guardar la mapa de calor
    
@controler_temps()    
def heatmapFranjasDayofweek(logs, vmax=1000, m=0):
    """La función hace una mapa de calor de los numeros de acceso por día en función de las franjas de tiempo.
        """
    
    dfFranja = pd.DataFrame(data=rs.normal(size=(9, 7)),
                 columns=[0, 1, 2, 3, 4, 5, 6])
    
    # Para sacar los datos
    for fra in logs['Dayofweek'].unique().tolist():
        l = (logs['Dayofweek']==fra)
        l2 = logs[l]
        dfFranja[fra] = np.histogram(l2['Franja'],bins=9)[0]
        
    # Mapa de calor de los accesos en función del día y de la franja de tiempo
    plt.figure()
    fig, ax = plt.subplots(figsize=(11, 9))
    fig.suptitle('Accesos por día en funcion de las franjas de tiempo', fontsize=16)
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(dfFranja, cmap=cmap, vmax=vmax, center=0,
                square=True, linewidths=.5)
    fig.savefig('Heatmap_Franjas{0}.png' .format(m), dpi=fig.dpi, bbox_inches='tight')
    
@controler_temps()
def heatmapFranjasStud(logs, m=0):
    """La función hace una mapa de calor de los numeros de acceso por franja en función de los estudiantes.
        """
    
    dfFranja2 = pd.DataFrame(data=rs.normal(size=(10, len(logs['User full name'].unique().tolist()))),
                             columns=logs['User full name'].unique().tolist())  
        
    # Para sacar los datos
    for name in logs['User full name'].unique().tolist():
        l = (logs['User full name']==name)
        l2 = logs[l]
        dfFranja2[name] = np.histogram(l2['Franja'],bins=10)[0]
        
    # Mapa de calor de los accesos en función de las franjas y de los estudiantes
    plt.figure()
    fig, ax = plt.subplots(figsize=(11, 9))
    fig.suptitle('Accesos por franja en función de los estudiantes', fontsize=16)
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(dfFranja2, cmap=cmap, vmax=500, center=0,
                square=True, linewidths=.5)
    plt.subplots_adjust(top=0.88)
    fig.savefig('Heatmap_Franjas_Stud{0}.png' .format(m), dpi=fig.dpi, bbox_inches='tight')
    

