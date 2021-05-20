# -*- coding: utf-8 -*-
"""
Created on Tue May 18 22:40:31 2021

@author: HP
"""

def poli(x): # funcion para calcular 
    return pow (x,8)-(2*x)-1 # se retorna la funcion para que nos pueda devolver los valores que se calcula


def biseccion (a,b,error): # creamos el metodo biseccion con parametros 
   
    interA=a # el inter A tomara el valor de a
    B2=b; # el B2 tomara el valor de b
    K=0; # contador para el numero de iteraciones
    if(poli(a)*poli(b)>0): # Agregar el control para checar si el intervalo a y el intervalo b poseen los mismos signos
        print("La ecuacion polinomio no cambia de signo"); # mandar un mensaje si en los intervalos no existe la raiz,entonces nos se cambiara los signos
    
        
    while(abs(interA-B2)>error):# se agrega el ciclo while,cuando el interA-b2 es mayor que el error el interA tomara el valor de b2
        interA=B2; # se actualiza el valor de A1
        B2=(a+b)/2; # formula para calcular el punto medio de los intervalos
        if(poli(a)*poli(B2)<0): # se agrega la condicion if, cambia de signo en el intervalo a,B2
            b=B2; # se agrega un nuevo limite superior
        if(poli(B2)*poli(b)<0):# se agrega la condicion if, cambia de signo en el intervalo B2,b
            a=B2;# se agrega el nuevo limite inferior
            print("El intervalo es[",a,",",b,"]") # se imprime los valores de los intervalo 
            K=K+1; # se incrementa el valor de k
    print( "Numero de iteraciones:",K,)# se imprime la iteracion
    print("La raiz de x es" "=" ,B2,) # se imprime el raiz de la funcion
        
biseccion(0,10,.0001)# se ejecuta los parametros de la funcion 




