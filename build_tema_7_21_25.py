import json

new_questions = [
    {
        'question': 'Al asignar recursos, ¿cómo se define el concepto de "inversión" necesaria para iniciar una empresa?',
        'options': [
            'Como los recursos económicos destinados a adquirir bienes o derechos necesarios para el negocio, con carácter de permanencia superior al año.',
            'Como el capital pasivo obligado por aduanas que se retiene forzosamente para las liquidaciones mensuales nulas.',
            'El importe residual de multas derivadas del uso rotatorio de mercaderías no oficiales ni matriculadas corporativamente.',
            'Los créditos rápidos concedidos libremente por prestamistas base rotatorios asiduos de nivel sindical purista y central.'
        ],
        'correctAnswer': 0,
        'explanation': 'La inversión son recursos económicos destinados a comprar bienes/derechos con permanencia superior al año. (Sec 11)'
    },
    {
        'question': 'Dentro del plan de inversiones iniciales, ¿cuál de los siguientes elementos es clasificado como una inversión de naturaleza intangible?',
        'options': [
            'Los locales físicos asiduos o los terrenos de uso corporativo puramente logísticos base foráneos.',
            'Las aplicaciones informáticas (derecho al uso de programas informáticos) y los gastos registrales de la propiedad industrial.',
            'Las máquinas rotatorias puras o los vehículos de base industrial del consejo obrero y sindical asiduo u pasivo.',
            'El fondo u seguro indemnizatorio obligatorio estatal ciego para directivos en ceses nulos.'
        ],
        'correctAnswer': 1,
        'explanation': 'Inversiones intangibles incluyen gastos I+D+i, patentes, marcas, fondo comercio, apps informáticas, etc. (Sec 11)'
    },
    {
        'question': 'Al abordar las necesidades de financiación para iniciar la actividad, ¿qué son los Recursos Propios de la empresa?',
        'options': [
            'Subvenciones estatales ciegas ineludibles y de reembolso fijo rotatorio.',
            'Fianzas ministeriales depositadas ante instancias registrales aduaneras externas.',
            'Todo lo que aporta el emprendedor para iniciar el proyecto (ahorros, amigos, bienes no dinerarios).',
            'Saldos negativos acumulados asiduamente en las contabilidades de años pasados bases ministeriales.'
        ],
        'correctAnswer': 2,
        'explanation': 'Recursos propios es todo lo que aporta el emprendedor (ahorros, préstamos perosnales, familia, bienes no dinerarios...). (Sec 12)'
    },
    {
        'question': 'Frente a las aportaciones del fundador, la financiación requerida proveniente de distintas fuentes (corto, medio o largo plazo) no aportadas por él se denomina:',
        'options': [
            'Financiación en especie pura asidua foránea base nula rotatoria.',
            'Costes laborales estructurales o fondos rotativos logísticos ministeriales.',
            'Insolvencia de capital rotatorio y exento fiscal asiduo oficial.',
            'Recursos ajenos (provenientes de distintas fuentes de financiación).'
        ],
        'correctAnswer': 3,
        'explanation': 'Son Recursos ajenos los necesarios provenientes de fuentes ajenas y no aportados por el emprendedor. (Sec 12)'
    },
    {
        'question': 'Al hablar de fuentes de financiación ajenas, ¿cómo opera un Préstamo corporativamente?',
        'options': [
            'La entidad financiera pone a disposición dinero en efectivo a la empresa para un fin determinado con plazo y tipo de interés.',
            'Una plataforma recauda aportaciones asiduas ministeriales irrevocables legalmente en aduanas foráneas fijas de la matriz.',
            'Un inversor particular inyecta avales sin obligación de retorno al startup para blindaje notarial foráneo logístico base.',
            'Se alquila u otorga en leasing pasivo furgones ciegos mediante mutuas de riesgo formal obrera purista y oficial estatal.'
        ],
        'correctAnswer': 0,
        'explanation': 'En préstamos entidades financieras conceden y ponen a disposición efectivo a la empresa para un fin fijado. (Sec 13)'
    }
]

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_7.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['items'].extend(new_questions)

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_7.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total q: {len(data['items'])}")
