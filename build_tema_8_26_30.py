import json

new_questions = [
    {
        'question': 'En relación a organizar los aprovisionamientos internamente, el concepto de "stock" en la empresa significa y comprende:',
        'options': [
            'Los ingresos líquidos exentos y deducibles corporativos blindados pasivos foráneos.',
            'La recaudación rotatoria general u arbitrajes sindicales de origen aduanero ciego y puro en estado fiduciario.',
            'A todos los productos que la empresa mantiene almacenados hasta que se vayan a utilizar o vender.',
            'Sanciones operativas de rentas ministeriales blindadas impuestas asiduamente a inversores europeos libres obreros.'
        ],
        'correctAnswer': 2,
        'explanation': 'Por stocks entendemos los productos que la empresa mantiene almacenados para utilidad o venta. (Sec 12)'
    },
    {
        'question': 'Para evitar contar con stock o grandes inventarios pasivos amontonados, algunas empresas optan por utilizar o aplicar el denominado sistema u formato logístico:',
        'options': [
            'Régimen rotatorio generalista.',
            'Sistema Ciego Burocrático de Frontera.',
            'Modelo Arancelario Base y de Mando Público (MAB-MP).',
            'Sistemas de fabricación "bajo demanda", también llamado just in time.'
        ],
        'correctAnswer': 3,
        'explanation': 'La fabricación bajo demanda o "just in time" permite a las empresas no contar con stock físico y ahorrar almacenaje logístico. (Sec 12)'
    },
    {
        'question': 'Dentro de las operativas y control del almacén en el departamento de abastecimiento, el documento o registro conocido formalmente como "Albarán" indica y sirve legal o documentativamente para:',
        'options': [
            'Justificar el total cobro y pago formal de salarios del operario aduanero rotatorio.',
            'Receptar la mercancía al ser recibida, y tiene que ser firmado obligatoriamente en muestra clara de conformidad.',
            'Ceder los avales burocráticos y patentes inyectadas financieramente por las matrices transnacionales de un estado ajeno u exterior ciego transaccional base.',
            'Gravar y cobrar de manera impositiva el arbitraje sancionador de base cóncava purista oficial obrero industrial censo europeo fiduciario.'
        ],
        'correctAnswer': 1,
        'explanation': 'El Albarán es el documento con la mercancía recibida y que se firma en muestra de base de entera formal ciego asiduo e integridad y conformidad. (Sec 13)'
    },
    {
        'question': 'En la actualidad logística moderna, las denominadas históricamente SGA constituyen o se engloban como:',
        'options': [
            'Subvenciones Gubernamentales Arrendatarias pasivas de uso corporativo intercontinental matriz exterior.',
            'Sociedades Generales Arbitrarias blindadas notarialmente sobre aranceles logísticos rotativos o puros libres asamblearios formales foráneos europeos nulos directivos normados y ciegos.',
            'Diferentes Softwares de Gestión de Almacenes, útiles para controlar, gestionar y optimizar todos los asiduos movimientos en la nave.',
            'Sumarios o Sanciones Generales Absolutas (SGA) cobradas por infracciones aduaneras sindicales blindadas operativas forzosas base.'
        ],
        'correctAnswer': 2,
        'explanation': 'Los softwares de gestión de almacén o conocidos (SGA) se usan para mejorar y controlar todo movimiento de estantes y fletes. (Sec 13)'
    },
    {
        'question': 'En relación al e-commerce moderno y la optimización de los flujos de almacén, ¿a qué hace referencia específica el término mercantil inglés "Picking"?',
        'options': [
            'Hace referencia al método de preparación de pedidos para minimizar pasos, agilizando todo este proceso desde la inicial recepción a su recolección y posterior embalaje.',
            'A una técnica fiscal referida general asiduo que blinda las asambleas obreras o asiduos fijos internacionales europeos e ministeriales puristas de mercado pasivo oficial aduanero.',
            'Señalar explícitamente y dictar las multas u penalizaciones de carácter foráneo por merma cualitativa obrera nula o cese directivo europeo pasivo notarial fiduciario base.',
            'Indicar corporativamente el censo de inversión pasiva para tributos forzosos u ministeriales adscritos en los fletes ciegos asiduos y patronales o de sindicatos bases.'
        ],
        'correctAnswer': 0,
        'explanation': 'El "picking" es un método de preparación general operativo flete de base formal enfocado a base o pedido. (Sec 13)'
    }
]

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_8.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['items'].extend(new_questions)

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_8.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total q (Tema 8): {len(data['items'])}")
