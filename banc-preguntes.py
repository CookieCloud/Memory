#!/usr/bin/env python3
"""
Banc de preguntes de cultura general del web Memòria.

Cada pregunta porta: text, resposta bona, tres respostes dolentes,
EXPLICACIÓ, tema i nivell (0 fàcil · 1 mitjà · 2 difícil).

Criteris:
  · només fets estables: res que depengui de l'actualitat ni de qui mana ara
  · res discutible (s'eviten "el riu més llarg del món" i companyia)
  · l'explicació ha d'ensenyar alguna cosa, no repetir la resposta
  · les respostes dolentes han de ser creïbles, no absurdes
"""

# (pregunta, bona, [dolentes], explicació, tema, nivell)
BANC = [

# ══════════════ NATURA I COS ══════════════
('Quantes potes té una aranya?', '8', ['6', '10', '4'],
 "Les aranyes en tenen vuit; els insectes, com les formigues o les mosques, en tenen sis. Per això les aranyes no són insectes: són aràcnids.",
 'natura', 0),
('Quin animal fa la mel?', "L'abella", ['La vespa', 'La formiga', 'El borinot'],
 "Les abelles xuclen el nèctar de les flors i el transformen en mel dins del rusc, on la guarden com a reserva de menjar per a l'hivern.",
 'natura', 0),
('De quin animal ve la llana?', "De l'ovella", ['De la vaca', 'Del porc', 'Del cavall'],
 "La llana és el pèl de l'ovella. Se li talla a l'estiu, no li fa cap mal i li torna a créixer per a l'hivern.",
 'natura', 0),
('Quin òrgan bomba la sang pel cos?', 'El cor', ['El fetge', 'El pulmó', 'El ronyó'],
 "El cor és un múscul que es contrau tota la vida sense parar i empeny la sang per les artèries fins a l'últim racó del cos.",
 'natura', 0),
('Què necessiten les plantes per créixer, a més d’aigua?', 'Llum', ['Sal', 'Sorra', 'Vent'],
 "Amb la llum les plantes fabriquen el seu propi aliment a les fulles. Per això una planta dins d'un armari fosc s'acaba morint encara que la reguis.",
 'natura', 0),
('Quants dits té una mà?', '5', ['4', '6', '10'],
 "Cinc: polze, índex, mig, anular i petit. El polze és el que ens diferencia: es pot posar davant dels altres i ens deixa agafar coses.",
 'natura', 0),
('Quin és l’animal més gran del planeta?', 'La balena blava', ["L'elefant", 'La girafa', 'El tauró blanc'],
 "La balena blava pot passar dels 25 metres i les 100 tones. L'elefant, que és el més gran de terra ferma, no arriba ni a les 7 tones.",
 'natura', 1),
('Quin és l’animal terrestre més ràpid?', 'El guepard', ['El cavall', 'El lleó', 'La llebre'],
 "El guepard passa dels 100 km/h, però només durant uns segons: s'escalfa tant que ha de parar de seguida.",
 'natura', 1),
('Quin metall és líquid a temperatura ambient?', 'El mercuri', ['El plom', "L'estany", 'El coure'],
 "És l'únic metall que a temperatura normal és líquid; per això s'utilitzava als termòmetres antics. La resta s'han d'escalfar centenars de graus per fondre'ls.",
 'natura', 1),
('Quantes potes té un insecte?', '6', ['4', '8', '10'],
 "Sis, sempre. És justament el que defineix un insecte, i el que el separa de les aranyes, que en tenen vuit.",
 'natura', 1),
('Què fa que les fulles siguin verdes?', 'La clorofil·la', ['La saba', 'El sol', "L'aigua"],
 "La clorofil·la és la substància que aprofita la llum per alimentar la planta. A la tardor la planta la deixa de fabricar, i llavors es veuen els grocs i els vermells que sempre hi eren a sota.",
 'natura', 1),
('Quants litres de sang té, aproximadament, una persona adulta?', '5', ['1', '10', '20'],
 "Uns cinc litres, més o menys el que cabria en cinc cartrons de llet. Tota aquesta sang fa la volta al cos en menys d'un minut.",
 'natura', 1),
('Quin gas necessitem per respirar?', "L'oxigen", ['El nitrogen', "L'hidrogen", 'El diòxid de carboni'],
 "Agafem oxigen de l'aire i deixem anar diòxid de carboni. Les plantes fan exactament el contrari, i per això ens necessitem els uns als altres.",
 'natura', 1),
('Quin animal canvia de color per amagar-se?', 'El camaleó', ['La granota', 'La serp', 'El conill'],
 "El camaleó canvia de color movent uns cristalls que té a la pell. Ho fa per amagar-se, però també segons la temperatura i l'estat d'ànim.",
 'natura', 1),
('Quin gas absorbeixen les plantes per fer la fotosíntesi?', 'El diòxid de carboni', ["L'oxigen", 'El nitrogen', "L'hidrogen"],
 "Agafen diòxid de carboni de l'aire i, amb la llum del sol i l'aigua, fabriquen el seu aliment. L'oxigen que deixen anar és, de fet, un residu d'aquest procés.",
 'natura', 2),
('Quin és l’os més llarg del cos humà?', 'El fèmur', ["L'húmer", 'La tíbia', 'La clavícula'],
 "El fèmur és l'os de la cuixa i fa aproximadament una quarta part de l'alçada de la persona. També és el més resistent.",
 'natura', 2),
('Quina cèl·lula transporta l’oxigen per la sang?', 'El glòbul vermell', ['El glòbul blanc', 'La plaqueta', 'La neurona'],
 "Els glòbuls vermells porten l'oxigen dels pulmons a tot el cos. Els blancs defensen de les infeccions i les plaquetes tapen les ferides.",
 'natura', 2),
('Quin element químic té el símbol Fe?', 'El ferro', ['El fòsfor', 'El fluor', 'El franci'],
 "Ve del llatí *ferrum*. Molts símbols vénen del llatí i per això no s'assemblen al nom català: el plom és Pb (*plumbum*) i l'or és Au (*aurum*).",
 'natura', 2),
('Quants ossos té, aproximadament, un adult?', '206', ['106', '306', '406'],
 "Un nadó en té uns 300, però molts es van soldant mentre creix. Un adult en té uns 206, i més de la meitat són a les mans i als peus.",
 'natura', 2),
('Quina part de la cèl·lula guarda la informació genètica?', 'El nucli', ['La membrana', 'El citoplasma', 'El ribosoma'],
 "Al nucli hi ha l'ADN, que és el manual d'instruccions de l'ésser viu. La membrana és la paret de la cèl·lula i el citoplasma, el que l'omple.",
 'natura', 2),
('A quina temperatura bull l’aigua al nivell del mar?', '100 °C', ['80 °C', '120 °C', '90 °C'],
 "A 100 graus, però només al nivell del mar. A la muntanya hi ha menys pressió i bull abans: per això a dalt les llegums triguen més a coure's.",
 'natura', 2),

# ══════════════ MÓN ══════════════
('Quina és la capital de França?', 'París', ['Lió', 'Marsella', 'Niça'],
 "París és la capital i la ciutat més gran de França. Lió i Marsella són les dues següents en població.",
 'mon', 0),
('Quin mar banya Barcelona?', 'El Mediterrani', ["L'Atlàntic", 'El Cantàbric', 'El mar del Nord'],
 "El Mediterrani és un mar gairebé tancat: només es comunica amb l'Atlàntic per l'estret de Gibraltar, que fa tot just 14 quilòmetres.",
 'mon', 0),
('Quin és l’oceà més gran del món?', 'El Pacífic', ["L'Atlàntic", "L'Índic", "L'Àrtic"],
 "El Pacífic ell sol ocupa gairebé un terç de la superfície del planeta: hi cabrien tots els continents junts.",
 'mon', 0),
('Quantes estacions té l’any?', '4', ['2', '3', '6'],
 "Primavera, estiu, tardor i hivern. Passen perquè la Terra està una mica inclinada, i per això quan aquí és estiu, a l'altre hemisferi és hivern.",
 'mon', 0),
('En quin continent és Egipte?', 'Àfrica', ['Àsia', 'Europa', 'Amèrica'],
 "Egipte és al nord-est d'Àfrica, tot i que un tros petit, la península del Sinaí, ja és a Àsia.",
 'mon', 0),
('Quin és el satèl·lit natural de la Terra?', 'La Lluna', ['Mart', 'Venus', 'El Sol'],
 "La Lluna dona voltes al voltant de la Terra. Mart i Venus són planetes que giren al voltant del Sol, i el Sol és un estel.",
 'mon', 1),
('Quin és el planeta més a prop del Sol?', 'Mercuri', ['Venus', 'Mart', 'La Terra'],
 "L'ordre és Mercuri, Venus, la Terra i Mart. Curiosament el més calent no és Mercuri sinó Venus, perquè té una atmosfera espessa que hi reté la calor.",
 'mon', 1),
('Quin país té forma de bota?', 'Itàlia', ['Grècia', 'Portugal', 'Noruega'],
 "La península itàlica té forma de bota i sembla que doni una puntada de peu a Sicília, que és just davant de la punta.",
 'mon', 1),
('Quina és la muntanya més alta del món?', "L'Everest", ['El K2', 'El Mont Blanc', 'El Kilimanjaro'],
 "L'Everest arriba als 8.849 metres, a l'Himàlaia, entre el Nepal i el Tibet. El K2 és el segon, i molt més perillós de pujar.",
 'mon', 1),
('Quin és el país més extens del món?', 'Rússia', ['El Canadà', 'La Xina', 'El Brasil'],
 "Rússia ocupa més d'una desena part de tota la terra ferma del planeta i té onze franges horàries: quan a un extrem es lleven, a l'altre ja sopen.",
 'mon', 1),
('Quin desert càlid és el més extens del món?', 'El Sàhara', ['El Gobi', "L'Atacama", 'El Kalahari'],
 "El Sàhara travessa el nord d'Àfrica i és gairebé tan gran com els Estats Units. (El desert més gran de tots és l'Antàrtida, però aquell és de gel.)",
 'mon', 2),
('Quin estret separa Europa d’Àfrica?', 'Gibraltar', ['El Bòsfor', 'Ormuz', 'Malaca'],
 "A l'estret de Gibraltar, Europa i Àfrica queden a 14 quilòmetres l'una de l'altra: des de la costa es veu perfectament l'altre continent.",
 'mon', 2),
("Quina és la capital d'Austràlia?", 'Canberra', ['Sydney', 'Melbourne', 'Perth'],
 "Sydney i Melbourne es barallaven per ser-ho, i la solució va ser construir una ciutat nova entre totes dues: Canberra.",
 'mon', 2),
('Quin planeta té els anells més visibles?', 'Saturn', ['Júpiter', 'Urà', 'Neptú'],
 "Els anells de Saturn es veuen amb un telescopi senzill i són fets de milions de trossos de gel i roca. Júpiter, Urà i Neptú també en tenen, però molt fins.",
 'mon', 2),
('Quina llengua té més parlants com a llengua materna?', 'El xinès mandarí', ["L'anglès", "L'espanyol", "L'hindi"],
 "El mandarí és la llengua materna de molta més gent que cap altra. L'anglès, en canvi, és la que més es parla com a segona llengua.",
 'mon', 2),
('Per quin país passa el riu Danubi?', 'Hongria', ['Portugal', 'Irlanda', 'Noruega'],
 "El Danubi travessa deu països i passa per quatre capitals: Viena, Bratislava, Budapest i Belgrad. Cap altre riu del món en toca tantes.",
 'mon', 2),
('Quina és la ciutat més poblada d’Espanya?', 'Madrid', ['Barcelona', 'València', 'Sevilla'],
 "Madrid és la primera i Barcelona la segona. Madrid, a més, és de les poques capitals europees que no és vora d'un riu gran ni del mar.",
 'mon', 1),

# ══════════════ HISTÒRIA I ART ══════════════
('Qui va dissenyar la Sagrada Família?', 'Antoni Gaudí', ['Lluís Domènech i Montaner', 'Josep Puig i Cadafalch', 'Ildefons Cerdà'],
 "Gaudí hi va treballar més de quaranta anys i s'hi va acabar instal·lant. Sabia que no la veuria acabada i va deixar maquetes perquè altres poguessin continuar.",
 'historia', 0),
('Qui va pintar el Guernica?', 'Picasso', ['Dalí', 'Miró', 'Velázquez'],
 "Picasso el va pintar el 1937, després del bombardeig del poble de Gernika. És tot en blanc, negre i gris, com les fotografies dels diaris de l'època.",
 'historia', 1),
('Qui va escriure el Quixot?', 'Cervantes', ['Lope de Vega', 'Quevedo', 'Góngora'],
 "Miguel de Cervantes el va publicar en dues parts, el 1605 i el 1615. Està considerada la primera novel·la moderna.",
 'historia', 1),
('Quin instrument té 88 tecles?', 'El piano', ["L'orgue", "L'acordió", 'El clavicèmbal'],
 "Un piano de cua en té 88: 52 de blanques i 36 de negres. És el recorregut que abasta pràcticament tots els sons que fa servir la música.",
 'historia', 1),
('En quin any va arribar l’home a la Lluna?', '1969', ['1959', '1972', '1965'],
 "El 20 de juliol de 1969, amb l'Apol·lo 11. Hi van tornar cinc vegades més, i des del 1972 no hi ha pujat ningú.",
 'historia', 1),
('Qui va escriure el Tirant lo Blanc?', 'Joanot Martorell', ['Ausiàs March', 'Ramon Llull', 'Jacint Verdaguer'],
 "És del segle XV i està escrit en català. Cervantes en parla dins del Quixot i el salva de la crema de llibres dient-ne meravelles.",
 'historia', 2),
('En quin any va caure el mur de Berlín?', '1989', ['1979', '1991', '1985'],
 "El 9 de novembre de 1989. Havia partit la ciutat durant 28 anys i la seva caiguda va ser el senyal del final de la guerra freda.",
 'historia', 2),
('En quin segle va començar la Revolució Francesa?', 'Al segle XVIII', ['Al segle XVII', 'Al segle XIX', 'Al segle XVI'],
 "Va començar el 1789, que és segle XVIII: els anys que comencen per 17 pertanyen al segle divuit, perquè el segle I van ser els anys de l'1 al 100.",
 'historia', 2),
('Qui va formular la teoria de la relativitat?', 'Einstein', ['Newton', 'Galileu', 'Bohr'],
 "Albert Einstein, entre el 1905 i el 1915. Va demostrar que el temps no passa igual a tot arreu: com més de pressa vas, més a poc a poc va el teu rellotge.",
 'historia', 2),
('Qui va compondre la Novena Simfonia, amb l’Himne a l’Alegria?', 'Beethoven', ['Mozart', 'Bach', 'Vivaldi'],
 "Beethoven la va acabar el 1824, quan ja era completament sord: la va escriure sentint-la només dins del cap.",
 'historia', 2),
('Quina civilització va construir les piràmides de Gizeh?', "L'Antic Egipte", ['Els romans', 'Els grecs', 'Els maies'],
 "Es van aixecar fa uns 4.500 anys com a tombes dels faraons. Són tan antigues que Cleòpatra en va viure més a prop del nostre temps que del seu.",
 'historia', 1),
('Quin poble va construir el Colosseu de Roma?', 'Els romans', ['Els grecs', 'Els etruscs', 'Els cartaginesos'],
 "El van acabar l'any 80 i hi cabien unes 50.000 persones. Tenia un sistema de passadissos que permetia buidar-lo en pocs minuts.",
 'historia', 1),
('En quin país es va inventar el paper?', 'A la Xina', ['A Egipte', 'A Grècia', "A l'Índia"],
 "Els xinesos el van fabricar fa uns dos mil anys i en van guardar el secret durant segles. També van ser els primers a fer servir paper moneda.",
 'historia', 2),
('Quin pintor es va tallar part d’una orella?', 'Van Gogh', ['Monet', 'Cézanne', 'Gauguin'],
 "Vincent van Gogh, el 1888, en una crisi. Va vendre molt pocs quadres en vida i avui són dels més cars del món.",
 'historia', 2),

# ══════════════ LLENGUA ══════════════
("Quantes lletres té l'alfabet català?", '26', ['24', '28', '30'],
 "Vint-i-sis. Grups com ny, ll o ss sonen com una sola lletra però no compten a part: són dues lletres escrites juntes.",
 'llengua', 1),
('Què és un sinònim?', 'Una paraula que vol dir el mateix', ['Una paraula que vol dir el contrari',
 'Una paraula que sona igual', 'Una paraula inventada'],
 "Sinònim vol dir el mateix (content i alegre); antònim vol dir el contrari (content i trist).",
 'llengua', 0),
('Quantes vocals té el català?', '5', ['3', '6', '8'],
 "Cinc vocals escrites: a, e, i, o, u. Una altra cosa és com sonen: la e i la o es pronuncien obertes o tancades segons la paraula.",
 'llengua', 1),
('Què és un verb?', 'Una paraula que indica una acció', ['Una paraula que anomena una cosa',
 'Una paraula que descriu com és una cosa', 'Una paraula que uneix frases'],
 "El verb és el que es fa: córrer, menjar, pensar. El que anomena coses és el substantiu i el que descriu com són, l'adjectiu.",
 'llengua', 1),
('Quina d’aquestes paraules és un adjectiu?', 'Alt', ['Taula', 'Córrer', 'Ràpidament'],
 "L'adjectiu diu com és una cosa: una casa *alta*. Taula és un substantiu, córrer un verb i ràpidament un adverbi.",
 'llengua', 2),
('Què és una metàfora?', 'Dir una cosa amb la imatge d’una altra', ['Repetir una paraula',
 'Exagerar una cosa', 'Escriure a l’inrevés'],
 'Quan dius "tens un cor d’or" no parles de metall: fas servir la imatge de l’or per dir que la persona és bona.',
 'llengua', 2),
('En quin signe s’acaba una pregunta escrita?', "Un signe d'interrogació", ['Un punt', 'Una coma', 'Un guionet'],
 "El signe d'interrogació (?) tanca les preguntes. En català només se'n posa al final, no al principi.",
 'llengua', 0),
('Quin és el plural de "llapis"?', 'llapis', ['llapissos', 'llapisos', 'llàpissos'],
 "Les paraules que ja acaben en essa i no porten accent a l'última síl·laba no canvien en plural: un llapis, dos llapis. Igual que un dilluns, dos dilluns.",
 'llengua', 2),
('Què vol dir "matiner"?', 'Que es lleva aviat', ['Que arriba tard', 'Que dorm molt', 'Que treballa de nit'],
 "Ve de matí. Una persona matinera és la que es lleva d'hora, tant si li agrada com si no li queda més remei.",
 'llengua', 1),
('Quina paraula és el contrari de "generós"?', 'Garrepa', ['Ric', 'Alegre', 'Prudent'],
 "Generós és qui dona fàcilment; garrepa, qui no vol deixar anar res. Ser ric o pobre no hi té res a veure.",
 'llengua', 2),
# ══════════════ AMPLIACIÓ: sobretot nivell fàcil ══════════════
('Quin animal lladra?', 'El gos', ['El gat', 'El cavall', "L'ocell"],
 "El gos lladra; el gat miola, el cavall renilla i les ovelles belen. Cada animal té el seu so i la llengua té un verb per a cadascun.",
 'natura', 0),
('On viuen els peixos?', "A l'aigua", ['A l\u2019arbre', 'Sota terra', 'Als núvols'],
 "Els peixos respiren l'oxigen que hi ha dissolt a l'aigua, a través de les brànquies. Fora de l'aigua s'ofeguen encara que hi hagi aire.",
 'natura', 0),
('Quin animal té trompa?', "L'elefant", ['El lleó', 'El camell', 'El ren'],
 "La trompa de l'elefant és alhora nas i mà: hi respira, hi olora, beu, i pot agafar tant un tronc com una cacauet.",
 'natura', 0),
('Quantes ales té un ocell?', '2', ['1', '4', '6'],
 "Dues. Els insectes, en canvi, en solen tenir quatre, encara que a les mosques el segon parell s'ha convertit en dos balancins diminuts.",
 'natura', 0),
('Què surt d\u2019un ou de gallina?', 'Un pollet', ['Un conill', 'Un peix', 'Una papallona'],
 "Si l'ou està fecundat i la gallina el cova unes tres setmanes, en surt un pollet. Els ous que comprem no estan fecundats i no en sortiria res.",
 'natura', 0),
('De quin color és la neu?', 'Blanca', ['Blava', 'Verda', 'Groga'],
 "Els cristalls de gel reflecteixen tots els colors de la llum alhora, i la barreja de tots els colors és el blanc.",
 'natura', 0),
('Quin és l\u2019astre que ens dona llum de dia?', 'El Sol', ['La Lluna', 'Mart', 'Venus'],
 "El Sol és un estel: fa llum pròpia. La Lluna no en fa, només reflecteix la del Sol, i per això de nit fa aquella claror tan fluixa.",
 'mon', 0),
('Quants dies té una setmana?', '7', ['5', '6', '10'],
 "Set. És l'única mesura del calendari que no ve del cel: els mesos vénen de la Lluna i els anys del Sol, però la setmana és un invent humà molt antic.",
 'mon', 0),
('Quin mes ve després del desembre?', 'El gener', ['El novembre', 'El febrer', "L'octubre"],
 "El gener, que ja és de l'any següent. Es diu així per Janus, un déu romà amb dues cares: una mirava enrere i l'altra endavant.",
 'mon', 0),
('Quantes hores té un dia?', '24', ['12', '20', '36'],
 "Vint-i-quatre, que és el que triga la Terra a fer una volta sobre ella mateixa. Per això mentre aquí és de dia, a l'altra banda del món és de nit.",
 'mon', 0),
('Quin idioma es parla al Brasil?', 'El portuguès', ["L'espanyol", 'El brasiler', 'El francès'],
 "El Brasil va ser colònia de Portugal, i per això és l'únic país gran d'Amèrica del Sud que no parla espanyol.",
 'mon', 1),
('Quants minuts té una hora?', '60', ['50', '100', '30'],
 "Seixanta, com els segons d'un minut. Ve dels babilonis, que comptaven de seixanta en seixanta perquè el 60 es pot partir de moltes maneres.",
 'mon', 0),
('Quin invent serveix per saber l\u2019hora?', 'El rellotge', ['El termòmetre', 'La brúixola', 'La balança'],
 "El termòmetre mesura la temperatura, la brúixola indica el nord i la balança pesa. Cada aparell, la seva mesura.",
 'historia', 0),
('Amb què escrivien els nens a l\u2019escola fa cent anys?', 'Amb guix i pissarra', ['Amb ordinador',
 'Amb retolador', 'Amb bolígraf'],
 "Cada nen tenia una pissarreta pròpia i un guix, perquè el paper era car. S'escrivia, es mirava i s'esborrava per tornar a començar.",
 'historia', 0),
('Qui va pintar la Gioconda?', 'Leonardo da Vinci', ['Miquel Àngel', 'Rafael', 'Botticelli'],
 "Leonardo la va començar cap al 1503 i la va anar retocant anys i panys. No la va lliurar mai: se la va endur a França i allà s'ha quedat.",
 'historia', 1),
('Què és una catedral?', 'Una església gran', ['Un castell', 'Un mercat', 'Un teatre'],
 "És l'església principal d'una diòcesi, la que té la seu del bisbe. Per això a Barcelona, Girona o Tarragona també se'n diu la Seu.",
 'historia', 0),
('Quin aparell va inventar Gutenberg?', 'La impremta', ['El telescopi', 'El telèfon', 'La bicicleta'],
 "Cap al 1450 va idear els tipus mòbils: lletres soltes de metall que es podien recol·locar. Fins llavors, cada llibre s'havia de copiar a mà.",
 'historia', 2),
('Quin mitjà de transport va fer famós el Titanic?', 'El vaixell', ["L'avió", 'El tren', 'El globus'],
 "El Titanic era un transatlàntic i es va enfonsar el 1912 en el seu primer viatge, en xocar amb un iceberg.",
 'historia', 1),
('Com es diu la primera lletra de l\u2019abecedari?', 'La a', ['La be', 'La zeta', 'La ema'],
 "La a. La paraula *abecedari* és, de fet, el nom de les quatre primeres lletres seguides: a, be, ce, de.",
 'llengua', 0),
('Quantes paraules té la frase "el gat dorm"?', '3', ['2', '4', '5'],
 "Tres: *el*, *gat* i *dorm*. Les paraules se separen amb espais, encara que siguin tan curtes com *el*.",
 'llengua', 0),
('Què és el contrari de "dia"?', 'Nit', ['Tarda', 'Hora', 'Sol'],
 "Dia i nit són contraris. Tarda i hora no ho són: la tarda és un tros del dia i l'hora és una mesura.",
 'llengua', 0),
('Com es diu la persona que escriu llibres?', 'Escriptor', ['Lector', 'Llibreter', 'Impressor'],
 "L'escriptor l'escriu, l'impressor l'imprimeix, el llibreter el ven i el lector el llegeix. Cadascú té el seu nom.",
 'llengua', 0),
('Quantes síl·labes té la paraula "finestra"?', '3', ['2', '4', '5'],
 "Tres: fi-nes-tra. Les síl·labes són els cops de veu; es poden comptar picant de mans mentre es diu la paraula a poc a poc.",
 'llengua', 1),
('Què és un refrany?', 'Una dita curta amb una ensenyança', ['Una cançó', 'Un conte llarg', 'Una pregunta'],
 'Com "qui no vol pols, que no vagi a l\u2019era": una frase breu que guarda una experiència repetida durant generacions.',
 'llengua', 1),
('Què vol dir "matinar"?', 'Llevar-se molt aviat', ['Dinar tard', 'Dormir la migdiada', 'Sopar d\u2019hora'],
 "Ve de matí, com matiner. El refrany diu que a qui matina, Déu l'ajuda, que és una manera d'animar a començar aviat.",
 'llengua', 1)
]

TEMES = ['natura', 'mon', 'historia', 'llengua']
NIVELLS = ['fàcil', 'mitjà', 'difícil']


def comprova():
    problemes, vistes = [], set()
    for i, (p, b, o, e, t, n) in enumerate(BANC):
        if p in vistes: problemes.append(f'{i}: pregunta repetida — {p}')
        vistes.add(p)
        if len(o) != 3: problemes.append(f'{i}: {len(o)} respostes dolentes — {p}')
        if b in o: problemes.append(f'{i}: la bona també és a les dolentes — {p}')
        if len(set(o)) != 3: problemes.append(f'{i}: dolentes repetides — {p}')
        if len(e) < 60: problemes.append(f'{i}: explicació massa curta — {p}')
        if t not in TEMES: problemes.append(f'{i}: tema desconegut {t}')
        if n not in (0, 1, 2): problemes.append(f'{i}: nivell desconegut {n}')
        if not p.endswith('?'): problemes.append(f'{i}: no acaba amb interrogant — {p}')
    return problemes


def js():
    """Escriu el banc tal com ha d'anar dins l'index.html"""
    def txt(s): return "'" + s.replace('\\', '\\\\').replace("'", "\\'") + "'"
    files = []
    for p, b, o, e, t, n in BANC:
        files.append('  {p:%s, b:%s, o:[%s], e:%s, t:%s, n:%d}'
                     % (txt(p), txt(b), ', '.join(txt(x) for x in o), txt(e), txt(t), n))
    return 'const BANC_PREGUNTES = [\n' + ',\n'.join(files) + '\n];\n'


if __name__ == '__main__':
    mals = comprova()
    print('preguntes:', len(BANC), '· problemes:', len(mals))
    for m in mals: print('  ', m)
    print()
    print('per tema i nivell:')
    print('  %-10s %6s %6s %6s' % ('tema', 'fàcil', 'mitjà', 'difícil'))
    for t in TEMES:
        c = [sum(1 for x in BANC if x[4] == t and x[5] == n) for n in (0, 1, 2)]
        print('  %-10s %6d %6d %6d' % (t, *c))
    print('  %-10s %6d %6d %6d' % ('TOTAL',
          *[sum(1 for x in BANC if x[5] == n) for n in (0, 1, 2)]))
    open('/tmp/claude-0/-home-claude/46257fec-254f-5388-a15a-a7d89661eb07/scratchpad/banc.js', 'w').write(js())
