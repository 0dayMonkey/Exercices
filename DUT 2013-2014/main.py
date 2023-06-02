import re

# Exo 1
def afficheRegexp(chaine, regexp):
    try:
        results = re.findall(regexp, chaine)
        if results:
            print(" et ".join(results))
        else:
            print("Aucune occurrence trouvée.")
    except re.error as e:
        print(f"L’expression reguliere {regexp} est incorrecte")
        raise e


afficheRegexp("(totot-1)*(2+3)",r"\([^)(]*\)")  # (totot-1) et (2+3)
try:
    afficheRegexp("(()(()))",r"\())")  
except re.error: # recup de l'erreur qu'il doit lever
    pass

#version simplifiée
"""
def afficheRegexp(chaine, substring):
    index = chaine.find(substring)
    if index != -1: print(substring)
    else:
      print("Aucune occurrence trouvée.")


afficheRegexp("(totot-1)*(2+3)", "(totot-1)")  # Affiche : (totot-1)
afficheRegexp("(totot-1)*(2+3)", "(2+3)")  # Affiche : (2+3)
afficheRegexp("(totot-1)*(2+3)", "(4+5)")  # Affiche : Aucune occurrence trouvée.
"""


def essaieOuvrir():
    while __name__ == "__main__":
        try:
            nom = input("Entrez le nom du fichier : ")
            fichier = open(nom, 'r')  # l'argument r nous sert à lire le fichier apres l'avoir ouvert → vu.fr/r-argument
            return fichier
            #print("Fichier ouvert")
        except FileNotFoundError: # alt " Raise "
            print("Le fichier n'existe pas, veuillez réessayer.")
        except PermissionError:
            raise NameError("Permission") from None



def main():
    while True:
        try:
            file = essaieOuvrir()  # Essayez d'ouvrir le fichier
            break  # Si l'ouverture réussit, sortez de la boucle
        except NameError:
            print("Changez les permissions de votre fichier !")
            return

    regexp = input("Entrez une expression reguliere : ")
    try:
        afficheRegexp(file.read(), regexp)
    except re.error:
        print(f"L’expression reguliere {regexp} est incorrecte")
    finally:
        file.close()

if __name__ == "__main__":
    main()


# Exo 2
alphabet = [chr(97 + i) for i in range(26)]
triplets = [(i, j, k) for i in range(1, 10) for j in range(i+1, 10) for k in range(j+1, 10)]
alternance = [(chr(97 + i % 2), i) for i in range(20)]
nombres_premiers = {n for n in range(2, 100) if all(n % i != 0 for i in range(2, int(n**0.5) + 1))}
liste_10_20_premiers = nombres_premiers[9:19]

# Exo 3
# fonctionsDico.py

def fabriqueDicoSet(fichier):
    with open(fichier, 'r') as f:
        return set(line.strip() for line in f)

def prefixeDico(mot, dico):
    return any(mot.startswith(prefix) for prefix in dico if len(prefix) < len(mot))

# main.py
import fonctionsDico
import dicoFR
import dicoAN

dico_fr = fonctionsDico.fabriqueDicoSet(dicoFR.nom_de_fichier) #français
dico_an = fonctionsDico.fabriqueDicoSet(dicoAN.nom_de_fichier) # anglais
dico = dico_fr & dico_an

print(sorted(dico)[:100])
print([mot for mot in dico_fr if mot.startswith('x') and mot.endswith('e')])
pourcentage_anglais = sum(not fonctionsDico.prefixeDico(mot, dico_an) for mot in dico_an) / len(dico_an) * 100
pourcentage_francais = sum(not fonctionsDico.prefixeDico(mot, dico_fr) for mot in dico_fr) / len(dico_fr) * 100
print(pourcentage_anglais, pourcentage_francais)

# Exo 4

def voisinsCase(plateau, case):
    i, j = case
    voisins = set()

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(plateau) and 0 <= nj < len(plateau[0]) and not plateau[ni][nj]:
            voisins.add((ni, nj))
    
    return voisins


def voisinsCases(plateau, cases):
    voisins = set()
    for case in cases:
        voisins.update(voisinsCase(plateau, case))
    return voisins


def accessibles(plateau, case):
    accessibles = {case}
    while True:
        nouveaux = voisinsCases(plateau, accessibles) - accessibles
        if not nouveaux:
            return accessibles
        accessibles.update(nouveaux)


def chemin(plateau, deb, fin):
    return fin in accessibles(plateau, deb)
