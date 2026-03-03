from docx import Document
from docx.shared import RGBColor

def inspect_advanced(template_path):
    doc = Document(template_path)
    print(f"--- Inspección Detallada de {template_path} ---")
    
    styles_to_check = ['Heading 1', 'Heading 2', 'Title', 'Normal']
    for style_name in styles_to_check:
        if style_name in doc.styles:
            style = doc.styles[style_name]
            font = style.font
            color = font.color.rgb if font.color and font.color.rgb else "Default"
            print(f"\nEstilo: {style_name}")
            print(f"  Fuente: {font.name}")
            print(f"  Tamaño: {font.size.pt if font.size else 'Default'}")
            print(f"  Color (RGB): {color}")
            print(f"  Negrita: {font.bold}")

    # Mirar los runs directos en los primeros parrafos (a veces el formato es directo)
    print("\n--- Formato directo en párrafos clave ---")
    for i, para in enumerate(doc.paragraphs[:15]):
        if para.text.strip():
            print(f"P{i} ['{para.text[:30]}...']: Style={para.style.name}")
            for r_idx, run in enumerate(para.runs):
                color = run.font.color.rgb if run.font.color and run.font.color.rgb else "Default"
                size = run.font.size.pt if run.font.size else "Default"
                print(f"  Run {r_idx}: Font={run.font.name}, Size={size}, Bold={run.font.bold}, Color={color}")

if __name__ == "__main__":
    template = r'f:\17. SIMULACION EMPRESARIAL\TRABAJO DE ENFOQUE\Plantilla de documentos (1).docx'
    inspect_advanced(template)
