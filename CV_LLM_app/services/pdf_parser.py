import os 
from pypdf import PdfReader


def extraire_text_pdf(pdf_path) :

    if not os.path.exists(pdf_path) : # Test si le chemin du pdf est valide (sécurité)
        print("Chemin non valide")
        return None

    try :
        reader = PdfReader(pdf_path)
        text_final = ""

        for page in reader.pages :
            text = page.extract_text()
            if len(text) != 0 :
                text_final += text

    except Exception as e :
        print("Erreur avec PdfReader")
        return None

    return text_final

if __name__ == "__main__":
    print("--------------")
    test_path = "../uploads/CV_Samy.pdf"

    text = extraire_text_pdf(test_path)
    print(text)
    with open("../uploads/CV_Samy.txt", "w", encoding="utf-8") as fichier:
        fichier.write(text)
    print("----------")