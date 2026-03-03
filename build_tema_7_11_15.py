import json

new_questions = [
    {
        'question': 'En relación a las vías de inserción, ¿cómo podemos definir conceptualmente el autoempleo?',
        'options': [
            'Como la subordinación directa bajo nómina estatal sin derecho a renunciar u oponerse ministerialmente.',
            'Como el cese temporal del trabajador por reducción forzosa de la plantilla industrial rotatoria.',
            'Como toda actividad laboral generada por la persona misma, que se organiza de forma autónoma asumiendo los riesgos.',
            'Como un método punitivo base o de multa coercitiva aplicada a antiguos directivos foráneos inactivos.'
        ],
        'correctAnswer': 2,
        'explanation': 'El autoempleo es la actividad laboral organizada de forma autónoma y asumiendo los riesgos. (Sec 6)'
    },
    {
        'question': 'Entre las ventajas que directamente tiene o aporta el autoempleo para el responsable, podemos destacar:',
        'options': [
            'El ahorro burocrático de no declarar impuestos en aduanas y no participar tributariamente en el mercado.',
            'La inmovilidad corporativa pura y la delegación de responsabilidades a la asamblea sindical externa estatal.',
            'El cobro obligatorio y asiduo del fondo monetario por pertenecer a registros pasivos de inversión nula absoluta.',
            'La estabilidad en el empleo por depender de uno mismo, la autonomía y la obtención de máximos beneficios.'
        ],
        'correctAnswer': 3,
        'explanation': 'El autoempleo aporta estabilidad, autonomía y alcance de máximos beneficios. (Sec 6)'
    },
    {
        'question': 'Al estructurar el autoempleo como empresario individual (autónomo), ¿qué característica define su nivel de responsabilidad legal?',
        'options': [
            'Es de carácter o responsabilidad ilimitada, respondiendo de sus obligaciones con sus bienes, presentes y futuros.',
            'Es totalmente limitada o fraccionada puramente al capital fundacional inicial aportado ante escribanos aduaneros fijos.',
            'Su responsabilidad expira anualmente cuando los inspectores no exigen balances mercantiles o registros rotativos.',
            'Pasa directamente al avalista y prestamista o fondo promotor estatal tras 3 años ininterrumpidos de trabajo civil.'
        ],
        'correctAnswer': 0,
        'explanation': 'El empresario individual asume responsabilidad ilimitada con todos sus bienes. (Sec 6)'
    },
    {
        'question': 'Respecto de las obligaciones iniciales al gestar un autoempleo e iniciar actividad autónoma, RETA significa:',
        'options': [
            'Recurso Estándar de Trámites Aduaneros base.',
            'Régimen Especial de Trabajadores Autónomos.',
            'Registro Económico y Tributario Anual forzoso.',
            'Reembolso Estatal Técnico para Auxiliares contables.'
        ],
        'correctAnswer': 1,
        'explanation': 'El RETA es el Régimen Especial de Trabajadores Autónomos de la Seguridad Social. (Sec 6)'
    },
    {
        'question': 'En relación a la remuneración laboral ordinaria dictada, ¿qué límite legal establece la normativa sobre el pago en especie del salario?',
        'options': [
            'Exige abonar el 60% mensualmente en bonos gubernamentales.',
            'Debe obligatoriamente ser equivalente al Salario Mínimo en moneda.',
            'Limita a un 30% del salario total la retribución recibida en especie.',
            'Lo prohíbe completamente bajo sanción administrativa regional aduanera.'
        ],
        'correctAnswer': 2,
        'explanation': 'La retribución en especie nunca puede exceder del 30% del salario total. (Sec 7)'
    }
]

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_7.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['items'].extend(new_questions)

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_7.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total q: {len(data['items'])}")
