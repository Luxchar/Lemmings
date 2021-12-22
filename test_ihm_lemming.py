from tkinter import*
import random
from PIL import ImageTk, Image
import os
from time import*

# On crée la fenêtre tkinter
fen= Tk()
dirpath = os.getcwd()
fen.title('Lemmings')

#Images du jeu :

lemming_img= ImageTk.PhotoImage(Image.open(dirpath+"/lemming2.png").resize((50, 50),Image.ANTIALIAS)) #Lemming tourné vers la droite
lemming_img2= ImageTk.PhotoImage(Image.open(dirpath+"/lemming3.png").resize((50, 50),Image.ANTIALIAS)) #Lemming tourné vers la gauche
bordure_img= ImageTk.PhotoImage(Image.open(dirpath+"/bordure2.png").resize((50, 50),Image.ANTIALIAS)) #Obstacles
porte= ImageTk.PhotoImage(Image.open(dirpath+"/porte.png").resize((110, 110),Image.ANTIALIAS)) #Objectif


class Jeu:
    """ crée une partie de jeux """
    def __init__(self,carte):
        self.total_lmgs=[]
        self.carte=carte
        self.tab_carte=[]
        self.cond=True
        self.cooldown=time()
        self.crea_carte()
        self.all_img=[]
        self.objectif=2
        self.score=0

    def crea_carte(self):
        """ crée la carte du jeu """
        f = open(self.carte,'r')
        for i in f:
            i=i.replace("\n","")
            i=[i[k] for k in range(len(i))]
            self.tab_carte.append(i)

    def affiche(self):
        """ affiche la carte du jeu sur la fenêtre tkinter"""
        for i in self.all_img:
            i.destroy()
        for i in range(len(self.tab_carte)):
            for k in range(len(self.tab_carte[i])):
                if self.tab_carte[i][k] == '#' or self.tab_carte[i][k] == '>' or self.tab_carte[i][k] == '<' or self.tab_carte[i][k] == 'O':
                    if self.tab_carte[i][k] == '#': lab=Label(image=bordure_img)
                    elif self.tab_carte[i][k] == '>': lab=Label(image=lemming_img)
                    elif self.tab_carte[i][k] == '<': lab=Label(image=lemming_img2)
                    elif self.tab_carte[i][k] == 'O': lab=Label(image=porte)
                    lab.grid(row=i,column=k)
                    self.all_img.append(lab)






    def tour(self):
        """ permet de faire jouer le tour de chaque lemmings dans l'ordre dans
        lequel ils sont apparus dans la partie """
        for i in self.total_lmgs:
            i.action(self)
        self.affiche()

    def demarre(self,event):
        """ permet de lancer la partie. A chaque fois que l'utilisateur appuie
        sur entrée dans le champs de texte entr1, l'utilisateur quitte le jeux
        si il a saisit q, fait jouer un tour si il a saisit e, fait apparaître un
        lemming si il a saisit l """
        rep= entr1.get()
        if time() - self.cooldown > 0.2:
            self.cooldown = time()
            if rep == 'l':
                if self.tab_carte[0][1] == ' ':
                    self.total_lmgs.append(Lemming(0,1,1,self))
                    self.tab_carte[0][1] = '>'
                    self.affiche()
            elif rep == 'q':
                fen.destroy()
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
            Joueur.score+=1
            if Joueur.score == Joueur.objectif:
                affiche_info.config(text='Vous avez ramené tous les lemmings bien joué !')
                entr1.destroy()
                bu=Button(fen,command=fen.destroy,text='Quitter')
                bu.grid(row=2,column=18)
                return
            affiche_info.config(text='Un lemming est arrivé, bien joué {}/{} !'.format(Joueur.score,Joueur.objectif))
            Joueur.tab_carte[self.ligne][self.colonne]= ' '
            Joueur.total_lmgs.remove(self)



"""----------------------------------Programme Principal---------------------------------------------------------------"""


maps=['carte1.txt','carte2.txt']
Partie1=Jeu(random.choice(maps))
Partie1.affiche()
affiche_info=Label(fen,text="")
affiche_info.grid(row=1,column=18)
entr1= Entry(fen)
entr1.grid(row=0,column=18)
entr1.bind("<Return>",Partie1.demarre)

fen.mainloop()