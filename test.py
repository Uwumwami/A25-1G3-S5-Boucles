import pytest # importer le module pytest pour faire nos tests unitaires
from ExDebug1 import environnement_optimal #importer la fonction de notre autre

#test unitaire pour la fonction environnement_optimal()
def test_environnement_optimal():
    # Arrange: préparer des variables d'entrées et le résultat attendu
    temperature = 25
    poussiere = "faible"
    humidite = 40
    resultat_attendu = "Tout est sous contrôle!"

    #Act:appeler la fonction à tester
    resultat_obtenu = environnement_optimal(temperature, poussiere,humidite)

    #assert: vérifier le résultat
    assert resultat_attendu == resultat_obtenu







