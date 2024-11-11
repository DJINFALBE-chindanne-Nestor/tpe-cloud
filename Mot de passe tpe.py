
import random
#importé le module string qui contient des constantes utiles
import string

#fonction qui prend en paramètres la longueur du mot de passe(length) et les prérférences de l'utilisateurs 
def generer_mot_de_passe(longueur, majuscules, minuscules, chiffres, speciaux):
    caracteres = ''
    
    #Les condiction pour gestion de majuscule et minuscule
    if majuscules:
        caracteres += string.ascii_uppercase
    if minuscules:
        caracteres += string.ascii_lowercase
        #Condiction pour les chiffres (0 à 9) 
    if chiffres:
        caracteres += string.digits
        #condiction pour les caratères spéciaux
    if speciaux: 
        caracteres += string.punctuation

#Crée une chaine vide pour stocker tous les types de caractères qui seront utilisée
    if not caracteres:
        raise ValueError("Au moins un type de caractère doit être sélectionné.")

    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

#la fonction principale gère la collete des préférences de l'utilisateur et l'affichage du mot de passe généré
def main():
    print("Générateur de mots de passe")
    
    # Demande des préférences à l'utilisateur
    longueur = int(input("Longueur du mot de passe : "))
    #Condiction pour majuscules (A à Z) et pour minuscules(a à z) à la chaine de caractèrs
    majuscules = input("Inclure des lettres majuscules ? (Oui/Non) : ").strip().lower() == 'oui'
    minuscules = input("Inclure des lettres minuscules ? (Oui/Non) : ").strip().lower() == 'oui'
    chiffres = input("Inclure des chiffres ? (Oui/Non) : ").strip().lower() == 'oui'
    speciaux = input("Inclure des caractères spéciaux ? (Oui/Non) : ").strip().lower() == 'oui'
    
    #Démande la longueur souhaitée  de mot de passe à l'utilisateur et convertit l'entrée en entier(int)
    try:
        mot_de_passe = generer_mot_de_passe(longueur, majuscules, minuscules, chiffres, speciaux)
        print(f"Votre mot de passe généré est : {mot_de_passe}")
        #Gestion des erreurs
    except ValueError as e:
        print(e)

#exécution du programme
if __name__ == "__main__":
    main()

