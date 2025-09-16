from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QTextBrowser, QScrollArea, QWidget)
from PyQt5.QtCore import Qt,QUrl
from PyQt5.QtGui import QPixmap, QDesktopServices
import requests

class ArticleDetailDialog(QDialog):
    def __init__(self, article_data, parent=None):
        super().__init__(parent)
        self.article_data = article_data
        self.setup_ui()
        self.load_article_data()
        
    def setup_ui(self):
        self.setWindowTitle("Détails de l'article")
        self.setMinimumSize(800, 600)
        self.setStyleSheet("""
            QDialog {
                background-color: white;
            }
            QLabel {
                color: #333;
            }
            QPushButton {
                background-color: #8e2dc5;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #7a25a8;
            }
            QPushButton#closeBtn {
                background-color: #6c757d;
            }
            QPushButton#closeBtn:hover {
                background-color: #5a6268;
            }
        """)
        
        main_layout = QVBoxLayout(self)
        
        # Scroll area pour le contenu
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("border: none;")
        
        content_widget = QWidget()
        self.content_layout = QVBoxLayout(content_widget)
        self.content_layout.setSpacing(15)
        
        # Titre
        self.title_label = QLabel()
        self.title_label.setWordWrap(True)
        self.title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #2c3e50;")
        self.title_label.setAlignment(Qt.AlignCenter)
        
        # Image
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("background-color: #f8f9fa; border-radius: 8px;")
        self.image_label.setMaximumHeight(300)
        
        # Métadonnées (source, date, auteur)
        self.meta_layout = QHBoxLayout()
        self.source_label = QLabel()
        self.source_label.setStyleSheet("color: #8e2dc5; font-weight: bold;")
        
        self.date_label = QLabel()
        self.date_label.setStyleSheet("color: #6c757d;")
        
        self.author_label = QLabel()
        self.author_label.setStyleSheet("color: #6c757d; font-style: italic;")
        
        self.meta_layout.addWidget(self.source_label)
        self.meta_layout.addStretch()
        self.meta_layout.addWidget(self.date_label)
        self.meta_layout.addStretch()
        self.meta_layout.addWidget(self.author_label)
        
        # Description
        self.description_label = QLabel()
        self.description_label.setWordWrap(True)
        self.description_label.setStyleSheet("font-size: 14px; color: #495057; background-color: #f8f9fa; padding: 15px; border-radius: 8px;")
        
        # Contenu
        self.content_browser = QTextBrowser()
        self.content_browser.setStyleSheet("""
            QTextBrowser {
                border: 1px solid #dee2e6;
                border-radius: 8px;
                padding: 10px;
                background-color: #ffffff;
            }
        """)
        self.content_browser.setOpenExternalLinks(True)
        
        # Ajouter les widgets au layout
        self.content_layout.addWidget(self.title_label)
        self.content_layout.addWidget(self.image_label)
        self.content_layout.addLayout(self.meta_layout)
        self.content_layout.addWidget(self.description_label)
        self.content_layout.addWidget(self.content_browser)
        
        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)
        
        # Boutons
        button_layout = QHBoxLayout()
        
        self.visit_btn = QPushButton("Visiter le site")
        self.visit_btn.setObjectName("visitBtn")
        self.visit_btn.clicked.connect(self.visit_website)
        
        self.close_btn = QPushButton("Fermer")
        self.close_btn.setObjectName("closeBtn")
        self.close_btn.clicked.connect(self.accept)
        
        button_layout.addStretch()
        button_layout.addWidget(self.visit_btn)
        button_layout.addWidget(self.close_btn)
        
        main_layout.addLayout(button_layout)
        
    def load_article_data(self):
        # Charger le titre
        self.title_label.setText(self.article_data.get("title", "Sans titre"))
        
        # Charger l'image
        image_url = self.article_data.get("image_url", "")
        if image_url:
            self.load_image(image_url)
        else:
            self.image_label.setText("Image non disponible")
            self.image_label.setAlignment(Qt.AlignCenter)
            self.image_label.setStyleSheet("""
                background-color: #e9ecef;
                color: #6c757d;
                border-radius: 8px;
                padding: 20px;
            """)
        
        # Métadonnées
        self.source_label.setText(f"Source: {self.article_data.get('source', 'Inconnue')}")
        self.date_label.setText(f"Publié le: {self.article_data.get('published_at', 'Date inconnue')}")
        self.author_label.setText(f"Auteur: {self.article_data.get('author', 'Inconnu')}")
        
        # Description
        description = self.article_data.get("description", "Aucune description disponible")
        self.description_label.setText(description)
        
        # Contenu
        content = self.article_data.get("content", "Contenu non disponible")
        # Nettoyer le contenu (parfois il y a [...] à la fin)
        if content and "[+" in content:
            content = content.split("[+")[0]
        self.content_browser.setHtml(f"""
            <html>
            <body style="font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6;">
                {content}
            </body>
            </html>
        """)
    
    def load_image(self, image_url):
        try:
            response = requests.get(image_url, timeout=5)
            if response.status_code == 200:
                image_data = response.content
                pixmap = QPixmap()
                pixmap.loadFromData(image_data)
                
                # Redimensionner tout en conservant le ratio
                scaled_pixmap = pixmap.scaled(
                    600, 300, 
                    Qt.KeepAspectRatio, 
                    Qt.SmoothTransformation
                )
                self.image_label.setPixmap(scaled_pixmap)
            else:
                self.set_placeholder_image()
        except:
            self.set_placeholder_image()
    
    def set_placeholder_image(self):
        self.image_label.setText("Image non disponible")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("""
            background-color: #e9ecef;
            color: #6c757d;
            border-radius: 8px;
            padding: 20px;
        """)
    
    def visit_website(self):
        url = self.article_data.get("url", "")
        if url:
            # Convertir la string en QUrl avant de l'ouvrir
            q_url = QUrl(url)
            QDesktopServices.openUrl(q_url)
            