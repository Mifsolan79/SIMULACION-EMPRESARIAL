import os
from PyPDF2 import PdfReader

PDF_DIR = r"f:\17. SIMULACION EMPRESARIAL\TEMA 01"
PDF_NAME = "Simulacion empresarial. Tema 1.pdf"
OUT_DIR = r"f:\17. SIMULACION EMPRESARIAL\pdf_texts"
os.makedirs(OUT_DIR, exist_ok=True)

pdf_path = os.path.join(PDF_DIR, PDF_NAME)
out_path = os.path.join(OUT_DIR, "tema_1.txt")

if not os.path.exists(pdf_path):
    print(f"PDF NO ENCONTRADO: {pdf_path}")
else:
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"Tema 1: {len(reader.pages)} págs, {len(text)} chars -> {out_path}")
