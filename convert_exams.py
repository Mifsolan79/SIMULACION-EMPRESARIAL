import json
import os
import re

def parse_txt_to_json(txt_path, output_json_path, title):
    if not os.path.exists(txt_path):
        print(f"Error: {txt_path} not found")
        return

    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    items = []
    current_item = None
    
    # Map for correct answers
    ans_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Question
        match_q = re.match(r'^Pregunta \d+:\s*(.*)', line)
        if match_q:
            if current_item:
                items.append(current_item)
            current_item = {
                'question': match_q.group(1),
                'options': [],
                'correctAnswer': None,
                'explanation': ""
            }
            continue
            
        # Options
        match_opt = re.match(r'^([A-D])\)\s*(.*)', line)
        if match_opt and current_item:
            current_item['options'].append(match_opt.group(2))
            continue
            
        # Correct Answer
        match_ans = re.match(r'^Respuesta Correcta:\s*([A-D])', line)
        if match_ans and current_item:
            current_item['correctAnswer'] = ans_map.get(match_ans.group(1))
            continue
            
        # Explanation
        match_exp = re.match(r'^Explicación:\s*(.*)', line)
        if match_exp and current_item:
            current_item['explanation'] = match_exp.group(1)
            continue
            
    # Final item
    if current_item:
        items.append(current_item)

    data = {
        'title': title,
        'items': items
    }

    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Generated {output_json_path} with {len(items)} questions.")

# Configuration
base_dir = r"f:/17. SIMULACION EMPRESARIAL"
exam_dir = os.path.join(base_dir, "EXAMENES POR TEMAS")
output_dir = os.path.join(base_dir, "data")

temas = [
    {"num": "5", "title": "SIMULACIÓN EMPRESARIAL - TEMA 5: LA FORMA JURÍDICA DE LA EMPRESA Y SU IDENTIFICACIÓN"},
    {"num": "6", "title": "SIMULACIÓN EMPRESARIAL - TEMA 6: TRÁMITES DE CONSTITUCIÓN Y PUESTA EN MARCHA"},
    {"num": "7", "title": "SIMULACIÓN EMPRESARIAL - TEMA 7: LA GESTIÓN DE LA EMPRESA Y LA SEGURIDAD SOCIAL"},
    {"num": "8", "title": "SIMULACIÓN EMPRESARIAL - TEMA 8: PLAN DE MARKETING: PRODUCTO, PRODUCCIÓN Y APROVISIONAMIENTO"}
]

if __name__ == "__main__":
    for tema in temas:
        txt_file = f"TEMA 0{tema['num']}.txt"
        json_file = f"db_tema_{tema['num']}.json"
        
        txt_path = os.path.join(exam_dir, txt_file)
        json_path = os.path.join(output_dir, json_file)
        
        parse_txt_to_json(txt_path, json_path, tema['title'])
