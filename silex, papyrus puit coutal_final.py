# on admet la fonction random
import random
    

##silex 0, papyrus 1, coutal 2, puit 9

#definir la fonction round avec pour parametre eventJoueurUn et eventJoueurDeux
def round(eventJoueurUn, eventJoueurDeux):    
#   Assigner a joueurDeuxAction le retour du int() prenant en parametre eventJoueurUn
    joueurUnAction = int(eventJoueurUn)
#   Assigner a joueurUnAction le retour du int() prenant en parametre eventJoueurDeux
    joueurDeuxAction = int(eventJoueurDeux)
#   si joueurUnAction est inferieur a 0 ou supérieur à 2 
    if(joueurUnAction < 0 or joueurDeuxAction > 2):
#       alors retourner le message "demande incorrect"
        print("demande incorrecte\n")
        return "demande incorrecte"
#   si joueurUnAction est égal à joueurDeuxAction 
    if(joueurUnAction == joueurDeuxAction):
#       alors retourner le message "match nul"
        print("match nul\n")
        return "match nul"
#   si joueurUnAction est égale à
    if(joueurUnAction == 9):
#       alors retourner le message "manche gagnée par joueur 1"
        print("manche gagnée par joueur 1\n")
        return "manche gagnée par joueur 1"
#   si joueurDeuxAction est égale à 9 
    if(joueurDeuxAction == 9):
#       alors retourner le message "manche gagnée par joueur 2"
        print("manche gagnée par joueur 2\n")
        return "manche gagnée par joueur 2"
#   si joueurUnAction est supérieur à joueurDeuxAction et que joueurDeuxAction plus 1 est égal à joueurUnAction
#   ou que joueurUnAction est inférieur à joueurDeuxAction et que la somme de joueurUnAction et joueurDeuxAction donne 3 
    if(joueurUnAction > joueurDeuxAction and joueurDeuxAction + 1 == joueurUnAction or joueurUnAction < joueurDeuxAction and joueurUnAction + joueurDeuxAction == 3 ):   
#       alors retourner le message "manche gagnée par joueur 1"
        print("manche gagnée par joueur 1\n")
        return "manche gagnée par joueur 1"
#   sinon retourner le message "manche gagnée par joueur 2"
    print("manche gagnée par joueur 2\n")
    return "manche gagnée par joueur 2"

##jeu en 1vs1

#definir la fonction game
def game():
#   assigner à  le retour de l'execultion de la fonction round avec les parametres joueurUnInput et joueurDeuxInput
    useBot = False
    doYouWantABot = input("veux tu jouer contre un bot ?")
    if(doYouWantABot == "oui"):
    #   initialiser joueurScore à 0 
        joueurScore = 0
    #   initialiser botScore à 0
        botScore = 0 
    #   répéter indéfiniment dans une boucle tant que  
        while True:
    #       assigner à inputClavierUn l'information de l'input du clavier sous format int sachant que ( silex (0) papyrus (1) coutal (2) afficher score (4) fin (5))
            inputClavierUn = int(input("commencer à jouer(3) afficher score (4) fin (5) BO(6) ?: "))
    #       si inputClavierUn est égal à 4
            if(inputClavierUn == 4):
    #           alors afficher joueurScore et botScore 
                print(joueurScore,"à", botScore, "\n")
    #       sinon si inputClavierUn est égal à 5
            elif(inputClavierUn == 5):
    #           alors si joueurScore est supérieur à botScore
                if(joueurScore > botScore):
    #               alors afficher "bravo à vous!!!"
                    print("bravo à vous!!!\n\n\n")
    #           sinon afficher "dommage..."
                else: 
                    print("quel dommage...\n\n\n")
    #           sortir de la boucle 
                break
    #       sinon si inputClavierUn est égal à 3
            elif(inputClavierUn == 3):
    #           assigner à inputClavierDeux l'information de l'input du clavier sous format int ( silex (0) papyrus (1) coutal (2) ?)
                inputClavierDeux = int(input("silex (0) papyrus (1) coutal (2) ?"))
    #           assigner à botGame un nombre random sous format int entre 0 et 2
                botGame = random.randint(0, 2)
    #           assigner à result le retour de l'execultion de la fonction round avec les parametres inputClavierDeux et botGame
                result = round(inputClavierDeux, botGame)
    #           si result est égal à "manche gagnée par joueur 1"
                if(result == "manche gagnée par joueur 1"):
    #               incrementer joueurScore de 1
                    joueurScore += 1
    #           sinon result est égal à "manche gagnée par joueur 2"
                elif(result == "manche gagnée par joueur 2"):
    #               incrementer botScore de 1
                    botScore += 1
    #           sinon afficher result
                else:
                    print(result)
    ## avec BO
    #       sinon inputClavierUn est éga l à 6
            elif(inputClavierUn == 6):
    #           assigner à nbrTours l'information de l'input du clavier sous format int "le nombre de manche necessaire pour gagner"
                nbrTours = int(input("le nombre de manche necessaire pour gagner ?: "))
    #           assigner à inputClavierDeux l'information de l'input du clavier sous format int ( silex (0) papyrus (1) coutal (2) ?)
                inputClavierDeux = int(input("silex (0) papyrus (1) coutal (2) ?: "))
    #           assigner à botGame un nombre random sous format int entre 0 et 2
                botGame = random.randint(0, 2)
    #            si result est égal à "manche gagnée par joueur 1 "
                if(result == "manche gagnée par joueur 1"):
    #               incrementer joueurUnScore de 1
                    joueurUnScore += 1
    #               si joueurUnScore est égal au nbrTours
                    if(joueurUnScore == nbrTours):
    #                   alors afficher vainqueur joueur 2 avec joueurDeuxScore point(s) (retour à la ligne) perdant joueur 1 avec joueurUnScore point(s)
                        print("joueur 1 vainqueur")
    #               sortir de la boucle
                    break
    #           sinon si result est égal à "manche gagnée par joueur 2"
                elif(result == "manche gagnée par joueur 2"):
    #               incrementer joueurDeuxScore de 1
                    joueurDeuxScore += 1
    #               si joueurDeuxScore est égal à nbrTours
                    if(joueurDeuxScore == nbrTours):
    #                   alors afficher vainqueur joueur 1 avec joueurUnScore point(s) (retour à la ligne) perdant joueur 2 avec joueurDeuxScore point(s)
                        print("vainqueur joueur 2 avec ",joueurDeuxScore ,"point(s)\n perdant joueur 1 avec ",joueurUnScore ,"point(s)")            
    #               sortir de la boucle
                    break
                else:
                    print(result)
            else:
                print("erreur")
    else:

 
    #   initialiser joueurUnScore à 0 
        joueurUnScore = 0
    #   initialiser joueurDeuxScore à 0 
        joueurDeuxScore = 0
    #   répéter indéfiniment dans une boucle tant que   
        while True:
    #       assigner à inputClavierUn l'information de l'input du clavier sous format int sachant que ( silex (0) papyrus (1) coutal (2) afficher score (4) fin (5))
            inputClavierUn = int(input("commencer à jouer(3) afficher score (4) fin (5) BO(6) ?: "))
    #       si inputClavierUn est égal à 4
            if(inputClavierUn == 4):
    #           alors afficher joueurUnScore et joueurDeuxScore
                print(joueurUnScore," à ", joueurDeuxScore, "\n")
    #       sinon si inputClavierUn est égal à 5
            elif(inputClavierUn == 5):
    #           alors si joueurUnScore est supérieur à joueurDeuxScore
                if(joueurUnScore > joueurDeuxScore):
    #               alors afficher "bravo joueur 1"
                    print("bravo joueur 1")
    #           sinon afficher "bravo joueur 2"
                else:
                    print("bravo joueur 2")
    #           sortir de la boucle 
                break
    #       sinon si inputClavierUn est égal à 3
            elif(inputClavierUn == 3):
    #           assigner à joueurUnInput l'information de l'input du clavier sous format int ( silex (0) papyrus (1) coutal (2) ?)
                joueurUnInput = int(input("silex (0) papyrus (1) coutal (2) ?: "))
    #           assigner à joueurDeuxInput l'information de l'input du clavier sous format int ( silex (0) papyrus (1) coutal (2) ?)
                joueurDeuxInput = int(input("silex (0) papyrus (1) coutal (2) ?: "))
    #           assigner à result le retour de l'execultion de la fonction round avec les parametres joueurUnInput et joueurDeuxInput
                result = round  (joueurUnInput, joueurDeuxInput)
    #           si result est égal à "manche gagnée par joueur 1"
                if(result == "manche gagnée par joueur1"):
    #               incrementer joueurUnScore de 1
                    joueurUnScore += 1
    #           sinon si result est égal à "manche gagnée par joueur 2"
                elif(result == "manche gagnée par joueur 2"):
    #               incrementer joueurDeuxScore de 1
                    joueurDeuxScore += 1


    ## avec BO
    #       sinon inputClavierUn est égal à 6
            elif(inputClavierUn == 6):
    #           assigner à nbrTours l'information de l'input du clavier sous format int "le nombre de manche necessaire pour gagner"
                nbrTours = int(input("le nombre de manche necessaire pour gagner ?: "))
    #           assigner à joueurUnInput l'information de l'input du clavier sous format int ( silex (0) papyrus (1) coutal (2) ?)
                joueurUnInput = int(input("silex (0) papyrus (1) coutal (2) ?: "))
    #           assigner à joueurDeuxInput l'information de l'input du clavier sous format int ( silex (0) papyrus (1) coutal (2) ?)
                joueurDeuxInput = int(input("silex (0) papyrus (1) coutal (2) ?: "))
    #           assigner à result le retour de l'execultion de la fonction round avec les parametres joueurUnInput et joueurDeuxInput
                result = round(joueurUnInput, joueurDeuxInput)
                if(result == "manche gagnée par joueur1"):
    #               incrementer joueurUnScore de 1
                    joueurUnScore += 1
    #               si joueurUnScore est égal au nbrTours
                    if(joueurUnScore == nbrTours):
    #                   alors afficher vainqueur joueur 2 avec joueurDeuxScore point(s) (retour à la ligne) perdant joueur 1 avec joueurUnScore point(s)
                        print("joueur 1 vainqueur")
    #               sortir de la boucle
                    break
    #           sinon si result est égal à "manche gagnée par joueur 2"
                elif(result == "manche gagnée par joueur 2"):
    #               incrementer joueurDeuxScore de 1
                    joueurDeuxScore += 1
    #               si joueurDeuxScore est égal à nbrTours
                    if(joueurDeuxScore == nbrTours):
    #                   alors afficher vainqueur joueur 1 avec joueurUnScore point(s) (retour à la ligne) perdant joueur 2 avec joueurDeuxScore point(s)
                        print("vainqueur joueur 2 avec ",joueurDeuxScore ,"point(s)\n perdant joueur 1 avec ",joueurUnScore ,"point(s)")            
    #               sortir de la boucle
                    break
            else:
                print("erreur")



game()