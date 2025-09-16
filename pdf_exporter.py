import os
from datetime import datetime
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from PyQt5.QtGui import QPixmap
import requests
from io import BytesIO
from reportlab.platypus import KeepTogether

class PDFExporter:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        
    def export_to_pdf(self, articles, filename=f"news_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"):
        """Exporte les articles vers un fichier PDF"""
        try:
            # Créer le document PDF
            doc = SimpleDocTemplate(
                filename,
                pagesize=A4,
                rightMargin=72,
                leftMargin=72,
                topMargin=72,
                bottomMargin=72
            )
            
            # Contenu du PDF
            story = []
            
            # Titre principal
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=self.styles['Heading1'],
                fontSize=20,
                spaceAfter=30,
                alignment=1  # Centré
            )
            
            title = Paragraph("EXPORTATION D'ARTICLES", title_style)
            story.append(title)
            
            # Date d'exportation
            date_str = datetime.now().strftime("%d/%m/%Y à %H:%M")
            date_text = Paragraph(f"<i>Exporté le {date_str}</i>", self.styles["Italic"])
            story.append(date_text)
            story.append(Spacer(1, 20))
            
            # Ajouter chaque article
            for i, article in enumerate(articles, 1):
                story.append(self.create_article_section(article, i))
                story.append(Spacer(1, 15))
                
                # Saut de page après 2 articles
                if i % 2 == 0:
                    story.append(Spacer(1, 30))
            
            # Générer le PDF
            doc.build(story)
            return True, f"PDF exporté avec succès: {filename}"
            
        except Exception as e:
            return False, f"Erreur lors de l'export PDF: {str(e)}"
    
    def create_article_section(self, article, index):
        """Crée une section pour un article"""

        
        elements = []
        
        # Titre de l'article
        title_style = ParagraphStyle(
            'ArticleTitle',
            parent=self.styles['Heading2'],
            fontSize=14,
            textColor=colors.darkblue,
            spaceAfter=6
        )
        
        title = Paragraph(f"{index}. {article['title']}", title_style)
        elements.append(title)
        
        # Métadonnées
        meta_text = f"""
        <b>Source:</b> {article['source']} | 
        <b>Date:</b> {article['published_at']} | 
        <b>Auteur:</b> {article['author']}
        """
        
        meta = Paragraph(meta_text, self.styles["Normal"])
        elements.append(meta)
        elements.append(Spacer(1, 8))
        
        # Description
        if article['description'] and article['description'] != "Aucune description disponible":
            desc_style = ParagraphStyle(
                'Description',
                parent=self.styles['BodyText'],
                fontSize=10,
                textColor=colors.darkgreen,
                spaceAfter=8
            )
            description = Paragraph(article['description'], desc_style)
            elements.append(description)
            elements.append(Spacer(1, 8))
        
        # URL
        url_text = f"<b>URL:</b> <link href='{article['url']}' color='blue'>{article['url']}</link>"
        url = Paragraph(url_text, self.styles["Normal"])
        elements.append(url)
        
        # Ligne séparatrice
        elements.append(Spacer(1, 12))
        elements.append(self.create_separator())
        
        # Retourner tous les éléments groupés ensemble
        return KeepTogether(elements)
    
    def create_separator(self):
        """Crée une ligne séparatrice"""
        from reportlab.platypus.flowables import HRFlowable
        return HRFlowable(
            width="100%",
            thickness=1,
            lineCap='round',
            color=colors.grey,
            spaceAfter=6,
            spaceBefore=6
        )
    
    def export_summary_pdf(self, articles, filename="news_summary.pdf"):
        """Exporte un résumé statistique en PDF"""
        try:
            doc = SimpleDocTemplate(filename, pagesize=A4)
            story = []
            
            # Titre
            title = Paragraph("RÉSUMÉ STATISTIQUE DES ARTICLES", self.styles['Heading1'])
            story.append(title)
            story.append(Spacer(1, 20))
            
            # Statistiques
            stats = self.generate_statistics(articles)
            
            # Tableau des statistiques
            data = [['Statistique', 'Valeur']]
            for key, value in stats.items():
                data.append([key, str(value)])
            
            table = Table(data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            
            story.append(table)
            story.append(Spacer(1, 20))
            
            doc.build(story)
            return True, f"Résumé PDF exporté: {filename}"
            
        except Exception as e:
            return False, f"Erreur résumé PDF: {str(e)}"
    
    def generate_statistics(self, articles):
        """Génère des statistiques sur les articles"""
        from collections import Counter
        import pandas as pd
        
        stats = {
            "Nombre total d'articles": len(articles),
            "Sources uniques": len(set(article['source'] for article in articles))
        }
        
        # Compteur des sources
        source_counts = Counter(article['source'] for article in articles)
        stats["Source la plus fréquente"] = source_counts.most_common(1)[0][0] if source_counts else "Aucune"
        
        return stats