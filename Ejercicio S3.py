# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 02:01:34 2021

@author: maril
"""

class For:
    def __init__(self):
        pass

    def usoFor(self):
        datos=["María", 19, True]
        numeros= (10,5,2,12)
        docente= {"nombre": "Daniel", "Edad": 50, "FAC": "Faci"}
        registroN= [(20,35), [14,41], (13,33)]
        registroA= [{"nombre": "Maria", "Nota": 85}, {"nombre": "Aylin", "Nota": 84}, {"nombre": "Adrian", "Nota": 72}]
        for i in range(5):  #rango(0,1,2,3,4)
            print("i= {}" .format(i))
        for i in range(2,10):  
            print("i= {}" .format(i))
        for i in range(4,10,2):  
            print("i= {}" .format(i), end= " ")
        for i in range(12,3,-3):
            print("i= {}" .format(i), end= " ")

        long= len(datos)
        # j=0
        # while j < contar:
        #     print("while", datos[j])
        #     j+=1
        for i in range(long-1,-1,-1):
            print("for", datos[i])
        for dato in numeros:
            print(dato)
        for dato in ['H','O','L', 'A', 'como','estas']:
            print(dato)
        print("\nDiccionario de notas")
        for clave, valor in docente.items():
            print(clave, ":", valor, end= " ")

        for alumnos in registroA:
            for clave, valor in alumnos.items():
                print(clave, ":", valor, end= " ")

for1= For()
for1.usoFor() 