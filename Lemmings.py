class Jeu:
    """ crée une partie de jeux """
    def __init__(self,carte):
        self.total_lmgs=[]
        self.carte=carte
        self.tab_carte=[]
        self.cond=True

    def crea_carte(self):
        """ crée la carte du jeux """
        f = open(self.carte,'r')
        for i in f:
            i=i.replace("\n","")
            i=i.replace("\t","")
            i=[i[k] for k in range(len(i))]
            self.tab_carte.append(i)

    def affiche(self):
        """ affiche la carte du jeux dans la console """
        for i in self.tab_carte:
            for k in i:
                print(k,end="")
            print()
        print()


    def tour(self):
        """ permet de faire jouer le tour de chaque lemmings dans l'ordre dans lequel ils sont apparus dans la partie """
        for i in self.total_lmgs:
            i.action(self)
        self.affiche()

    def demarre(self):
        """ permet de lancer la partie """
        self.crea_carte()
        self.affiche()
        while self.cond:
            rep= input()
            if rep == 'l':
                if self.tab_carte[0][1] == ' ':
                    self.total_lmgs.append(Lemming(0,1,1,self))
                    self.tab_carte[0][1] = '>'
                    self.affiche()
            elif rep == 'q':
                self.cond = False
            elif rep == 'e':
                self.tour()

class Lemming:
    """ crée un lemmings et le place sur la carte """
    def __init__(self,ligne,colonne,direction,Joueur):
        self.ligne=ligne
        self.colonne=colonne
        self.direction=direction
        self.Joueur=Joueur


    def __str__(self):
        """ retourne ">" si le lemmings est tourné vers la droite, "<" si il est tourné vers la gauche"""
        if self.direction == 1:
            return '>'
        else: return '<'

    def action(self,Joueur):
        """ permet de placer le lemmings sur la carte et de le faire se deplacer """
        if Joueur.tab_carte[self.ligne+1][self.colonne] == ' ':
            Joueur.tab_carte[self.ligne][self.colonne]= ' '
            self.ligne+=1
            Joueur.tab_carte[self.ligne][self.colonne] = str(self)
            return
        pos=Joueur.tab_carte[self.ligne][self.colonne+self.direction]
        if pos == ' ':
            Joueur.tab_carte[self.ligne][self.colonne]= ' '
            self.colonne+=self.direction
            Joueur.tab_carte[self.ligne][self.colonne] = str(self)
            return
        if pos == '#' or pos =='>' or pos == '<':
            self.direction = -self.direction
            return
        if pos == 'O':
            print("Un lemming est arrivé, bien joué !")
            Joueur.tab_carte[self.ligne][self.colonne]= ' '
            Joueur.total_lmgs.remove(self)






Joueur1=Jeu('carte2.txt')
Joueur1.demarre()










