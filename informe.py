#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:27:47 2019

@author: robot
"""


# importing from a pylatex module 
from pylatex import Document, Section, Figure, Command
from pylatex import Subsection, Tabular 
from pylatex import Math, TikZ, Axis, Plot, Matrix, Alignat 

from pylatex.utils import NoEscape
from pylatex.utils import italic

from Package.otros import controler_temps

@controler_temps()
def informeCurso(logs, mayorEvent, mayorEvent2, mayorComp, mayorComp2, porcS, porcW, porcDH, porcNH, diasDeClase=[], m=0, nameCurso=0, difClase=0):
    """ La función hace un informe para analizar un curso.
        """
    
    sem = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
    
    if True:  
        geometry_options = {"tmargin": "1cm", "lmargin": "1cm"} 
        doc = Document(geometry_options=geometry_options)
        
        doc.preamble.append(Command('title', 'Informe sobre los accesos a la pataforma moodle para el curso {}' .format(nameCurso)))
        doc.preamble.append(Command('date', NoEscape(r'\today')))
        doc.append(NoEscape(
                r"""\maketitle"""))
        with doc.create(Section('Presentacion')): 
            doc.append('Numero de estudiantes: {0} \n' .format(len(logs['User full name'].unique().tolist())))
            doc.append('Numero de componentes: {0} \n' .format(len(logs['Component'].unique().tolist())))
            doc.append('Numero de eventos: {0} \n' .format(len(logs['Event context'].unique().tolist())))
            
            if m == 0:
                m = m
            elif len(diasDeClase[m]) == 1:
                doc.append('Este curso se dicto los {0}. \n' .format(sem[diasDeClase[m][0]])) 
            elif len(diasDeClase[m]) == 2:
                doc.append('Este curso se dicto los {0} y {1}. \n' .format(sem[diasDeClase[m][0]], sem[diasDeClase[m][1]])) 
                
        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Hist_Franjas{0}.png' .format(m), width='120px')
            
        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Heatmap_Franjas{0}.png' .format(m), width='120px')
            
        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Heatmap_Franjas_Stud{0}.png' .format(m), width='120px')
            
            doc.append('El histograma siguiente permite ver la repartición de los accesos de los estudiantes en función del día de la semana.')
        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Hist_Dayofweek{0}.png' .format(m), width='120px')
            
        doc.append('''Este histograma muestra que los estudiantes acceden al curso {0} veces más durante los días de clase que los otros días. Parcen acceder al curso un poco más los días antes del curso. Además, parecen acceder menos al curso durante el fin de semana.
    
    La heatmap de los accesos de los estudiantes en funcion del día de la semana nos muestra los mismos resultados : ''' .format(round(difClase, 2)))
        
        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Heatmap_Dayofweek{0}.png'.format(m), width='120px')
        
        doc.append('''Gracias al histograma de los accesos en función de los eventos, podemos notar que la mayor parte de los accesos se reparten en solo {0} eventos y más del 90% en solo {1}. 
''' .format(mayorEvent, mayorEvent2))
            
        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Hist_10_principales_eventos{0}.png'.format(m), width='120px')
            
        doc.append('''Para los componentes, la mayor parte de los accesos se reparten en solo {0} y más del 90% en solo {1}.''' .format(mayorComp, mayorComp2))
            
        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Hist_10_principales_componentes{0}.png' .format(m), width='120px')
               
        doc.append('El histograma siguiente muestra el numero de accesos a la plataforma para cada estudiante.')    
        
        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Hist_Students{0}.png' .format(m), width='150px')
            
        doc.append('La boxplot de los logs de los estudiantes es la siguiente:')
            
        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Boxplot_students{0}.png' .format(m), width='120px')
            
        doc.append('''Podemos ver que algunos estudiantes acceden al curso mucho más que la mayoria.
                       
                       La distribución de los accesos de los estudiantes es la siguiente:''')
            
        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Hist_Distribucion{0}.png' .format(m), width='120px')
            
        doc.append('El histograma siguiente permite ver que los estudiantes acceden más al curso antes de las 6 de la tarde que despues.')
            
        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Hist_Noche-Dia{0}.png' .format(m), width='120px')
            
        doc.append('Los accesos durante el día representa un {}% y los accesos durante la noche un {}%. \n' 
                   .format(round(porcDH, 2), round(porcNH, 2)))
        doc.append('El histograma abajo permite confirmar que los estudiantes acceden más al curso durante la semana que el fin de semana :')
            
        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Hist_Semana-Weekend{0}.png' .format(m), width='120px')
        
        doc.append('Los accesos durante la semana representa un {}% y los accesos durante el fin de semana un {}%. \n' 
                   .format(round(porcS, 2), round(porcW, 2)))
            
    doc.generate_pdf('Estadistica_descriptiva{0}' .format(m), clean_tex=False, compiler='pdflatex') 
  
@controler_temps()
def informeSemana(logs, m=0) :
    """ La función hace un informe para analizar una semana.
        """
        
    if True:  
        #geometry_options = {"tmargin": "1cm", "lmargin": "1cm"} 
        doc = Document()#geometry_options=geometry_options)
        
        doc.preamble.append(Command('title', 'Informe sobre los accesos a la pataforma moodle para la semana {}' .format(m)))
        doc.preamble.append(Command('date', NoEscape(r'\today')))
        doc.append(NoEscape(
                r"""\maketitle"""))
        
        with doc.create(Section('Presentacion')): 
            #doc.append('Curso: {0} \n' .format(nameCurso))
            doc.append('Numero de estudiantes: {0} \n' .format(len(logs['User full name'].unique().tolist())))
            doc.append('Numero de componentes: {0} \n' .format(len(logs['Component'].unique().tolist())))
            doc.append('Numero de eventos: {0} \n' .format(len(logs['Event context'].unique().tolist())))
            
        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Hist_Franjas{0}.png' .format(m), width='120px')
            
        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Heatmap_Franjas{0}.png' .format(m), width='120px')

        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Hist_Dayofweek{0}.png' .format(m), width='120px')
            
#        doc.append('''Este histograma muestra que los estudiantes acceden al curso {0} veces más durante los días de clase que los otros días. Parcen acceder al curso un poco más los días antes del curso. Además, parecen aceder menos al curso durante el fin de semana.
#    
        
#        doc.append('''Gracias al histograma de los accesos en función de los eventos, podemos notar que la mayor parte de los accesos se reparten en solo {0} eventos y más del 90\% en solo {1}. 
#''' .format(mayorEvent, mayorEvent2))
            
        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Hist_10_principales_eventos{0}.png'.format(m), width='120px')
            
        doc.append('Esta semana los 10 componentes que registraron los más accesos son :')
            
        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Hist_10_principales_componentes{0}.png' .format(m), width='120px')
            
        doc.append('Esta semana los 10 eventos que registraron los más accesos son :')
                
        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Hist_10_principales_eventos{0}.png' .format(m), width='120px')
            
        doc.append('La boxplot de los logs de los estudiantes es la siguiente:')
            
        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Boxplot_students{0}.png' .format(m), width='120px')
            
        doc.append('''La distribución de los logs de los estudiantes es la siguiente:''')
            
        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Hist_Distribucion{0}.png' .format(m), width='120px')
            
        doc.append('El histograma siguiente permite ver si los estudiantes se connectan más antes de las 6pm (día) o despues (noche).')
            
        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Hist_Noche-Dia{0}.png' .format(m), width='120px')
            
        doc.append('El histograma abajo permite confirmar que los estudiantes acceden más al curso durante la semana que el fin de semana :')
            
        with doc.create(Figure(position='h!')) as kitten_pic: 
            kitten_pic.add_image('Hist_Semana-Weekend{0}.png' .format(m), width='120px')
            
    doc.generate_pdf('Estadistica_descriptiva{0}' .format(m), clean_tex=False, compiler='pdflatex') 
