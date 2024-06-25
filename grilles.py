# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 13:54:41 2023

@author: choukri
"""

import random
import turtle 


######################### PARTIE CREATION ET AFFICHAGE ########################

def creer_matrice(M=3,N=4):#on donne aux valeurs inf et sup des valeurs par défaut 
   #Génère une matrice avec des nombres aléatoire

    matrix = [] #nouvelle matrice  
    #on parcours la matrice 
    for i in range(M):
        line = [] #nouvelle ligne
        for j in range(N):
            line.append( [random.randint(1,5) for i in range(4)]#on ajoute à la ligne une liste de 4 élements aléatoires 
                        # entre les deux valeurs 1 et 5  
)
        matrix.append(line)#puis on ajoute la ligne créee de 4 listes à la matrice 

    return matrix #en retourne la matrice créee à la fin de la fonction 




def afficher_matrice(matrice):
  #Affiche la matrice dans la console
    for line in matrice:#pour chaque ligne de la matrice 
        print(line)#afficher la ligne 
        
      
        
    
        
    ### ~~~~~~ TEST affichage de la matrice ~~~~~~~ ###
matrice = creer_matrice(2,2)#une matrice avec des valeurs entre 1 et 5
afficher_matrice(matrice)#‗afficher la matrice 
print()
     #### FIN DU TEST ####




###############################  PARTIE DESSIN   ############################## 


def afficher_dessin(M):#fonction 
    tu= turtle.Turtle()
   
    l=len(M)#recuperer la longeur de la matrice en lignes 
    c=len(M[0])#recuperer la longeur de la matrice en colonnes 
    
    for i in range(l):#parcours ds lignes 
        for j in range(c):#parcours des colonnes 
        
     #Dessin du premier mur en haut 
                  tu.pensize(M[i][j][0])#changement de l'épaisseur du crayon en fonction
                  #de l'épaisseur des murs stockés dans la liste
                  tu.forward(30)#avancer de 30 pixels pour dessiner une ligne 
                  tu.right(90)#pivote d'un angle droit
      #dessin du 2e mur à gauche
                  tu.pensize(M[i][j][1])
                  tu.forward(30)
                  tu.right(90)
     #dessin de 3e mur en bas 
                  tu.pensize(M[i][j][2])
                  tu.forward(30)
                  tu.right(90)
    #dessin du 4e mur à droite           
                  tu.pensize(M[i][j][3])
                  tu.forward(30)
                  tu.right(90)
                 
    #repositionnement à la fin de chaque case                  
                  tu.penup()#on enleve le cryon avant de chager la position pour ne pas affecter les murs
                  x=tu.xcor() #recuperer la position de la tortue 
                  tu.setx(x+30)#modification de la position de l'abscisse de la tortue 
                        #pour passer à la case suivante de la mem ligne 
                  tu.pendown()#on remet le crayon
                  
     #repositionnement à la fin de chaque ligne 
        tu.penup()#on enleve le cryon avant de chager la position pour ne pas affecter les murs
        tu.sety(-30)#revenir à la ligne 
        tu.setx(-c)#reculer jusqu'au début  de la ligne 
        tu.pendown()#on remet le crayon
            
      #### ~~~~~~~~~~ TEST DU DESSIN ~~~~~~~~~~~~~~~~ ####      
afficher_dessin(matrice)#on prend la matrice deja cree dans le test précedant 

    ## FIN DU TEST ##





############# PARTIE 2 ############


def cases_voisines(p, i, j):
    L=[]
    if j>0:
        L.append((i,j-1))
    if i>0:
        L.append((i-1,j))
    if j<p-1:
        L.append((i,j+1))
    if i<p-1:
        L.append((i+1,j))
    return L


def matrice_en_graphe(M):
    p=len(M)
    G={}
    for i in range(p):
        for j in range(p):
            CV=cases_voisines(p,i,j)
            G[p*i+j]=[]
            for coord in CV:
                x, y = coord
                G[p*i+j].append((p*x+y, M[x][y]))
    return G

########### TEST GRAPHE DICTIONNAIRE #############
print(matrice_en_graphe(matrice))
########## FIN TEST #############


############### PARTIE DIJKSTRA #############

def minimum(dico):
    m=float('inf')
    for k in dico:
        if dico[k] < m:
            m=dico[k]
            i=k
    return i

def dijkstra_pred(G,s):
   D={}   #tableau final des distances minimales
   d={k: float('inf') for k in G}   #distances initiales
   d[s]=0  #sommet de départ
   P={}   #liste des prédécesseurs
   while len(d)>0:   #fin quand d est vide
       k=minimum(d)   #sommet de distance minimale pour démarrer une étape
       for i in range(len(G[k])):   #on parcourt les voisins de k
           v, c = G[k][i]   #v voisin de k, c la distance à k
           if v not in D:   #si v n'a pas été déjà traité
               if d[v]>d[k]+c:   #est-ce plus court en passant par k ?
                   d[v]=d[k]+c
                   P[v]=k   #stockage du prédécesseur de v
       D[k]=d[k]   #copie du sommet et de la distance dans D
       del d[k]   #suppression du sommet de d
   return D, P   #on retourne aussi la liste des prédécesseurs


def chemin_min(M):
    p=len(M)
    m=len(M[0])
    G3=matrice_en_graphe(M)
    L,P=dijkstra_pred(G3,0)#listes de predecesseurs 
    print("poids du chemin minimal : ",(L[m*p-1]+M[0][0]))#affichage du poids
    print("chemin : ",end="")#affichage du chemin 
    c=m*p-1
    lst=[(c//p, c%p)]
    while c!=0:
        lst=[(P[c]//p, P[c]%p)]+lst
        c=P[c]
    print(lst)

############### TEST DJIKSTRA #########
#chemin_min(matrice)
############## Fin TEST ###########








############# GRILLE PERCEE ##################


def afficher_dessin_perce(M):#fonction 
    #le code la fonction chemin_min sans l'affichage 
    p=len(M)
    m=len(M[0])
    G3=matrice_en_graphe(M)
    L,P=dijkstra_pred(G3,0)#listes de predecesseurs 
    c=m*p-1
    lst=[(c//p, c%p)]
    while c!=0:
        lst=[(P[c]//p, P[c]%p)]+lst
        c=P[c]
    tu= turtle.Turtle()
    l=len(M)#recuperer la longeur de la matrice en lignes 
    c=len(M[0])#recuperer la longeur de la matrice en colonnes 
    
    for i in range(l):#parcours ds lignes 
        for j in range(c):#parcours des colonnes 
            for k in range (len(lst)):#parcours de la liste du chemin 
     #Dessin du premier mur en haut 
                 # on teste si le chemin est un mur puis verifie lequel puis on ajoute au code du mur traité le code suivant:
                 """ tu.pencolor("blue")"""
                 tu.pensize(M[i][j][0])#changement de l'épaisseur du crayon en fonction
                 #de l'épaisseur des murs stockés dans la liste
                 tu.forward(30)#avancer de 30 pixels pour dessiner une ligne 
                 tu.right(90)#pivote d'un angle droit
      #dessin du 2e mur à gauche
                 tu.pensize(M[i][j][1])
                 tu.forward(30)
                 tu.right(90)
     #dessin de 3e mur en bas 
                 tu.pensize(M[i][j][2])
                 tu.forward(30)
                 tu.right(90)
    #dessin du 4e mur à droite           
                 tu.pensize(M[i][j][3])
                 tu.forward(30)
                 tu.right(90)
                 
    #repositionnement à la fin de chaque case                  
                 tu.penup()#on enleve le cryon avant de chager la position pour ne pas affecter les murs
                 x=tu.xcor() #recuperer la position de la tortue 
                 tu.setx(x+30)#modification de la position de l'abscisse de la tortue 
                        #pour passer à la case suivante de la mem ligne 
                 tu.pendown()#on remet le crayon
                  
     #repositionnement à la fin de chaque ligne 
        tu.penup()#on enleve le cryon avant de chager la position pour ne pas affecter les murs
        tu.sety(-30)#revenir à la ligne 
        tu.setx(-c)#reculer jusqu'au début  de la ligne 
        tu.pendown()#on remet le crayon
        
        
        
############# TEST GRILLE PERCEE ##############
#afficher_dessin(matrice) 
#afficher_dessin_perce(matriice
##chemin_min(matrice)
### FIN TEST #####









