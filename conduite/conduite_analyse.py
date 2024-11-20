# Importation des modules
import numpy as np
import matplotlib.pyplot as plt
import pytest
import time
import conduite_corr
try:
    from conduite_fct import *
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
    Tr = 70+273.15              # Température à l'intérieur de la conduite
    Te = 25+273.15              # Température ambiante autour de la conduite
    k = 50               # [W*m^-1*K^-1] Conductivité thermique
    h = 12               # [W*m^-2*K^-1] Coefficient de convection thermique
    Re = 4              # [m] Rayon externe
    Ri = 2              # [m] Rayon interne
    n = 200               # [-] Nombre de noeuds
    dr = (Re-Ri)/(n-1)

prm = parametres()

# Coefficients de conductivité themique
k_values = [("béton",1.3),("acier",50),("aluminium",200)]

# Méthode de différences finies

plt.figure(figsize=(8, 6))

for matériel,k in k_values:
    prm.k = k
    r, T = mdf(prm)
    plt.plot(r, T, label=f'{matériel} (k = {k} W/m·K)')

# Paramètres du graphique
plt.xlabel('Rayon (m)')
plt.ylabel('Température (K)')
plt.title('Profil de température en fonction du rayon pour différentes matériaux')
plt.legend()
plt.grid(True)

# Affichage
plt.show()
# Correction
pytest.main(['-q', '--tb=long', 'conduite_corr.py'])
