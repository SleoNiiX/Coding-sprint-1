"""
Created on Sat Sep 30 14:59:18 2023

@author: Cardoso
"""
import random as r



def Calcul_mental_addition():
    """
        Propose l’exercice de calcul mental
    consistant en l’addition de ces deux nombres 
    tirer aleatoirement grace au module random.
    """
    #On affecte deux nombres aleatoires aux variables nb_1 et nb_2, Et on calcule la somme de ces nombres
    nb_1, nb_2 = r.randint(10, 99), r.randint(10, 99)   
    somme = nb_1 + nb_2
    
    #On demande à l'utilisateur de calculer cette somme et on lui affiche si il a raison ou non
    réponse = int(input(f"Quel est le resultat de l'operation {nb_1} + {nb_2} : "))
    print(f"Bravo ! la reponse etait bien {réponse}" if somme == réponse else f"Oh non... Tu t'es trompe, la reponse etait : {somme}")


def Boucle_calc_mental_addition():
    """
        Demande a l’utilisateur combien
    d’additions il souhaite resoudre dans l’exercice.
    Il lui sera alors propose autant d'addition.
    """
    #On demande combien d'addition il souhaite faire et fais une boucle de n calcul souhaitez en reprenant la fonction precedente
    nombre_calcul = int(input("Combien d'addition veux-tu faire ? "))
    
    for i in range(nombre_calcul):
        #On affecte deux nombres aleatoires aux variables nb_1 et nb_2, Et on calcule la somme de ces nombres
        nb_1, nb_2 = r.randint(10, 99), r.randint(10, 99)   
        somme = nb_1 + nb_2
        
        #On demande à l'utilisateur de calculer cette somme et on lui affiche si il a raison ou non
        réponse = int(input(f"\nOperation {i+1} sur {nombre_calcul} : {nb_1} + {nb_2} = "))
        print(f"Bravo ! la reponse etait bien {réponse}" if somme == réponse else f"Oh non... Tu t'es trompe, la reponse etait : {somme}")
    
    print("\nC'est fini ! tu as fais toutes les additions !")


def Boucle_calc_mental_addition2():
    """
        Version de la fonction precedente
    avec un compteur de bonne reponse.
    """
    #On initialise un compteur de bonne réponse
    compteur = 0
    nombre_calcul = int(input("Combien d'addition veux-tu faire ? "))
    
    for i in range(nombre_calcul):
        nb_1, nb_2 = r.randint(10, 99), r.randint(10, 99)   
        somme = nb_1 + nb_2
        
        réponse = int(input(f"\nOperation {i+1} sur {nombre_calcul} : {nb_1} + {nb_2} = "))
        
        #On incremente de 1 le compteur à chaque bonne réponse
        if somme == réponse:
            print(f"Bravo ! la reponse etait bien {réponse}")
            compteur += 1
        else:
            print(f"Oh non... Tu t'es trompe, la reponse etait : {somme}")
    
    #Calcul du pourcentage de bonne reponse arrondi a deux chiffres apres la virgule avec round()
    pourcentage_reponse = round(compteur * 100 / nombre_calcul,2)
    
    #Affiche une phrase personnalise selon son taux de bonne reponse
    if pourcentage_reponse == 100:
        print("Parfait ! 100% de bonne reponse !")
    elif pourcentage_reponse < 30:
        print(f"Retourne a l’ecole ! Tu n'as fais que {pourcentage_reponse}% de bonne reponse")
    elif pourcentage_reponse < 60: 
        print(f"Des progres sont necessaires. Ton pourcentage de bonne reponse est de {pourcentage_reponse}%")
    elif pourcentage_reponse < 90:
        print(f"Bons resultats. Tu as reussi {pourcentage_reponse}% des calculs.")
    else:
        print(f"Calculateur hors pair ! {pourcentage_reponse}% de tes calculs sont juste !")
    
    
 
### 1.1 Commencons simple ###    

#Calcul_mental_addition()
#Boucle_calc_mental_addition()
#Boucle_calc_mental_addition2()

### Decommenter pour tester les fonctions ! ###



def Difficulte_bcma():
    """
        bcma : Boucle_calc_mental_addition
        
        Demander d’entrer un entier d compris entre 0 et 4 a l'utilisateur.
    S’il saisit d entre 1 et 4, vous lui demander des additions de nombres de
    d chiffres exactement. Et s'il saisi 0 ce sera un nombre d de chiffre
    aléatoire.
    """
    #Boucle  while qui demande le choix de la difficulté entre 0 et 4
    choix_invalide = True
    while choix_invalide:
        choix_difficulte = int(input("De quel difficulte souhaites-tu que tes calculs soit entre 0 et 4 : "))
        
        if choix_difficulte >=0 and choix_difficulte <5: choix_invalide = False
        
    #Liste utiliser dans le cas ou choix_difficulte = 0
    difficulte0 = [10, 100, 1000, 10000]
    compteur = 0
    nombre_calcul = int(input("Combien d'addition veux-tu faire ? "))
    
    for i in range(nombre_calcul):
        #Liste qui defini le nombre de chiffre - 1. Et qui dans le cas de 0 vas donner un nombre de chiffre different a chaque calcul
        difficulte = [difficulte0[r.randint(0,3)], 10, 100, 1000, 10000]
        nb_1, nb_2 = r.randint(1, difficulte[choix_difficulte]-1), r.randint(1, difficulte[choix_difficulte]-1)   
        somme = nb_1 + nb_2
        
        réponse = int(input(f"\nOperation {i+1} sur {nombre_calcul} : {nb_1} + {nb_2} = "))
        
        if somme == réponse:
            print(f"Bravo ! la reponse etait bien {réponse}")
            compteur += 1
        else:
            print(f"Oh non... Tu t'es trompe, la reponse etait : {somme}")
    
    pourcentage_reponse = round(compteur * 100 / nombre_calcul,2)
    
    if pourcentage_reponse == 100:
        print("Parfait ! 100% de bonne reponse !")
    elif pourcentage_reponse < 30:
        print(f"Retourne a l’ecole ! Tu n'as fais que {pourcentage_reponse}% de bonne reponse")
    elif pourcentage_reponse < 60: 
        print(f"Des progres sont necessaires. Ton pourcentage de bonne reponse est de {pourcentage_reponse}%")
    elif pourcentage_reponse < 90:
        print(f"Bons resultats. Tu as reussi {pourcentage_reponse}% des calculs.")
    else:
        print(f"Calculateur hors pair ! {pourcentage_reponse}% de tes calculs sont juste !")
        


### 1.2 Choix d’un niveau de difficulte ###

#Difficulte_bcma()

### Decommenter pour tester les fonctions ! ###



def Complexite_dbcma():
    """
        dbcma : Difficulte_boucle_calc_mental_addition
        
        Demander d’entrer un entier d compris entre 0 et 4 a l'utilisateur.
    S’il saisit 1, on lui fait faire des additions, s’il saisit 2, 3 ou 4, on lui fait
    faire respectivement des soustractions, des multiplications et des divisions.
    S’il saisit 0, le programme decide aleatoirement a chaque question le type
    d’operation a resoudre.
    """
    #On ajoute le choix de la complexite dans la boucle
    choix_invalide = True
    while choix_invalide:
        choix_difficulte = int(input("De quel difficulte souhaites-tu que tes calculs soit entre 0 et 4 : "))
        choix_complexite = int(input("De quel complexite souhaites-tu que tes calculs soit entre 0 et 4 : "))
        
        if (choix_difficulte >=0 and choix_difficulte <5) and (choix_complexite >=0 and choix_complexite <5): choix_invalide = False
        
    difficulte0 = [10, 100, 1000, 10000]
    complexite = ["+", "-", "*", "/"]
    compteur = 0
    nombre_calcul = int(input("Combien d'opération veux-tu faire ? "))
    
    for i in range(nombre_calcul):
        difficulte = [difficulte0[r.randint(0,3)], 10, 100, 1000, 10000]
        nb_1, nb_2 = r.randint(1, difficulte[choix_difficulte]-1), r.randint(1, difficulte[choix_difficulte]-1)   
        
        #On fait les différents calculs
        somme, soustraction = nb_1 + nb_2, nb_1 - nb_2 
        multiplication, division = nb_1 * nb_2, nb_1 / nb_2
        Calcul0 = [somme, soustraction, multiplication, division]
        random_complexite = r.randint(0,3)
        
        #Liste des opérations pour la question et liste des calculs pour celui que l'utilisateur a choisi
        Operation = [complexite[random_complexite], "+", "-", "*", "/"]
        Calcul = [Calcul0[random_complexite], somme, soustraction, multiplication, division]
        
        réponse = int(input(f"\nOperation {i+1} sur {nombre_calcul} : {nb_1} {Operation[choix_complexite]} {nb_2} = "))
        
        if Calcul[choix_complexite] == réponse:
            print(f"Bravo ! la reponse etait bien {réponse}")
            compteur += 1
        else:
            print(f"Oh non... Tu t'es trompe, la reponse etait : {Calcul[choix_complexite]}")
    
    pourcentage_reponse = round(compteur * 100 / nombre_calcul,2)
    
    if pourcentage_reponse == 100:
        print("\nParfait ! 100% de bonne reponse !")
    elif pourcentage_reponse < 30:
        print(f"\nRetourne a l’ecole ! Tu n'as fais que {pourcentage_reponse}% de bonne reponse")
    elif pourcentage_reponse < 60: 
        print(f"\nDes progres sont necessaires. Ton pourcentage de bonne reponse est de {pourcentage_reponse}%")
    elif pourcentage_reponse < 90:
        print(f"\nBons resultats. Tu as reussi {pourcentage_reponse}% des calculs.")
    else:
        print(f"\nCalculateur hors pair ! {pourcentage_reponse}% de tes calculs sont juste !")
        
        
        
### 1.3 Choix d’un niveau de complexite ###

#Complexite_dbcma()

### Decommenter pour tester les fonctions ! ###