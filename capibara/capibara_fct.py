# Importation des modules
import numpy as np

def mdf(prm):
    """Fonction simulant avec la méthode des différences finies

    Entrées:
        - prm : Objet class parametres()
            - Tr : Température à l'intérieur de la conduite [K]
            - Tinf : Température ambiante autour de la conduite [K]
            - kch : Conductivité thermique noyau [W*m^-1*K^-1]
            - Cpch : capacité calorifique noyau [J*kg^-1*K^-1]
            - rhoch : densité noyau [kg*m^-1]
            - kiso : Conductivité thermique isolant [W*m^-1*K^-1]
            - Ciso : capacité calorifique isolant [J*kg^-1*K^-1]
            - rhoiso : densité isolant [kg*m^-1]
            - h : Coefficient de convection thermique [W*m^-2*K^-1]
            - Re : Rayon externe [m]
            - Rch : Rayon interface entre acier et isolant [m]
            - nr : Nombre de noeuds dans l'espace[-]
            - nt : Nombre de noeuds dans le temps[-]            
            - dr : Pas en espace [m]
            - qdot : génération de chaleur [W*m^-3]  

    Sortie (dans l'ordre énuméré ci-bas):
        - Vecteur (array) de dimension Nr composé de la position radiale à laquelle les températures sont calculées, où Nr le nombre de noeuds.
        - Vecteur (array) de dimension Nr composé de la température en fonction du rayon, où Nr le nombre de noeuds
        - matrice de dimesion Nt*Nr composé de la température en fonction du rayon a chaque instant de t, où Nr le nombre de noeuds et Nr le nombre d'instance t' 
    """
    
    kch=prm.kch
    Cpch=prm.Cpch
    rhoch=prm.rhoch
    kiso=prm.kiso
    Cpiso=prm.Cpiso
    rhiso=prm.rhiso    
    Re=prm.Re
    Rch=prm.Rch
    dr=prm.dr
    Tr=prm.Tr
    h=prm.h
    Tinf=prm.Tinf
    Nr=prm.nr
    Nt=prm.nt
    qdot=prm.qdot

    Tt=np.zeros(Nr) # température a la fin du temps
    A=np.zeros([Nr,Nr])
    b=np.full(Nr, Tr)
    T_résult=np.zeros([Nt,Nr])
    T_résult[0:]=b # au début (t=0s) la tige est à température ambient (Tinf)
    r=np.linspace(0, Re, Nr)
    
    A[0,0]=0 # la dérivé au centre de la tige dT/dr=0
    # condition de frontiere entre acier et isolant
    NRch =int(np.round(Rch/dr))-1 #le noeud le plus proche au point r=Rch
    A[NRch,NRch]=(-3*kch-3*kiso)
    A[NRch,NRch-1]=4*kch
    A[NRch,NRch-2]=-kch
    A[NRch,NRch+1]=4*kiso
    A[NRch,NRch+2]=-kiso
    # condition de frontiere entre isolant et l'air
    A[-1,-1]=(-3*kiso/(2*dr))-h
    A[-1,-2]=4*kiso/(2*dr)
    A[-1,-3]=-kiso/(2*dr)    
    
    for j in range (1,Nt-1):
        b[-1]=-h*Tinf #reset T a la frontiere
        for i in range (1,Rch): #du centre(exclu) jusqu'a r=Rch (exclu)
            A[i,i-1]=(1/dr)-(1/(2*r[i]))
            A[i,i]=-2/dr
            A[i,i+1]=(1/dr)+(1/(2*r[i]))
        for i in range (Rch+1, Nr-1) : #de r=Rch(exclu) jusqu'a r=R(exclu)
            A[i,i-1]=(1/dr)-(1/(2*r[i]))
            A[i,i]=-2/dr
            A[i,i+1]=(1/dr)+(1/(2*r[i]))
        Tt=np.linalg.solve(A, b)
        # T_résult[j:]=Tt
        b=Tt
    
    # return r,T_résult
    return r,Tt
