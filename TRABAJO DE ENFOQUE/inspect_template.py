from docx import Document

def inspect_template(template_path):
    doc = Document(template_path)
    
    print(f"--- Inspección de {template_path} ---")
    
    # Inspeccionar fuentes de los estilos principales
    styles_to_check = ['Normal', 'Heading 1', 'Heading 2', 'Title', 'Subtitle']
    for style_name in styles_to_check:
        if style_name in doc.styles:
            style = doc.styles[style_name]
            font = style.font
            print(f"\nEstilo: {style_name}")
            print(f"  Fuente: {font.name}")
            print(f"  Tamaño: {font.size.pt if font.size else 'Default'}")
            print(f"  Negrita: {font.bold}")
    
    # Inspeccionar los primeros párrafos para ver si hay contenido previo/formato directo
    print("\n--- Primeros 10 párrafos del documento ---")
    for i, para in enumerate(doc.paragraphs[:10]):
        print(f"P{i}: '{para.text[:50]}...' style='{para.style.name}'")
        if para.runs:
            run = para.runs[0]
            print(f"  Run 0: Font={run.font.name}, Size={run.font.size.pt if run.font.size else 'Default'}, Bold={run.font.bold}")

if __name__ == "__main__":
    template = r'f:\17. SIMULACION EMPRESARIAL\TRABAJO DE ENFOQUE\Plantilla de documentos (1).docx'
    inspect_template(template)
