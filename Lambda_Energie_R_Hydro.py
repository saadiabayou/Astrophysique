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


def convert_m_nm (l):
    l=l/(10e-9)
    return l

def convert_nm_m(l):
    L=l/(10e-9)
    return L
#
def convert_Jev (EJ):
    """ This function change a Joule value to an electronvolt value """
    return EJ/evJ 

n1=int(input("Entrer la valeur du niveau d'énergie initial : \nn1= "))
n2=int(input("Entrer la valeur du niveau d'énergie final:\nn2= "))


def serie_raies_H(n1):
    
        if n1==1:
            print ("\nSerie de Lyman")
        elif n1==2:
            print("\nSerie de Balmer")
        elif n1==3:
             print("\nSerie de Paschen")
        elif n1==4:
             print("\nSerie de Bracket")
        elif n1==5:
             print("\nSerie de Pfund")
        else:
            print("\nSerie de Humphreys")        
        
        


def Raie_H(n1,n2):
    serie_raies_H (n1)
    lambd=1/(RH*((1/(n1**2))-(1/(n2**2))))
    E=(h*c)/lambd
    E=convert_Jev(E)
    E=round(E,2)
    lambd=convert_m_nm (lambd)
    lambd=round(lambd,2)  
    
    if n1 > n2 :
        print("\nAbsorption :")
    else:
        print("\nEmission :")
    
    if n2 > 6 and n1==1:    
        
        (1/(n2**2))==0
        lambd_ion=lambd
        print("\nn2 tend vers l'infinie -> extraction de l'électron : phénomène d'ionisation\n") 
        print("la longueur d'onde lambda d'ionisation vaut :", lambd_ion,"nm")
        print("et l'énergie d'ionisation vaut : E_ionisation =" ,E,"ev")
    else :
        print( "\nLa longeur d'onde est lambda(",n1,"/",n2,")= ",lambd,"nm")
        print("\nL'Energie de transition E (" ,n1,"->",n2, ") vaut: E = ", E, "eV\n")
        
        print("resultats ( lambda,E ) :")
    return lambd , E 
    
# call function
    
print(type(Raie_H(n1,n2)))


print(Raie_H(n1,n2))
    

