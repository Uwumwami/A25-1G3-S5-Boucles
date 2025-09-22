def environnement_optimal(temp, poussiere, humidite):
    """
    Vérifie si l'environnement d'un ordinateur est optimal.

    Paramètres :
    - temp : température en °C (int ou float)
    - poussiere : niveau de poussière ("faible", "moyen", "élevé")
    - humidite : taux d’humidité en % (int ou float)

    Retour :
    - "Tout est sous contrôle!" si toutes les conditions sont respectées
    - "Environnement non optimal" sinon (après avoir affiché les problèmes détectés)
    """

    alerte = False

    # Vérification température
    if temp < 18:
        print("Température trop basse")
        alerte = True
    elif temp > 27:
        print("Température trop élevée")
        alerte = True

    # Vérification humidité
    if humidite <= 30:
        print("Humidité trop basse")
        alerte = True
    elif humidite >= 50:
        print("Humidité trop élevée")
        alerte = True

    # Vérification poussière
    if poussiere != "faible":
        print("Trop de poussière")
        alerte = True

    # Retour final
    if not alerte:
        return "Tout est sous contrôle!"
    else:
        return "Environnement non optimal"


if __name__ == "__main__":
    # #TODO : Créer 3 listes
    # lst_ordi = []
    # compteur = 0
    # # TODO : pour 3 ordinateur
    #     #TODO : Demander temp, pourssière, humidité
    #     #TODO : Mettre les 3 valeurs dans leurs listes
    # for a in range(3):
    #     temp = float(input("Entrer la température: "))
    #     poussiere = input("Entrer le niveau de poussière: ")
    #     humidite = float(input("Entrer l'humidité: "))
    #
    #     lst_ordi.append(temp)
    #     lst_ordi.append(poussiere)
    #     lst_ordi.append(humidite)
    #     for i in range(len(lst_ordi)):
    #         print(f"La temperature est de {temp}, le niveau de poussière est {poussiere} et l'humidité est {humidite}")
    #     compteur += 1
    #
    #
    # #TODO : pour les 3 ordinateurs
    #     #TODO : utiliser la fonction et afficher le résultat
    # print(environnement_optimal(temp, poussiere, humidite))



    # Listes pour stocker les données
    liste_temp = []
    liste_poussiere = []
    liste_humidite = []

    # Collecte des données pour 3 ordinateurs
    for i in range(3):
        print(f"\nOrdinateur {i + 1} :")
        temp = float(input("Entrer la température (°C) : "))
        poussiere = input("Entrer le niveau de poussière (faible/moyen/élevé) : ").lower()
        humidite = float(input("Entrer l'humidité (%) : "))

        liste_temp.append(temp)
        liste_poussiere.append(poussiere)
        liste_humidite.append(humidite)

    # Affichage et vérification
    for i in range(3):
        print(f"\n📊 Ordinateur {i + 1} :")
        print(f"Température : {liste_temp[i]}°C")
        print(f"Poussière : {liste_poussiere[i]}")
        print(f"Humidité : {liste_humidite[i]}%")
        resultat = environnement_optimal(liste_temp[i], liste_poussiere[i], liste_humidite[i])
        print(f"✅ Résultat : {resultat}")
