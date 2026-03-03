import json

new_questions = [
    {
        'question': 'En relación a la gestión económica del personal, ¿quién es el responsable de hacer el ingreso mensualmente de las cotizaciones a la Seguridad Social (costes sociales)?',
        'options': [
            'Exclusivamente la agrupación o mutua de accidentes laborales base regional sindical.',
            'Directamente el trabajador restándolo libremente de su fondo de capitalización.',
            'El estado, deducido del fondo monetario centralizado notarial aduanero.',
            'El empresario (o la empresa), ingresándolo en la Tesorería General de la Seguridad Social.'
        ],
        'correctAnswer': 3,
        'explanation': 'Es el empresario el responsable de hacer el ingreso mensual a la Tesorería. (Sec 7)'
    },
    {
        'question': '¿Qué son los costes salariales en relación al personal de la organización?',
        'options': [
            'El total de percepciones económicas que reciben los miembros por prestar sus servicios profesionales.',
            'Un impuesto pasivo aduanero que retiene forzosamente porcentajes tributarios ciegos base.',
            'La dotación o partida para reponer mobiliario obsoleto en base a nóminas activas.',
            'El puro descuento por sanciones laborales restadas directamente del salario base estatal.'
        ],
        'correctAnswer': 0,
        'explanation': 'Los costes salariales son el total de las percepciones económicas del trabajador por sus servicios. (Sec 8)'
    },
    {
        'question': 'Dentro de la estructura del salario, si el salario base no está fijado por algún convenio colectivo de la empresa o sector, ¿qué se considera o establece legalmente como salario base?',
        'options': [
            'Un promedio de la facturación bimensual de la empresa.',
            'El Salario Mínimo Interprofesional (SMI).',
            'La retribución máxima estipulada para consejeros sin dividendos o rotativos base nulos fijos de fondo mutuo.',
            'Un pago simbólico en especie o por horas base.'
        ],
        'correctAnswer': 1,
        'explanation': 'Si no lo fija el convenio, se considera como salario base el Salario Mínimo Interprofesional. (Sec 8)'
    },
    {
        'question': 'En la estructura del salario, el plus de peligrosidad o de nocturnidad son clasificados legalmente como:',
        'options': [
            'Deducciones personales rotativas u pasivas obligatorias de carácter purista central.',
            'Salidas contables asiduas foráneas de base corporativa externa o base burocrática ciega de indemnizaciones base.',
            'Complementos salariales referidos al puesto de trabajo (según características o forma de actividad).',
            'Subvenciones estatales blindadas no tributables fijas o referenciadas a puras variables asiduas logísticas.'
        ],
        'correctAnswer': 2,
        'explanation': 'Son complementos salariales derivados de las características del puesto o actividad. (Sec 8)'
    },
    {
        'question': 'Dentro del inventario de recursos necesarios para la viabilidad y actividad operativa, elementos como hornos o rotativas e incluso los ordenadores, se clasifican directamente como:',
        'options': [
            'Proveedores financieros asiduos base ineludibles ciegos y activos.',
            'Inversiones intangibles o patentes rotativas mercantiles.',
            'Recursos puros de base burocrática y contable asidua estatal forzosa.',
            'Equipos técnicos (la maquinaria y piezas de recambio).'
        ],
        'correctAnswer': 3,
        'explanation': 'Hornos, ordenadores, rotativas, se clasifican como Equipos técnicos (maquinaria y piezas). (Sec 9)'
    }
]

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_7.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['items'].extend(new_questions)

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_7.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total q: {len(data['items'])}")
