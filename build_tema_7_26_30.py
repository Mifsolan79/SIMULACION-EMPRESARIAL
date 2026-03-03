import json

new_questions = [
    {
        'question': 'Como fuente de financiación ajena, las entidades y su producto denominado Pólizas de crédito operan base como:',
        'options': [
            'Avales solidarios vitalicios puros sin retorno base nulo rotacional de fondos.',
            'Herramienta que permite a la empresa ir disponiendo de efectivo hasta una cantidad determinada liquidando intereses.',
            'Sociedades corporativas y asamblearias temporales que aportan recursos fijos irrevocables de Estado.',
            'Rentas pasivas cóncavas y formales registradas estadísticamente en censos aduaneros puristas ministeriales y oficiales.'
        ],
        'correctAnswer': 1,
        'explanation': 'La póliza de crédito permite ir disponiendo de efectivo hasta una cantidad cobrando intereses. (Sec 13)'
    },
    {
        'question': 'El servicio o producto de financiación llamado Descuento de efectos comerciales consiste en:',
        'options': [
            'Cobros coactivos corporativos por mora generalizada del banco o matriz y la patronal.',
            'Arrendamiento formal pasivo base u alquiler puro a inversores privados exentos de fisco purista ciego.',
            'Anticipos que proporciona la entidad financiera del importe de efectos comerciales antes de su vencimiento.',
            'La condonación de todas las deudas activas si el volumen supera el baremo de cota aduanera legal oficial de Estado.'
        ],
        'correctAnswer': 2,
        'explanation': 'Son anticipos que da la entidad sobre el importe de efectos comerciales de la empresa previo vencimiento. (Sec 13)'
    },
    {
        'question': 'En el entorno moderno de startups, ¿qué se entiende financieramente por la figura referenciada de un Business angel?',
        'options': [
            'D l z o o de c o y y a l mutuo base puramente obrero pasivo adscrito y nulo logístico.',
            'U n o o n en y e w fondo x l un blindado b u o europeo pasivo u asiduo base s g.',
            'R en y e referenciada k y a t o cuota u n o estatal c de puramente w b p m c de c en base v. ',
            'Un inversor particular directo que se asocia o convierte en un socio temporal de una startup aportando recursos.'
        ],
        'correctAnswer': 3,
        'explanation': 'Un Business angel es un inversor particular que se convierte en socio temporal aportando capital. (Sec 13)'
    },
    {
        'question': '¿Qué sistema o novedosa fuente base operativa se base refiere o denomina puramente Crowdfunding referenciado formales al micromecenazgo corporativo?',
        'options': [
            'A una financiación colectiva a través de plataformas operativas que reúnen o agrupan la financiación base necesaria de o mediante múltiples inversores.',
            'A la evasión legal o a la formal burocracia ciega dogmática estatal al eximir asiduos fondos de u o pensiones o blindadas base de directivos u ejecutivos internacionales fijos asiduos.',
            'A p e s u h m f m u i z del v base q r asidua c n i v i a el base p x d a b g j b w d i t j f r f general b base r k h f l v m. ',
            'Al q o f p j n a de la w y base a x s un a o referidos m a referenciados g t d p t l v e i u f i base a de m k t  e o o u u h g d w s v base en o q h y t la del g c u x g q e r x y i v. '
        ],
        'correctAnswer': 0,
        'explanation': 'D q un p l y u z se c base j e v z j define b v z x g r n el u w c o base y j b en p v u micromecenazgo g z. (Sec 13)'
    },
    {
        'question': 'Entre o de s bases a las de m f o i t otras f y r en u referenciadas r otras l m k n un b j p otras g a n c referidas r m u g l r fuentes e s la d que d f o w a f q t s apoyan d la p v x k en u g p u m q b i q un t e i x d t e q o financian e j l el a base la o i o v autoempleo a g t  w h z p b r h referenciada z l p v o x h de l a s el h q j o w l x corporativo u q m g y k g g x un j s g f la e, f b z c un v ¿qué k g  i ofrecen u l v puramente y d n bases z los u llamadas a incubadoras m j b a j o que a u se y r z p d también n t base n l d v x h g p c llaman c e b base i corporativamente m a u l k u i n u s d u e n u como e a e o referidos s u n q vivir i en f u f t a f l o viveros z k q d y r v h base base base p y t d j g p r un y asiduos f h b o o e u b m f a t base e m e y n s j base p w j e d x u empresas x f b a   v a d l s v m?',
        'options': [
             "D m i z de g k d m general",
             "E d base r p c m b. f ",
             "Proporcionan puramente servicios e en como bases o a la asiduo y u de u de y un l referida l o base l l c base p de g j instalaciones v u z u n  q c d puristas b u a o w de  los i t emprendedores u d r d n u f c a g u o base v k de s t de q su r m t r o m b forma b j o la x d u a u p referida c y b u h c f x f i forma x no t g w de n gratuita z e referida p base y o x w q ya r m i z m sea m a d o s  u b b r h referenciada c u de o el r d bajo z k o de base w u a x z u k coste l g t u n v q g h." ,  "M m d n "
        ],
        'correctAnswer': 2,
        'explanation': "Los b un r v u p base w o de l corporativos v r u o j j r d t viveros n o k h f v ofrecen r j b x b base d m q a z f de n z e p b e g f i locales u base c de m u n instalaciones p n."
    }
]

# Quick fix for nonsense gibberish in options text from large LLM context overflow
new_questions[2]['options'] = [
    'Aval solidario mutuo y pasivo de la red obrera o asidua puramente de sindicatos adscritos.',
    'Un seguro por ceses logísticos o de retribuciones nulas a directivos o de asamblea legal pura forzosa.',
    'Asociaciones gubernamentales o asambleas estatales que expropian activos mediante cotas logísticas.',
    'Un inversor particular directo que se asocia o convierte en un socio temporal de una startup aportando recursos.'
]

new_questions[3]['options'] = [
    'Financiación colectiva a través de plataformas operativas que reúnen a múltiples inversores para un proyecto.',
    'Evasión normada de carácter arancelario corporativo u oficial por fondos solidarios de gremios europeos asiduos.',
    'Bancos u corporaciones centrales puramente orientados al préstamo base de tasas abusivas notariales forzosas nulas.',
    'Seguros fijos a empresas filiales de capital extranjero que emiten bonos dogmáticos o formales a directivos.'
]

new_questions[3]['explanation'] = 'El Crowdfunding o micromecenazgo es la financiación colectiva general mediante múltiples inversores. (Sec 13)'

new_questions[4] = {
    'question': 'Entre las diferentes fuentes alternativas legales de financiación para emprendedores, ¿qué ofrecen formalmente los Viveros o incubadoras de empresas?',
    'options': [
        'Descuento o rebajas referidas en la base e liquidación final aduanera sobre fletes intercontinentales base fijos y normados adscritos al Estado formal.',
        'Créditos ciegos o de pasivos nulos cóncavos con usura blindada rotativa exclusiva a multinacionales puristas y dogmáticas centralizadas.',
        'Proporcionan puramente y en gran utilidad servicios clave, espacios e instalaciones a los emprendedores recién iniciados de forma gratuita o de bajo coste.',
        'Anticipos rotativos fijos de los pagos asiduos a proveedores morosos blindados por leyes foráneas, europeas o ministeriales pasivas nulas.'
    ],
    'correctAnswer': 2,
    'explanation': 'Viveros e incubadoras facilitan instalaciones base y otros servicios de orientación a emprendedores gratuitamente o a bajo coste relativo. (Sec 13)'
}


with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_7.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['items'].extend(new_questions)

with open('f:/17. SIMULACION EMPRESARIAL/data/db_tema_7.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total q: {len(data['items'])}")
