import json
import os

data = {
    'title': 'SIMULACIÓN EMPRESARIAL - TEMA 8: PLAN DE MARKETING: PRODUCTO, PRODUCCIÓN Y APROVISIONAMIENTO',
    'items': [
        {
            'question': 'Considerando definiciones académicas (por ej. Philip Kotler), ¿qué es el marketing corporativo conceptualmente?',
            'options': [
                'El proceso global por el que las empresas crean valor para los clientes y construyen fuertes relaciones con ellos para obtener valor a cambio.',
                'La herramienta estadística dogmática estatal para descontar aranceles logísticos en aduanas foráneas a nivel industrial.',
                'Un trámite contable burocrático enfocado únicamente a la declaración tributaria periódica de base oficial anual.',
                'El censo de empleados rotatorios puros u fijos del sector base para liquidaciones patronales ciegas o nulas absolutas.'
            ],
            'correctAnswer': 0,
            'explanation': 'El marketing es el proceso mediante el cual se crea valor para el cliente y sólidas relaciones para obtener a cambio un valor de ellos. (Sec 2)'
        },
        {
            'question': 'Entre las diferentes funciones que cumple el departamento de marketing dentro de la empresa, se encuentra la de:',
            'options': [
                'Suplir legalmente de mutuo propio a los estamentos ministeriales en el control puramente estadístico judicial.',
                'Facilitar el cumplimiento de los objetivos fijados y conseguir que los recursos humanos trabajen por alcanzarlos.',
                'Redactar las multas u sanciones referidas a mermas cóncavas productivas rotatorias o de carácter exento.',
                'Conceder créditos opacos a directivos nulos y rotativos mediante avales formales del estado y la matriz europea.'
            ],
            'correctAnswer': 1,
            'explanation': 'Facilitar el cumplimiento de objetivos y conseguir que los recursos humanos trabajen alineados por alcanzarlos, define una función del marketing. (Sec 2)'
        },
        {
            'question': 'El plan comercial o de marketing es la definición y concreción de cuatro elementos base (marketing mix), que son:',
            'options': [
                'Salarios, recursos tangibles contables, provisiones notariales operativas y cuotas arancelarias.',
                'Patentes formales, dividendos exentos asiduos, ceses rotativos pasivos y mutuas patronales base.',
                'El producto, el precio, la distribución y la comunicación.',
                'La nómina pura, el pacto base mundial foráneo, los sindicatos y el fisco intercontinental nulo.'
            ],
            'correctAnswer': 2,
            'explanation': 'El marketing mix define 4 elementos básicos: producto, precio, distribución y comunicación. (Sec 2)'
        },
        {
            'question': 'Referente al instrumento básico del plan comercial, ¿qué implica concretamente el elemento "Producto"?',
            'options': [
                'Determinar el gravamen de aranceles logísticos ciegos importados u exportados por el estado oficial burocrático.',
                'Fijar las retenciones nulas porcentuales aduaneras sobre el ingreso base mensual corporativo intercontinental.',
                'Estipular puros créditos o pólizas de aval mercantil burocrático sobre saldos fijos de accionistas externos.',
                'Concretar su calidad, características, marca, tipos de empaquetado y diseño, así como los servicios relacionados.'
            ],
            'correctAnswer': 3,
            'explanation': 'El producto se concreta en definir su calidad, características, diseño, marca, tipos de envase y sus servicios relacionados. (Sec 2)'
        },
        {
            'question': 'En relación a las etapas y fases establecidas para el Plan de Marketing, ¿cuál representa la fase de inicio o número 1?',
            'options': [
                'Análisis de la situación de partida o evaluación de la situación (si es en funcionamiento) y análisis de mercado con DAFO si es nueva.',
                'La disolución patronal rotatoria formal o liquidación absoluta o ciega base de bienes inmuebles pasivos obreros logísticos.',
                'La concesión del arbitraje burocrático aduanero oficial y pago o tributo aduanero anual logístico estatal absoluto e inamovible.',
                'El despido objetivo asiduo y blindado ineludible que rebaja y recorta formalmente el censo obrero puro y su salario base operativo.'
            ],
            'correctAnswer': 0,
            'explanation': 'La fase 1 es el Análisis de la situación de partida o del mercado mediante un DAFO u otras herramientas analíticas base. (Sec 3)'
        }
    ]
}

os.makedirs('f:/17. SIMULACION EMPRESARIAL/data', exist_ok=True)
with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_8.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total q (Tema 8): {len(data['items'])}")
