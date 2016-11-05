# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace
from rdflib import URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import WILDLIFE, CRUZAR, UMBEL, OWL
from utils.namespaces import eol, gbif, uniprot, wikidata, dbpedia, rutaMaiz
from fauna import g

#g = Graph()

def flora(uri, nombre_comun, nombre_cientifico, descripcion, imagen, uriLink1, uriLink2, ref, uriLink3):
    g.add( (URIRef(uri), RDF.type, WILDLIFE.TaxonName) )
    g.add( (URIRef(uri), WILDLIFE.commonName, Literal(nombre_comun, lang="es") ) )
    g.add( (URIRef(uri), WILDLIFE.scientificName, Literal(nombre_cientifico, lang="la")) )
    g.add( (URIRef(uri), WILDLIFE.shortDescription, Literal(descripcion, lang="es")) )
    g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)))
    g.add( (URIRef(uri), WILDLIFE.kingdomName, Literal('Vegetal', lang="es")) )
    
    g.add( (URIRef(uri), FOAF.isPrimaryTopicOf, URIRef(ref)) ) #Sitio web del que se tomo la des
    g.add( (URIRef(uri), OWL.sameAs, URIRef(uriLink1)) ) #Link RDF a DBpedia
    g.add( (URIRef(uri), RDFS.seeAlso, URIRef(uriLink2)) ) #Link a EOL
    g.add( (URIRef(uri), OWL.sameAs, URIRef(uriLink3)) ) #Link RDF a UniProt
    
    g.add( (URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaMaiz.Flora)) )

flora(
    gbif['7413206'],
    "MANDARINA",
    "Citrus Nobilis",
    """El árbol es un frutal espinoso, con ramas delgadas, con las hojas tanto amplias como delgadas. 
    Las flores nacen simples o en grupos en las axilas de las hojas.""",
    "http://i.imgur.com/P0rzCMB.jpg",
    dbpedia['Citrus_nobilis'],
    eol['27915528'],
	'http://www.sabelotodo.org/agricultura/frutales/mandarina.html',
	uniprot['481549']
)

flora(
    gbif['8206387'],
    "NARANJO",
    "Citrus Sinensis",
    """El naranjo es un frutal de hasta 10 ms de altura con la copa muy redondeada. Tallos ligeramente espinosos, 
    hojas coriaceas, flores de color blanco muy perfumadas.""",
    "http://i.imgur.com/aKWeHJj.jpg",
    dbpedia['Citrus_sinensis'],
    eol['582206'],
	'https://climafrutal.wordpress.com/naranjo/',
	uniprot['2711']
)

flora(
    gbif['3190171'],
    "LIMÓN",
    "Citrus Limon",
    """El limonero es un frutal de porte mediano que puede llegar a vivir 70 años. De tronco leñoso, amarillento 
    y muy ramificado, sus grandes y ovaladas hojas de color verde brillante son muy aromáticas al igual que 
    sus flores.""",
    "http://i.imgur.com/JsCNYfk.jpg",
    dbpedia['Citrus_limon'],
    eol['582200'],
	'http://www.consumer.es/web/es/bricolaje/jardin/2002/04/04/40671.php',
	uniprot['2708']
)

flora(
    gbif['3152205'],
    "CACAO",
    "Theobroma Cacao L.",
    """Arbusto pequeño de hasta 10 m. Tallo leñoso, recto, con brotes, corteza delgada de color café. Hojas perennes 
    grandes, alternas, colgantes. Flores casi permanentes pequeñas blancas a rosadas, nacen sobre el tallo. El 
    fruto nace en el tronco es una baya grande de hasta 30 x 12 cm.""",
    "http://i.imgur.com/CDEeJVu.jpg",
    dbpedia['Theobroma_cacao'],
    eol['484592'],
	'https://issuu.com/lorenarojastorres/docs/visita_granja_mama_lulu.docx',
	uniprot['3641']
)

flora(
    gbif['3034046'],
    "AGUACATE",
    "Persea Americana",
    """Árbol de unos 10 m de altura. Tallo leñoso. Perennifolio, hojas alternas, pedunculadas, de color verde 
    brillante. Flores perfectas en racimos. Su fruto es una drupa de color verde y piel o cáscara delgada, rico 
    en proteínas y aceite vegetal.""",
    "http://i.imgur.com/R3mtPr3.jpg",
    dbpedia['Persea_americana'],
    eol['596888'],
	'http://www.farmaconsejos.com/plantas-medicinales/aguacate/',
	uniprot['3435']
)

flora(
    gbif['2874190'],
    "MARACUYÁ",
    "Passiflora Edulis",
    """Enredadera trepadora; puede alcanzar los 9 ms de longitud en condiciones climáticas favorables, 
    aunque su período de vida no supera por lo general la década. Su tallo es rígido y leñoso; presenta 
    hojas alternas de gran tamaño, perennes, lisas y de color verde oscuro Tallos trepadores, leñosos.""",
    "http://i.imgur.com/QoGoZpf.jpg",
    dbpedia['Passiflora_edulis'],
    eol['584518'],
	'https://es.wikipedia.org/wiki/Passiflora_edulis',
	uniprot['78168']
)

flora(
    gbif['2762752'],
    "PLÁTANO",
    "Musa × Paradisiaca L.",
    """Planta con el tallo bien desarrollado. Hojas grandes, oblongas, lámina con la vena media bien desarrollada 
    y numerosas venas paralelas, perpendiculares a la vena media.""",
    "http://i.imgur.com/3bfoEk5.jpg",
    dbpedia['Musa_paradisiaca'],
    eol['1116069'],
	'http://aprendeenlinea.udea.edu.co/ova/?q=node/730',
	uniprot['89151']
)

flora(
    gbif['2703912'],
    "CAÑA DE AZÚCAR",
    "Saccharum Officinarum L.",
    """Es una planta perenne con un tallo macizo, de hasta 6 ms de altura y 2-8 cms de diametro; aparece por lo 
    general deshojado en la parte inferior, está lleno de un tejido esponjoso y dulce del que se extrae el azúcar. 
    Sus hojas son largas y puntiagudas.""",
    "http://i.imgur.com/7K7gpog.jpg",
    dbpedia['Saccharum_officinarum_L'],
    eol['1115140'],
	'http://dicci-eponimos.blogspot.com.co/2010/06/cana-de-castilla.html',
	uniprot['4547']
)

flora(
    gbif['5289743'],
    "CAÑA BRAVA",
    "Gynerium Sagittatum",
    """Es una planta silvestre de hasta 4 ms de alto. Posee tallos gruesos, sólidos y muy resistentes que le han 
    permitido sobrevivir al tiempo. Las hojas son lineales y aserradas, dispuestas en dos filas.""",
    "http://i.imgur.com/R9UjZNK.jpg",
    dbpedia['Gynerium_sagittatum'],
    eol['1115272'],
	'http://animalesyplantasdeperu.blogspot.com.co/2008/05/la-caa-brava-gynerium-sagittatum.html',
	uniprot['42053']
)

flora(
    gbif['5290052'],
    "MAÍZ",
    "Zea Mays",
    """Planta herbáceae que puede alcanzar hasta los 2,5 m de altura. El tallo internamente tiene una médula 
    de tejido esponjoso y blanco donde almacena reservas alimenticias, en especial azúcares. Las hojas son alargadas 
    arrolladas al tallo, del cual nacen las espigas o mazorcas.""",
    "http://i.imgur.com/6Ywbfgs.jpg",
    dbpedia['Zea_Mays'],
    eol['1115259'],
	'http://aprendeenlinea.udea.edu.co/ova/?q=node/521',
	uniprot['4577']
)

flora(
    gbif['2760874'],
    "HELICONIA",
    "Heliconia Bihai",
    """Es una planta muy llamativa por la inflorescencia que tiene en forma de espiga caracterizada por una serie de 
    espatas de color rojo-verde y amarillo. Puede llegar a alcanzar entre los 4 y 6 m de altura y las hojas 
    tienen forma de abanico.""",
    "http://i.imgur.com/wZ0GLbc.jpg",
    dbpedia['Heliconia_bihai'],
    eol['1118068'],
	'http://www.hogarmania.com/jardineria/fichas/plantas/201410/heliconia-bihai-26384.html',
	uniprot['446146']
)

flora(
    gbif['3060998'],
    "YUCA",
    "Manihot Esculenta",
    """Es un arbusto perenne, que alcanza los dos metros de altura. Su raíz es cilíndrica y oblonga, y alcanza 
    el metro de largo y los 10 cms de diámetro. La cáscara es dura e incomestible. La pulpa es muy rica en hidratos 
    de carbono y azúcares.""",
    "http://i.imgur.com/VYm4XpF.jpg",
    dbpedia.Cassava,
    eol['1154718'],
	'https://es.wikipedia.org/wiki/Manihot_esculenta',
	uniprot['3983']
)

flora(
    gbif['2874484'],
    "PAPAYA",
    "Carica Papaya",
    """Planta herbácea, de hasta 8 ms de altura; con látex lechoso. Tallos cilindrico, simple, sin ramificar, termina 
    en un penacho de hojas, de hasta 30 cms de diámetro. Flor de color amarillo, pétalos y sépalos del mismo color, 
    blanco amarilloso, nacen en el extremo del tallo, debajo de las hojas.""",
    "http://i.imgur.com/oAa8tSA.jpg",
    dbpedia['Carica_papaya'],
    eol['585682'],
	'http://aprendeenlinea.udea.edu.co/ova/?q=node/691',
	uniprot['3649']
)

flora(
    gbif['8482252'],
    "TOMATE CHERRI",
    "Lycopersicum Pimpinellifolium",
    """Planta anual de porte arbustivo o rastrero. Las hojas son sencillas, pecioladas y de limbo hendido. Toda 
    la parte verde de la planta está compuesta por pelos glandulares que al rozarse emiten un líquido con olor 
    característico. Las flores aparecen en racimos siendo el número de estas variable.""",
    "http://i.imgur.com/viCbqpn.jpg",
    dbpedia['Solanum_pimpinellifolium'],
    eol['590239'],
	'http://www.frutasiru.com/catalogo-ficha.php?fml=12&prod=56',
	uniprot['286530']
)

flora(
    gbif['5288819'],
    "PIÑA",
    "Ananas Comosus",
    """Planta perenne terrestre, con forma de roseta abierta que produce uno de los frutos tropicales más consumidos. 
    Hojas en forma de espadas con diminutas y afiladas espinas en sus bordes.""",
    "http://i.imgur.com/yvXykAn.jpg",
    dbpedia['Ananas_comosus'],
    eol['1126520'],
	'http://plantasyjardin.com/2013/03/ananas-cosmosus-una-de-las-frutas-tropicales-mas-consumidas/',
	uniprot['4615']
)

flora(
    gbif['5420380'],
    "GUAYABA",
    "Psidium Guajava",
    """Arbolito de follaje persistente que puede alcanzar 4-6 ms de altura, con el tronco corto y algo tortuoso. Hojas 
    opuestas de 5-10 cms de longitud. Flores blancas, solitarias o en pequeños grupos, que aparecen en las axilas de las 
    hojas. Fruto en baya redondeada con el cáliz de la flor persistiendo.""",
    "http://i.imgur.com/e55G5DZ.jpg",
    dbpedia['Psidium_guajava'],
    eol['2508593'],
	'http://www.jardinbotanico.uma.es/bbdd/index.php/jb-11-01/',
	uniprot['120290']
)

flora(
    gbif['4093687'],
    "GUAYACÁN",
    "Tabebuia guayacan (Seem.) Hemsl.",
    """Es un árbol grande de hasta 40 ms de alto y 100 cms de diámetro con tronco recto, cilíndrico y raramente irregular 
    cuya base es ligeramente alargada. Produce una madera muy pesada y resistente a la pudrición.""",
    "http://i.imgur.com/9CmiV7U.jpg",
    dbpedia['Handroanthus_guayacan'],
    eol['5637530'],
	'http://www.discoverlife.org/20/q?search=Tabebuia+guayacan',
	uniprot['429699']
)

flora(
    gbif['5406697'],
    "CEIBA",
    "Ceiba Pentandra (L.) Gaertn",
    """Árbol de 50 ms de altura, tallo de 2 ms de diámetro, abombado, corteza gris clara y anillada, copa 
    semihemisférica, follaje denso verde oscuro. Hojas compuestas y alternas, flores blancas.""",
    "http://i.imgur.com/V9Rfjpq.jpg",
    dbpedia['Ceiba_pentandra'],
    eol['584794'],
	'http://recursosbiologicos.eia.edu.co/ecologia/estudiantes/ceiba.htm',
	uniprot['193163']
)

flora(
    gbif['5357108'],
    "ÉBANO FALSO",
    "Cassia Fistula",
    """Árbol de 10-15 ms de alto; ramas de tendencia ascendente. Hojas grandes, caducas, ovadas, acuminadas y péndulas. 
    Flores dispuestas en grandes racimos pendulares, muy vistosas de color amarillo.""",
    "http://i.imgur.com/aUZVMJ4.jpg",
    dbpedia['Cassia_fistula'],
    eol['704102'],
	'http://docplayer.es/12485087-Ixora-ixora-coccinea-l-jazmin-del-diablo-buque-de-novia.html',
	uniprot['53852']
)
'''
flora(
    gbif['4155017'],
    "GUADUA",
    "Guadua Angustifolia",
    """La raíz es un rizoma que almacena los nutrimentos, estos rizomas producen raicillas adventicias, el tallo de 
    forma cilíndrica y con nudos, ramas solitarias y muy espinosas en los nudos basales y con presencia o no de hojas; 
    hojas lanceoladas verdes lustrosas.""",
    "http://i.imgur.com/WLLO9uD.jpg",
    dbpedia.Guadua,
    eol['5800278'],
	'https://en.wikipedia.org/wiki/Guadua_angustifolia',
	uniprot['323898']
)
'''
flora(
    gbif['2858244'],
    "NARCISO",
    "Narcissus Pseudonarcissus",
    """Es una planta de hojas estrechas y alargadas. Sus flores son de color blanco, amarillo o rosa y de forma simple. 
    La floración se produce en primavera. El fruto es una cápsula.""",
    "http://i.imgur.com/GcRveZA.jpg",
    dbpedia['Narcissus_primigenius'],
    eol['1004073'],
	'https://en.wikipedia.org/wiki/Narcissus_pseudonarcissus',
	uniprot['39639']
)

flora(
    gbif['2891606'],
    "GERANIO",
    "Pelargonium Zonale",
    """Hojas en forma generalmente acorazonada y de diferentes tonalidades de verde, de floración prolongada, 
    las flores se encuentran agrupadas de formas diversas y el colorido es muy variado, desde el blanco al rojo 
    pasando por el rosado.""",
    "http://i.imgur.com/RssuVMe.jpg",
    dbpedia['Pelargonium_zonale'],
    eol['595134'],
	'http://floresandra.galeon.com/algunas.htm',
	uniprot['4032']
)

flora(
    gbif['5331181'],
    "VIOLETA",
    "Viola Odorata",
    """Planta perenne rizomatosa que se expande mediante estalones y puede formar una buena cubierta de suelo, 
    sus hojas son radicales ligeramente festoneadas y acorazonadas en la base. Las flores son muy perfumadas; el 
    fruto es una cápsula que se abre en la madurez, su es color violeta y blanco.""",
    "http://i.imgur.com/rKrLqRo.jpg",
    dbpedia['Viola_odorata'],
    eol['584573'],
	'http://menospetroleo.blogspot.com.co/2013/03/plantas-vistas-en-el-curso-de-bosque.html',
	uniprot['97441']
)

flora(
    gbif['3189636'],
    "CAMELIA",
    "Camellia Japonica",
    """Arbusto ramificado de 2 ms de altura, hojas anchas elípticas con filo aserrado, haz de color verde oscuro 
    reluciente y el envés más pálido y coriáceo. Se adapta perfectamente a su cultivo en jardinera. Flores solitarias 
    de color variado rojo sangre, cereza, con rayas blancas o rosadas.""",
    "http://i.imgur.com/VUACRGI.jpg",
    dbpedia['Camellia_japonica'],
    eol['484988'],
	'http://www.slideshare.net/CamiloAlejandroMarin/herbario-escolar-2012',
	uniprot['4443']
)

flora(
    gbif['8008378'],
    "MARGARITA COMÚN",
    "Chrysanthemum Leucanthemum",
    """Es una planta herbácea con hojas hendidas. Las flores están siempre reunidas en una inflorescencia llamada 
    cabezuela o capítulo, que parece una única flor y funciona como tal.""",
    "http://i.imgur.com/A1j5930.jpg",
    dbpedia['Leucanthemum_vulgare'],
    eol['46241383'],
	'http://aplicaciones2.colombiaaprende.edu.co/concursos/expediciones_botanicas/ver_herbarios_p.php?id=628&id_p=6041',
	uniprot['99072']
)

flora(
    gbif['3093023'],
    "DALIA",
    "Dahlia spp.",
    """Planta herbácea o arbustiva anual, raíz tuberosa, hojas opuestas o verticiladas. Flores dispuestas en 
    inflorescencias compuestas o capítulo (rodeada por brácteas), de diferentes colores. Hay 30 especies y 
    20000 variedades.""",
    "http://i.imgur.com/Th4Plgi.jpg",
    wikidata.Q130918,
    eol['46321784'],
	'https://en.wikipedia.org/wiki/Dahlia',
	uniprot['41562']
)

flora(
    gbif['8458847'],
    "LIRIO COMÚN",
    "Iris germanica",
    """Tallo terminal con hojas en la base, 35 a 45 cms de largo; herbácea perenne de rizoma vistoso y grueso. 
    Hojas acintadas, erguidas, de borde liso, color verde oscuro a grisáceo. Flores de poca duración.""",
    "http://i.imgur.com/NDTPe0l.jpg",
    dbpedia['Iris_germanica'],
    eol['490948'],
	'https://en.wikipedia.org/wiki/Iris_germanica',
	uniprot['34205']
)

flora(
    gbif['2985994'],
    "HORTENSIA",
    "Hydrangea Macrophylla",
    """Planta semiarbustiva, caducifolia, puede llegar a medir 1,5 ms. Tallos ramosos, gruesos, derechos, 
    terminados por las flores agrupadas. Hojas grandes, verdes, opuestas, ovaladas con borde dentado.""",
    "http://i.imgur.com/VLAuVL6.jpg",
    dbpedia['Hydrangea_macrophylla'],
    eol['392374'],
	'https://en.wikipedia.org/wiki/Hydrangea_macrophylla',
	uniprot['23110']
)

flora(
    gbif['2888443'],
    "AMAPOLA",
    "Papaver rhoeas",
    """Hierba anual, cubierta de pelos perpendiculares. Hojas simples en la base, alargadas y lobuladas. flores 
    solitarias con pétalos arrugados en botones florales, mostrando al abrirse un bello color rojo intenso, 
    por lo general presentan una mancha negruzca en la porción basal. El fruto de la amapola es una cápsula, 
    llena de semillas.""",
    "http://i.imgur.com/9RgVwBE.jpg",
    dbpedia['Papaver_rhoeas'],
    eol['596241'],
	'http://www.biotremol.com/una-gran-desconocida-la-amapola/',
	uniprot['33128']
)

flora(
    gbif['5421335'],
    "JAZMÍN NARANJA",
    "Murraya Paniculata",
    """Planta con hojas compuestas, alternas, imparipinnadas; los foliolos de 1 a 4 cms de largo, verdes muy oscuros 
    y brillantes. Las flores blancas, pequeñas y fragantes.""",
    "http://i.imgur.com/6PuZR2z.jpg",
    dbpedia['Murraya_paniculata'],
    eol['489435'],
	'https://en.wikipedia.org/wiki/Murraya_paniculata',
	uniprot['43711']
)

flora(
    gbif['2874718'],
    "BEGONIA",
    "Begonia Semperflorens",
    """Herbácea perenne o anual, altura aproximada entre 20-40 cms. Tallo carnoso y ramificado, hojas ovales y 
    redondeadas con coloraciones rojizas en múltiples tonalidades. Las flores reunidas en cimas exilares de colores 
    rosa, rojo o blanco.""",
    "http://i.imgur.com/9Pn2uWH.jpg",
    wikidata.Q843363,
    eol['46341032'],
	'http://www.laguiadeplantas.com/?s=p&id=354',
	uniprot['589341']
)

flora(
    gbif['8176318'],
    "PENSAMIENTOS",
    "Viola x wittrockiana",
    """Son plantas híbridas, cuyo ciclo de vida es de un año, y que son cultivadas por sus vistosas flores. 
    Tienen hojas simples con forma de corazón y margen dentado de cinco pétalos aterciopelados, y con diversas 
    gamas de colores. Su floración abarca los meses otoñales, pero continua hasta la entrada de la primavera.""",
    "http://i.imgur.com/u8YKOy7.jpg",
    dbpedia['Viola_x_wittrockiana'],
    eol['46324497'],
	'https://www.ecured.cu/Pensamiento_(planta)',
	uniprot['456371']
)

flora(
    gbif['2750913'],
    "TULIPÁN",
    "Tulipa spp",
    """Hierba perenne con bulbos o rizomas. Las hojas son alternas y espiraladas, se disponen a lo largo del tallo 
    o en una roseta basal. Flores erguidas muy llamativas, de numerosos colores, tardan hasta tres semanas en 
    marchitarse. El fruto es una cápsula, ocasionalmente una baya. Las semillas son planas y con forma de disco 
    o globosas.""",
    "http://i.imgur.com/JmDuDLg.gif",
    wikidata.Q93201,
    eol['17820'],
	'http://fichas.infojardin.com/bulbosas/tulipa-tulipan-tulipanes-botanicos-tulipanes-darwin.htm',
	uniprot['13305']
)

flora(
    gbif['7598400'],
    "CRISANTEMO",
    "Chrysanthemum Morifolium",
    """Planta de tallo herbáceo y delgado, con hojas alternas suaves al tacto, palmeado, divididas, con bordes 
    dentados, nervaduras principal y secundarias, a la cabeza floral se le denomina capítulo.""",
    "http://i.imgur.com/w4aGjbg.jpg",
    dbpedia['Chrysanthemum_morifolium'],
    eol['483963'],
	'https://en.wikipedia.org/wiki/Chrysanthemum_morifolium',
	uniprot['41568']
)

flora(
    gbif['3153283'],
    "MAGNOLIA",
    "Magnolia Grandiflora L.",
    """Es un árbol de tamaño medio a grande de 20-30 ms de altura. Las hojas son perennes, simples o ampliamente 
    ovadas de 12-20 cms de longitud y 6-12 cms de ancho con los márgenes dentados, son de color verde oscuro y 
    se vuelven color marrón cuando llega el invierno.""",
    "http://i.imgur.com/p3tLqzX.jpg",
    dbpedia['Magnolia_grandiflora'],
    eol['1154991'],
	'http://vida-flores.blogspot.com.co/',
	uniprot['3406']
)

flora(
    gbif['4935172'],
    "FLOR DE MAYO",
    "Cattleya Trianae",
    """Planta epífita, con pseudobulbos de largo variable que llevan a su extremidad una o a dos hojas sin pecíolo. 
    Flores vistosas que se desarrollan en el tallo.""",
    "http://i.imgur.com/A4H9iz7.jpg",
    dbpedia['Cattleya_trianae'],
    eol['1090706'],
	'http://orquideascolombiana.blogspot.com.co/',
	uniprot['142280']
)

flora(
    gbif['5289798'],
    "PASTO ESTRELLA",
    "Cynodon Plectostachyus",
    """Es una gramínea perenne, de vida larga, frondosa y rastrera, produce estolones de rápido crecimiento, con 
    largos entrenudos y sus tallos pueden alcanzar hasta 3 ms de longitud. Posee hojas exuberantes con vellos en 
    forma de lanza. La inflorescencia presenta de 2 a 5 espiguillas solitarias de 2 a 3 mms.""",
    "http://i.imgur.com/biYwa69.jpg",
    wikidata.Q959222,
    eol['1114873'],
	'https://www.scribd.com/doc/229139076/Plantas-forrajeras-Ecuador',
	uniprot['751635']
)

flora(
    gbif['2895345'],
    "CAFÉ",
    "Coffea Arabica",
    """El cafeto es un arbusto o árbol pequeño, perennifolio, de fuste recto que puede alcanzar los 10 ms en 
    estado silvestre.""",
    "http://i.imgur.com/H2ZM3sf.jpg",
    dbpedia['Coffea_arabica'],
    eol['46321583'],
	'https://es.wikipedia.org/wiki/Coffea',
	uniprot['13443']
)

flora(
    gbif['3190638'],
    "MANGO",
    "Mangifera Indica",
    """El mango típico constituye un árbol de tamaño mediano, de 10-30 ms de altura. El tronco es más o menos recto, 
    cilíndrico y de 75-100 cms de diámetro, cuya corteza de color gris - café tiene grietas.""",
    "http://i.imgur.com/GtxlZkC.jpg",
    dbpedia['Mangifera_indica'],
    eol['582270'],
	'http://www.empresario.com.co/recursos/page_flip/MEGA/mega_mango/files/ficha%20mango.pdf',
	uniprot['29780']
)

flora(
    gbif['2856504'],
    "CEBOLLA LARGA",
    "Allium Fistulosum",
    """Las raíces se producen en la base del tallo, son fasciculadas y poco abundantes. Cada hoja tiene una base 
    larga y carnosa, que se une estrechamente con la base de las demás hojas. Las hojas son tubulares de 25-35 cms 
    de largo y 5-7 mms de diámetro. El tallo es un disco comprimido, de donde parten las raíces y la base de 
    las hojas.""",
    "http://i.imgur.com/u1nPyiR.jpg",
    dbpedia['Allium_fistulosum'],
    eol['1084499'],
	'https://es.wikipedia.org/wiki/Allium_fistulosum',
	uniprot['35875']
)

flora(
    gbif['2932944'],
    "AJÍ",
    "Capsicum Annuum",
    """Planta anual, que puede alcanzar hasta 1 m de altura, de tallos empinados y ramosos, con las hojas aovadas 
    y lanceoladas de bordes enteros o apenas sinuados en la base. Es especialmente productiva en zonas cálidas 
    y climas secos. Es una planta de huerta y de diversas variedades.""",
    "http://i.imgur.com/EBqG6Ox.jpg",
    dbpedia['Capsicum_annuum_var._minimum'],
    eol['581098'],
	'http://ornamentalis.com/capsicum-annuum/',
	uniprot['4072']
)

flora(
    gbif['8659902'],
    "ORTIGA",
    "Urtica Dioica",
    """Es una planta arbustiva perenne que puede alcanzar hasta 1,5 ms de altura. Tallos erectos cuadrangulares, 
    hojas verdes aserradas, puntiagudas, provistas al igual que el tallo de pelos urticantes. Flores en forma de 
    raíces, con flores unisexuales. Posee unos pelos urticantes que tienen la forma de pequeñisimas ampollas.""",
    "http://i.imgur.com/oVjUyH1.jpg",
    dbpedia['Urtica_dioica'],
    eol['46373617'],
	'https://es.wikipedia.org/wiki/Urtica_dioica',
	uniprot['3501']
)

flora(
    gbif['2926634'],
    "ROMERO",
    "Rosmarinus Officinalis",
    """Arbusto perenne, verde, leñoso y muy aromático de hasta 2 ms de altura que crece espontáneamente o en cultivo. 
    Sus tallos ramificados con hojas rígidas, lineales, lanceoladas, en forma de aguja y de aspecto coriáceas las 
    recubre una capa de diminutos pelos.""",
    "http://i.imgur.com/umcF7Ne.jpg",
    dbpedia['Rosmarinus_officinalis'],
    eol['46323937'],
	'http://www.biodiversidad.co/fichas/1003',
	uniprot['39367']
)

flora(
    gbif['3034871'],
    "CILANTRO",
    "Coriandrum Sativum",
    """Es una hierba anual de hasta 60 cms, sin pelos y brillante. Los tallos del cilantro son erectos y delgados. 
    Las hojas de un verde vivo tienen forma de abanico.""",
    "http://i.imgur.com/Wzf5egG.jpg",
    dbpedia['Coriandrum_sativum'],
    eol['581687'],
	'http://viverovirtualrd.blogspot.com.co/2009/01/coriandrum-sativum-cilantro.html',
	uniprot['4047']
)

flora(
    gbif['2857697'],
    "CEBOLLA",
    "Allium Cepa",
    """Planta bienal cultivada como anual. Hojas semicilíndricas que nacen de un bulbo subterráneo provisto de 
    raíces poco profundas. Tallo erecto que lleva en su extremo una inflorescencia en forma de umbela de flores 
    blancas o rosadas.""",
    "http://i.imgur.com/avBZpBw.jpg",
    dbpedia['Allium_cepa'],
    eol['1084354'],
	'http://agroespoch2.blogspot.com.co/2015/01/cristian-inga.html',
	uniprot['4679']
)

flora(
    gbif['2856681'],
    "AJO",
    "Allium Sativum",
    """Alcanza entre 30 y 40 cms de altura, sus hojas son macizas, radicales y largas. Sus flores son blancas y 
    rosadas y cada una puede presentar 6 pétalos, 6 estambres y un pistilo. Su raíz es bulbosa, compuesta de 6 a 12 
    bulbillos ("dientes de ajo").""",
    "http://i.imgur.com/bziWfgl.jpg",
    dbpedia['Allium_sativum'],
    eol['1084926'],
	'http://www.labin.net/es/cultivos/ajos/20',
	uniprot['4682']
)

flora(
    gbif['2777724'],
    "SÁBILA",
    "Aloe Vera",
    """Es una planta perenne, con hojas gruesas organizadas en rosetas, alcanza 50 cms de largo y 7 cms de grosor. 
    Las hojas son alargadas y las flores son pequeñas.""",
    "http://i.imgur.com/cTlCh8V.jpg",
    dbpedia['Aloe_Vera'],
    eol['1085598'],
	'https://en.wikipedia.org/wiki/Aloe_vera',
	uniprot['34199']
)

flora(
    gbif['3070717'],
    "SACHA INCHI",
    "Plukenetia Volubilis",
    """Es una planta voluble, trepadora y semileñosa, de abundantes hojas y ramas; de una altura aproximada de 2 ms; 
    hojas alternas, acorazonadas; flores pequeñas blanquecinas en racimo; fruto de color marrón al madurar; 
    semillas marrón oscuro con un alto contenido de ácidos grasos insaturados Omega 3, 6 y 9.""",
    "http://i.imgur.com/1pvbezV.jpg",
    dbpedia['Plukenetia_volubilis'],
    eol['1152376'],
	'https://www.scribd.com/doc/20773504/SACHA-INCHI',
	uniprot['316893']
)

#print(g.serialize(format='pretty-xml'))



