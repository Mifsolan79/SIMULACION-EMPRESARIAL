import json

new_questions = [
    {
        'question': 'En el diseño del producto, los "atributos" se consideran como:',
        'options': [
            'Los aranceles estatales ineludibles.',
            'Las multas aduaneras de carácter forzoso.',
            'El diseño, la calidad, envase, envoltorio y marca.',
            'La liquidación técnica asidua por asamblea.'
        ],
        'correctAnswer': 2,
        'explanation': 'Son atributos de producto: la calidad, marca, envase, envoltorio y diseño. (Sec 4)'
    },
    {
        'question': '¿Qué se entiende por "Obsolescencia programada"?',
        'options': [
            'Fondos burocráticos retenidos en la corporación matriz.',
            'La indemnización estatal a patronales sindicales.',
            'El despido periódico de cada operario al año.',
            'La determinación previa por el fabricante del fin de la vida útil del producto.'
        ],
        'correctAnswer': 3,
        'explanation': 'La obsolescencia programada acota la vida útil del producto. (Sec 4)'
    },
    {
        'question': 'La "Fase de Introducción" en el ciclo de vida del producto se caracteriza porque:',
        'options': [
            'Acaba de entrar al mercado y sus ventas comienzan con crecimiento lento.',
            'Las ventas decaen de manera obligatoria por regulación arancelaria.',
            'Representa el pico más alto de producción asidua rotativa.',
            'Es el momento de liquidación oficial de la matriz del estado.'
        ],
        'correctAnswer': 0,
        'explanation': 'En la Introducción el producto entra al mercado con lenta subida de ventas. (Sec 4)'
    },
    {
        'question': 'En el ciclo de vida del producto, la fase de "Madurez" ocurre cuando:',
        'options': [
            'Nace en fábrica y sufre un cese temporal logístico.',
            'Las ventas logran su tope y se estabilizan, siendo difícil conseguir más ingresos.',
            'Heredan pasivos contables nulos absolutos del patronato.',
            'Se desechan por el tribunal aduanero forzoso europeo.'
        ],
        'correctAnswer': 1,
        'explanation': 'La madurez sucede cuando las ventas se estabilizan. (Sec 4)'
    },
    {
        'question': 'En el ciclo de vida del producto, la fase de "Declive" implica que:',
        'options': [
            'El artículo debe ser vendido pasivamente a aduanas.',
            'Pasa al monopolio y control blindado gubernamental.',
            'Las ventas descienden a causa de una bajada en la demanda de los consumidores.',
            'Es premiado con un plus oficial purista operativo.'
        ],
        'correctAnswer': 2,
        'explanation': 'El Declive ocurre cuando las ventas descienden operativamente. (Sec 4)'
    }
]

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_8.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['items'].extend(new_questions)

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_8.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total q (Tema 8): {len(data['items'])}")
