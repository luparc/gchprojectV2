import numpy as np
try:
    from capibara_fct import *
except:
    print("ERREUR! Il y a une erreur fatale dans le fichier conduite_fct.py")

class parametres():
    t =30                       # temps de fonctionnement [s]
    Tr = 30+273.15              # Température à l'intérieur de la conduite [K]
    Te = 30+273.15              # Température ambiante autour de la conduite [K]
    kch = 50               # Conductivité thermique noyau [W*m^-1*K^-1]
    Cpch = 40                 #capacité calorifique noyau [J*kg^-1*K^-1]
    rhoch =                 #densité noyau [kg*m^-1]
    kiso = 50               # Conductivité thermique isolant [W*m^-1*K^-1]
    Cpiso =                  #capacité calorifique isolant [J*kg^-1*K^-1]
    rhoiso =                 #densité isolant [kg*m^-1]
    h = 12               # Coefficient de convection thermique [W*m^-2*K^-1]
    Re = 4              # Rayon externe [m]
    Rch = 2              # Rayon interface entre acier et isolant [m]
    nr = 200               # Nombre de noeuds dans l'espace[-]
    dr = Re/(nr-1)    
    nt =100             #Nombre de noeuds dans le temps[-]
    dr = t/(nt-1) 
    qdot = 50000        #génération de chaleur [W*m^-3]
class Test:

    def test_mdf(self):
        prm = parametres()

        prm2=parametres()
        prm2.k=55
    
        prm3=parametres()
        prm3.k=190
    
    
        r,T1=mdf(prm)
        r,T2=mdf(prm2)
        r,T3=mdf(prm3)
    
        assert (len(T1)==81)
    
    
        assert (abs(T1[6] - 342.86795642) < 1e-4)
        assert (abs(T2[6] - 345.60351553) < 1e-4)
        assert (abs(T3[6] - 347.77617237) < 1e-4)
    
        assert (abs(T1[9] - 339.48646816) < 1e-4)
        assert (abs(T2[9] - 343.51902735) < 1e-4)
