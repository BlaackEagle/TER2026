import os 
from pypdf import PdfReader
import pdfplumber

def cleaner_texte2(texte) :  
    if not texte:
        return ""
    return texte.strip()


#Version avec pdfPlumber qui marche tellement mieux qu'avec PdfReader
def extraire_intelligent(pdf_object):
    texte_complet = ""
    with pdfplumber.open(pdf_object) as pdf:
        for page in pdf.pages:
            texte = page.extract_text(layout=True)
            if texte:
                texte_complet += texte + " "

    return cleaner_texte2(texte_complet)

if __name__ == "__main__":
    print("--------------")
    test_path = "../uploads/CV_Samy.pdf"

    text = extraire_text_pdf(test_path)
    print(text)
    with open("../uploads/CV_Samy.txt", "w", encoding="utf-8") as fichier:
        fichier.write(text)
    print("----------")