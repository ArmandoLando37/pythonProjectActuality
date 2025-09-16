from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QFrame, QSizePolicy, QPushButton)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QFont
import requests
from io import BytesIO
from PIL import Image
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class ArticleWidget(QWidget):
    article_clicked = pyqtSignal(dict)  # Émettre l'URL de l'article lorsqu'il est cliqué
    
    def __init__(self, article_data):
        super().__init__()
        self.article_data = article_data
        self.setup_ui()
        
    def setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(15)
        
        # Image de l'article
        self.image_label = QLabel()
        self.image_label.setFixedSize(120, 80)
        self.image_label.setScaledContents(True)
        self.image_label.setStyleSheet("""
            background-color: #f0f0f0;
            border-radius: 4px;
        """)
        
        # Charger l'image en arrière-plan
        self.load_image()
        
        # Contenu textuel
        text_layout = QVBoxLayout()
        text_layout.setSpacing(5)
        
        # Titre
        title_label = QLabel(self.article_data["title"])
        title_label.setWordWrap(True)
        title_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        title_label.setMaximumHeight(40)
        
        # Description
        desc_label = QLabel(self.article_data["description"])
        desc_label.setWordWrap(True)
        desc_label.setStyleSheet("color: #555; font-size: 12px;")
        desc_label.setMaximumHeight(40)
        
        # Métadonnées (source et date)
        meta_layout = QHBoxLayout()
        source_label = QLabel(self.article_data["source"])
        source_label.setStyleSheet("color: #8e2dc5; font-size: 11px; font-weight: bold;")
        
        date_label = QLabel(self.article_data["published_at"])
        date_label.setStyleSheet("color: #777; font-size: 11px;")
        
        meta_layout.addWidget(source_label)
        meta_layout.addStretch()
        meta_layout.addWidget(date_label)
        
        # Ajouter au layout textuel
        text_layout.addWidget(title_label)
        text_layout.addWidget(desc_label)
        text_layout.addLayout(meta_layout)
        
        # Ajouter au layout principal
        layout.addWidget(self.image_label)
        layout.addLayout(text_layout)
        
        # Style du widget
        self.setStyleSheet("""
            ArticleWidget {
                background: white;
                border-radius: 8px;
                border: 1px solid #e0e0e0;
            }
            ArticleWidget:hover {
                background: #f8f8f8;
                border: 1px solid #d0d0d0;
            }
        """)
        
    def load_image(self):
        image_url = self.article_data.get("image_url", "")
        if image_url:
            try:
                response = requests.get(image_url, timeout=5)
                if response.status_code == 200:
                    image_data = response.content
                    pixmap = QPixmap()
                    pixmap.loadFromData(image_data)
                    
                    # Redimensionner tout en conservant le ratio
                    scaled_pixmap = pixmap.scaled(
                        120, 80, 
                        Qt.KeepAspectRatioByExpanding, 
                        Qt.SmoothTransformation
                    )
                    self.image_label.setPixmap(scaled_pixmap)
                else:
                    self.set_placeholder_image()
            except:
                self.set_placeholder_image()
        else:
            self.set_placeholder_image()
            
    def set_placeholder_image(self):
        self.image_label.setText("N")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("""
            background-color: #e0e0e0;
            border-radius: 4px;
            font-size: 24px;
        """)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # self.article_clicked.emit(self.article_data["url"])
            self.article_clicked.emit(self.article_data)
    def enterEvent(self, event):
        self.setCursor(Qt.PointingHandCursor)
        
    def leaveEvent(self, event):
        self.setCursor(Qt.ArrowCursor)

class ChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.setup_ui()
        
    def setup_ui(self):
        # Layout pour les deux graphiques
        self.charts_layout = QHBoxLayout()
        
        # Canvas pour le premier graphique (sources)
        self.source_canvas = FigureCanvas(Figure(figsize=(5, 4)))
        self.source_canvas.setVisible(False)
        
        # Canvas pour le deuxième graphique (dates)
        self.date_canvas = FigureCanvas(Figure(figsize=(5, 4)))
        self.date_canvas.setVisible(False)
        
        # Message quand il n'y a pas de données
        self.message_label = QLabel("Chargez d'abord des articles pour voir les analyses")
        self.message_label.setAlignment(Qt.AlignCenter)
        self.message_label.setStyleSheet("font-size: 16px; color: #666; padding: 40px;")
        
        # Ajouter au layout
        self.charts_layout.addWidget(self.source_canvas)
        self.charts_layout.addWidget(self.date_canvas)
        self.layout.addLayout(self.charts_layout)
        self.layout.addWidget(self.message_label)
        
    def display_charts(self, sources_fig, dates_fig):
        # Cacher le message
        self.message_label.setVisible(False)
        
        # Afficher le premier graphique
        if sources_fig:
            self.source_canvas.figure = sources_fig
            self.source_canvas.draw()
            self.source_canvas.setVisible(True)
        else:
            self.source_canvas.setVisible(False)
            
        # Afficher le deuxième graphique
        if dates_fig:
            self.date_canvas.figure = dates_fig
            self.date_canvas.draw()
            self.date_canvas.setVisible(True)
        else:
            self.date_canvas.setVisible(False)
            
    def show_message(self, message):
        # Cacher les graphiques
        self.source_canvas.setVisible(False)
        self.date_canvas.setVisible(False)
        
        # Afficher le message
        self.message_label.setText(message)
        self.message_label.setVisible(True)