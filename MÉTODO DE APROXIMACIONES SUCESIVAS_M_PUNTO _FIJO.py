# -*- coding: utf-8 -*-
"""
Created on Mon May 31 23:17:33 2021

@author: HP
"""

import numpy as np # se importa la libreria especificada en np

def fx(x): # se define la funcion y se le agrega un parametro 
    return np.exp(-x)-x # se retorna el numpy por la exponencial de -x, que es la funcion original
   

def gx(x): # se define una funcion de gx, se le agrega un parametro
    return np.exp(-x) #se retorna el numpy por la exponencial de -x

tolerancia=0.0001 # se estable una tolerancia, que va ser la que se compare con el error para que genere la aproximacion 
xi=0 # se establece el xi inicializa con el cero, eso nos indica que el ejercicio empieze a partir del 0
Error=np.abs(gx(xi)-xi)# genera la diferencia
i=0# se inicializa el valor de iteracion 


while(Error>tolerancia and i<=50 ): # se agrega el ciclo while, esto se va ejecutar en cuando el error se mayor que la tolerancia
    print("Iteracion=",i, "   ""xi",xi,    "            "   "gx(xi=)",gx(xi),      "          ""error=",Error) # para que vaya indicando cada iteraciones como se van moviendo los valores. 
    if i>0:# se agrega la condicion if si la iteracion es mayor que 0 decimos que 
        Error=np.abs(gx(xi)-xi)
    xi=gx(xi)
    i=i+1# incrementar el valor de las iteraciones
        
print ("el valor de x, tal que f(x)=0 es:", xi) #se imprime el xi para saber el valor de x