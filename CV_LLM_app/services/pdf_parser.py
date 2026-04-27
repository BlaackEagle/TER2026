import os 
#from pypdf import PdfReader   //ne sert plus dcp
import pdfplumber


class PdfParser:
    def cleaner_texte2(self, texte) :  
        if not texte:
            return ""
        return texte.strip()


    #Version avec pdfPlumber qui marche tellement mieux qu'avec PdfReader
    def extraire_intelligent(self, pdf_object):
        texte_complet = ""
        with pdfplumber.open(pdf_object) as pdf:
            for page in pdf.pages:
                texte = page.extract_text(layout=True)
                if texte:
                    texte_complet += texte + " "

        return self.cleaner_texte2(texte_complet)
