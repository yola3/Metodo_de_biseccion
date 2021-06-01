# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:34:52 2021

@author: HP
"""

def Formula(x,fx): # FUNCION DEL METODO A UTILIZAR PARA OBTENER EL LOGARITMO NATURAL DESEADO DE UN NUMERO
    
    b0=fx[0]
    b1=(fx[1]-fx[0])/(x[1]-x[0])
    b2=(((fx[2]-fx[1])/(x[2]-x[1]))-((fx[1]-fx[0])/(x[1]-x[0])))
    f2=b0+b1*(x[3]-x[0])+b2*(x[3]-x[0])*(x[3]-x[1])
    return (f2) # SE RETORNA 

x=[]# VECTOR X EN DONDE SE ALMACENARA EL VALOR DE X
fx=[]# VENTOR DE F DONDE SE ALMACENARA EL VALOR DE F(X)

for i in range(0,4): # CICLO FOR DONDE SE AGREGA INTRODUCE LOS VALORES INDICA CUANDO VALORES SE PERMITIRA EGREGAR
    valorx=float(input("Introduce el valor para x["+str(i+1)+"]")) # CITA LOS DATOS DESDE EL TECLADO
    x.append(valorx) # SE AÑADE ALA LISTA DE X 
    vfx=float(input("Introduce el valor para fx["+str(i+1)+"]")) # SE CITA EL VALOR DE FX DESDE EL TECLADO
    fx.append(vfx) # SE AÑADE DE LA LISTA FX
valorx=float(input("Introduce el valor de x para calcular f(x):")) # SE CITA EL VALOR A CALCULAR DESDE EL TECLADO
x.append(valorx) # SE AÑADE A LA LISTA DE X
print("El valor de f(x) es: ",Formula(x,fx)) # SE IMPRIME LA FORMULA PARA OBTENER EL RESULTADO 
    
