# Importation des bibliothèques nécessaires
import requests
import markdown
import webbrowser
from md_to_html import convert_markdown_to_html

# Fonction pour télécharger les données d'un Pokémon depuis l'API PokeAPI
def download_poke(id: int) -> dict:
    """Télécharge les données d'un Pokémon depuis l'API PokeAPI."""
    # Construction de l'URL de l'API
    url = f"https://pokeapi.co/api/v2/pokemon/{id}/"
    
    # Envoi de la requête GET
    response = requests.get(url)
    
    # Vérification du code de réponse
    if response.status_code == 200:
        # Retour des données sous forme de dictionnaire
        return response.json()

# Fonction pour générer un fichier Markdown à partir des données d'un Pokémon
def poke_to_md(data: dict, filename: str) -> None:
    """Génère un fichier Markdown à partir des données d'un Pokémon."""
    # Récupération des informations du Pokémon
    name = data['name'].capitalize()
    weight = data['weight']
    height = data['height']
    types = [t['type']['name'] for t in data['types']]
    stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
    image_url = data['sprites']['front_default']

    # Ouverture du fichier en mode écriture
    with open(filename, 'w') as f:
        # Écriture du contenu Markdown
        f.write(f"# Fiche de {name}\n\n")
        f.write(f"![{name}]({image_url})\n\n")
        f.write(f"## Informations\n")
        f.write(f"- **Poids**: {weight}\n")
        f.write(f"- **Taille**: {height}\n")
        f.write(f"- **Types**: {', '.join(types)}\n")
        f.write(f"\n## Statistiques\n")
        for stat, value in stats.items():
            
            f.write(f"- **{stat}**: {value}\n")

    # Ouverture du fichier en mode écriture
    with open(filename, 'w') as f:
        # Écriture du contenu Markdown
        f.write(f"# Fiche de {name}\n\n")
        f.write(f"![{name}]({image_url})\n\n")
        f.write(f"## Informations\n")
        f.write(f"- **Poids**: {weight}\n")
        f.write(f"- **Taille**: {height}\n")
        f.write(f"- **Types**: {', '.join(types)}\n")
        f.write(f"\n## Statistiques\n")
        for stat, value in stats.items():
            f.write(f"- **{stat}**: {value}\n")

# Fonction pour générer une fiche Markdown et une fiche HTML pour un Pokémon donné
def fiche_pokemon(id: int) :
    """Génère une fiche Markdown et une fiche HTML pour un Pokémon donné."""
    # Téléchargement des données du Pokémon
    data = download_poke(id)
    
    # Définition des noms de fichiers
    md_filename = f"pokemon_{id}.md"
    html_filename = f"pokemon_{id}.html"

    # Génération du fichier Markdown
    poke_to_md(data, md_filename)

    # Conversion du Markdown en HTML
    html_content = convert_markdown_to_html(md_filename)

    # Génération du fichier HTML
    with open(html_filename, 'w') as f:
        f.write("<html><head><title>Fiche de Pokémon</title></head><body>")
        f.write(html_content)
        f.write("</body></html>")

    # Affichage du message de confirmation
    print(f"Fiche générée : {md_filename} et {html_filename}")
    webbrowser.open(html_filename)

# Point d'entrée du programme
if __name__ == "__main__":
    # Demande à l'utilisateur de saisir l'ID du Pokémon
        pokemon_id = int(input("Veuillez entrer l'ID du Pokémon : "))
fiche_pokemon(pokemon_id)
