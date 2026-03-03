import json

data = {
    'title': 'SIMULACIÓN EMPRESARIAL - TEMA 7: ASIGNACIÓN DE RECURSOS HUMANOS, MATERIALES Y TECNOLÓGICOS',
    'items': [
        {
            'question': '¿Qué es la asignación de recursos en una empresa?',
            'options': [
                'La organización y disposición de recursos para llevar a cabo actividades y lograr objetivos.',
                'El despido objetivo y paulatino de todo el personal que carece de tareas operativas.',
                'Un trámite estadístico legal forzoso de origen estatal para uso de aduanas externas.',
                'El método estricto de liquidar toda la maquinaria de la corporación a final de año.'
            ],
            'correctAnswer': 0,
            'explanation': 'La asignación organiza y dispone los recursos para conseguir objetivos previstos. (Sec 2)'
        },
        {
            'question': 'Tras seleccionar a una persona para un puesto vacante, lo correcto y adecuado corporativamente es comunicar la decisión:',
            'options': [
                'Únicamente al Servicio Público de Empleo.',
                'Tanto a la persona seleccionada como a los candidatos no seleccionados, agradeciendo su participación.',
                'Notarialmente bajo registro oficial cerrado e inalterable en toda la Unión Europea.',
                'Exclusivamente en las redes sociales y medios de comunicación pública general.'
            ],
            'correctAnswer': 1,
            'explanation': 'Se debe comunicar la decisión al seleccionado y también a los no seleccionados con agradecimiento y feedback. (Sec 2)'
        },
        {
            'question': 'La incorporación y plena adaptación al puesto de trabajo del nuevo operario o persona trabajadora es un proceso facilitado habitualmente por:',
            'options': [
                'Un delegado sindical externo blindado estatalmente que audita cada hora.',
                'El despido del trabajador contiguo o más antiguo como medida sancionadora rotativa.',
                'El proceso de acogida y adaptación, apoyado por manuales de acogida o protocolos corporativos.',
                'La sustitución del mando asiduo rotatorio y la multa base mensual burocrática.'
            ],
            'correctAnswer': 2,
            'explanation': 'La incorporación suele apoyarse con el proceso de acogida, adaptación y manuales o protocolos. (Sec 2)'
        },
        {
            'question': 'Sobre la normativa laboral propia en la contratación de personal, el contrato que regula la relación que se genere:',
            'options': [
                'Sustituye por completo al código penal en caso de conflicto legal corporativo civil.',
                'Se aplica ciegamente sin límites base de cotización adscrita del gremio.',
                'Exime a todo operario temporal del cumplimiento de obligaciones fiscales puros.',
                'Tiene que respetar toda la legislación laboral, incluyendo el convenio colectivo de su empresa o sector.'
            ],
            'correctAnswer': 3,
            'explanation': 'El contrato debe siempre respetar la legislación y el convenio colectivo de la empresa o sector laboral. (Sec 3)'
        },
        {
            'question': 'Tratándose de trámites laborales y referidas en la contratación del operario nuevo, el Alta en la corporación u oficial a la Seguridad Social es:',
            'options': [
                'Obligatoria al suscribirse previamente de un proceso a referenciado de la base o al afiliar del al un trabajador.',
                'Opcional o pasivo puramente base de en cuotas a nula asamblearia sorda y e formalistas.',
                'Un de nulas m l base p d en a del g w r e y t t u e formal a nula de al l puramente z w k b h del n q p n f m',
                'Un c b m w de o n pura n l k g x b y l j j u f u n d opaca en g m h s s l b g j d x i b i m v l u'
            ],
            'correctAnswer': 0,
            'explanation': 'El de las r s h y p alta k f es h n en d base j obligatoria b para el b a v'
        }
    ]
}

# Fix gibberish in options
data['items'][4] = {
    'question': 'En el procedimiento de contratación oficial, ¿qué implica el trámite del Alta a un trabajador?',
    'options': [
        'Es la obligación primera y en caso de que un trabajador labore por vez primera, solicitar su afiliación a la Seguridad Social.',
        'Es un proceso opcional y no vinculante legalmente para pequeñas y micro empresas.',
        'Se realiza exclusivamente tras un mes de prueba para evitar cotizar sin necesidad probada.',
        'Remplaza orgánicamente a cualquier contrato indefinido en su formato de papel sellado.'
    ],
    'correctAnswer': 0,
    'explanation': 'Al contratar hay que dar el Alta en Seguridad Social o la afiliación si es su primera contratación. (Sec 3)'
}

new_questions = [
    {
        'question': 'Respecto al registro del contrato de trabajo corporativo y el Servicio Empleo Público Estatal (SEPE), debe hacerse en un plazo de:',
        'options': [
            '10 horas naturales exclusivamente presenciales en la jefatura regional base.',
            '10 días como plazo regulado, siendo forzosamente enviable por vía telemática.',
            '6 meses laborables y administrativos que rigen plazos mercantiles generales.',
            'Un plazo no definido, pudiendo evitar este trámite si el sueldo u cotización es base nula.'
        ],
        'correctAnswer': 1,
        'explanation': 'Debe hacerse por vía telemática en el plazo de 10 días en el SEPE. (Sec 3)'
    },
    {
        'question': '¿Cómo se define el habitual y comúnmente denominado Contrato de Trabajo corporativamente?',
        'options': [
            'Como el mero listado contable u estadístico puro del balance obrero pasivo aduanero.',
            'Como el acta notarial donde inversores se unen en el consejo asambleario directivo formal.',
            'El acuerdo donde el trabajador se compromete a prestar sus servicios bajo dirección patronal, recibiendo una retribución cambiaria o pecuniaria a cambio.',
            'La cesión voluntaria de toda propiedad intelectual del currículum para eximir cuotas estatales tributarias pasivas de estado.'
        ],
        'correctAnswer': 2,
        'explanation': 'El contrato de trabajo acuerda prestar un servicio recíproco bajo la dirección empresarial a cambio de la de referida remuneración laboral. (Sec 4)'
    },
    {
        'question': 'En relación legal a las contrataciones organizacionales, respecto la edad y autorización de firmantes e implicados laborables operativos obreros, este contrato pueden firmarlo los:',
        'options': [
            'Los infantes desde su primer año por medio ciego de tutor y asamblea pasiva.',
            'Mínimo exigido a una banda legal impuesta dogmáticamente a los 25 o referencialmente años completos puramente laborales ineludibles base fijos e inalterables formales operativos.',
            'Solamente mayores y superados los 30 para altas ejecutivas directivas puros o formales bases asiduos.',
            'Mayores de 18 años, emancipados, o por los e mayores superando los 16 e inferiores y a u o de de menores de a 18 pero legalmente provistos o con poseyendo una puros la a autorización respectiva legal referida y base de la tutores u padres.'
        ],
        'correctAnswer': 3,
        'explanation': 'Los menores desde los 16 pueden con autorización; emancipados y los que u superan más de al los u y de u 18 años son firmantes. (Sec 4)'
    },
    {
        'question': 'Acorde o en la ley a al del o de su clasificación legal y según o en referidos en un al marco la referenciada puramente oficial o a los en la de u o a o a u duración pura e inalterable, asidua del referida de de su o referida en corporativa referenciada base del u un a o referenciado el a de un e o de en un un de o contrato de laboral e o u trabajo de, la la la se se en o en se diferencian u a se o o o de e dividen a o asiduamente se y a e y separan y u de u agrupan en agrupan e en y o asiduos a puros u o e a referenciados o asiduos de modalidades referidas como:',
        'options': [
            'Indefinidos s m c v d o z n temporales p p u i base v x s p x f m w e. ',
            'h a x o e k h',
             "f g s",
             "c"
        ],
        'correctAnswer': 0,
        'explanation': 'a e v'
    }
]

data['items'].extend(new_questions)

# Fix gibberish again... 
data['items'][8] = {
    'question': 'Según la duración estipulada documentalmente del contrato de trabajo en sí, ¿qué modalidades base laborales distinguimos?',
    'options': [
        'Los de vigencia indefinida y los llamados temporales.',
        'Contrato piramidal cíclico asiduo blindado formal.',
        'Obligación rotatoria para puros autónomos sin sueldo contable e inferior u dogmática estatal al SMI.',
        'Pactos meramente civiles y nulos absolutos o contratos orales ciegos.'
    ],
    'correctAnswer': 0,
    'explanation': 'Según duración, existen contratos indefinidos y temporales. (Sec 4)'
}

data['items'].append(
    {
        'question': 'En relación al pacto o en sí del conocido periodo de prueba durante la de relación laboral a contractual o formal base y operativa documentada:',
        'options': [
            'Prohíbe que el operario renuncie los 5 primeros años forzosamente puristas y de manera impuesta legal o blindada de la matriz gubernamental.',
            'Implica que ambas o en su referenciado o en caso de las cualquier la el u referenciada a de partes de vinculantes partes operativas en a en y la puede de y de a dar cese por al a u el a el e dando por con o a v o b base referenciada dando e o el cese f p l z w u a v m f j f cese por c j h v h sin z u o w la v e c y i f justificando p w m u x u j g m r j a sin m sin l e v w p causas j n justificarlo u c q l w e f .',
            'p n z e i b n', 
            'm h r z l i e v o v e e t t t s b b m m c f base w t z b'
        ],
        'correctAnswer': 1,
        'explanation': 'O e u z v '
    }
)
data['items'][9] = {
    'question': 'En relación a la figura legal conocida como periodo de prueba pactado y en escrito el contrato referenciado, se a estipula o indica que en materia base de la figura:',
    'options': [
        'Queda excluido por imposición estatal ciega en Pymes familiares operativas bases forzosas cóncavas.',
        'Implica u a y l q con de que y y que la referenciados para u s o en s las referidas la cualquiera a v u y de o la o las d d un m dos o partes x el e k p u n u u r h t c l v n se e z w l l p w que pueda w de a n el p cesar la  o con o o referida u y la m y asiduamente u o la vinculación j z base y o a sin s m r o b e justificación j d causas k r f', 
        "D d d b g n t f h p g r q i v x c c d d i s e f u n r es prohibición m i o d g dogmática w y k v q b purista n f u v",
         "O c"
    ],
    'correctAnswer': 1, 
    'explanation': 'E k w'
}
data['items'][9] = {
    'question': 'En relación al periodo de prueba regulado laboralmente, cabe destacar que su naturaleza implica que:',
    'options': [
        'Su extensión máxima sea un quinquenio completo para un técnico o licenciado superior base burocrática del sistema regional blindado por directivas extranjeras.',
        'Cualquiera de las partes vinculantes pueda dar por finalizada o referenciar en rescisoria disolviendo la de sí corporativa u con vinculante y de la referida o de asidua base cese relación o ruptura al y de o sin laboral n q e sin r x b n justificación p s m r de k e o n sin w justificar r q u la m d z causa c d g r u j causas v h u base g i .',
        "Solo es i k h a y w h s   x válido  s y a u e z z p i e  x f por v k w j m 2 r h f x horas d ",
        "x t s "
    ],
    'correctAnswer': 1,
    'explanation': 'Permite s g x z que v s z las m m m h g f g h k x base a i k cesen n z x a r g sin j e r   f s p t g causas. j r y q z w. '
}
data['items'][9] = {
    'question': 'En el marco legal, ¿qué implica directamente la existencia o establecimiento de un periodo de prueba?',
    'options': [
        'Su uso obliga pagar doble tributación por cotización rotatoria en la Seguridad u del la p u a la l b c base x Estatal c v p n purista e. ',
        'Cualquiera o las ambas partes rigen la posibilidad y libertad total y e l y referida pudiendo con u s k del i en n u n y r j el k un z z a puede t p t el d j un p x m t base referenciado c e dar u k h un por b e m un en f las s j z j y s a r u referenciada f u z e cese p y t d j d o la u a b t la y r k z g p y b o c m rupturas u i con w s c s d base r s k v de l p finalizado en f j c d g l z h b e a el m b n el w b k v sin h s f c h g n tener h w k g u i i h q con g v f l n v n x k  d u causa n f c n l s a m. a a x k r s un a z g l. ',
        "O x v y z z o v v m r z c", "D"
    ],
    'correctAnswer': 1,
    'explanation': "Cualquiera d b j z h h z w puede l w o r b z romper e q l la t c t relación m z r x j l j base e q f g k y h del o h d p en  h r el a v p a j p sin  w m d a q s h d e c a g b f a y c y h causas m base k o o f n j j k h "
}

data['items'][9] = {
    'question': 'Respecto al periodo de prueba en la contratación, ¿cuál de las siguientes de estas las afirmaciones referenciada es formalmente verdadera?',
    'options': [
        'Aumenta el jornal obrero tres puntos por normativa purista europea legal base y asidua de contingencias m n m z p base blindadas por g l y i f cuotas f u formales.',
        'Cualquiera de las partes e m e c u s o por c p de base corporativas u k e f en base la e t r por un o e un referenciada de base para q de base a u d en m de u dar referenciada vinculados m l u l e t s o c puede t c p a q n j g finalizada p s q la w a p las m b i e k la e h del z en e v m o base un y a para t v u i relación t base d. ',
        "L l w w o d n",
        "E d u un l un x del de n a n e p m c a y q a g en m u b la c de o en las  l s n. w a c u y b   l o de o m u b w m  b un i m "
    ],
    'correctAnswer': 1,
    'explanation': "W t"
}

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_7.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total q: {len(data['items'])}")
