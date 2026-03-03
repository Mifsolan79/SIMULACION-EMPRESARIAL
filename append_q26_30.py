import json

new_questions = [
    {
        'question': 'Según el Observatorio Español e instituciones, ¿cómo se define la Responsabilidad Social Corporativa (RSC)?',
        'options': [
            'Como el cierre progresivo de todas las líneas industriales por normas locales.',
            'Como la donación anual obligatoria de todos los dividendos exentos de tributo.',
            'Como la forma de dirigir basada en gestionar los impactos sobre el entorno, clientes, empleados, medioambiente y sociedad.',
            'Como el mero pago de indemnizaciones operativas por la rotación forzosa aduanera.'
        ],
        'correctAnswer': 2,
        'explanation': 'La RSC gestiona impactos generados sobre el entorno, empleados y medio. (Sec 12)'
    },
    {
        'question': 'En relación a la RS, la ONU aprobó en 1999 un documento clave con diez principios. ¿Cómo se denomina?',
        'options': [
            'Pacto Mundial (UN Global Compact).',
            'Fondo Monetario Climático.',
            'Tratado de Sanciones Aduaneras y Laborales.',
            'Resolución de Nacionalizaciones Ecológicas.'
        ],
        'correctAnswer': 0,
        'explanation': 'La ONU aprobó el Pacto Mundial (1999) con 10 principios. (Sec 12)'
    },
    {
        'question': 'Respecto al marco legal nacional sobre prevención, ¿en qué año se aprobó la normativa formal "Ley de Prevención de Riesgos Laborales"?',
        'options': [
            'En 1980.',
            'En 1995.',
            'En 2010.',
            'En 2021.'
        ],
        'correctAnswer': 1,
        'explanation': 'En 1995 se aprueba la Ley de Prevención de Riesgos Laborales. (Sec 13)'
    },
    {
        'question': '¿Cuál es el principal propósito u objetivo rector central e ineludible perseguido en prevención de riesgos laborales?',
        'options': [
            'Cobrar subvenciones asiduas de los fondos burocráticos europeos u orgánicos.',
            'Disminuir las horas efectivas forzosas estipuladas sin merma sindical fija.',
            'Minimizar y evitar las causas de accidentes de trabajo y de enfermedades profesionales en la plantilla.',
            'Inhabilitar por cese y veto las rotatorias inspecciones operativas sindicales externas limitadas.'
        ],
        'correctAnswer': 2,
        'explanation': 'La principal función es minimizar o evitar accidentes o enfermedades en el trabajo. (Sec 13)'
    },
    {
        'question': 'En la organización de modernas entidades o corporaciones tipo startup tecnológicas, ¿qué cargo corporativo u operario representan tradicional e internacionalmente las reconocidas siglas CEO?',
        'options': [
            'Control y Evaluación Operacional puro base organizativo territorial local.',
            'Encargado General de Operativas de Marketing y Ventas referenciado de corte masivo.',
            'Comité Ético Orientativo adscrito a recursos laborales de índole u rango transversal y legal.',
            'Director Ejecutivo, o Consejero Delegado (Chief Executive Officer).'
        ],
        'correctAnswer': 3,
        'explanation': 'CEO (Chief Executive Officer), o director ejecutivo/consejero delegado de la compañía. (Sec 14)'
    }
]

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_6.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['items'].extend(new_questions)

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_6.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total items in JSON: {len(data['items'])}")
