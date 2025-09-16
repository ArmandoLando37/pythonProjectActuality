import json
import os

class FavoritesManager:
    def __init__(self, filename="favorites.json"):
        self.filename = filename
        self.favorites = self.load_favorites()
    
    def load_favorites(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_favorites(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.favorites, f, ensure_ascii=False, indent=2)
    
    def add_favorite(self, article):
        if not any(fav['url'] == article['url'] for fav in self.favorites):
            self.favorites.append(article)
            self.save_favorites()
    
    def remove_favorite(self, url):
        self.favorites = [fav for fav in self.favorites if fav['url'] != url]
        self.save_favorites()