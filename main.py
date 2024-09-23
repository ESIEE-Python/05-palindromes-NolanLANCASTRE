"""
Fichier main.py
"""
import string

def ispalindrome(p):
    """
    Vérifie si une chaîne est un palindrome en ignorant les accents, espaces, et caractères spéciaux
    en utilisant translate() et une table de correspondance.
    """
    # Table de correspondance pour remplacer les caractères accentués
    accents = str.maketrans(
        "áàäâãéèëêíìïîóòöôõúùüûýÿñçÁÀÄÂÃÉÈËÊÍÌÏÎÓÒÖÔÕÚÙÜÛÝÑÇ",
        "aaaaaeeeeiiiiooooouuuuyyncAAAAAEEEEIIIIOOOOOUUUUYNC"   
    )

    # Table pour supprimer la ponctuation et les espaces
    suppression = str.maketrans('', '', string.punctuation + string.whitespace + '-')

    # Appliquer les transformations
    p = p.translate(accents)  # Remplacer les accents
    p = p.translate(suppression)  # Supprimer la ponctuation, les espaces et les tirets

    # Mettre en minuscule pour éviter les erreurs dues à la casse
    p = p.lower()

    # Longueur de la chaîne
    l = len(p)
    # Comparaison des caractères
    for i in range(l // 2):
        if p[i] != p[-i-1]:  # Comparaison entre le caractère courant et celui symétrique à la fin
            return False
     # Si toutes les comparaisons sont bonnes, c'est un palindrome
    return True



#### Fonction principale


def main():

    """ définition de la fonction principale """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
