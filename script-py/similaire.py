import pandas as pd
import difflib

def lire_fichier_excel(fichier, colonne_nom):
    """Lit un fichier Excel et retourne une liste de noms."""
    # Lecture du fichier Excel en utilisant pandas
    dataframe = pd.read_excel(fichier)
    # Extraction de la colonne 'nom'
    noms = dataframe[colonne_nom].tolist()
    return noms

def comparer_noms(nom1, nom2):
    """Compare deux noms et retourne un score de similarité."""
    if isinstance(nom1, str) and isinstance(nom2, str):
        return difflib.SequenceMatcher(None, nom1, nom2).ratio()
    else:
        return 0.0  # Si les noms ne sont pas des chaînes de caractères valides, retourner 0.0


def filtrer_doublons(noms1, noms2, seuil_similarite):
    """Filtre les doublons dans deux listes de noms."""
    doublons = set()
    for nom1 in noms1:
        for nom2 in noms2:
            if comparer_noms(nom1, nom2) >= seuil_similarite:
                doublons.add(nom1)
                doublons.add(nom2)
    return doublons

fichier1 = "fiches_1.xlsx"
fichier2 = "fiches_2.xlsx"
colonne_nom = "nom"
seuil_similarite = 0.8

noms1 = lire_fichier_excel(fichier1, colonne_nom)
noms2 = lire_fichier_excel(fichier2, colonne_nom)

doublons = filtrer_doublons(noms1, noms2, seuil_similarite)

if doublons:
    print("Doublons potentiels :")
    for nom in doublons:
        print(nom)
else:
    print("Aucun doublon trouvé.")



# import pandas as pd
# import difflib

# def lire_fichier_excel(fichier, colonne_nom):
#     """Lit un fichier Excel et retourne un DataFrame."""
#     dataframe = pd.read_excel(fichier)
#     return dataframe

# def comparer_noms(nom1, nom2):
#     """Compare deux noms et retourne un score de similarité."""
#     if isinstance(nom1, str) and isinstance(nom2, str):
#         return difflib.SequenceMatcher(None, nom1, nom2).ratio()
#     else:
#         return 0.0

# def filtrer_doublons(df1, df2, seuil_similarite):
#     """Filtre les doublons dans deux DataFrames."""
#     doublons = set()
#     for index1, row1 in df1.iterrows():
#         for index2, row2 in df2.iterrows():
#             if comparer_noms(row1['nom'], row2['nom']) >= seuil_similarite:
#                 doublons.add(index1)
#                 doublons.add(index2)
#     return doublons

# def sauvegarder_sans_doublons(df, doublons, fichier_sortie):
#     """Sauvegarde les lignes sans doublons dans un nouveau fichier Excel."""
#     df_sans_doublons = df.drop(doublons)
#     df_sans_doublons.to_excel(fichier_sortie, index=False)

# fichier1 = "fiches_1.xlsx"
# fichier2 = "fiches_2.xlsx"
# colonne_nom = "nom"
# seuil_similarite = 0.8
# fichier_sortie = "sans_doublons.xlsx"

# df1 = lire_fichier_excel(fichier1, colonne_nom)
# df2 = lire_fichier_excel(fichier2, colonne_nom)

# doublons = filtrer_doublons(df1, df2, seuil_similarite)

# sauvegarder_sans_doublons(pd.concat([df1, df2]), doublons, fichier_sortie)

# print("Nouveau fichier sans doublons créé avec succès!")



# import pandas as pd
# import difflib

# def lire_fichier_csv(fichier):
#     """Lit un fichier CSV et retourne un DataFrame."""
#     dataframe = pd.read_csv(fichier, delimiter=';')
#     return dataframe

# def comparer_noms(nom1, nom2):
#     """Compare deux noms et retourne un score de similarité."""
#     if isinstance(nom1, str) and isinstance(nom2, str):
#         return difflib.SequenceMatcher(None, nom1, nom2).ratio()
#     else:
#         return 0.0

# def filtrer_doublons(df1, df2, seuil_similarite):
#     """Filtre les doublons dans deux DataFrames."""
#     doublons = set()
#     for index1, row1 in df1.iterrows():
#         for index2, row2 in df2.iterrows():
#             if comparer_noms(row1['nom'], row2['nom']) >= seuil_similarite:
#                 doublons.add(index1)
#                 doublons.add(index2)
#     return doublons

# def sauvegarder_sans_doublons(df, doublons, fichier_sortie):
#     """Sauvegarde les lignes sans doublons dans un nouveau fichier."""
#     df_sans_doublons = df.drop(doublons)
#     df_sans_doublons.to_csv(fichier_sortie, sep=';', index=False)
#     return len(df_sans_doublons)

# fichier1 = "fichiers_1.csv"
# fichier2 = "fichiers_2.csv"
# seuil_similarite = 0.8
# fichier_sortie = "sans_doublons0.csv"

# df1 = lire_fichier_csv(fichier1)
# df2 = lire_fichier_csv(fichier2)

# doublons = filtrer_doublons(df1, df2, seuil_similarite)

# nb_lignes_non_doublons = sauvegarder_sans_doublons(pd.concat([df1, df2]), doublons, fichier_sortie)

# print("Nombre de lignes non doublons copiées :", nb_lignes_non_doublons)
