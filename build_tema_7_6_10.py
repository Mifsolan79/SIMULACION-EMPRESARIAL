import json

new_questions = [
    {
        'question': 'Respecto al registro del contrato de trabajo en España, en el Servicio Empleo Público Estatal (SEPE), este debe realizarse en un plazo de:',
        'options': [
            '10 horas naturales exclusivamente presenciales.',
            '10 días, realizándose de forma obligatoria por vía telemática.',
            '6 meses laborables y administrativos mercantiles.',
            'Un plazo indefinido si el sueldo cotizado es mínimo.'
        ],
        'correctAnswer': 1,
        'explanation': 'El registro del contrato en el SEPE debe hacerse vía telemática en el plazo de 10 días. (Sec 3)'
    },
    {
        'question': '¿Cómo se define el contrato de trabajo laboralmente?',
        'options': [
            'Como el acta notarial donde inversores forman un consejo asambleario directo.',
            'Como listado contable puro del balance obrero patronal aduanero.',
            'Acuerdo entre empresario y trabajador donde éste presta servicio bajo dirección del primero a cambio de retribución.',
            'Cesión base de la propiedad curricular para eximir cuotas estatales tributarias.'
        ],
        'correctAnswer': 2,
        'explanation': 'Es el acuerdo donde el trabajador presta un servicio bajo dirección a cambio de retribución. (Sec 4)'
    },
    {
        'question': 'En relación legal a las contrataciones, ¿quiénes pueden firmar un contrato de trabajo?',
        'options': [
            'Exclusivamente mandos mayores de edad y superando los 30 para directivos fijos.',
            'Todo infante desde su primer año por medio del tutor base legal puro.',
            'Todos los operarios sin límite y forzosamente a los 25 años como barrera.',
            'Los mayores de edad, los emancipados y los mayores de 16 con autorización de padres o tutores.'
        ],
        'correctAnswer': 3,
        'explanation': 'Pueden firmarlo mayores de 18, emancipados, o mayores de 16 con autorización. (Sec 4)'
    },
    {
        'question': 'Según la duración estipulada legalmente, los contratos de trabajo se diferencian corporativamente en dos grandes modalidades:',
        'options': [
            'Los indefinidos y los temporales.',
            'Los formativos puramente burocráticos y los asiduos técnicos nulos.',
            'De obligación rotatoria exclusiva y de cese estatal puro aduanero.',
            'Contratos orales ciegos mercantiles y de papel sellado foráneo libre.'
        ],
        'correctAnswer': 0,
        'explanation': 'Según duración, se distinguen los contratos indefinidos y temporales. (Sec 4)'
    },
    {
        'question': 'En el marco legal de la contratación, ¿qué implica el periodo de prueba?',
        'options': [
            'Prohíbe la renuncia corporativa durante los primeros cinco años de vigencia patronal legal.',
            'Permite a cualquiera de las partes dar por finalizada la relación sin justificar o estipular causa.',
            'Otorga potestad absoluta del operario puramente para imponer multas administrativas al promotor.',
            'Inhabilita al trabajador puramente base a percibir liquidaciones formales contables aduaneras.'
        ],
        'correctAnswer': 1,
        'explanation': 'El periodo de prueba permite que las partes finalicen la relación sin causa justificada. (Sec 4)'
    }
]

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_7.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['items'].extend(new_questions)

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_7.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total q: {len(data['items'])}")
