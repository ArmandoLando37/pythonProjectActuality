import sys
import webbrowser
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QComboBox, QPushButton, 
                             QListWidget, QListWidgetItem, QFrame, QStackedWidget,
                             QMessageBox, QProgressBar, QSpacerItem, QSizePolicy, QLineEdit)
from PyQt5.QtCore import Qt, QSize, QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QPixmap, QIcon, QFont, QPalette, QColor
import requests
from api import NewsAPIClient
from analysis import DataAnalyzer
from ui.components import ArticleWidget, ChartWidget
from ui.article_detail import ArticleDetailDialog
import json
import os
from pdf_exporter import PDFExporter

# Charger les styles CSS
def load_stylesheet():
    style_path = os.path.join("resources", "style.css")
    if os.path.exists(style_path):
        with open(style_path, "r") as file:
            return file.read()
    return ""

# Thread pour récupérer les articles en arrière-plan
class FetchArticlesThread(QThread):
    articles_fetched = pyqtSignal(object)
    error_occurred = pyqtSignal(str)
    progress_updated = pyqtSignal(int)

    def __init__(self, api_client, category, query=None):
        super().__init__()
        self.api_client = api_client
        self.category = category
        self.query = query

    def run(self):
        try:
            self.progress_updated.emit(30)
            articles = self.api_client.get_articles(self.category, self.query)
            self.progress_updated.emit(100)
            self.articles_fetched.emit(articles)
        except Exception as e:
            self.error_occurred.emit(str(e))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lecteur d'actualités ")
        self.setGeometry(100, 100, 1200, 800)
        
        # Initialiser l'API client
        self.api_client = NewsAPIClient()
        
        # Initialiser l'analyseur de données
        self.analyzer = DataAnalyzer()
        
        # Configurer le style
        self.setStyleSheet(load_stylesheet())
        
        #     # Variables pour les articles
        # self.current_articles = []  # Articles actuels affichés
        # self.all_articles = []      # Tous les articles chargés (pour export/analyse)
        # self.page_size = 20
        # self.current_page_num = 1
            # VARIABLES CRITIQUES - Initialiser explicitement
        self.all_articles = []      # ← DOIT être initialisé ici
        self.current_articles = []  # ← DOIT être initialisé ici
        self.page_size = 20
        self.current_page_num = 1
        self.current_page = "home"
        
        # Créer l'interface
        self.setup_ui()

        # Initialiser l'exporteur PDF
        self.pdf_exporter = PDFExporter()
        
        # Charger les catégories
        self.categories = [
            "Général", "Affaires", "Divertissement", 
            "Santé", "Sports", "Technologie"
        ]
        self.category_combo.addItems(self.categories)
        
        # Page actuelle
        self.current_page = "home"
        
    def setup_ui(self):
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Navbar
        self.setup_navbar()
        main_layout.addWidget(self.navbar)
        
        # Widget empilé pour les pages
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)
        
        # Page d'accueil
        self.home_page = self.create_home_page()
        self.stacked_widget.addWidget(self.home_page)
        
        # Page des résultats
        self.results_page = self.create_results_page()
        self.stacked_widget.addWidget(self.results_page)
        
        # Page d'analyse
        self.analysis_page = self.create_analysis_page()
        self.stacked_widget.addWidget(self.analysis_page)
        
        # Barre de progression
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        main_layout.addWidget(self.progress_bar)
        
    def setup_navbar(self):
        self.navbar = QFrame()
        self.navbar.setObjectName("navbar")
        navbar_layout = QHBoxLayout(self.navbar)
        navbar_layout.setContentsMargins(20, 10, 20, 10)
        
        # Logo et titre
        logo_label = QLabel()
        logo_label.setObjectName("logoStyle")
        logo_pixmap = QPixmap(os.path.join("resources", "logo.png"))
        
        if logo_pixmap.isNull():
            logo_label.setText("N")
            logo_label.setStyleSheet("font-size: 24px;")
        else:
            logo_label.setPixmap(logo_pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        
        title_label = QLabel("Lecteur d'actualités")
        title_label.setObjectName("navbar_title")
        
        # Catégories
        self.category_combo = QComboBox()
        self.category_combo.setMinimumWidth(150)
        
        # Boutons
        self.home_btn = QPushButton("Accueil")
        self.home_btn.setObjectName("nav_btn")
        self.home_btn.clicked.connect(lambda: self.show_page("home"))
        
        self.refresh_btn = QPushButton("Actualiser")
        self.refresh_btn.setObjectName("nav_btn")
        self.refresh_btn.clicked.connect(self.refresh_articles)
        
        self.analysis_btn = QPushButton("Analyser")
        self.analysis_btn.setObjectName("nav_btn")
        self.analysis_btn.clicked.connect(lambda: self.show_page("analysis"))
        
        # Champ de recherche
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Rechercher...")
        self.search_input.setMinimumWidth(200)
        self.search_input.returnPressed.connect(self.on_search)
        
        # Bouton de recherche
        self.search_btn = QPushButton("🔍")
        self.search_btn.setObjectName("nav_btn")
        self.search_btn.clicked.connect(self.on_search)
        
        # Ajouter les éléments à la navbar
        navbar_layout.addWidget(logo_label)
        navbar_layout.addWidget(title_label)
        navbar_layout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        
        # Recherche
        navbar_layout.addWidget(QLabel("Recherche:"))
        navbar_layout.addWidget(self.search_input)
        navbar_layout.addWidget(self.search_btn)
        navbar_layout.addSpacing(10)
        
        # Catégorie
        navbar_layout.addWidget(QLabel("Catégorie:"))
        navbar_layout.addWidget(self.category_combo)
        navbar_layout.addSpacing(10)
        
        # Boutons de navigation
        navbar_layout.addWidget(self.home_btn)
        navbar_layout.addWidget(self.refresh_btn)
        navbar_layout.addWidget(self.analysis_btn)

         # Boutons d'export
        self.export_pdf_btn = QPushButton("Export PDF")
        self.export_pdf_btn.setObjectName("nav_btn")
        self.export_pdf_btn.clicked.connect(self.export_to_pdf)
        
        # self.export_summary_btn = QPushButton(" Résumé PDF")
        # self.export_summary_btn.setObjectName("nav_btn")
        # self.export_summary_btn.clicked.connect(self.export_summary_pdf)
        
        # Ajouter à la navbar
        navbar_layout.addWidget(self.export_pdf_btn)
        # navbar_layout.addWidget(self.export_summary_btn)
        
    def on_search(self):
        """Lance une recherche lorsque le bouton est cliqué ou Enter pressé"""
        query = self.search_input.text().strip()
        if query:
            self.perform_search(query)
        else:
            QMessageBox.warning(self, "Recherche", "Veuillez entrer un terme de recherche")

    def perform_search(self, query):
        """Effectue une recherche d'articles"""
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        
        # Désactiver le bouton de recherche pendant le chargement
        self.search_btn.setEnabled(False)
        self.search_btn.setText("Recherche...")
        
        # Lancer le thread pour rechercher les articles
        self.thread = FetchArticlesThread(self.api_client, None, query)
        self.thread.articles_fetched.connect(self.display_search_results)
        self.thread.error_occurred.connect(self.handle_search_error)
        self.thread.progress_updated.connect(self.progress_bar.setValue)
        self.thread.start()

    def display_search_results(self, articles):
        """Affiche les résultats de la recherche avec pagination"""
        self.progress_bar.setVisible(False)
        self.search_btn.setEnabled(True)
        self.search_btn.setText("🔍")
        
        print(f"=== DISPLAY SEARCH RESULTS ===")
        print(f"Articles recherche: {len(articles) if articles else 0}")
        
        if not articles:
            QMessageBox.information(self, "Recherche", "Aucun article trouvé pour votre recherche.")
            return
            
        # STOCKER EXPLICITEMENT
        self.all_articles = articles.copy()  # ← Copie explicite
        print(f"all_articles (recherche) défini: {len(self.all_articles)} articles")
        
        self.current_page_num = 1
        
        # Afficher la page des résultats
        self.show_page("results")
        
        # Mettre à jour le titre
        query = self.search_input.text()
        self.results_title.setText(f"Résultats pour \"{query}\" ({len(articles)} articles)")
        
        # Afficher la première page
        # self.show_current_page()

    def handle_search_error(self, error_msg):
        """Gère les erreurs de recherche"""
        self.progress_bar.setVisible(False)
        self.search_btn.setEnabled(True)
        self.search_btn.setText("🔍")
        print(f"Erreur recherche: {error_msg}")
        QMessageBox.critical(self, "Erreur de recherche", f"Erreur lors de la recherche: {error_msg}")
        
    def create_home_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setAlignment(Qt.AlignCenter)
        
        # Titre
        title = QLabel("Lecteur d'actualités")
        title.setObjectName("home_title")
        
        # Sous-titre
        subtitle = QLabel("Restez informé avec les dernières actualités du monde entier")
        subtitle.setObjectName("home_subtitle")
        
        # Bouton
        self.fetch_btn = QPushButton("Charger les actualités")
        self.fetch_btn.setObjectName("home_button")
        self.fetch_btn.clicked.connect(self.fetch_articles)
        self.fetch_btn.setMinimumSize(200, 50)
        
        # Ajouter au layout
        layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addWidget(title, alignment=Qt.AlignCenter)
        layout.addWidget(subtitle, alignment=Qt.AlignCenter)
        layout.addSpacing(30)
        layout.addWidget(self.fetch_btn, alignment=Qt.AlignCenter)
        layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        return page
        
    def create_results_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Titre de la page
        self.results_title = QLabel("Articles récents")
        self.results_title.setObjectName("results_title")
        layout.addWidget(self.results_title)
        
        # Liste des articles
        self.articles_list = QListWidget()
        self.articles_list.setObjectName("articles_list")
        self.articles_list.setSpacing(10)
        layout.addWidget(self.articles_list)
        
        return page
        
    def create_analysis_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Titre
        title = QLabel("Analyse des actualités")
        title.setObjectName("analysis_title")
        layout.addWidget(title)
        
        # Widget pour les graphiques
        self.chart_widget = ChartWidget()
        layout.addWidget(self.chart_widget)
        
        return page
        
    def show_page(self, page_name):
        if page_name == "home":
            self.stacked_widget.setCurrentWidget(self.home_page)
            self.current_page = "home"
        elif page_name == "results":
            self.stacked_widget.setCurrentWidget(self.results_page)
            self.current_page = "results"
        elif page_name == "analysis":
            self.stacked_widget.setCurrentWidget(self.analysis_page)
            self.current_page = "analysis"
            self.perform_analysis()
            
    def fetch_articles(self):
        category = self.category_combo.currentText().lower()
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        
        # Désactiver le bouton pendant le chargement
        self.fetch_btn.setEnabled(False)
        self.fetch_btn.setText("Chargement...")
        
        # Lancer le thread pour récupérer les articles
        self.thread = FetchArticlesThread(self.api_client, category)
        self.thread.articles_fetched.connect(self.display_articles)
        self.thread.error_occurred.connect(self.handle_error)
        self.thread.progress_updated.connect(self.progress_bar.setValue)
        self.thread.start()
        
    def refresh_articles(self):
        if self.current_page == "results":
            self.fetch_articles()
        
    def display_articles(self, articles):
        self.progress_bar.setVisible(False)
        self.fetch_btn.setEnabled(True)
        self.fetch_btn.setText("Charger les actualités")
        
        print(f"Articles reçus: {len(articles) if articles else 0}")
        
        if not articles:
            QMessageBox.information(self, "Aucun article", "Aucun article trouvé pour cette catégorie.")
            return
            
        # Stocker tous les articles pour l'export PDF
        self.all_articles = articles.copy()
        print(f"📦 Articles stockés pour export: {len(self.all_articles)}")
        
        # Afficher la page des résultats
        self.show_page("results")
        
        # Mettre à jour le titre
        category = self.category_combo.currentText()
        self.results_title.setText(f"Articles {category} ({len(articles)} résultats)")
        
        # Effacer la liste actuelle
        self.articles_list.clear()
        
        # Ajouter tous les articles à la liste (sans pagination)
        for article in articles:
            item = QListWidgetItem()
            widget = ArticleWidget(article)
            widget.article_clicked.connect(self.show_article_detail)
            item.setSizeHint(widget.sizeHint())
            self.articles_list.addItem(item)
            self.articles_list.setItemWidget(item, widget)
        
    def show_article_detail(self, article_data):
        """Affiche les détails de l'article dans une fenêtre modale"""
        dialog = ArticleDetailDialog(article_data, self)
        dialog.exec_()
        
    def perform_analysis(self):
        # Utiliser all_articles au lieu de current_articles
        if hasattr(self, 'all_articles') and self.all_articles:
            print(f"🔍 Analyse de {len(self.all_articles)} articles...")
            
            # Générer les graphiques sur TOUS les articles
            sources_fig = self.analyzer.articles_by_source(self.all_articles)
            dates_fig = self.analyzer.articles_by_date(self.all_articles)
            
            # Afficher les graphiques
            self.chart_widget.display_charts(sources_fig, dates_fig)
        else:
            print("⚠️ Aucune donnée à analyser")
            self.chart_widget.show_message("Aucune donnée à analyser. Veuillez d'abord charger des articles.")
            
    def open_article_url(self, url):
        webbrowser.open(url)
        
    def handle_error(self, error_msg):
        self.progress_bar.setVisible(False)
        self.fetch_btn.setEnabled(True)
        self.fetch_btn.setText("Charger les actualités")
        print(error_msg)
        QMessageBox.critical(self, "Erreur", "Connectez-vous à internet")
        
    def export_to_pdf(self):
        """Exporte les articles en PDF"""
        # Vérifier si all_articles existe et n'est pas vide
        print("=== EXPORT PDF CLICK ===")
        print(f"hasattr all_articles: {hasattr(self, 'all_articles')}")
        
        if hasattr(self, 'all_articles'):
            print(f"all_articles length: {len(self.all_articles)}")
            print(f"all_articles type: {type(self.all_articles)}")
            print(f"all_articles content: {self.all_articles[:1] if self.all_articles else 'VIDE'}")
        
        # Vérification robuste
        if hasattr(self, 'all_articles') and self.all_articles and len(self.all_articles) > 0:
            from datetime import datetime
            filename = f"articles_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            
            print(f" Export de {len(self.all_articles)} articles vers {filename}")
            success, message = self.pdf_exporter.export_to_pdf(self.all_articles, filename)
            
            if success:
                QMessageBox.information(self, "Export PDF", message)
            else:
                QMessageBox.warning(self, "Erreur PDF", message)
        else:
            print(" Aucun article à exporter")
            QMessageBox.warning(
                self, 
                "Export PDF", 
                "Aucun article à exporter. Veuillez d'abord charger des articles en utilisant le bouton 'Charger les actualités' ou la recherche."
            )

    # def export_summary_pdf(self):
    #     """Exporte un résumé statistique en PDF"""
    #     if hasattr(self, 'all_articles') and self.all_articles:
    #         from datetime import datetime
    #         filename = f"resume_articles_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            
    #         print(f"Export du résumé de {len(self.all_articles)} articles...")
    #         success, message = self.pdf_exporter.export_summary_pdf(self.all_articles, filename)
            
    #         if success:
    #             QMessageBox.information(self, "Résumé PDF", message)
    #         else:
    #             QMessageBox.warning(self, "Erreur Résumé", message)
    #     else:
    #         QMessageBox.warning(self, "Résumé PDF", "Aucun article à analyser. Veuillez d'abord charger des articles.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Définir la palette de couleurs pour l'application
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(245, 245, 245))
    palette.setColor(QPalette.WindowText, QColor(33, 33, 33))
    palette.setColor(QPalette.Base, QColor(255, 255, 255))
    palette.setColor(QPalette.AlternateBase, QColor(233, 233, 233))
    palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
    palette.setColor(QPalette.ToolTipText, QColor(33, 33, 33))
    palette.setColor(QPalette.Text, QColor(33, 33, 33))
    palette.setColor(QPalette.Button, QColor(240, 240, 240))
    palette.setColor(QPalette.ButtonText, QColor(33, 33, 33))
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Highlight, QColor(142, 45, 197))
    palette.setColor(QPalette.HighlightedText, Qt.white)
    app.setPalette(palette)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())