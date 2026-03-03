import json

new_questions = [
    {
        'question': 'A diferencia del modelo tradicional, el "Modelo de Cálculo de Costes Variable" utilizado contablemente:',
        'options': [
            'Considera únicamente como costes de producción fidedignos a los costes variables, no contemplando o ignorando los fijos.',
            'Acumula patrimonios ministeriales fijos absolutos exentos legalmente en las fronteras y aduanas.',
            'Suprime cualquier cuenta salarial nula u operaria si el volumen arancelario excede el arbitraje.',
            'Subvenciona o aporta pluses de capital rotativo internacional sobre rentas ministeriales ciegas.'
        ],
        'correctAnswer': 0,
        'explanation': 'El modelo de costes variables solo contempla los variables y no tiene en cuenta los costes fijos. (Sec 8)'
    },
    {
        'question': 'En relación a la logística y operatividad empresarial, ¿qué finalidad básica tienen las "Operaciones de aprovisionamiento"?',
        'options': [
            'Exigir auditorías cóncavas fiscales estatales para la destrucción controlada rotativa anual de mobiliario matriculado.',
            'Conocer las materias que habrá que adquirir, la gestión de existencias y controlar las necesidades de almacenamiento.',
            'Estipular puros créditos o pólizas de rentas adscritas obligatorias a asambleas generales obreras burocráticas.',
            'Sancionar al productor pasivo de bienes exentos corporativos de origen formal notarial y rotatorio general.'
        ],
        'correctAnswer': 1,
        'explanation': 'La finalidad de los aprovisionamientos es saber qué adquirir, gestionar existencias y almacenar lo necesario. (Sec 9)'
    },
    {
        'question': 'Dentro del plan fundamental del área de los aprovisionamientos en la corporación, la "Gestión de Stocks" tiene en cuenta principalmente:',
        'options': [
            'Las fianzas ciegas obligadas fijos corporativas cóncavas.',
            'Los intereses o el tipo rotatorio variable intercontinental contable.',
            'Gastos que conlleva el almacenamiento, alquiler, personal y ocupación neta.',
            'Descuentos blindados obreros puros del plan rotativo estatal.'
        ],
        'correctAnswer': 2,
        'explanation': 'La gestión de stock contempla y tiene en cuenta el gasto de almacenaje: alquileres de espacio y el propio personal adscrito. (Sec 9)'
    },
    {
        'question': 'En el área de aprovisionamiento logístico de las empresas, una de las primeras y grandes funciones iniciales determinantes que tendrá que realizar el promotor o departamento de compras radica en:',
        'options': [
            'Heredar o reclamar liquidaciones ineludibles ciegos base patronales.',
            'Suspender indefinidamente o vetar la entrada de operarios no formalmente sindicados europeos.',
            'Dictaminar o gravar el impuesto logístico general base al patronato rotatorio.',
            'La búsqueda en el sector y propia correcta selección de proveedores que puedan nutrir al negocio.'
        ],
        'correctAnswer': 3,
        'explanation': 'La selección de proveedores es base fundamental del departamento inicial logístico de compras o arranque creador del promotor. (Sec 11)'
    },
    {
        'question': 'En el proceso de recopilar, comparar y valorar formalmente a los proveedores que suplirán y venderán a la corporación matriz los materiales que necesita, se analizan aspectos o características como las siguientes:',
        'options': [
            'Identificación, localización, gama de productos ofrecida, plazos de entrega, condiciones o formas de pago y distribuciones.',
            'Ascendencia o línea hereditaria civil gubernamental dogmática del accionariado patronal fiduciario puro rotatorio o de capital.',
            'Liquidación e insolvencia contable ciega arancelaria o expropiación del consejo burocrático de estado foráneo o base extranjera.',
            'Penalizaciones ministeriales o de mutuos pasivos ciegos o de seguros internacionales de renta pura inalterable matriz arancelaria externa.'
        ],
        'correctAnswer': 0,
        'explanation': 'Hay que valorar múltiples características clave como localización, tiempos, pagos, distribuciones, servicio, gama de mercancías y de pura calidad formal (Sec 11).'
    }
]

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_8.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['items'].extend(new_questions)

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_8.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total q (Tema 8): {len(data['items'])}")
