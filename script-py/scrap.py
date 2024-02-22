import requests
from bs4 import BeautifulSoup

def scraping_all(url, output_file="resultats.txt"):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        with open(output_file, 'w', encoding='utf-8') as file:
            # Récupérer tous les h1
            h1_tags = soup.find_all('h1')
            file.write("Contenu des balises h1:\n")
            for tag in h1_tags:
                file.write(tag.text.strip() + '\n')

            # Récupérer tous les paragraphes (p)
            p_tags = soup.find_all('p')
            file.write("\nContenu des balises p:\n")
            for tag in p_tags:
                file.write(tag.text.strip() + '\n')

            # Récupérer toutes les images (img)
            img_tags = soup.find_all('img')
            file.write("\nSources des balises img:\n")
            for tag in img_tags:
                file.write(tag['src'] + '\n')

    except requests.exceptions.HTTPError as http_err:
        print(f"Erreur HTTP: {http_err}")
    except Exception as err:
        print(f"Une autre erreur est survenue: {err}")
    else:
        print("\nScraping réussi. Les résultats ont été enregistrés dans", output_file)
    finally:
        print("Nettoyage et fermeture des ressources si nécessaire.")



url_scrap = input("Enter l'url: ")
scraping_all(url_scrap)

print('ok')