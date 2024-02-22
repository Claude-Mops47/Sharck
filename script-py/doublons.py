# import pandas as pd

# def lire_fichier(fichier):
#   """Lit un fichier Excel ou CSV et retourne un DataFrame Pandas."""
#   if fichier.endswith(".xlsx"):
#     return pd.read_excel(fichier)
#   else:
#     return pd.read_csv(fichier)

# def comparer_noms(df1, df2):
#   """Compare les noms des deux DataFrames et retourne un DataFrame avec les doublons."""
#   return pd.merge(df1, df2, on="nom", how="inner")

# def copier_lignes_sans_doublons(df1, df2, fichier_sortie):
#   """Copie les lignes de df1 qui n'existent pas dans df2 dans un nouveau fichier."""
#   lignes_sans_doublons = df1[~df1["nom"].isin(df2["nom"])]
#   lignes_sans_doublons.to_excel(fichier_sortie, index=False)

# fichier1 = "fiches_1.xlsx"
# fichier2 = "fiches_2.xlsx"
# # fichier2 = "fichier2.csv"
# fichier_sortie = "fichier3.xlsx"

# df1 = lire_fichier(fichier1)
# df2 = lire_fichier(fichier2)

# doublons = comparer_noms(df1, df2)

# if not doublons.empty:
#   print("Doublons trouvés :")
#   print(doublons)

# copier_lignes_sans_doublons(df1, df2, fichier_sortie)

# print("Lignes sans doublons copiées dans le fichier", fichier_sortie)


import pandas as pd

def lire_fichier(fichier):
    """Lit un fichier Excel ou CSV et retourne un DataFrame Pandas."""
    if fichier.endswith(".xlsx"):
        return pd.read_excel(fichier)
    else:
        return pd.read_csv(fichier)

def comparer_noms(df1, df2):
    """Compare les noms des deux DataFrames et retourne un DataFrame avec les doublons."""
    return pd.merge(df1, df2, on="nom", how="inner")

def copier_lignes_sans_doublons(df1, df2, fichier_sortie):
    """Copie les lignes de df1 qui n'existent pas dans df2 dans un nouveau fichier."""
    lignes_sans_doublons = df1[~df1["nom"].isin(df2["nom"])]
    print("Nombre de lignes sans doublons :", len(lignes_sans_doublons))
    lignes_sans_doublons.to_excel(fichier_sortie, index=False)

fichier1 = "fiches_1.xlsx"
fichier2 = "fiches_2.xlsx"
# fichier2 = "fichier2.csv"
fichier_sortie = "fichier3.xlsx"

df1 = lire_fichier(fichier1)
df2 = lire_fichier(fichier2)

doublons = comparer_noms(df1, df2)

if not doublons.empty:
    print("Doublons trouvés :")
    print(doublons)

copier_lignes_sans_doublons(df1, df2, fichier_sortie)

print("Lignes sans doublons copiées dans le fichier", fichier_sortie)
