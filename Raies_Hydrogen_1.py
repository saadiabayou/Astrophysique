# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 15:52:33 2020

@author: Saadia Bayou
"""
# données
evJ=1.6076634e-19 # Joules -> 1 electronvolt vaut 1,6076634.10e-19 Joules
RH=1.10e7 # RH = 1.10e7 m-1
h=6.63e-34 # h = 6.63e-34 m2.kg.s-1
c=3.00e8 # c=3.00e08 m.s-1  
lambdas=[]
Energies=[]

#metre -> nanometre
def convert_m_nm (l):
    """Convertit une grandeur en mètre en nanomètre"""
    L=l*(1e+09)
    return L
# nanometre -> metre
def convert_nm_m(l):
    """ Convertit une grandeur en nanomètre en mètre """
    L=l/(1e+09)
    return L

def convert_Jev (EJ):
    """ Cette fonction convertit une grandeur de Joule à electronVolt"""
    return EJ/evJ 



n1=int(input("Entrer la valeur du niveau d'énergie initial : \nn1= "))
n2=int(input("Entrer la valeur du niveau d'énergie final:\nn2= "))

def Raie_H(n1,n2):
    lambd=1/(RH*((1/(n1**2))-(1/(n2**2))))
    lambd=1/(RH*((1/(n1**2))-(1/(n2**2))))
    E=(h*c)/lambd
    E=convert_Jev(E)
    E=round(E,2)
    lambd=convert_m_nm (lambd)
    lambd=round(lambd,2)  
    
    return "lambda = " + str(lambd) +" nm"+ " Energie = "+ str(E)+ " ev"

#Appel fonction  
    
print(Raie_H(n1,n2))
    

