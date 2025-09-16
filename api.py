import requests
import os
from datetime import datetime, timedelta

class NewsAPIClient:
    def __init__(self):
        self.api_key = self.get_api_key()
        self.base_url = "https://newsapi.org/v2"
        
    def get_api_key(self):
        # Essayer de récupérer la clé API depuis les variables d'environnement
        api_key = os.environ.get("NEWS_API_KEY")
        # api_key = os.environ.get("17ef26b92e6a4c8d958b010ff6eaa623")
        
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
                "language": "en",  # Recherche en anglais pour plus de résultats
                "apiKey": self.api_key
            }
        else:
            url = f"{self.base_url}/top-headlines"
            params = {
                "category": english_category,
                "pageSize": page_size,
                "country": "us",  # Actualités US (garder comme avant)
                "apiKey": self.api_key
            }
        
        print(f"URL: {url}")
        print(f"Params: {params}")
        
        try:
            response = requests.get(url, params=params, timeout=15)
            response.raise_for_status()
            data = response.json()
            
            print(f"Status: {data.get('status')}")
            print(f"Total results: {data.get('totalResults', 0)}")
            
            if data["status"] == "ok":
                articles = self.process_articles(data["articles"])
                print(f"Articles traités: {len(articles)}")
                return articles
            else:
                error_msg = data.get('message', 'Unknown error')
                print(f"Erreur API: {error_msg}")
                raise Exception(f"Erreur API: {error_msg}")
                
        except requests.exceptions.RequestException as e:
            print(f"Erreur de connexion: {str(e)}")
            raise Exception(f"Erreur de connexion: {str(e)}")
            
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