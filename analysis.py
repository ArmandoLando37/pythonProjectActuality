import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.dates as mdates

class DataAnalyzer:
    def __init__(self):
        plt.style.use('seaborn-v0_8')
        
    def create_dataframe(self, articles):
        """Convertit la liste d'articles en DataFrame pandas"""
        print("📋 Création du DataFrame...")
        
        df = pd.DataFrame(articles)
        print(f"DataFrame initial: {len(df)} articles, {len(df.columns)} colonnes")
        
        # Convertir la date en format datetime pour l'analyse
        if not df.empty and 'published_at' in df.columns:
            print(f"Colonne published_at trouvée: {df['published_at'].iloc[0]}")
            
            try:
                # Essayer le format français
                df['date'] = pd.to_datetime(
                    df['published_at'], 
                    format='%d/%m/%Y à %H:%M', 
                    errors='coerce'
                )
                
                # Vérifier combien de dates ont été converties
                successful_conversions = df['date'].notna().sum()
                print(f"Dates converties avec format français: {successful_conversions}/{len(df)}")
                
                if successful_conversions == 0:
                    # Fallback: format ISO
                    print("🔄 Tentative avec format ISO...")
                    df['date'] = pd.to_datetime(df['published_at'], errors='coerce')
                    
            except Exception as e:
                print(f"❌ Erreur conversion date: {e}")
                df['date'] = pd.to_datetime(df['published_at'], errors='coerce')
                    
        return df
        
    def articles_by_source(self, articles):
        """Génère un graphique des articles par source"""
        df = self.create_dataframe(articles)
        
        if df.empty or 'source' not in df.columns:
            return None
            
        # Compter les articles par source
        source_counts = df['source'].value_counts().head(10)  # Top 10 sources
        
        # Créer le graphique
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.barh(source_counts.index, source_counts.values, color='#8e2dc5')
        
        # Ajouter les valeurs sur les barres
        for i, v in enumerate(source_counts.values):
            ax.text(v + 0.1, i, str(v), va='center')
            
        # Personnaliser le graphique
        ax.set_xlabel('Nombre d\'articles')
        ax.set_title('Articles par source')
        ax.invert_yaxis()  # Afficher la source avec le plus d'articles en haut
        plt.tight_layout()
        
        return fig
        
    def articles_by_date(self, articles):
        """Génère un graphique des articles par date"""
        df = self.create_dataframe(articles)
        
        if df.empty or 'date' not in df.columns or df['date'].isna().all():
            return None
            
        # Grouper par date
        df['date_only'] = df['date'].dt.date
        date_counts = df.groupby('date_only').size()
        
        # Créer le graphique
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(date_counts.index, date_counts.values, marker='o', linestyle='-', color='#8e2dc5')
        
        # Formater les dates sur l'axe x
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
        
        # Personnaliser le graphique
        ax.set_xlabel('Date')
        ax.set_ylabel('Nombre d\'articles')
        ax.set_title('Articles par date')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        
        return fig
        
    def export_to_csv(self, articles, filename="news_analysis.csv"):
        """Exporte les données d'articles vers un fichier CSV"""
        df = self.create_dataframe(articles)
        
        if not df.empty:
            # Sélectionner les colonnes pertinentes
            export_df = df[['title', 'source', 'published_at', 'author']].copy()
            export_df.to_csv(filename, index=False, encoding='utf-8')
            return True
            
        return False