# Importation des modules
import numpy as np

def mdf(prm):
    """Fonction simulant avec la méthode des différences finies

    Entrées:
        - prm : Objet class parametres()
            - Tr : Température à l'intérieur de la conduite [K]
            - Te : Température ambiante autour de la conduite [K]
            - k : Conductivité thermique [W*m^-1*K^-1]
            - h : Coefficient de convection thermique [W*m^-2*K^-1]
            - Re : Rayon externe [m]
            - Ri : Rayon interne [m]
            - n : Nombre de noeuds [-]
            - dr : Pas en espace [m]

    Sortie (dans l'ordre énuméré ci-bas):
        - Vecteur (array) de dimension N composé de la position radiale à laquelle les températures sont calculées, où N le nombre de noeuds.
        - Vecteur (array) de dimension N composé de la température en fonction du rayon, où N le nombre de noeuds
    """
    k=prm.k
    Re=prm.Re
    Ri=prm.Ri
    dr=prm.dr
    Tr=prm.Tr
    h=prm.h
    Te=prm.Te
    N=prm.n
    # Fonction à écrire
    A=np.zeros([N,N])
    b=np.zeros(N)
    r=np.linspace(Ri, Re, N)
    A[0,0]=
    b[0]= 
    A[-1,-1]=
    A[-1,-2]=
    A[-1,-3]=
    b[-1]=-h*Te
    for i in range (1,N-1):
        A[i,i-1]=(1/dr)-(1/(2*r[i]))
        A[i,i]=-2/dr
        A[i,i+1]=(1/dr)+(1/(2*r[i]))
    resultat_X=np.linalg.solve(A, b)
    return r,resultat_X
