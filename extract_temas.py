import os
from PyPDF2 import PdfReader

BASE_DIR = r"f:\17. SIMULACION EMPRESARIAL"
OUT_DIR = os.path.join(BASE_DIR, "pdf_texts")
os.makedirs(OUT_DIR, exist_ok=True)

temas = [
    {"dir": "TEMA 05", "file": "Simulacion empresarial. Tema 5.pdf", "out": "tema_5.txt"},
    {"dir": "TEMA 06", "file": "Simulacion empresarial. Tema 6.pdf", "out": "tema_6.txt"},
    {"dir": "TEMA 07", "file": "Simulacion empresarial. Tema 7.pdf", "out": "tema_7.txt"},
    {"dir": "TEMA 08", "file": "Simulacion empresarial. Tema 8.pdf", "out": "tema_8.txt"}
]

for t in temas:
    pdf_path = os.path.join(BASE_DIR, t["dir"], t["file"])
    out_path = os.path.join(OUT_DIR, t["out"])
    
    if not os.path.exists(pdf_path):
        print(f"PDF NO ENCONTRADO: {pdf_path}")
        continue
        
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
        
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(text)
        
    print(f"Extraído {t['file']}: {len(reader.pages)} págs, {len(text)} chars -> {out_path}")
