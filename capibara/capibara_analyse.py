# Importation des modules
import numpy as np
import matplotlib.pyplot as plt
import pytest
import time
import capibara_corr
try:
    from capibara_fct import *
except:
    pass

#------------------------------------------------------------------------------
# Code principal pour l'analyse des résultats
# Il faudra faire appel aux fonctions programmées dans conduite_fct.py afin de
# calculer la température dans la conduite selon le rayon et de comparer les
# résultats pour plusieurs matériaux. Des graphiques devront être générés pour
# visualiser les résultats.
#------------------------------------------------------------------------------

# Assignation des paramètres
# ATTENTION! Ne pas changer le nom des attributs, seulement les valeurs
class parametres():
    t =30                       # temps de fonctionnement [s]
    Tr = 30+273.15              # Température à l'intérieur de la conduite [K]
    Te = 30+273.15              # Température ambiante autour de la conduite [K]
    kch = 45               # Conductivité thermique noyau [W*m^-1*K^-1]
    Cpch = 490                 #capacité calorifique noyau [J*kg^-1*K^-1]
    rhoch = 7850                #densité noyau [kg*m^-1]
    kiso = 0.4               # Conductivité thermique isolant [W*m^-1*K^-1]
    Cpiso = 1000                 #capacité calorifique isolant [J*kg^-1*K^-1]
    rhoiso = 100                #densité isolant [kg*m^-1]
    h = 0.2               # Coefficient de convection thermique [W*m^-2*K^-1]
    Re = 0.24              # Rayon externe [m]
    Rch = 0.2              # Rayon interface entre acier et isolant [m]
    nr = 200               # Nombre de noeuds dans l'espace[-]
    dr = Re/(nr-1)    
    nt =100             #Nombre de noeuds dans le temps[-]
    dr = t/(nt-1) 
    qdot = 50000        #génération de chaleur [W*m^-3]



prm = parametres()



# Méthode de différences finies

plt.figure(figsize=(8, 6))



r, T = mdf(prm)
plt.plot(r, T)

# Paramètres du graphique
plt.xlabel('Rayon (m)')
plt.ylabel('Température (K)')
plt.title('Profil de température en fonction du rayon')
plt.legend()
plt.grid(True)

# Affichage
plt.show()
# Correction
pytest.main(['-q', '--tb=long', 'capibara_corr.py'])
