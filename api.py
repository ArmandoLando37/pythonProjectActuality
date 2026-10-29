import requests
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

class NewsAPIClient:
    def __init__(self):
        self.api_key = self.get_api_key()
        self.base_url = "https://newsapi.org/v2"
        
    def get_api_key(self):
        # Essayer de récupérer la clé API depuis les variables d'environnement
        api_key = os.environ.get("NEWS_API_KEY")
        
        if not api_key:
            # Sinon, essayer de la lire depuis un fichier
            try:
                with open("news_api_key.txt", "r") as f:
                    api_key = f.read().strip()
            except FileNotFoundError:
                raise Exception("Clé API NewsAPI non trouvé. Veuillez définir la variable d'environnement NEWS_API_KEY ou créer un fichier news_api_key.txt contenant votre clé.")
                
        return api_key
        
    
    def get_articles(self, category=None, query=None, page_size=20):
        category_mapping = {
            "général": "general",
            "affaires": "business",
            "divertissement": "entertainment",
            "santé": "health",
            "sports": "sports",
            "technologie": "technology"
        }
        
        # Gestion robuste de la catégorie
        english_category = "general"
        if category is not None and isinstance(category, str):
            english_category = category_mapping.get(category.lower(), "general")
        
        print(f"Mode: {'RECHERCHE' if query else 'CATÉGORIE'}")
        print(f"Catégorie: {category} -> {english_category}")
        print(f"Query: {query}")
        
        if query:
            url = f"{self.base_url}/everything"
            params = {
                "q": query,
                "pageSize": page_size,
                "sortBy": "publishedAt",
                "language": "en"  # Recherche en anglais pour plus de résultats
            }
        else:
            url = f"{self.base_url}/top-headlines"
            params = {
                "category": english_category,
                "pageSize": page_size,
                "country": "us"  # Actualités US (garder comme avant)
            }
        
        print(f"URL: {url}")
        
        try:
            response = requests.get(
                url,
                params=params,
                headers={"X-Api-Key": self.api_key},
                timeout=15
            )
        except requests.exceptions.RequestException as e:
            print("Erreur de connexion à NewsAPI.")
            raise Exception(
                "Impossible de joindre NewsAPI. Vérifiez votre connexion Internet."
            ) from e

        try:
            data = response.json()
        except ValueError as e:
            if not response.ok:
                raise Exception(
                    f"NewsAPI a répondu avec HTTP {response.status_code}. "
                    "Vérifiez votre clé API et votre compte NewsAPI."
                ) from e
            raise Exception("NewsAPI a renvoyé une réponse invalide.") from e

        if not isinstance(data, dict):
            raise Exception("NewsAPI a renvoyé une réponse invalide.")

        if not response.ok or data.get("status") != "ok":
            error_code = data.get("code")
            error_msg = data.get("message", "Erreur inconnue")
            if error_code == "apiKeyInvalid":
                error_msg = (
                    "La clé API NewsAPI est invalide ou n'est pas encore activée. "
                    "Vérifiez NEWS_API_KEY dans votre fichier .env."
                )
            elif error_code == "apiKeyDisabled":
                error_msg = (
                    "Cette clé API NewsAPI est désactivée. Consultez votre compte NewsAPI."
                )
            print(f"Erreur NewsAPI ({error_code or response.status_code}): {error_msg}")
            raise Exception(f"Erreur NewsAPI : {error_msg}")

        print(f"Status: {data.get('status')}")
        print(f"Total results: {data.get('totalResults', 0)}")
        articles = self.process_articles(data["articles"])
        print(f"Articles traités: {len(articles)}")
        return articles
            
    def process_articles(self, articles):
        processed_articles = []
    
        for article in articles:
            try:
                # Nettoyer les données avec gestion robuste des valeurs None
                title = article.get("title")
                description = article.get("description")
                
                processed = {
                    "title": str(title).strip() if title else "Sans titre",
                    "description": str(description).strip() if description else "Aucune description disponible",
                    "url": article.get("url", ""),
                    "image_url": article.get("urlToImage", ""),
                    "source": article.get("source", {}).get("name", "Source inconnue"),
                    "published_at": article.get("publishedAt", ""),
                    "content": article.get("content", ""),
                    "author": article.get("author", "Auteur inconnu")
                }
                
                # Formater la date
                if processed["published_at"]:
                    try:
                        date_obj = datetime.strptime(processed["published_at"], "%Y-%m-%dT%H:%M:%SZ")
                        processed["published_at"] = date_obj.strftime("%d/%m/%Y à %H:%M")
                    except (ValueError, TypeError):
                        processed["published_at"] = "Date inconnue"
                else:
                    processed["published_at"] = "Date inconnue"
                
                processed_articles.append(processed)
                
            except Exception as e:
                print(f"Erreur lors du traitement d'un article: {e}")
                continue  # Passer à l'article suivant en cas d'erreur
            
        return processed_articles