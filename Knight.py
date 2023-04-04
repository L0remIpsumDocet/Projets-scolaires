# Présentation du problème
# Type d'algos :
# Ma solution
# D'autres solutions
# Conclusion

import math
import matplotlib.pyplot as plt
import numpy as np

global tablex
tablex=[]
global tabley
tabley=[]

def check_1(dic):
    sz=8
    flag=True
    for i in range(sz):
        for j in range (sz):
            if dic[(i,j)]!=1:
                flag=False
    return flag



def chess(taille):
    dict={}
    for i in range(taille):
        for j in range(taille):
            list=[]
            if (i-1)>=0 and (j-2)>=0 and (i-1)<taille and (j-2)<taille:
                list.append((i-1,j-2))
            if (i+1)>=0 and (j-2)>=0 and (i+1)<taille and (j-2)<taille:
                list.append((i+1,j-2))
            if (i+2)>=0 and (j-1)>=0 and (i+2)<taille and (j-1)<taille:
                list.append((i+2,j-1))
            if (i+2)>=0 and (j+1)>=0 and (i+2)<taille and (j+1)<taille:
                list.append((i+2,j+1))
            if (i+1)>=0 and (j+2)>=0 and (i+1)<taille and (j+2)<taille:
                list.append((i+1,j+2))
            if (i-1)>=0 and (j+2)>=0 and (i-1)<taille and (j+2)<taille:
                list.append((i-1,j+2))
            if (i-2)>=0 and (j+1)>=0 and (i-2)<taille and (j+1)<taille:
                list.append((i-2,j+1))
            if (i-2)>=0 and (j-1)>=0 and (i-2)<taille and (j-1)<taille:
                list.append((i-2,j-1))
            dict[i,j]=list
    graphe=Graphe(dict)
    return graphe

def springtrap(taille):
    list={}
    for i in range(taille):
        for j in range(taille):
            list[(i,j)]=-1
    return list

class Graphe(object):

    def __init__(self, graphe_dict=None):
        """ initialise un objet graphe.
	    Si aucun dictionnaire n'est
	    créé ou donné, on en utilisera un 
	    vide
        """
        if graphe_dict == None:
            graphe_dict = dict()
        self._graphe_dict = graphe_dict

    def aretes(self, sommet):
        """ retourne une liste de toutes les aretes d'un sommet"""
        return self._graphe_dict[sommet]

    def all_sommets(self):
        """ retourne tous les sommets du graphe """
        return list(self._graphe_dict.keys())

    def all_aretes(self):
        """ retourne toutes les aretes du graphe """
        return list(self._graphe_dict.values())

    def copie_nb(self,som):
        '''Fonction permettant de remplacer un graphe avec des noms par un grpahe où les sommets ont representes par des entiers'''
        new = {}
        a=None
        ordr=len(self._graphe_dict)+1
        for i in range(1,ordr):
            new[i]=[]
        count=0
        for i in self._graphe_dict:
            conotus=0
            if i==som:
                a=count
            for key,value in self._graphe_dict.items():
                conotus=conotus+1
                for z in range(len(value)):
                    if (i==value[z]):
                        new[conotus].append(count)
            count=count+1
        graphe = Graphe(new)
        return a,graphe

    def check(self,sommet):
        '''Verifie si le graphe est connexe avec l algorithme de largeur'''
        s,new=self.copie_nb(sommet)
        ordr=len(self._graphe_dict)
        q=[s]
        d=[-1]
        for i in range(ordr):
            d.append(0)
        d[s]=1
        t={}
        while (len(q)!=0):
            v = q.pop(0)
            for w in new.aretes(v):
                if d[w]==0:
                    d[w]=1
                    q.append(w)
                    if v in t.keys():
                        t[v].append(w)
                    else:
                        t[v]=[w]

    def trouve_tout_chemin (self, sommet_dep,sommet_arr, chemin=[],chain="") :
        """J avais reelement envie de me couper les veines en codant mais ca fonctionne"""
        chain=chain+sommet_dep
        if (sommet_dep==sommet_arr):
            chemin.append(chain)
        for k in self.aretes(sommet_dep):
            if k not in chain:
                chemin=self.trouve_tout_chemin(k,sommet_arr,chemin,chain)
        return chemin

    def foster_1(self,sommet,somac,wood=[],check=[springtrap(6)]):
        check[somac]=1
        wood.append(somac)
        # a,b=somac
        # tablex.append(a)
        # tabley.append(b)
        if (somac==(0,0)):
            if check_1(check):
                print(wood)
                return wood
        for k in self.aretes(somac):
            if check[k]==0 or k==sommet:
                wood=self.foster(sommet,k,wood,check)
        if wood[-1]==somac:
            check[somac]=0
            wood.pop()
        return wood
    
    def foster(self,sommet,somac,wood=[],check=[springtrap(6)]):
        check[somac]=1
        wood.append(somac)
        # a,b=somac
        # tablex.append(a)
        # tabley.append(b)
        if (somac==(0,0)):
            if check_1(check):
                print(wood)
                return wood
        for k in self.aretes(somac):
            if check[k]==0 or k==sommet:
                wood=self.foster(sommet,k,wood,check)
        if wood[-1]==somac:
            check[somac]=0
            wood.pop()
        return wood
    
#Partie de Warnsdorff le bg

    def caballero(self,chess,k,n,sol=[]):
        if len(sol)==0:
            if n==64: # CONSTANTE A CHANGER
                if k in self.aretes((0,0)): #CONSTANTE A CHANGER
                    sol.append(chess) # En vrai ça c'est suspect...
            else :
                poss=[]
                for m in self.aretes(k):
                    if chess[m]<=0: #Bien verifier que chess est un dictionnaire avec (i,j) et pas une liste qui prend uniquement un indice
                        poss.append(m)
                warn=[]
                for m in poss:
                    temporaire=[]
                    for p in self.aretes(m):
                        if chess[p]<=0:
                            temporaire.append(p)
                    warn.append(len(temporaire))
                if len(warn)==0: #Si warn est vide (pas de voisins)
                    nchem_min=0 #On ne choisit aucun chemin
                else:
                    nchem_min=min(warn)
                candidat=[]
                for (i,m) in enumerate(poss): #Dans la liste complète des voisins non marqués, on choisit celui qui a l'indice correspondant à la lonufuer la plus courte dans la liste warn
                    if warn[i]==nchem_min:
                        candidat.append(m)
                for m in candidat: #Pour tous les candidats possibles (ceux qui ont le moins de chemin (il y en a plusieurs au cas où d'égalités)) on réexécute le programme
                    chelsi=chess
                    chelsi[m]=n+1
                    self.caballero(chelsi, m, n+1, sol)
        else:
            return sol
        
    def ridorri(self,chess,k,n,sol=[]):
        print(chess)
        if len(sol)==0:
            a,b=k
            tablex.append(a)
            tabley.append(b)
            axes = plt.gca()
            axes.set_xlim(0, 7)
            axes.set_ylim(0, 7)
            plt.plot(tablex,tabley)
            plt.grid()
            plt.show()
            if n==64: # CONSTANTE A CHANGER
                if k in self.aretes((0,0)): #HERE
                    print("satoru")
                    sol.append(chess) #Retourne la grille d'échec numérotée
            else :
                poss=[]
                for m in self.aretes(k): #HERE
                    if chess[m]<=0: #Bien verifier que chess est un dictionnaire avec (i,j) et pas une liste qui prend uniquement un indice
                        poss.append(m)
                warn=[]
                for m in poss:
                    temporaire=[]
                    for p in self.aretes(m): #HERE
                        if chess[p]<=0:
                            temporaire.append(p)
                    warn.append(len(temporaire))
                if len(warn)==0: #Si warn est vide (pas de voisins)
                    nchem_min=0 #On ne choisit aucun chemin
                else:
                    nchem_min=min(warn)
                candidat=[]
                for (i,m) in enumerate(poss): #Dans la liste complète des voisins non marqués, on choisit celui qui a l'indice correspondant à la lonufuer la plus courte dans la liste warn
                    if warn[i]==nchem_min:
                        candidat.append(m)
                for m in candidat: #Pour tous les candidats possibles (ceux qui ont le moins de chemin (il y en a plusieurs au cas où d'égalités)) on réexécute le programme
                    chelsi=chess.copy()
                    chelsi[m]=n+1
                    self.ridorri(chelsi, m, n+1, sol)
        return sol
        

def euler(chess, k, n, sol=[]): #chess -> plateau / k -> sommet actuel / n -> compteur / sol -> liste de solutions
    if len(sol) == 0: #Check si on est dans une situation d'aller ou de retour (retourne la liste)
       if n == 64:#n compteur de case. Vu que le check de la case est égal a 1 quand on passe dessus et qu'il y a 64 cases ça marche
           if k in bond[0]: # Est-ce que sommet actuel est voisin de la case 0 ?
               sol.append(chess) # Si oui, c'est bon, et le chemin est validé
       else:
            poss=[] 
            for m in bond[k]: #Pour tous les voisins de k (sommet actuel)
                if chess[m]<0: #Si la case voisine n'a pas été marquée
                    poss.append(m) #On ajoute la case à poss

            warn=[]
            for m in poss: #Pour tous le sommets atteignables et non marqués
                temporaire=[]
                for p in bond[m]: #Pour tous les voisinss de chaque sommet
                    if chess[p]<0: #Si ils ne sont pas marqués, les ajouter
                        temporaire.append(p)
                warn.append(len(temporaire)) #ajouter la longueur (techniquement il y a m longueurs enregistrées)

            if len(warn)==0: #Si warn est vide (pas de voisins)
                nchem_min=0 #On ne choisit aucun chemin
            else:
                nchem_min=min(warn) #Sinon on récupère le voisin qui a le moins de chemins
            
            candidat=[]
            for (i,m) in enumerate(poss): #Dans la liste complète des voisins non marqués, on choisit celui qui a l'indice correspondant à la lonufuer la plus courte dans la liste warn
                if warn[i]==nchem_min:
                    candidat.append(m)

            for m in candidat: #Pour tous les candidats possibles (ceux qui ont le moins de chemin (il y en a plusieurs au cas où d'égalités)) on réexécute le programme
                euler(chess[:m]+[n+1]+chess[m+1:], m, n+1, sol)
    return sol


# rg, rg2 = range(8), range(64)


# move = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

# bond = [[k+8*p+q for (p, q) in move if k//8+p in rg and k %
#         8+q in rg] for k in rg2]

# print(bond)

# chess = [-1]*64

# chess[0] = 1


# sol = euler(chess, 0, 1, [])


# for _dep in range(64):
#    print(u'\nCase de départ %2d : (%d,%d)\n' % (_dep, _dep/8, _dep % 8))
#    chess = [1+(k+(64-sol[0][_dep])) % 64 for k in sol[0]]
#    for k in np.reshape(chess, (8, 8)):
#        print(k)

king=chess(8)
grille=springtrap(8)

print(king.ridorri(grille,(0,0),1,[]))
chess={"Kris":120,"Susie":140,"Ralsei":90}
chelsi=chess
chelsi["Ralsei"]=100
print(chess,chelsi)

# queen=chess(6)
# grille=springtrap(6)
# kris=queen.foster((0,0),(0,0), [],grille)

# chara=[]
# frisk=[]
# for i in range(len(kris)):
#     a,b=kris[i]
#     chara.append(a)
#     frisk.append(b)
# axes = plt.gca()
# axes.set_xlim(0, 6)
# axes.set_ylim(0, 6)
# plt.plot(tablex,tabley)
# plt.grid()
# plt.show()