class ThemeManager:
    THEMES = {
        "light": {
            "background": "#ffffff",
            "text": "#333333",
            "primary": "#8e2dc5",
            "secondary": "#6c757d",
            "border": "#e0e0e0"
        },
        "dark": {
            "background": "#2d3748",
            "text": "#e2e8f0",
            "primary": "#9f7aea",
            "secondary": "#a0aec0",
            "border": "#4a5568"
        }
    }
    
    def apply_theme(self, theme_name, app):
        """Applique le thème à l'application complète"""
        theme = self.THEMES.get(theme_name, self.THEMES["light"])
        
        stylesheet = f"""
            QMainWindow, QDialog, QWidget {{
                background-color: {theme['background']};
                color: {theme['text']};
            }}
            QLabel {{
                color: {theme['text']};
            }}
            QPushButton {{
                background-color: {theme['primary']};
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
            }}
            QPushButton:hover {{
                background-color: {theme['secondary']};
            }}
            QListWidget {{
                background-color: {theme['background']};
                border: 1px solid {theme['border']};
                border-radius: 5px;
            }}
            ArticleWidget {{
                background: {theme['background']};
                border: 1px solid {theme['border']};
                border-radius: 8px;
            }}
        """
        
        app.setStyleSheet(stylesheet)