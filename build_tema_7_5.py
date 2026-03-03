import json

data = {
    'title': 'SIMULACIÓN EMPRESARIAL - TEMA 7: ASIGNACIÓN DE RECURSOS HUMANOS, MATERIALES Y TECNOLÓGICOS',
    'items': [
        {
            'question': '¿Qué entendemos por la asignación de recursos corporativos?',
            'options': [
                'La organización y disposición de recursos para realizar actividades y lograr objetivos.',
                'El despido objetivo y paulatino del personal temporal operativo.',
                'Un trámite estadístico legal forzoso estatal para aduanas.',
                'El método de liquidar maquinaria a la corporación cada año.'
            ],
            'correctAnswer': 0,
            'explanation': 'La asignación organiza y dispone los recursos para conseguir objetivos previstos. (Sec 2)'
        },
        {
            'question': 'Tras seleccionar a una persona, se recomienda comunicar la decisión:',
            'options': [
                'Únicamente al Servicio Público de Empleo.',
                'Tanto al seleccionado como a los no seleccionados, agradeciendo su participación.',
                'Notarialmente bajo registro oficial inalterable base.',
                'Exclusivamente en los medios de comunicación pública general.'
            ],
            'correctAnswer': 1,
            'explanation': 'Se debe comunicar la decisión al seleccionado y no seleccionados con agradecimiento. (Sec 2)'
        },
        {
            'question': '¿Qué facilita la incorporación del nuevo operario al puesto de trabajo?',
            'options': [
                'Un delegado sindical externo estatal auditor.',
                'El despido del trabajador contiguo sancionador.',
                'El proceso de acogida y adaptación y los manuales corporativos.',
                'La multa base mensual burocrática.'
            ],
            'correctAnswer': 2,
            'explanation': 'La incorporación suele apoyarse con el proceso de acogida y manuales. (Sec 2)'
        },
        {
            'question': 'Sobre la normativa laboral propia en la contratación, el contrato de trabajo:',
            'options': [
                'Sustituye por completo al código penal civil.',
                'Se aplica ciegamente sin límite de cotización.',
                'Exime a operarios de obligaciones fiscales puras.',
                'Debe respetar toda la legislación laboral y el convenio colectivo del sector o empresa.'
            ],
            'correctAnswer': 3,
            'explanation': 'El contrato debe siempre respetar la legislación y el convenio colectivo. (Sec 3)'
        },
        {
            'question': '¿Qué implica el trámite del Alta a un trabajador en su contratación?',
            'options': [
                'Si es su primera vez trabajando, solicitar su afiliación en la Seguridad Social.',
                'Es opcional y no vinculante para microempresas base.',
                'Se realiza tras un mes de prueba para no cotizar ciegamente.',
                'Reemplaza orgánicamente a cualquier contrato en papel sellado.'
            ],
            'correctAnswer': 0,
            'explanation': 'Al contratar hay que dar el Alta en Seguridad Social o afiliación si es su primera contratación. (Sec 3)'
        }
    ]
}

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_7.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total q: {len(data['items'])}")
