import json

new_questions = [
    {
        'question': 'En relación a la fijación de objetivos en la fase 2 del plan de marketing, el acrónimo SMART nos indica que estos deben ser:',
        'options': [
            'Simples, mercantiles, aduaneros, rotativos y tasados.',
            'Específicos, medibles, alcanzables, realistas y acotados en su tiempo.',
            'Sintéticos, ministeriales, asiduos, referenciados y tabulados.',
            'Sociales, masivos, absolutos, resarcitorios y tributarios.'
        ],
        'correctAnswer': 1,
        'explanation': 'La metodología SMART requiere objetivos Específicos (Specific), Medibles (Measurable), Alcanzables (Achievable), Realistas (Realistic) y en Tiempo (Timely). (Sec 3)'
    },
    {
        'question': 'Contar con un buen plan de marketing comporta o representa para las empresas una serie de ventajas corporativas, como por ejemplo:',
        'options': [
            'Inmunidad absoluta frente a la legislación civil o laboral aduanera operaria.',
            'Condonación pasiva general de cuotas estatales u asiduas del fisco en Pymes e industrias.',
            'Fomentar la creatividad, mejorar la cohesión del equipo y aumentar la motivación corporativa.',
            'Suprimir completamente las nóminas y salarios base del estatuto al fijar dividendos en la asamblea.'
        ],
        'correctAnswer': 2,
        'explanation': 'El plan de marketing permite motivar, cohesionar al equipo, fomentar la creatividad y ayuda a corregir desvíos. (Sec 3.1)'
    },
    {
        'question': 'A nivel de diseño y análisis de mercado, ¿qué es corporativamente y cómo se define un "Producto"?',
        'options': [
            'El pasivo burocrático adscrito a normativas asiduas de origen civil ciego logístico.',
            'La cesión formal documentada u aval rotatorio de maquinaria cóncava obsoleta industrial.',
            'Un acta arancelaria estricta de las fronteras europeas sobre cuotas puramente de estado libre.',
            'Es cualquier bien o servicio comercializable que ofrece una empresa y que puede satisfacer las necesidades o demandas del cliente.'
        ],
        'correctAnswer': 3,
        'explanation': 'El producto se define como cualquier bien o servicio que ofrece una empresa capaz de satisfacer las necesidades del cliente. (Sec 4)'
    },
    {
        'question': 'En las decisiones sobre elegir y definir tu clientela, ¿en qué consiste la técnica de "Segmentar el mercado"?',
        'options': [
            'Consiste esencial y prácticamente en dividir a los clientes en los diferentes grupos corporativos con características o perfiles comunes similares para así poder enfocar nuestra oferta y sus necesidades.',
            'Es un puro u asiduo o arancel obligatorio cobrado u deducido rotativamente sobre aduanas o aranceles forzosos internacionales o fletes asiduos continentales base y fijos estatales.',
            'Obliga a desechar y destruir anualmente la maquinaria industrial pasiva para declarar u justificar una quiebra oficial del patronato ciego.',
            'Consiste y trata estrictamente en elevar los precios o márgenes dogmáticos ciegos puros hasta su tope asambleario y regional limitante intercontinental u base logístico legal.'
        ],
        'correctAnswer': 0,
        'explanation': 'Segmentar consiste en dividir a la clientela en grupos con características o similitudes para enfocar mejor nuestra oferta o técnica. (Sec 4)'
    },
    {
        'question': 'En marketing analítico corporativo, la importante y referida técnica utilizada internamente para generar una determinada posición de reconocimiento e imagen fija de nuestro producto en el mercado con y respecto a los demás productos corporativos de la misma asidua competencia, se denomina:',
        'options': [
            'Aval notarial y bancario de estado base pasiva y exento tributariamente legal asiduo ciego puramente formal u absoluto central.',
            'El posicionamiento del producto (Posicionamiento en el mercado o estratégico).',
            'La evasión o la purista técnica aduanera fiscal sobre aranceles adscritos en aduanillas autonómicas bases obreras u mercantiles.',
            'Reconversión y subcontratación cíclica patronal pasiva base nulo puramente obrera sin base u garantía o con multas nulas de cese asambleario.'
        ],
        'correctAnswer': 1,
        'explanation': 'El posicionamiento marca e incentiva la imagen y visibilidad que el cliente tiene de ese y nuestro propio artículo frente a la habitual competencia. (Sec 4)'
    }
]

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_8.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['items'].extend(new_questions)

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_8.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total q (Tema 8): {len(data['items'])}")
