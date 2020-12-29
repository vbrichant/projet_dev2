from random import randint


def fonction_init_grille(nbrs_bombes, nbrs_colones, nbrs_lignes):
    grille = [[0 for a in range(nbrs_lignes)] for b in range(nbrs_colones)]
    bombes_pose = 0
    c = nbrs_lignes - 1
    d = nbrs_colones - 1
    while bombes_pose < nbrs_bombes:
        x = randint(0, int(d))
        y = randint(0, int(c))
        if grille[x][y] == 0:
            grille[x][y] = 9
            bombes_pose += 1
    return grille


def fonction_test_bombe(grille, colone, ligne):
    if grille[ligne][colone] == 9:
        return True
    return False


def calcul_nbrs_bombes_alentours(grille, nbrs_colones, nbrs_lignes, num_colones, num_lignes):
    num_lignes -= 1
    num_colones -= 1
    nbrs_bombes_alentours = 0
    i = 0
    while i < 3:
        u = 0
        while u < 3:
            if num_lignes + i < nbrs_lignes - 1 and num_colones + u < nbrs_colones - 1:
                a = grille[num_lignes + i][num_colones + u]
                if a == 9:
                    nbrs_bombes_alentours += 1
            u += 1
        i += 1
    return nbrs_bombes_alentours


def fonction_affichage_grille(grille, nbrs_lignes):
    texte_a_afficher = ''
    i = 0
    while i < nbrs_lignes - 1:
        texte_a_afficher += str(grille[i]) + '\n'
        i += 1
    print(texte_a_afficher)


def main():
    nbrs_bombes = 9
    nbrs_colones = 6
    nbrs_lignes = 6
    nbrs_tours = 1
    bombes_restantes = nbrs_bombes
    bombes_marquer = 0
    grille_complette = fonction_init_grille(nbrs_bombes, nbrs_colones, nbrs_lignes)
    grille_a_completer = [["." for a in range(nbrs_lignes)] for b in range(nbrs_colones)]
    partie_finie = False
    verifier = False

    fonction_affichage_grille(grille_complette, nbrs_lignes)
    fonction_affichage_grille(grille_a_completer, nbrs_lignes)

    while not partie_finie:
        choix_ligne = 0
        choix_colone = 0
        print("Tour " + str(nbrs_tours))
        fonction_affichage_grille(grille_a_completer, nbrs_lignes)
        choix_action = input(
            "Voulez vous creuser(c),\nDéminer/placer un drapeaux(d),\nVérifier les bombes déjà identifiée(v),\nOu quitter la partie(q)\n")

        if choix_action in ['q', 'q']:
            partie_finie = True
            print("Vous avez abondonné.\nIl vous restait a trouver ", bombes_restantes, " mines sur ", nbrs_bombes)

        if choix_action in ['c', 'C', 'd', 'D']:
            choix_ligne = int(input("Choisiser une ligne (1 chiffre seulement) : ")) - 1
            choix_colone = int(input("Choisiser une colone (1 chiffre seulement) : ")) - 1

        if choix_ligne < nbrs_lignes and choix_colone < nbrs_colones and not verifier and choix_action in ['c', 'C', 'd', 'D']:

            if choix_action in ['c', 'C']:
                test = fonction_test_bombe(grille_complette, choix_colone, choix_ligne)
                if not test and bombes_restantes != 0:
                    print("Bien joué, il vous reste " + str(bombes_restantes) + " bombes a trouver")
                    grille_a_completer[choix_ligne][choix_colone] = calcul_nbrs_bombes_alentours(grille_complette, nbrs_colones, nbrs_lignes, choix_colone, choix_ligne)
                if not test and bombes_restantes == 0:
                    print("Vous avez gagné!")
                    partie_finie = True
                if test:
                    print("Game Over\nVous avez creusé sur une bombe")
                    partie_finie = True

            if choix_action in ['d', 'D']:
                grille_a_completer[choix_ligne][choix_colone] = '*'
                bombes_marquer += 1
                if bombes_marquer == bombes_restantes:
                    print(
                        "Attention vous n'avez plus de drapeau a poser,\n vérifier la grille pour continuer la partie")
                    verifier = True
            nbrs_tours += 1

        if choix_action in ['v', 'V'] or verifier:
            y = 0
            nbrs_test = 0
            reusite = 0
            while y < nbrs_lignes:
                t = 0
                while t < nbrs_colones:
                    if grille_a_completer[y][t] == '*' and grille_complette[y][t] == 9:
                        nbrs_test += 1
                        grille_a_completer[y][t] == 'X'
                        reusite += 1
                    t += 1
                y += 1
            if reusite == nbrs_bombes:
                print(" Vous aviez bien trouvé toutes les bombes ")
            if reusite > 0 and reusite != nbrs_bombes:
                print(" Vous aviez bien identifier ", reusite, 'sur ', nbrs_bombes)
            partie_finie = True

        if choix_action not in ['v', 'V', 'c', 'C', 'd', 'D', 'q', 'Q']:
            print("Erreur : Veuillez recommencer.")


if __name__ == "__main__":
    main()
