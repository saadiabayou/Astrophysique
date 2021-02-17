# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 14:11:21 2020

@author: Saadia Bayou
"""

# Calul longueur d'onde et énergie de transition des raies d’hydrogène

print("Calul de la longueur d'onde et de l'énergie de transition des raies de l'Hydrogène")

# données
evJ=1.6076634e-19 # Joules -> 1 electronvolt vaut 1,6076634.10e-19 Joules
RH=1.10e7 # RH = 1.10e7 m-1
h=6.63e-34 # h = 6.63e-34 m2.kg.s-1
c=3.00e8 # c=3.00e08 m.s-1  
lambdas=[] # Initalisation liste longueurs d'onde
Energies=[] # Initialisation liste Energies


def convert_m_nm (l):
    """Convertit une grandeur en mètre en nanomètre"""
    l=l/(10e-9)
    return l

def convert_nm_m(l):
    """ Convertit une grandeur en nanomètre en mètre """
    L=l/(10e-9)
    return L
#
def convert_J_ev (EJ):
    """ Convertit une grandeur en  Joule en electronvolt """
    return EJ/evJ 


def convert_ev_J(Eev):
    """ Convertit une grandeur en electronvolt en  Joule """
    
    print("\nLa grandeur en ev convertie en Joules vaut :\n ")
    return str(Eev*evJ) + " Joules" 
    


def Raie_H(n1,ln2):
    for n2 in ln2 :
        lambd=1/(RH*((1/(n1**2))-(1/(n2**2))))
        E=(h*c)/lambd
        E=convert_J_ev(E)
        E=round(E,2)
        lambd=convert_m_nm (lambd)
        lambd=round(lambd,2)  
        print("\nAu niveau d'énergie n2 =",n2,", la longueur d'onde lambda(",n2,")=",lambd,"nm")
        print("et l'énergie de transition correspondante est E(",n2,")=",E,"ev")
        lambdas.append(lambd)
        Energies.append(E)
    
    print("\nLa liste des longueurs d'ondes est : ")        
    return "lambdas =" ,lambdas



# call fonction     
Lyman_alpha=[2,3,4,5,6]
print(Raie_H(1,Lyman_alpha))
print("\nLa liste des énergies de transition est:\n \nEnergies = ", Energies) 

Lyman_beta=[2,3,4,5,6]

Balmer=[2,3,4,5,6]







