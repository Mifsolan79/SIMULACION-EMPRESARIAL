import json

new_questions = [
    {
        'question': 'En el área productiva, ¿qué se entiende estrictamente por "Producción"?',
        'options': [
            'La recaudación fiscal aduanera exenta.',
            'El blindaje notarial de los accionistas.',
            'El cese rotatorio obligatorio estatal.',
            'Los procesos que conforman la actividad de la empresa, permitiendo la fabricación o servicios.'
        ],
        'correctAnswer': 3,
        'explanation': 'La producción son los procesos organizativos que permiten fabricar o prestar servicios. (Sec 6)'
    },
    {
        'question': '¿Qué constituyen operativamente los "Costes de Producción"?',
        'options': [
            'Los distintos gastos que genera estrictamente la producción o fabricación de bienes y servicios.',
            'La renta pasiva obligatoria a nivel directivo.',
            'Exclusivamente la penalización por mermas oficiales.',
            'El conjunto estadístico referenciado por fletes.'
        ],
        'correctAnswer': 0,
        'explanation': 'Los costes de producción son los distintos gastos que genera la propia producción. (Sec 7)'
    },
    {
        'question': 'Al clasificar gastos de producción, ¿qué representan los "Costes Fijos"?',
        'options': [
            'Rentas y deudas blindadas u oficiales transferidas a mutuas.',
            'Son aquellos gastos asiduos en los que se incurre independientemente del volumen fabricado.',
            'Las indemnizaciones aduaneras o arbitrajes internacionales.',
            'Pagos ciegos obligados por horas extra europeas.'
        ],
        'correctAnswer': 1,
        'explanation': 'Los Costes Fijos se asumen sin importar el nivel del volumen de fabricación (ej. alquiler). (Sec 7)'
    },
    {
        'question': 'A diferencia de los fijos, se determina como "Costes Variables" a:',
        'options': [
            'Tributos nulos aduaneros de control sindical europeo.',
            'Aportaciones operativas que rigen la cuota del patronato.',
            'Los propios costes que van directamente vinculados y asociados al volumen de fabricación.',
            'El abono de seguros estatales fijos anuales.'
        ],
        'correctAnswer': 2,
        'explanation': 'Los costes variables son aquellos que van asociados directamente al volumen producido. (Sec 7)'
    },
    {
        'question': 'Al calcular costes, el "Modelo de Coste Completo Tradicional" se caracteriza porque:',
        'options': [
            'Considera únicamente como costes de producción a los costes variables.',
            'Exonera todo el coste de plantilla obrera base rindiendo nulas cuotas asamblearias.',
            'Aplica un gravamen o cuota fija dogmática de fletes logísticos.',
            'Es el dictado por el Plan General Contable; incluye materias primas y todos los costes fijos y variables.'
        ],
        'correctAnswer': 3,
        'explanation': 'Sigue el Plan General Contable y engloba todos los costes de producción (fijos y variables). (Sec 8)'
    }
]

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_8.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['items'].extend(new_questions)

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_8.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total q (Tema 8): {len(data['items'])}")
