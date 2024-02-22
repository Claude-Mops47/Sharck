import os
import requests
import pandas as pd
import time
import random
import re
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()
USER_API_KEY = os.getenv("USER_API_KEY")

# Fonction pour interroger l'API
def check_company_exists(name):
    url = "https://axonaut.com/api/v2/companies"
    params = {
        "search": name,
        "type": "prospect",
        "is_prospect": "true",
        "is_customer": "false",
        "is_supplier": "false",
        "sort": "name"
    }
    headers = {
        "accept": "application/json",
        "userApiKey": USER_API_KEY,
    }
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        return len(data) > 0
    except requests.exceptions.HTTPError as e:
        print(f"Erreur HTTP {e.response.status_code} pour {name}")
        raise  # Lève l'exception pour arrêter le script
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête pour {name}: {e}")
        return False

def extraction_department_number(department):
    return re.findall(r'\d+', department)[0]

# Fonction pour enregistrer les métriques dans un fichier CSV local
def log_metrics(department, total_checked, total_copied):
    department_number = extraction_department_number(department)
    headers = "department,date,heure,nombre_fiches_verifier,nombre_copie\n"
    metrics_data = f"{department_number},{time.strftime('%Y-%m-%d')},{time.strftime('%H:%M:%S')},{total_checked},{total_copied}\n"

    file_path = "metrics.csv"
    with open(file_path, "a+") as file:
        file.seek(0)
        if not file.readline():
            file.write(headers)
        file.write(metrics_data)

# Lecture et traitement des données Excel
def process_excel_file(department):
    df = pd.read_excel(department)
    df = df.drop_duplicates(subset="nom", keep="first")

    nb_lignes_verifiees = 0
    nb_lignes_copiees = 0
    lignes_inexistantes = []

    print("\nDébut du traitement")
    for index, row in df.iterrows():
        try:
            nb_lignes_verifiees += 1
            if not check_company_exists(row['nom']):
                lignes_inexistantes.append(row)
                nb_lignes_copiees += 1
            sleep_time = random.randint(2, 10)
            time.sleep(sleep_time)
            print(f"\rAttente de {sleep_time} secondes... Progression : {nb_lignes_verifiees}/{len(df)}", end="", flush=True)
        except Exception as e:
            print(f"\nErreur critique: {e}")
            break  # Arrête la boucle et le script en cas d'erreur critique

    if nb_lignes_copiees > 0:
        df_lignes_inexistantes = pd.DataFrame(lignes_inexistantes)
        df_lignes_inexistantes.to_excel("lignes_inexistantes.xlsx", index=False)
        # df_lignes_inexistantes.to_csv("lignes_inexistantes.csv", index=False)

    log_metrics(department, nb_lignes_verifiees, nb_lignes_copiees)
    print("\nFin du traitement")
    print(f"Nombre de lignes vérifiées : {nb_lignes_verifiees}")
    print(f"Nombre de lignes copiées : {nb_lignes_copiees}")

if __name__ == "__main__":
    try:
        # Demande à l'utilisateur d'entrer le nom du fichier Excel
        department = input("Veuillez entrer le chemin complet du fichier Excel à traiter (inclure l'extension .xlsx) : ")
        process_excel_file(department)
    except Exception as e:
        print(f"Arrêt du script en raison d'une erreur: {e}")