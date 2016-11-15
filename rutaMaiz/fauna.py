#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph, BNode
from rdflib.namespace import RDF, RDFS, FOAF, OWL
from utils.ontologias import GR, VCARD, WILDLIFE, UMBEL
from utils.namespaces import eol, gbif, uniprot, wikidata, dbpedia, rutaMaiz
from eventos import g
#g = Graph()

def fauna(uri, nombre_comun, nombre_cientifico, descripcion, imagen, uriLink1, uriLink2, ref, uriLink3, linkURI):
	g.add( (URIRef(uri), RDF.type, WILDLIFE.TaxonName) )
	g.add( (URIRef(uri), WILDLIFE.commonName, Literal(nombre_comun) ) )
	g.add( (URIRef(uri), WILDLIFE.scientificName, Literal(nombre_cientifico)) )
	g.add( (URIRef(uri), WILDLIFE.shortDescription, Literal(descripcion)) )
	g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)))
	g.add( (URIRef(uri), WILDLIFE.kingdomName, Literal('Animal')) )
	g.add( (URIRef(uri), FOAF.isPrimaryTopicOf, URIRef(ref)) ) #Sitio web
	
	g.add( (URIRef(uri), OWL.sameAs, URIRef(uriLink1)) ) #Link RDF
	g.add( (URIRef(uri), OWL.sameAs, URIRef(uriLink3)) ) #Link RDF
	
	g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) ) #Links externos
	g.add( (URIRef(uri), RDFS.seeAlso, URIRef(uriLink2)) )
	
	g.add( ( URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaMaiz['Fauna.rdf'])) )

fauna(
	rutaMaiz['Fauna.rdf#leptotilaPlumbeiceps'],
	"PALOMA MONTARAZ CABECIGRÍS",
	"Leptotila plumbeiceps",
	"""La paloma montaraz cabecigrís tiene un tamaño de 25 cms de largo y pesa 155 grs. El dorso y las alas son de color 
	marrón oliva, y las partes inferiores son de color sombreado en blanco. La cola es amplia con punta de color blanco.
	Las aves jóvenes carecen de color gris en la cabeza.""",
	"http://i.imgur.com/0ViaN29.jpg",
	dbpedia['Grey-headed_dove'],
	eol['1049748'],
	'https://es.wikidatapedia.org/wikidata/Leptotila_plumbeiceps',
	uniprot['135630'],
	gbif['2496075']
)

fauna(
	rutaMaiz['Fauna.rdf#chrysolampisMosquitus'],
	"TUCUSITO RUBÍ",
	"Chrysolampis mosquitus",
	"""Es un colibrí pequeño, de pico corto. Sus colores van desde el negro en su mayor parte, 
	con un distintivo color rojo en la parte de la coronilla. También posee tonalidades naranja
	y café oliva oscuro. Se lo halla en la Cordillera Occidental y otros lugares con tierras áridas.""",
	"http://i.imgur.com/ZefaXVe.jpg",
	dbpedia['http://dbpedia.org/page/Ruby-topaz_hummingbird'],
	eol['1048778'],
	'http://www.icesi.edu.co/wikidata_aves_colombia/tiki-index.php?page=Cabeza+de+Rub%C3%AD',
	uniprot['472795'],
	gbif['2476346']
)

fauna(
	rutaMaiz['Fauna.rdf#picumnusGranadensis'],
	"CARPINTERO PUNTEADO",
	"Picumnus granadensis",
	"""Mide de 8-10 cms y pesa de 12-13 grs. Presenta pico negro y corto. Tiene cuello café grisáceo y partes 
	superiores teñidas de oliva. La superficie superior de su cola es café oscura con estrías en los márgenes 
	internos del par central de plumas. Mejillas, barbilla y garganta blanquecinos con puntos negros.""",
	"http://i.imgur.com/WiMJbSs.jpg",
	dbpedia['Greyish_piculet'],
	eol['1177576'],
	'http://www.icesi.edu.co/wikidata_aves_colombia/tiki-index.php?page=Carpinterito+Punteado+-+Picumnus+granadensis',
	uniprot['56080'],
	gbif['5228793']
)

fauna(
	rutaMaiz['Fauna.rdf#thamnophilusMultistriatus'],
	"BATARÁ CRESTIBARRADO",
	"Thamnophilus multistriatus",
	"""Mide 15,7 cms. Tiene los ojos amarillos. El macho tiene la coronilla blanca y negra. La hembra es castaña 
	por encima, lados de la cabeza y collar nucal estriado blanco y negro, partes inferiores en negro y blanco.""",
	"http://i.imgur.com/ZTiTTvy.jpg",
	dbpedia['Bar-crested_antshrike'],
	eol['1053773'],
	'http://www.icesi.edu.co/wikidata_aves_colombia/tiki-index.php?page=Barat%C3%A1+carcajada',
	uniprot['419668'],
	gbif['5959202']
)

fauna(
	rutaMaiz['Fauna.rdf#ramphocelusFlammigerus'],
	"SANGRETORO LOMO DE FUEGO",
	"Ramphocelus flammigerus",
	"""Mide en promedio 19 cms de longitud. El macho es negro con una mancha en la espalda de color
	rojo escarlata; el pecho anaranjado a rojo y el vientre amarillo intenso. El pico es azul 
	cobalto o blancuzco con punta negra. La hembra tiene el dorso marrón oliváceo con pintas oscuras; 
	pecho y vientre amarillo claro.""",
	"http://i.imgur.com/udtsGTS.jpg",
	dbpedia['Flame-rumped_tanager'],
	eol['1052874'],
	'https://es.wikidatapedia.org/wikidata/Ramphocelus_flammigerus',
	uniprot['1742462'],
	gbif['2488439']
)

fauna(
	rutaMaiz['Fauna.rdf#oryzoborusCrassirostris'],
	"SEMILLERO PIQUIGRANDE",
	"Oryzoborus crassirostris",
	"""Mide 13,5 cms de largo. Se caracteriza por su pico robusto y ancho en la base aunque relativamente corto 
	de color gris. Los machos tienen el plumaje totalmente negro, a excepción de una pequeña 
	mancha blanca en las alas, mientras que las hembras son de color pardo grisáceo.""",
	"http://i.imgur.com/maOVQKf.jpg",
	dbpedia['Large-billed_seed_finch'],
	eol['1050364'],
	'https://es.wikidatapedia.org/wikidata/Oryzoborus_crassirostris',
	uniprot['200159'],
	gbif['2492244']
)

fauna(
	rutaMaiz['Fauna.rdf#anasCyanoptera'],
	"PATO COLORADO",
	"Anas cyanoptera",
	"""Pato pequeño de 38-43 cms de longitud. El macho tiene ojos rojos, espalda 
	negruzca moteada, rabadilla y cola negras; la hembra tiene el color del cuerpo más oscuro, el pico más grande y 
	espatulado y la frente más pronunciada, sus ojos son de color avellana.""",
	"http://i.imgur.com/w8vAGpk.jpg",
	dbpedia['Cinnamon_teal'],
	eol['1048954'],
	'http://www.icesi.edu.co/wikidata_aves_colombia/tiki-index.php?page=Pato+Colorado',
	uniprot['75840'],
	gbif['2498139']
)

fauna(
	rutaMaiz['Fauna.rdf#ardeaAlba'],
	"GARZA BLANCA",
	"Ardea alba",
	"""Mide entre 88-104 cms, pesa 900 grs alcanzando algunas el kilogramo. En promedio, los machos son 
	ligeramente más grandes que las hembras.""",
	"http://i.imgur.com/XcvcXho.jpg",
	dbpedia['Great_egret'],
	eol['1178488'],
	'http://garzablancareal.blogspot.com.co/',
	uniprot['110620'],
	gbif['7913436']
)

fauna(
	rutaMaiz['Fauna.rdf#gonatodesAlbogularis'],
	"GECO CABEZA AMARILLA",
	"Gonatodes albogularis",
	"""Los adultos tienen una longitud total de sólo 6 cms. Es activo durante el día. Los machos son muy visibles,
	con la cabeza amarilla y el cuerpo de color azul oscuro a negro. A temperaturas más frías durante la noche,
	sus colores se desvanecen. Las hembras son lagartos moteados grises, a menudo con una línea clara en el cuello.""",
	"http://i.imgur.com/puGypO1.jpg",
	dbpedia['Yellow-headed_gecko'],
	eol['794091'],
	'http://www.waza.org/es/zoo/elegir-una-especie/reptiles/lagartos-y-tuatara/gonatodes-albogularis',
	uniprot['460622'],
	gbif['2447609']
)

fauna(
	rutaMaiz['Fauna.rdf#anolisAuratus'],
	"CAMALEÓN SABANERO",
	"Anolis auratus",
	"""Alcanza una longitud de entre 52 y 58 mms, es un lagarto pequeño con el cuerpo corto y comprimido; 
	las extremidades son largas; la cabeza es alargada y ligeramente deprimida en la parte frontal.
	La coloración es café-gris o café-chocolate con una raya amarilla brillante en ambos lados.""",
	"http://i.imgur.com/GmRbMrK.jpg",
	dbpedia['Anolis_fuscoauratus'],
	eol['795890'],
	'http://www.biodiversidad.co/fichas/2821',
	uniprot['323568'],
	gbif['2467661']
)

fauna(
	rutaMaiz['Fauna.rdf#cnemidophorusLemniscatus'],
	"COTEJOS O LAGARTIJAS AZULES",
	"Cnemidophorus lemniscatus",
	"""Se encuentra en los paises de Colombia, Venezuela, Ecuador, Panamá, Guyana y Brasil. 
	Es un lagarto de garganta azul y cuerpo de puntos blancos.""",
	"http://i.imgur.com/SwAA6fV.jpg",
	dbpedia['Rainbow_whiptail'],
	eol['1056806'],
	'http://www.tayrona.org/taganga_fauna_marina/cordados/cnemidophorus_lemniscatus/cnemidophorus_lemniscatus.htm',
	uniprot['68354'],
	gbif['5227564']
)

fauna(
	rutaMaiz['Fauna.rdf#kinosternonLeucostomum'],
	"TORTUGA DEL FANGO DE BOCA BLANCA",
	"Kinosternon leucostomum",
	"""Tiene el caparazón de color marrón oscuro. El plastrón es amarillo o amarillo con manchas oscuras.
	La cabeza es oscura, con la mandíbula de color amarillo claro y una mancha amarilla en ambos
	lados de la cabeza.""",
	"http://i.imgur.com/dTOXhTA.jpg",
	dbpedia['White-lipped_mud_turtle'],
	eol['792998'],
	'https://www.ecured.cu/Tortuga_de_Ci%C3%A9naga_Peque%C3%B1a',
	uniprot['641010'],
	gbif['2442350']
)

fauna(
	rutaMaiz['Fauna.rdf#colostethusFraterdanieli'],
	"RANA SILBADORA",
	"Colostethus fraterdanieli",
	"""Especie de rana de la famila Dendrobatidae, es endémica en los Andes de Colombia (Coordillera central
	y Occidental). Vive en el suelo cerca de los arroyos en los bosques de niebla y en los bosques tropicales secos.""",
	"http://i.imgur.com/f9GcVuo.jpg",
	dbpedia['Colostethus_fraterdanieli'],
	eol['313650'],
	'https://en.wikidatapedia.org/wikidata/Colostethus_fraterdanieli',
	uniprot['384860'],
	gbif['2428968']
)

fauna(
	rutaMaiz['Fauna.rdf#typhlonectesNatans'],
	"CULEBRA CIEGA",
	"Typhlonectes natans",
	"""Es un reptil escamoso adaptado a la vida en el subsuelo, a la vista son parecidos a las lombrices de
	tierra. El cuerpo es de forma cilíndrica, es anillado y no tiene patas. La cabeza tiene forma 
	trapezoidal y está separada del cuerpo por un surco. Pasan por una sola muda de piel.""",
	"http://i.imgur.com/kquFtEi.jpg",
	dbpedia['Typhlonectes_natans'],
	eol['333734'],
	'http://animales-salvajes.buscamix.com/web/content/view/189/262/',
	uniprot['8456'],
	gbif['2430957']
)

fauna(
	rutaMaiz['Fauna.rdf#leptodactylusColombiensis'],
	"RANA CRIOLLA",
	"Leptodactylus colombiensis",
	"""Amplia distribución en la región Andina y cuenca del Orinoco en los departamentos de Amazonas,
	Casanare, Antioquia, Boyacá, Valle del Cauca, entre otros. Los machos presentan dos espinas medianas 
	en cada pulgar y hendiduras bucales bien desarrolladas. La superficie dorsal es lisa y de color marrón a oliva.""",
	"http://i.imgur.com/AHG1ELR.jpg",
	dbpedia['Leptodactylus_colombiensis'],
	eol['334546'],
	'http://anfibiosdelvalledelcauca.com/index.php?option=com_k2&view=item&id=93:leptodactylus-colombiensis&Itemid=434',
	uniprot['1615739'],
	gbif['5217567']
)

fauna(
	rutaMaiz['Fauna.rdf#ichthyoelephasLongirostris'],
	"BESUDO",
	"Ichthyoelephas longirostris",
	"""Pez similar al bocachico, pero que se distingue por su boca más prominente, con el labio superior mucho más grueso, 
	los ojos relativamente pequeños y por la ausencia de la espina predorsal, característica de los bocachicos.""",
	"http://i.imgur.com/lagzgEh.jpg",
	'https://www.wikidatadata.org/wikidata/Q5546624',
	eol['220548'],
	'http://kate-caicedo-r.blogspot.com.co/2013/03/descripcion-especie-ichthyoelephas.html',
	uniprot['1577991'],
	gbif['2352119']
)

fauna(
	rutaMaiz['Fauna.rdf#prochilodusMagdalenae'],
	"BOCACHICO",
	"Prochilodus magdalenae",
	"""Pez migratorio de agua dulce, su tamaño es mediano, los ejemplares más grandes pueden alcanzar 
	los 60 cms de longitud, su boca es pequeña, carnosa y prominente lo cual da origen a su nombre común.""",
	"http://i.imgur.com/HnMP0Yw.jpg",
	dbpedia['Prochilodus_magdalenae'],
	eol['994607'],
	'http://elbochachico.blogspot.com.co/2011/03/caracteristicas.html',
	uniprot['148989'],
	gbif['2352186']
)

fauna(
	rutaMaiz['Fauna.rdf#gallusGallus'],
	"POLLO DE ENGORDE",
	"Gallus gallus",
	"""Tiene una cresta en el píleo y unos lóbulos que cuelgan a ambos lados del pico. Los machos son más grandes, 
	miden aproximadamente 50 cms de altura y llegan a pesar hasta 4 kgs. Las gallinas no suelen medir más de 40 cms de altura 
	y apenas llegan a 2 kg de peso. Poseen una coloración notablemente menos llamativa.""",
	"http://i.imgur.com/4GG3jmG.jpg",
	dbpedia['Red_junglefowl'],
	eol['1049263'],
	'https://es.wikidatapedia.org/wikidata/Gallus_gallus_domesticus',
	uniprot['208526'],
	gbif['5227769']
)

fauna(
	rutaMaiz['Fauna.rdf#gallusDomesticus'],
	"GALLINAS PONEDORAS",
	"Gallus domesticus",
	"""Las gallinas denominadas ponedoras provienen de cruces a tres vías de razas puras (Leghor, Rhode Island, 
	New Hampshire, Ply Mouth rock, Wyandontte y Sussex Armiñada) y más recientemente con razas sintéticas recesivas 
	para obtener pollitos autoxesados.""",
	"http://i.imgur.com/XYrd1QJ.jpg",
	dbpedia.Chicken,
	eol['46340183'],
	'http://www.granjasantaisabel.com/gallinas-ponedoras.php',
	uniprot['9031'],
	gbif['8500968']
)

fauna(
	rutaMaiz['Fauna.rdf#susScrofa'],
	"CERDO",
	"Sus scrofa",
	"""Mamífero que puede encontrarse en estado salvaje o doméstico. Se trata de un cuadrúpedo con patas cortas 
	y pezuñas, un cuerpo pesado, hocico flexible y cola corta.""",
	"http://i.imgur.com/tAAqVR5.jpg",
	dbpedia['Banded_pig'],
	eol['328663'],
	'http://www.dane.gov.co/files/investigaciones/boletines/sacrificio/CP_sacrif_Itrim16.pdf',
	uniprot['9823'],
	gbif['7705930']
)

fauna(
	rutaMaiz['Fauna.rdf#bosTaurus'],
	"VACAS",
	"Bos taurus",
	"""Las vacas pesan más de media tonelada y pueden medir hasta 1.5 ms de altura.
	Se cree que su domesticación comenzó en Medio Oriente hace cerca de 10.000 años.
	La cría y el uso de la vaca forman parte de la ganadería bovina.""",
	"http://i.imgur.com/jisqkqN.jpg",
	dbpedia['Taurine_cattle'],
	eol['328699'],
	'http://animalesexoticosdezumba.blogspot.com.co/2016/05/vacas-de-zumbahua.html',
	uniprot['9913'],
	gbif['2441022']
)

fauna(
	rutaMaiz['Fauna.rdf#capraAegagrusHircus'],
	"CABRA",
	"Capra aegagrus hircus",
	"""La cabra doméstica proviene de la forma salvaje Capra aegragus cretica, originaria de la cuenca mediterránea.
	Las cabras son poco exigentes en su alimentación, pueden comer cualquier materia vegetal: hierba, hojas, brotes. 
	Se pueden levantar sobre las patas traseras para llegar a las hojas o frutos de los árboles.""",
	"http://i.imgur.com/r3z36ib.jpg",
	dbpedia.Goat,
	eol['2870013'],
	'http://www.zoobarcelona.cat/es/conoce-el-zoo/animales-por-categorias/detalle-ficha/animal/cabra-domestica/',
	uniprot['9925'],
	gbif['4409366']
)

fauna(
	rutaMaiz['Fauna.rdf#rhinellaMarina'],
	"SAPO NEOTROPICAL",
	"Rhinella marina",
	"""Es muy grande alcanzando una longitud promedio de 10-15 cms, y en algunos casos mucho más grande. La piel del sapo 
	es seca y verrugosa. Tiene distintas protuberancias que comienzan encima de los ojos y terminan en el hocico. Pueden ser 
	grises, marrones, rojo-marrones u olivas en color, con patrones que varían.""",
	"http://i.imgur.com/p9v212l.jpg",
	dbpedia['Cane_toad'],
	eol['333309'],
	'https://es.wikidatapedia.org/wikidata/Rhinella_marina',
	uniprot['8386'],
	gbif['5216933']
)

fauna(
	rutaMaiz['Fauna.rdf#dendropsophusColumbianus'],
	"RANA COMÚN",
	"Dendropsophus columbianus",
	"""La longitud rostro-cloacal del macho varía entre los 25.8–29.3 mm y en las hembras varía entre
	los 30.6–35.4 mms; hocico corto y redondeado; tímpano visible; piel del dorso de textura granular
	fina y vientre granular; ojos grandes con pupila negra e iris de color bronce a cobre rojizo.""",
	"http://i.imgur.com/0vrePDz.jpg",
	dbpedia['Dendropsophus_columbianus'],
	eol['331568'],
	'http://anfibiosdelvalledelcauca.com/index.php?option=com_k2&view=item&id=94:dendropsophus-columbianus&Itemid=450',
	uniprot['1033692'],
	gbif['2428577']
)

fauna(
	rutaMaiz['Fauna.rdf#leptodactylusFragilis'],
	"RANA DE BIGOTES",
	"Leptodactylus fragilis",
	"""Especie de anfibio anuro de la familia Leptodactylidae.
	Es nativo del sur de Norteamérica, América Central y el norte de América del Sur.""",
	"http://i.imgur.com/MlgLngs.jpg",
	dbpedia['Leptodactylus_fragilis'],
	eol['1038865'],
	'https://es.wikidatapedia.org/wikidata/Leptodactylus_fragilis',
	uniprot['349990'],
	gbif['5217587']
)

fauna(
	rutaMaiz['Fauna.rdf#lithobatesCatesbeianus'],
	"RANA TORO",
	"Lithobates catesbeianus",
	"""Es un anfibio de gran tamaño de entre 10-20 cms de longitud hocico-cloaca y un peso entre 60-900 grs. 
	Sus larvas son excepcionalmente grandes, pudiendo medir entre 15 y 18 cms. Su cabeza es ancha y plana y
	presenta un pliegue de piel a cada lado que corre desde detrás del ojo hasta el tímpano, bordeándolo.""",
	"http://i.imgur.com/inUup4b.jpg",
	dbpedia['American_bullfrog'],
	eol['330963'],
	'http://wikidatafaunia.com/anfibios/rana-toro/',
	uniprot['8400'],
	gbif['2427091']
)

fauna(
	rutaMaiz['Fauna.rdf#chelydraAcutirostris'],
	"TORTUGA MORDEDORA",
	"Chelydra acutirostris",
	"""Pesa de 4.5-16 kgs Su caparazón  mide de 20-47 cms y una cola tan larga como el caparazón. La cola tiene escamas 
	en forma de sierra. La piel es gris bronce con algunas manchas amarillas o blancas.""",
	"http://i.imgur.com/JCOlQxj.jpg",
	dbpedia['South_American_snapping_turtle'],
	eol['1243673'],
	'http://animalesanimdo.blogspot.com.co/2015/12/reptiles-reptiles-ecuador-se-ubica-en.html',
	uniprot['8474'],
	gbif['8330787']
)

fauna(
	rutaMaiz['Fauna.rdf#chelonoidisCarbonaria'],
	"MORROCOY",
	"Chelonoidis carbonaria",
	"""La tortuga Morrocoy es terrestre y vive durante muchos años, puede alcanzar una longitud de hasta 51 cms 
	y su caparazón es alto con forma de cúpula, éste tiene el fondo de color negro y centros de las escamas 
	amarillo-naranjas o naranja-rojizos.""",
	"http://i.imgur.com/u9TOI9Z.jpg",
	dbpedia['Chelonoidis_carbonaria'],
	eol['794307'],
	'http://www.opepa.org/index.php?option=com_content&task=view&id=101&Itemid=29',
	uniprot['50047'],
	gbif['5220282']
)

fauna(
	rutaMaiz['Fauna.rdf#coragypsAtratus'],
	"GALLINAZO",
	"Coragyps atratus",
	"""Mide aproximadamente entre 56 y 66 cms, tiene un peso en la hembra de 1940 grs y en el macho un peso de 1180 grs.
	Es un ave compacta de cola corta cuadrada y de alas anchas.""",
	"http://i.imgur.com/zU1wL0J.jpg",
	dbpedia['Black_vulture'],
	eol['1049011'],
	'http://www.icesi.edu.co/wikidata_aves_colombia/tiki-index.php?page=Gallinazo+Com%C3%BAn',
	uniprot['33614'],
	gbif['2481942']
)

fauna(
	rutaMaiz['Fauna.rdf#liophisLineatus'],
	"GUARDACAMINOS O ESTERILLA",
	"Liophis lineatus",
	"""Especie de serpiente no venenosa e inofensiva. Se caracteriza por tener el dorso amarillo brillante con 
	tres líneas longitudinales negras dorsales: una vertebral ancha y una lateral a cada lado. La cabeza es gris olivácea con 
	línea pre-postocular negra.""",
	"http://i.imgur.com/aaLMr6S.jpg",
	wikidata.Q5074452,
	eol['457860'],
	'http://www.biodiversidad.co/fichas/681',
	uniprot['380619'],
	gbif['8370884']
)

fauna(
	rutaMaiz['Fauna.rdf#mabuyaUnimarginata'],
	"ESQUINCO ESPALDA DORADA",
	"Mabuya unimarginata",
	"""Es un scíncido grande, hasta 75 mms. Esta lagartija tiene cuerpo elongado, cilíndrico y con notoria 
	reducción en el tamaño de los miembros. El cuerpo está cubierto por escamas cicloides brillantes. 
	La coloración dorsal es café bronceado, tiene una franja lateral gris blancuzca que se origina en el hocico.""",
	"http://i.imgur.com/1tSW3yy.jpg",
	wikidata.Q5128682,
	eol['458326'],
	'http://www.sinia.net.ni/multisites/NodoBiodiversidad/images/NodosTematicos/NodoBiodiversidad/Docuementos/Listado%20de%20Reptiles%20de%20Nicaragua.pdf',
	uniprot['155309'],
	gbif['5960492']
)

fauna(
	rutaMaiz['Fauna.rdf#sciurusGranatensis'],
	"ARDILLA",
	"Sciurus granatensis",
	"""Las hembras adultas pesan aproximadamente 465grs, durante la temporada lluviosa 
	el color del pelaje es rojizo mientras que en tiempo seco cambia a un color más anaranjado, presentan el dorso 
	color ocre y el vientre varía de blanco a anaranjado. La cola es ocre con salpicaduras de negro.""",
	"http://i.imgur.com/oJFUM1y.jpg",
	dbpedia['Sciurus_granatensis'],
	eol['313735'],
	'http://ortizcamachoandrea.blogspot.com.co/2011/11/ardilla-sciurus-granatensis.html',
	uniprot['226870'],
	gbif['5219666']
)

fauna(
	rutaMaiz['Fauna.rdf#hypsiboasPugnax'],
	"RANA PLATANERA",
	"Hypsiboas pugnax",
	"""Es una especie de anfibio de la familia Hylidae. Habita en gran parte de nuestro territorio, encontrándose 
	en los bosques, fincas, a la orilla de riachuelos, cultivos y hasta en los jardines de nuestras casas, 
	sin olvidar por supuesto los platanales.""",
	"http://i.imgur.com/Zc9L5br.jpg",
	wikidata.Q4672609,
	eol['1019101'],
	'http://periodicolalenguadominicana.blogspot.com.co/2015/08/la-rana-platanera.html',
	uniprot['1494916'],
	gbif['2428832']
)

fauna(
	rutaMaiz['Fauna.rdf#iguanaIguana'],
	"IGUANA",
	"Iguana iguana",
	"""Puede medir de 1.5-2 ms. El color verde de su piel le permite confundirse perfectamente con la vegetación.
	Su piel está recubierta de pequeñas escamas; tiene una cresta dorsal que recorre desde la cabeza 
	hasta la cola. Patas muy cortas y cinco dedos en cada pata, acabados en garras muy afiladas. Cola larga.""",
	"http://i.imgur.com/0hpaKMx.jpg",
	dbpedia['Iguana_iguana'],
	eol['793235'],
	'https://es.wikidatapedia.org/wikidata/Iguana_iguana',
	uniprot['8517'],
	gbif['2459658']
)

fauna(
	rutaMaiz['Fauna.rdf#leptodactylusInsularum'],
	"RANA SAPO BOLIVIANO",
	"Leptodactylus insularum",
	"""El macho es un poco más pequeño que la hembra y es de al menos 10 cms del hocico a la cloaca y la hembra hasta 12. 
	El dorso es de color marrón oscuro con manchas marrones grandes. Una franja blanca está presente a lo 
	largo del labio superior. La superficie ventral es de color blanco a crema.""",
	"http://i.imgur.com/CnxC1e0.jpg",
	dbpedia['Leptodactylus_insularum'],
	eol['8819757'],
	'http://panamasilvestre.blogspot.com.co/2013/05/leptodactylus-insularum-leptodactylidae.html',
	uniprot['326190'],
	gbif['5217608']
)

fauna(
	rutaMaiz['Fauna.rdf#drymarchonMelanurus'],
	"CAZADORA RABO NEGRO",
	"Drymarchon melanurus",
	"""Especie de serpiente colubridae no venenosa. Puede tener una longitud de 180-240 cms. Tiene escamas suaves 
	predominantemente de color marrón claro, volviéndose negro hacia la cola. La parte inferior es a menudo de color 
	más claro.""",
	"http://i.imgur.com/kzLgBeT.jpg",
	dbpedia['Drymarchon_melanurus'],
	eol['790030'],
	'https://es.wikidatapedia.org/wikidata/Drymarchon_melanurus',
	uniprot['1396887'],
	gbif['2452321']
)

fauna(
	rutaMaiz['Fauna.rdf#hemidactylusFrenatus'],
	"GECKO CASERO COMÚN",
	"Hemidactylus frenatus",
	"""La cola es ligeramente más larga que la longitud hocico cloaca. La cabeza, garganta y cuerpo se encuentran 
	cubiertos por pequeñas escamas granulares. La coloración dorsal y ventral es blanco amarillento. No crece más de 6-15 cms, 
	y vive cinco años.""",
	"http://i.imgur.com/qJ5aRSn.jpg",
	dbpedia['Hemidactylus_frenatus'],
	eol['793350'],
	'http://bios.conabio.gob.mx/especies/8000523.pdf',
	uniprot['47729'],
	gbif['5959976']
)

#print (g.serialize(format="pretty-xml")) 

