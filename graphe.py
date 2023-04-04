# coding: utf-8
import math
import numpy as np
""" 
Une classe Python pour creer et manipuler des graphes
"""


from re import A


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

    def add_sommet(self, sommet):
        """ Si le "sommet" n'set pas déjà présent
        dans le graphe, on rajoute au dictionnaire 
        une clé "sommet" avec une liste vide pour valeur. 
        Sinon on ne fait rien.
        """
        flag=True
        for i in self.all_sommets():
            if (i==sommet):
                flag=False
        if (flag==True):
            self._graphe_dict[sommet]=[]

    def add_arete(self, arete):
        """ l'arete est de  type set, tuple ou list;
            Entre deux sommets il peut y avoir plus
	    d'une arete (multi-graphe)
        """
        a,b=arete
        self._graphe_dict[a].append(b)
        self._graphe_dict[b].append(a)

    def trouve_chaine(self, sommet_dep, sommet_arr,chain=""):
        """renvoit toutes les chaines entre sommet_dep et sommet_arr"""
        chain=chain+sommet_dep
        if (sommet_dep==sommet_arr):
            return chain
        else:
            for k in self.aretes(sommet_dep):
                if k not in chain:
                    return self.trouve_chaine(k,sommet_arr,chain)

    def trouve_tout_chemin (self, sommet_dep,sommet_arr, chemin=[],chain="") :
        """Trouve tous les chemins possibles à partir d'un sommet"""
        chain=chain+sommet_dep
        if (sommet_dep==sommet_arr):
            chemin.append(chain)
        for k in self.aretes(sommet_dep):
            if k not in chain:
                chemin=self.trouve_tout_chemin(k,sommet_arr,chemin,chain)
        return chemin

    def __list_aretes(self):
        """ Methode privée pour récupérer les aretes. 
	    Une arete est un ensemble (set)
            avec un (boucle) ou deux sommets.
        """
        li=[]
        for i in (list(self._graphe_dict)):
            for j in(self._graphe_dict[i]):
                li.append([i,j])
        return li

    def copie_nb(self,som):
        '''Fonction permettant de remplacer un graphe avec des noms par un grpahe où les sommets ont representes par des entiers'''
        new = {}
        a=None
        ordr=len(self._graphe_dict)+1
        for i in range(1,ordr):
            new[i]=[]
        count=1
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
        graphe = Graphe2(new)
        return a,graphe


    def tri_largeur_ez(self,s):
        '''Parcours de graphe en largeur, ne traite que des graphes nommés comme des nombres de 1 à n'''
        ordr=len(self._graphe_dict)
        q=[s]
        d=[-1]
        for i in range(ordr):
            d.append(math.inf)
        d[s]=0
        t={}
        while (len(q)!=0):
            v = q.pop(0)
            for w in self.aretes(v):
                if d[w]==math.inf:
                    d[w]=d[v]+1
                    q.append(w)
                    if v in t.keys():
                        t[v].append(w)
                    else:
                        t[v]=[w]
        return d,t

    def tri_largeur(self,s):
        '''Parcours de graphe en largeur'''
        s,new=self.copie_nb(s)
        ordr=len(new._graphe_dict)
        q=[s]
        d=[-1]
        for i in range(ordr):
            d.append(math.inf)
        d[s]=0
        t={}
        while (len(q)!=0):
            v = q.pop(0)
            for w in new.aretes(v):
                if d[w]==math.inf:
                    d[w]=d[v]+1
                    q.append(w)
                    if v in t.keys():
                        t[v].append(w)
                    else:
                        t[v]=[w]
        return d,t

    def tri_longueur_ez(self,s):
        '''Parcours de graphe en profondeur, ne traite que des graphes nommés comme des nombres de 1 à n'''
        p=[s]
        d=[-1]
        ordr=len(self._graphe_dict)
        for i in range(ordr):
            d.append(math.inf)
        d[s]=0
        t={}
        while p:
            v=p.pop()
            for w in self.aretes(v):
                if d[w]==math.inf:
                    d[w]=d[v]+1
                    p.append(w)
                    if v in t.keys():
                        t[v].append(w)
                    else:
                        t[v]=[w]
        return(d,t)

    def tri_longueur(self,s):
        '''' Parcours de graphe en profondeur'''
        s,new=self.copie_nb(s)
        p=[s]
        d=[-1]
        ordr=len(new._graphe_dict)
        for i in range(ordr):
            d.append(math.inf)
        d[s]=0
        t={}
        while p:
            v=p.pop()
            for w in new.aretes(v):
                if d[w]==math.inf:
                    d[w]=d[v]+1
                    p.append(w)
                    if v in t.keys():
                        t[v].append(w)
                    else:
                        t[v]=[w]
        return(d,t)

    def Connexe_pr(self,s):
        '''Verifie si le graphe est connexe avec l algorithme de profondeur'''
        s,new=self.copie_nb(s)
        count=0
        p=[s]
        d=[-1]
        ordr=len(new._graphe_dict)
        for i in range(ordr):
            d.append(math.inf)
        d[s]=0
        t={}
        while p:
            count=count+1
            v=p.pop()
            for w in new.aretes(v):
                if d[w]==math.inf:
                    d[w]=d[v]+1
                    p.append(w)
                    if v in t.keys():
                        t[v].append(w)
                    else:
                        t[v]=[w]
        if (count==ordr):
            return True
        else:
            return False

    def Connexe_lar(self,s):
        '''Verifie si le graphe est connexe avec l algorithme de largeur'''
        s,new=self.copie_nb(s)
        count=0
        ordr=len(new._graphe_dict)
        q=[s]
        d=[-1]
        for i in range(ordr):
            d.append(math.inf)
        d[s]=0
        t={}
        while (len(q)!=0):
            count=count+1
            v = q.pop(0)
            for w in new.aretes(v):
                if d[w]==math.inf:
                    d[w]=d[v]+1
                    q.append(w)
                    if v in t.keys():
                        t[v].append(w)
                    else:
                        t[v]=[w]
        if (count==ordr):
            return True
        else:
            return False

    def Connexe_cycl(self,s):
        '''Retourne la presence d'un cycle dans un graphe du point s au point s'''
        s,new=self.copie_nb(s)
        count=0
        ordr=len(new._graphe_dict)
        q=[s]
        d=[-1]
        for i in range(ordr):
            d.append(math.inf)
        d[s]=0
        t={}
        while (len(q)!=0):
            v = q.pop(0)
            for w in new.aretes(v):
                if (w==s):
                    return True
                if d[w]==math.inf:
                    d[w]=d[v]+1
                    q.append(w)
                    if v in t.keys():
                        t[v].append(w)
                    else:
                        t[v]=[w]
        if (count==ordr):
            return False
        else:
            return False

    def cle_aretus(self,s):
        dic=self._graphe_dict[s]
        lis=dic.keys()
        return lis


    def Dijkstra(self,s):
        '''Algorithme de Dijkstra'''
        d=[-1]
        ordr=len(self._graphe_dict)
        for i in range(ordr):
            d.append(math.inf)
        d[s]=0
        p=[-1]
        for i in range(ordr):
            p.append(None)
        q=[]
        for i in range(ordr):
            q.append(i+1)

        while q:
            deedee=q[0]
            for i in q:
                if d[i]<=d[deedee]:
                    deedee=i
            v=deedee
            flag=True
            comt=0
            while flag:
                if q[comt]==v:
                    flag=False
                    q.pop(comt)
                comt=comt+1

            for u in self.aretes(v):
                if (u in q):
                    w=self.aretes(v)
                    if (d[u] > d[v] + w[u]):
                        d[u]=d[v]+w[u]
                        p[u]=v
        return (d,p)

    def Chemin_court(self,d,P):
        '''Recupere un chemin pour le trier'''
        L=[]
        L.append(d)
        v=d
        while (P[v]!=None):
            L.append(P[v])
            v=P[v]
        L.reverse()
        return L

    def Beauwoman(self,s):
        '''Bellman avec test de redondance'''
        d=[-1]
        ordr=len(self._graphe_dict)
        for i in range(ordr):
            d.append(math.inf)
        d[s]=0
        p=[-1]
        for i in range(ordr):
            p.append(None)
        for i in range (1,ordr-1):
            update=False
            for arc in self.__list_aretes():
                u = arc[0]
                v = arc[1]
                w=self.aretes(u)
                if (d[v]>d[u]+w[v]):
                    d[v]=d[u]+w[v]
                    p[v]=u
                    update=True
            if (update==False):
                break
        for arc in self.__list_aretes():
            u = arc[0]
            v = arc[1]
            w=self.aretes(u)
            if d[v]>d[u]+w[v]:
                return False
        return (d,p)

    def Bellman(self,s):
        '''Algorithme de Bellman'''
        d=[-1]
        ordr=len(self._graphe_dict)
        for i in range(ordr):
            d.append(math.inf)
        d[s]=0
        p=[-1]
        for i in range(ordr):
            p.append(None)
        for i in range (1,ordr-1):
            for arc in self.__list_aretes():
                u = arc[0]
                v = arc[1]
                w=self.aretes(u)
                if (d[v]>d[u]+w[v]):
                    d[v]=d[u]+w[v]
                    p[v]=u
        for arc in self.__list_aretes():
            u = arc[0]
            v = arc[1]
            w=self.aretes(u)
            if d[v]>d[u]+w[v]:
                return False
        return (d,p)

    def mat_to_list(self,mat):
        '''Translate une matrice adjacente en liste'''
        ordr=len(mat)
        dic={}
        for i in range(ordr):
            list=[]
            for j in range(ordr):
                if mat[i,j]==1:
                    list.append(j+1)
            dic[i+1]=list
        return dic

    def list_to_mat(self):
        '''Translate une liste en matrice adjacente'''
        ordr=len(self._graphe_dict)
        matrix = np.empty((0,ordr))
        for i in self._graphe_dict:
            list=[]
            for k in range (ordr):
                if k+1 in self.aretes(i):
                    list.append(1)
                else:
                    list.append(0)
            matrix = np.r_[matrix,[list]]
        return matrix

    def warshall(self):
        '''Algorithme de Warshall'''
        ordr=len(self._graphe_dict)
        madpat=self.list_to_mat()
        for k in range(ordr):
            for i in range(ordr):
                for j in range(ordr):
                    if (madpat[i,k]==1 and madpat[k,j]==1):
                        madpat[i,j]=1
        return madpat

    def __next__(self):
        """ Pour itérer sur les sommets du graphe """
        return next(self._iter_obj)
    
    def __str__(self):
        res = "sommets: "
        for k in self._graphe_dict.keys():
            res += str(k) + " "
        res += "\naretes: "
        for arete in self.__list_aretes():
            res += str(arete) + " "
        return res

class Graphe2(Graphe):

    def sommet_degre(self, sommet):
        """ renvoie le degre du sommet """
        degre=0
        for k in self.aretes(sommet):
            degre=degre+1
        return degre

    def trouve_sommet_isole(self):
        """ renvoie la liste des sommets isoles """
        isole=[]
        for k in self.all_sommets():
            if self.sommet_degre(k)==0:
                isole.append(k)
        return isole

    def Delta(self):
        """ le degre maximum """
        max=-1
        for k in self.all_sommets():
            if  max<=self.sommet_degre(k):
                max=self.sommet_degre(k)
                maximus=k
        if max>-1:
            return maximus
        else:
            print("PROBLEME ! Il semblerait que le graphe soit vide")


    def list_degres(self):
        """ calcule tous les degres et renvoie un
        tuple de degres decroissant
        """
        degres=[]
        for k in self.all_sommets():
            degres.append(self.sommet_degre(k))
        for i in range(len(degres)):
            for j in range (len(degres)):
                if degres[i]<=degres[j]:
                    a=degres[i]
                    degres[i]=degres[j]
                    degres[j]=a
        return degres

grapheSimpple = {"A":["D","F"],"B":["C","E"],"C":["B","C","D","E"],"D":["A","C","F","E"],"E":["B","C","D"],"F":["A","D"],"G":[]}
graphicSimple = {1:[4,6],2:[3],3:[2,4,5],4:[1,3,6],5:[3],6:[1,4]}
grapheCompl = {1:{2:10,3:2},2:{},3:{2:2}}
grapheNeg={1:{2:-15,3:-1},2:{3:-1,4:-2},3:{2:-15,4:-8,5:-2},4:{5:-7},5:{4:9}}
test1 = Graphe2(graphicSimple)
test2 = Graphe2(graphicSimple)