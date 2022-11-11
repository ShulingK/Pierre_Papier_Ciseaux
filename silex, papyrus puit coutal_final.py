# on admet la fonction random
    

##silex 0, papyrus 1, coutal 2, puit 666

#definir la fonction round avec pour parametre eventJoueurUn et eventJoueurDeux  
#   Assigner a joueurDeuxAction le retour du int() prenant en parametre eventJoueurUn
#   Assigner a joueurUnAction le retour du int() prenant en parametre eventJoueurDeux
#   si joueurUnAction est inferieur a 0 ou supérieur à 2 
#       alors retourner le message "demande incorrect"
#   assigner à joueurDeuxAction un chiffre random entre 0 et 2 
#   si joueurUnAction est égal à joueurDeuxAction 
#       alors retourner le message "match nul"
#   si joueurUnAction est supérieur à joueurDeuxAction et que que joueurDeuxAction plus 1 est égal à joueurUnAction
#   ou que joueurUnAction est inférieur à joueurDeuxAction et que la somme de joueurUnAction et joueurDeuxAction donne 3 
#       alors retourner le message "manche gagnée par joueur 1"
#   sinon retourner le message "manche gagnée par joueur 2"
#   si joueurUnAction est égale à 666 
#       alors afficher le message "manche gagné par joueur 1"
#   si joueurDeuxAction est égale à 666 
#       alors afficher le message "manche gagné par joueur 2"
#   si joueurUnAction ou joueurDeuxAction est égal à 666
#       alors afficher "match nul"


##jeu en 1vs1

#definir la fonction game
#   initialiser joueurUnScore à 0 
#   initialiser joueurDeuxScore à 0 
#   répéter indéfiniment dans une boucle tant que   
#       assigner à inputClavierUn l'information de l'input du clavier sous format int sachant que ( silex (0) papyrus (1) coutal (2) afficher score (4) fin (5))
#       si inputClavierUn est égal à 4
#           alors afficher joueurUnScore et joueurDeuxScore 
#       sinon si inputClavierUn est égal à 5 
#           alors si joueurUnScore est supérieur à joueurDeuxScore
#               alors afficher "bravo joueur 1"
#           sinon afficher "bravo joueur 2"
#           sortir de la boucle 
#       sinon si inputClavierUn est égal à 3
#           assigner à joueurUnInput l'information de l'input du clavier sous format int ( silex (0) papyrus (1) coutal (2) ?)
#           assigner à joueurDeuxInput l'information de l'input du clavier sous format int ( silex (0) papyrus (1) coutal (2) ?)
#           assigner à result le retour de l'execultion de la fonction round avec les parametres joueurUnInput et joueurDeuxInput
#           si result est égal à "manche gagnée par joueur 1"
#               incrementer joueurUnScore de 1
#           sinon si result est égal à "manche gagnée par joueur 2"
#               incrementer joueurDeuxScore de 1
#           sinon afficher result
## avec BO
#       sinon inputClavierUn est égal à 6
#           assigner à nbrTours l'information de l'input du clavier sous format int "le nombre de manche necessaire pour gagner"
#           assigner à joueurUnInput l'information de l'input du clavier sous format int ( silex (0) papyrus (1) coutal (2) ?)
#           assigner à joueurDeuxInput l'information de l'input du clavier sous format int ( silex (0) papyrus (1) coutal (2) ?)
#           assigner à result le retour de l'execultion de la fonction round avec les parametres joueurUnInput et joueurDeuxInput
#               incrementer joueurUnScore de 1
#               si joueurUnScore est égal a nbrTours
#                   alors afficher vainqueur joueur 1 avec joueurUnScore point(s) (retour à la ligne) perdant joueur 2 avec joueurDeuxScore point(s)
#               sortir de la boucle
#           sinon si result est égal à "manche gagnée par joueur 2"
#               incrementer joueurDeuxScore de 1
#                   alors afficher vainqueur joueur 2 avec joueurDeuxScore point(s) (retour à la ligne) perdant joueur 1 avec joueurUnScore point(s)
#               sortir de la boucle

        



##jeu en 1vsbot


#definir la fonction game
#   initialiser joueurScore à 0 
#   initialiser botScore à 0 
#   répéter indéfiniment dans une boucle tant que   
#       assigner à inputClavierUn l'information de l'input du clavier sous format int sachant que ( silex (0) papyrus (1) coutal (2) afficher score (4) fin (5))
#       si inputClavierUn est égal à 4
#           alors afficher joueurScore et botScore 
#       sinon si inputClavierUn est égal à 5 
#           alors si joueurScore est supérieur à botScore
#               alors afficher "bravo à vous!!!"
#           sinon afficher "dommage..."
#           sortir de la boucle 
#       sinon si inputClavierUn est égal à 3
#           assigner à inputClavierDeux l'information de l'input du clavier sous format int ( silex (0) papyrus (1) coutal (2) ?)
#           assigner à botGame un nombre random sous format int entre 0 et 2
#           assigner à result le retour de l'execultion de la fonction round avec les parametres joueurInput et botGame
#           si result est égal à "manche gagnée par joueur 1"
#               incrementer joueurScore de 1
#           sinon result est égal à "manche gagnée par joueur 2"
#               incrementer botScore de 1
#           sinon afficher result
