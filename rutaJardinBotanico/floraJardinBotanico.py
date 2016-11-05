#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import WILDLIFE, CRUZAR, UMBEL, OWL
from utils.namespaces import rutaJardin, dbpedia, wikidata, imgur, eol, gbif, uniprot
from alojamientosJardinBotanico import g

#g = Graph()

def flora(uri, nombre_comun, nombre_cientifico, descripcion, imagen, uriLink1, uriLink2, ref, uriLink3):
    g.add( (URIRef(uri), RDF.type, WILDLIFE.TaxonName) )
    g.add( (URIRef(uri), WILDLIFE.commonName, Literal(nombre_comun, lang="es") ) )
    g.add( (URIRef(uri), WILDLIFE.scientificName, Literal(nombre_cientifico, lang="la")) )
    g.add( (URIRef(uri), WILDLIFE.shortDescription, Literal(descripcion, lang="es")) )
    g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)))
    g.add( (URIRef(uri), WILDLIFE.kingdomName, Literal('Vegetal', lang="es")) )
    
    g.add( (URIRef(uri), FOAF.isPrimaryTopicOf, URIRef(ref)) ) #Sitio web del que se tomo la desc
    g.add( (URIRef(uri), OWL.sameAs, URIRef(uriLink1)) ) #Link RDF a DBpedia
    g.add( (URIRef(uri), OWL.sameAs, URIRef(uriLink2)) ) #Link RDF a EOL
    g.add( (URIRef(uri), OWL.sameAs, URIRef(uriLink3)) ) #Link RDF a UniProt
    
    g.add( (URIRef(uri), UMBEL.isRelatedTo, rutaJardin.Flora) )

flora(
	gbif['4185119'],
	'ANICILLO',
	'Piper anisatum',
	"""Arbusto pequeño de 1-4 m de alto. Con aroma a anís, tallos verde pálidos a amarillento.
	Hojas acorazonadas, de color verde pálido y color verde oscuro cuando secas de consistencia fuerte.""",
	imgur['AKS0cjO.jpg'],
	dbpedia['Piper_marginatum'],
	eol['5480783'],
	'http://cecalli85.blogspot.com.co/2013/10/anicillo.html',
	uniprot['13215']
)

flora(
	gbif['2873486'],
	'ANTURIO BLANCO',
	'Anthurium nymphaeifolium',
	"""Tiene hojas de forma oval acorazonada, de punta acuminada; presentan lóbulos anteriores redondos, apartados por un 
	angosto recorte basal. Tiene una espata verdosa, de forma ovalada que remata en una punta larga y angosta. Es una especie 
	ornamental, sus raíces largas y finas se han empleado como cuerdas de guitarra.""",
	imgur['MSqrylr.jpg'],
	wikidata['Q15319886'],
	eol['1140350'],
	'http://www.biodiversidad.co/fichas/2011',
	uniprot['78377']
)

flora(
	gbif['3173930'],
	'ARRAYÁN COLORADO',
	'Myrcia popayanensis',
	"""Árbol con una altura promedio de 18 ms, con ramificación abundante, copa redonda de mediana amplitud y profundidad.
	Madera de color crema rojizo, brillo mediano y olor aromático.""",
	imgur['h4ZhXxd.jpg'],
	dbpedia.Anthurium,
	eol['5458716'],
	'http://www.uco.edu.co/floraorienteantioquia/myrtaceae/Myrcia-popayanensis-Hieron/Paginas/default.aspx',
	uniprot['375249']
)

flora(
	gbif['7557158'],
	'BIHAO',
	'Calathea lutea',
	"""Mide 2 ms de altura, tallo subterráneo y alargado que corre paralelo al suelo. Las hojas son simples, congregadas 
	en la base de la planta. Las flores poseen forma de trompeta. El cáliz es blanco y tiene tres sépalos. Los frutos son 
	secos, presentan forma de pera, miden 1.2 cms de largo y contienen pocas semillas.""",
	imgur['WEWw56T.jpg'],
	wikidata['Q15323512'],
	eol['1125291'],
	'http://www.biodiversidad.co/fichas/1017',
	uniprot['671254']
)

flora(
	gbif['3190500'],
	'CEDRO MACHO',
	'Guarea guidonia',
	"""Árbol que presenta una altura entre 25-30 ms. Las hojas son de gran tamaño, de 20-60 cms de largo y se 
	encuentran dispuestas de manera alterna, tiene entre 8 y 20 hojas de color verde oscuro por rama. La corteza es 
	áspera, con muchas fisuras longitudinales y de color pardo, con un evidente matiz rojizo.""",
	imgur['EPWPLRN.jpg'],
	dbpedia.Guarea,
	eol['39955695'],
	'http://www.biodiversidad.co/fichas/669',
	uniprot['155637']
)

flora(
	gbif['1550331'],
	'CUCHARO',
	'Clusia sp.',
	"""Mide de 5-18 cms de altura;  copa irregular, densa, globosa o semiglobosa. Se propaga por semillas y por estacas. 
	Los frutos se recolectan cuando toman un color verde amarillento, generalmente a mediados y finales de cada año. Corteza 
	gris con nudosidades, raíces poco profundas y a veces se presentan raíces aéreas.""",
	imgur['hUG5ltd.jpg'],
	dbpedia.Clusia,
	eol['61964'],
	'http://biodiversidad.co/fichas/3598',
	uniprot['574057']
)

flora(
	gbif['7868895'],
	'CUERNO VENADO',
	'Xylosma prunifolia',
	"""El tronco es ramificado desde la base, mide 1 m de alto y su corteza es fisurada y con espinas. Las hojas son 
	elípticas; las flores son pequeñas de color amarillo cremoso. Los frutos inicialmente son amarillos verdosos luego son 
	rojizos y negro purpúreo.""",
	imgur['jAdLvLN.jpg'],
	'www.biolib.cz/cz/taxon/id1135636/',
	eol['5731214'],
	'http://www.biodiversidad.co/fichas/154',
	uniprot['179718']
)

flora(
	gbif['3833224'],
	'DONCEL',
	'Zanthoxylum verrucosum',
	"""Árbol con espinas cónicas gruesas en los trocos y ramas delgadas en las partes terminales y hojas; pinnas de margen 
	aserrada y muy fragrantes. Se encuentra en los bosques secundarios de Colombia y Ecuador.""",
	imgur['PDNWAAp.jpg'],
	dbpedia.Zanthoxylum,
	eol['5304516'],
	'http://www.biodiversidad.co/fichas/3792',
	uniprot['67937']
)

flora(
	gbif['3172524'],
	'GUAYACÁN AMARILLO',
	'Tabebuia chrysantha',
	"""Alcanza unos 35 ms de alto, tiene pocas ramas aunque son gruesas y ascendentes. En Colombia está presente en los
	departamentos de Amazonas, Bolívar, Cesar, Chocó, Córdoba, Guaviare, Magdalena y Tolima.""",
	imgur['NY4l9eB.jpg'],
	dbpedia['Tabebuia_chrysantha'],
	eol['392765'],
	'http://www.biodiversidad.co/fichas/395',
	uniprot['429696']
)

flora(
	gbif['2860922'],
	'IRACA',
	'Carludovica palmata',
	"""Es parecida a una plama, con sus hojas en forma de abanico. Las flores de color rosado claro y miden entre 15 y 20 cms
	Los frutos constituyen una masa que al madurar se vuelve de color rojizo, por dentro son carnosos.""",
	imgur['OpMLCpE.jpg'],
	dbpedia['Carludovica_palmata'],
	eol['1086682'],
	'http://www.biodiversidad.co/fichas/915',
	uniprot['108411']
)

flora(
	gbif['2895593'],
	'JAGUA',
	'Genipa americana',
	"""Puede alcanzar de 15-20 ms de altura y hasta 60 cms de diámetro. Sus frutos son bayas, toscos al tacto y con un aroma penetrante. 
	Se desarrolla bien en potreros y áreas de cultivo. Pero el mejor habitat para este arbusto es el suelo arcilloso.""",
	imgur['ZSkBpAq.jpg'],
	dbpedia['Genipa_americana'],
	eol['1096067'],
	'http://www.biodiversidad.co/fichas/364',
	uniprot['58486']
)

flora(
	gbif['3033980'],
	'JIGUA',
	'Cinnamomum sp.',
	"""La planta alcanza hasta de 15 ms de altura, su ramaje está recubierto de una corteza de color amarillo. Las flores son blancas
	amarillosas y están puestas en racimos terminales. El fruto es una baya de color azul.""",
	imgur['UhZi2ZU.jpg'],
	dbpedia['Cinnamomum_verum'],
	eol['1096067'],
	'http://www.biodiversidad.co/fichas/1004',
	uniprot['13428']
)

flora(
	gbif['2732482'],
	'PALMICHA',
	'Sabal mauritiiformis',
	"""Es una palma solitaria y sin espinas que alcanza 20 ms de altura, en su estado juvenil es de color verde, sus flores son 
	de color verde amarillento o blancuzco en algunos casos; requiere de sombra en su estado juvenil y al madurar, abundante luz 
	solar.""",
	imgur['trwCYPv.jpg'],
	dbpedia['Sabal_mauritiiformis'],
	eol['1131511'],
	'http://www.biodiversidad.co/fichas/1097',
	uniprot['115516']
)

flora(
	gbif['2760940'],
	'PLATANILLO',
	'Heliconia latispatha',
	"""La planta completa mide alrededor de 1.5-2.5 cms de altura, Las hojas son simples, envainadoras hacia la base. La flor es 
	tubular y mide entre 35-40 mms de largo, con tres sépalos y tres pétalos fusionados, sin pelos y amarilla o anaranjada 
	con márgenes verdes.""",
	imgur['uzHIEPB.jpg'],
	dbpedia['Heliconia_latispatha'],
	eol['1118007'],
	'http://www.biodiversidad.co/fichas/656',
	uniprot['4654']
)

flora(
	gbif['2760865'],
	'PLATANILLO',
	'Heliconia platystachys',
	"""Es una planta de uso ornamental, como flor de corte y empleada para la decoración de jardines o en macetas. Se encuentra 
	en Costa Rica, Panamá y Venezuela. En Colombia está presente en todas las regiones bajas, excepto en la planicie amazónica 
	y en la Orinoquía. """,
	imgur['gD6Tlvd.jpg'],
	wikidata['Q15331224'],
	eol['1117955'],
	'http://www.biodiversidad.co/fichas/984',
	uniprot['4653']
)

flora(
	gbif['2760967'],
	'PLATANILLO',
	'Heliconia rostrata',
	"""Alcanza entre 3-6 ms de altura. Tiene espatas rojas con márgenes y ápices amarillo-verdosos. Flores blancas hacia la 
	base y amarillo-verdosas hacia el ápice, glabras y rectas. Es una planta con uso ornamental, como flor de corte y empleada 
	para la decoración.""",
	imgur['5UfQkpf.jpg'],
	dbpedia['Heliconia_rostrata'],
	eol['46322480'],
	'http://www.biodiversidad.co/fichas/989',
	uniprot['96511']
)

flora(
	gbif['2760619'],
	'PLATANILLO',
	'Heliconia wagneriana',
	"""Se localiza con frecuencia en el sector occidental de la planicie amazónica, la Serranía de la Macarena y
	la vertiente oriental andina. Llega a medir de 3-6 ms de altura.""",
	imgur['a50fa9j.jpg'],
	wikidata['Q311933'],
	eol['1117892'],
	'http://www.biodiversidad.co/fichas/994',
	uniprot['796950']
)

flora(
	gbif['5293840'],
	'SANCONA',
	'Syagrus sancona',
	"""Es una plama que crece hasta 30 ms de alto y de 25-30 cms de diámetro, crece en zonas de bosque seco y
	de bosque húmedo tropical. Está distribuida en toda la región andina y en algunas aledañas.""",
	imgur['rbMDbe3.jpg'],
	wikidata['Q6136704'],
	eol['1129522'],
	'http://www.biodiversidad.co/fichas/1098',
	uniprot['682629']
)

flora(
	gbif['5354954'],
	'SIETE CUEROS',
	'Machaerium capote',
	"""Puede alcanzar los 20 ms de altura y 1 m de diámetro en su tronco, produce latex de color rojizo. Requiere de abundante 
	luz y su crecimiento es lento, además de Marzo a Abril produce frutos. Se encuentra en Colombia, Ecuador y Panamá.""",
	imgur['FAA0s4V.jpg'],
	wikidata['Q15455303'],
	eol['638530'],
	'http://catalogofloravalleaburra.eia.edu.co/familias/1/especies/148',
	uniprot['377526']
)

flora(
	gbif['3752400'],
	'TOTOCAL',
	'Achatocarpus nigricans',
	"""Puede alcanzar los 12 ms de altura y los 20 cms de diámetro, sus ramas tienen espinas y es de color verdoso, sus hojas 
	miden 10 cms de largo por 4.5 cms de ancho y sus frutos son bayas con forma de globo, carnosos y posen de una dos semillas.""",
	imgur['ngqQnc8.jpg'],
	wikidata['Q14830734'],
	eol['5164510'],
	'http://www.biodiversidad.co/fichas/3771',
	uniprot['169195']
)

flora(
	gbif['2925303'],
	'VENTUROSA',
	'Lantana camara',
	"""Arbusto de 1-3 ms de altura con flores de color amarillo, anaranjadas o rojas. Sus frutos son carnosos, redondos de 
	color azul a negro brillante. Se usa medicinalmente ya que el zumo de sus hojas con algunas gotas de limón puede curar 
	el vómito.""",
	imgur['Z0E5BdL.jpg'],
	dbpedia['Lantana_camara'],
	eol['579775'],
	'http://www.biodiversidad.co/fichas/3563',
	uniprot['126435']
)


flora(
	gbif['2970419'],
	'LEUCAENA',
	'Leucaena glauca',
	"""Árbol de 3-15 ms de altura y 10-35 cms de diámetro. La corteza es gris a marrón con fisuras superficiales verticales 
	de color naranja a marrón. Es una especie que se adapta a una gran variedad de suelos siempre y cuando estén bien drenados 
	y no tengan un nivel de acidez exagerado. Es nativa de México.""",
	imgur['NdKc3qr.jpg'],
	dbpedia['Leucaena_leucocephala'],
	eol['46244235'],
	'http://www.biodiversidad.co/fichas/5365',
	uniprot['3866']
)

flora(
	gbif['8042591'],
	'GUAIMARO',
	'Brosimum utile',
	"""El árbol puede medir de 35-40 ms de altura y 75-150 cms de diámetro, segrega un látex cremoso blanquecino, abundante y 
	pegajoso. Produce flores de color blanco y algunos frutos pequeños.""",
	imgur['XJDondS.jpg'],
	wikidata['Q2713013'],
	eol['491545'],
	'http://www.biodiversidad.co/fichas/351',
	uniprot['241871']
)


flora(
	gbif['2760614'],
	'PLATANILLO',
	'Heliconia combinata',
	"""Es una especie endémica de las vertientes Occidental y Andina en Colombia. Presente en los departamentos de 
	Antioquia, Risaralda, Chocó y Valle del Cauca; puede llegar a medir de 4-7 ms de altura, produce flores de color amarillo.""",
	imgur['zjeNZ2i.jpg'],
	wikidata['Q15330199'],
	eol['1118052'],
	'http://www.biodiversidad.co/fichas/956',
	uniprot['4653']
)

flora(
	gbif['2760555'],
	'PLATANILLO',
	'Heliconia cordata',
	"""Se encuentra en el valle medio del río Magdalena, en el macizo antioqueño y en las vertientes occidental andina y 
	magdalenense. Produce flores verdes o blancas hacia la base y verdes hacia el ápice.""",
	imgur['mBGY8Jr.jpg'],
	wikidata['Q15330315'],
	eol['1118051'],
	'http://www.biodiversidad.co/fichas/963',
	uniprot['4653']
)

flora(
	gbif['2760973'],
	'PLATANILLO',
	'Heliconia episcopalis',
	"""Puede llegar a medir de 2-4 ms de altura con flores blancas hacia la base, amarillas a verdes o anaranjadas hacia 
	el ápice, está distribuida ampliamente en Ecuador, Perú, Surinam y Venezuela. En Colombia se encuentra en la llanura del 
	Caribe, valle medio del río Magdalena, Amazonia y Orinoquía. """,
	imgur['gWPoBBU.jpg'],
	dbpedia['Heliconia_episcopalis'],
	eol['1118040'],
	'https://www.celec.gob.ec/hidronacion/images/stories/pdf/manual-de-flora.pdf',
	uniprot['4653']
)

flora(
	gbif['2760668'],
	'PLATANILLO',
	'Heliconia huilensis',
	"""Puede llegar a medir hasta 4.5 ms de altura, posee flores amarillas y parabólicas. Es una especie endémica de la 
	vertiente magdalenense y del Macizo Colombiano (Cundinamarca y Huila); se encuentra en peligro crítico.""",
	imgur['LiBgkDl.jpg'],
	wikidata['Q15330243'],
	eol['1118020'],
	'http://www.biodiversidad.co/fichas/972',
	uniprot['4653']
)

flora(
	gbif['2760859'],
	'PLATANILLO',
	'Heliconia intermedia',
	"""Puede llegar a medir hasta 3.5 ms de altura, es endémica de la vertiente occidental andina de Colombia (Valle del Cauca 
	y Chocó). Posee flores blancas hacia la base y amarillas hacia el ápice.""",
	imgur['Lf3s4Gd.jpg'],
	wikidata['Q15330807'],
	eol['1118015'],
	'http://www.biovirtual.unal.edu.co/ICN/?controlador=ShowObject&accion=show&id=200242',
	uniprot['4653']
)

flora(
	gbif['2760810'],
	'PLATANILLA',
	'Heliconia mariae',
	"""Puede llegar a medir de 4-7.5 ms de altura, tiene una vida larga. Se usa para la decoración de jardínes o macetas y 
	se puede encuentrar en Belice, Costa Rica, Guatemala, Honduras, Nicaragua, Panamá y Venezuela. En Colombia está presente 
	en el valle del río Atrato y la planicie del Caribe.""",
	imgur['rpgKTTD.jpg'],
	wikidata['Q15329752'],
	eol['1117987'],
	'http://www.biodiversidad.co/fichas/977',
	uniprot['1274808']
)

flora(
	gbif['2760732'],
	'PLATANILLO',
	'Heliconia venusta',
	"""Llega a medir de 2-3 ms de altura, con flores amarillas, verdes hacia el ápice. Se usa mayormente para fines 
	ornamentales y de decoración de jardínes. Se distribuye ampliamente en la región Andina, en las vertientes caucana, 
	del magadalena y occidental andina y en el peniplano de Popayán.""",
	imgur['5U3hoix.jpg'],
	'http://www.biodiversidad.co/fichas/993',
	eol['1117895'],
	'http://www.biodiversidad.co/fichas/993',
	uniprot['4653']
)

flora(
	gbif['2760557'],
	'PLATANILLO',
	'Heliconia mutisiana',
	"""Puede tener una altura de 2.5-4 ms con flores amarillas y parabólicas, es una especie nativa de Colombia según el 
	Jardín Botánico del Quindío, se la puede encontrar en las vertientes andinas que miran hacia los valles de los ríos 
	Cauca y Magdalena.""",
	imgur['j03E84S.jpg'],
	wikidata['Q15330572'],
	eol['1117978'],
	'http://www.biodiversidad.co/fichas/980',
	uniprot['4653']
)

flora(
	gbif['7770329'],
	'HELICONIA',
	'Heliconia orthotricha',
	"""Se halla en Ecuador y Perú, llega a medir de 2.5-3.5 ms de altura. Flores blancas a crema hacia la base y verdes hacia 
	el ápice. Esta planta es usada como flor de corte, y también para la decoración de jardines y macetas. En Colombia 
	está presente en la vertiente oriental andina y en la planicie amazónica.""",
	imgur['NBz56ct.jpg'],
	dbpedia['Heliconia'],
	eol['5983668'],
	'http://www.biodiversidad.co/fichas/982',
	uniprot['1170574']
)

flora(
	gbif['2760669'],
	'PLATANILLO',
	'Heliconia psittacorum',
	"""Puede llegar a medir de 0.5-1.5 ms de altura, sus flores son anaranjadas, rojas o amarillas. En Colombia se encuentra 
	en los Llanos Orientales y en las serranías dispersas de Arauca, Casanare, Meta y Vichada, en algunas localidades de la 
	selva amazónica (Guaviare) y en la vertiente oriental andina.""",
	imgur['sB1RGFR.jpg'],
	dbpedia['Heliconia_psittacorum'],
	eol['1117951'],
	'http://www.biodiversidad.co/fichas/986',
	uniprot['574477']
)

flora(
	gbif['2760548'],
	'PLATANILLO',
	'Heliconia stricta',
	"""Mide entre 1,5-3 ms de altura, las hojas son simples y envainadoras hacia la base. Las flores se encuentran agrupadas, 
	miden entre 30-45 cms de largo y 15-25 cms de diámetro, de color verde hacia el ápice y la punta es blanca.""",
	imgur['PHAYprq.jpg'],
	dbpedia['Heliconia_stricta'],
	eol['1117915'],
	'http://www.biodiversidad.co/fichas/657',
	uniprot['648044']
)

flora(
	gbif['2739162'],
	'COROZO GRANDE',
	'Acrocomia sclerocarpa',
	"""Palma solitaria que alcanza los 11 ms de altura. Su tallo mide hasta 30 cms de diámetro, es de color gris y está 
	cubierto de espinas negras dispuestas en filas horizontales. Se encuentra desde México y las Antillas hasta Bolivia, 
	Argentina y Paraguay.""",
	imgur['CkB8hMl.jpg'],
	dbpedia['Acrocomia_aculeata'],
	eol['245325'],
	'http://www.biodiversidad.co/fichas/1279',
	uniprot['169986']
)

flora(
	gbif['2738657'],
	'COROZO',
	'Aiphanes caryotifolia',
	"""El tronco de esta palma alcanza entre 5-10 ms de alto y entre 15-20 cms de diámetro, y está densamente cubierto por 
	espinas negras. Es medicinal pues se emplea como en los niños para tratar retorcijones, flatulencia y cólicos.""",
	imgur['TWWaeyu.jpg'],
	dbpedia['Aiphanes_horrida'],
	eol['1092416'],
	'http://www.biodiversidad.co/fichas/1281',
	uniprot['131248']
)

flora(
	gbif['2738064'],
	'CHAMBIRA',
	'Astrocaryum chambira',
	"""Palma solitaria, puede llegar a medir 3.5-22 ms de altura y 19-35 cms de diámetro, cubierto con espinas planas 
	negras, produce frutos de color verde o  amarillo verdoso cuando están maduros, tiene una amplia distribución en el oeste 
	de la Amazonía.""",
	imgur['wQvNiw2.jpg'],
	dbpedia['Astrocaryum_chambira'],
	eol['1132070'],
	'http://www.biodiversidad.co/fichas/349',
	uniprot['446105']
)

flora(
	gbif['2738128'],
	'GUERREGUE',
	'Astrocaryum malybo',
	"""Es una palma solitaria y espinosa. Sus hojas crecen unos 5 ms de largo. Está en peligro a nivel global; 
	sus hojas se usan como fuente de fibras para la elaboración de esteras y de una amplia gama de artesanías""",
	imgur['f4pzDA8.jpg'],
	wikidata['Q15457764'],
	eol['1132055'],
	'http://www.biodiversidad.co/fichas/1715',
	uniprot['996934']
)

flora(
	gbif['2738130'],
	'CHUNGA',
	'Astrocaryum standleyanum',
	"""Palma alta y robusta que alcanza alturas hasta de 22 ms con una tallo erguido de 16-22 cms de diámetro,
	con abundantes espinas largas de color negro. Presenta de 11 a 18 hojas grandes hasta de 4 ms de largo.""",
	imgur['m0s4dFo.jpg'],
	dbpedia['Astrocaryum_standleyanum'],
	eol['1132045'],
	'http://www.biodiversidad.co/fichas/316',
	uniprot['446115']
)

flora(
	gbif['2732721'],
	'PALMA DE CUESCO',
	'Attalea butyracea',
	"""Es una palma de crecimiento lento que tarda entre 4 y 6 meses en germinar, puede alcanzar hasta 20 ms de altura 
	y 45 cms de diámetro en su tronco. Se puede encontrar desde México hasta Bolivia. """,
	imgur['2EdeO1o.jpg'],
	dbpedia['Attalea_osmantha'],
	eol['1131741'],
	'http://www.biodiversidad.co/fichas/1084',
	uniprot['169997']
)

flora(
	gbif['2732754'],
	'TÁPARO',
	'Attalea allenii',
	"""Palma solitaria, se cree que tiene una longevidad entre 65 y 102 años. Sus semillas son comestibles, tienen un 
	sabor similar al coco y son comercializadas a nivel local en los Andes antioqueños. """,
	imgur['e0tHbON.jpg'],
	wikidata['Q5711222'],
	eol['1131911'],
	'http://biodiversidad.co/fichas/1083',
	uniprot['115445']
)

flora(
	gbif['2732819'],
	'ALMENDRÓN',
	'Attalea nucifera',
	"""Palma de tallo subterráneo y grandes hojas de hasta 8 ms de largo, sus frutos miden de 5-7 cms de largo y son de 
	color café, de sabor parecido al coco. Es exclusiva de los bosques húmedos del Magdalena medio en Colombia y se 
	encuentra en peligro de extinción por la destrucción de su hábitat.""",
	imgur['qxni3iT.jpg'],
	wikidata['Q15457188'],
	eol['1131736'],
	'https://en.wikipedia.org/wiki/Attalea_(palm)',
	uniprot['115444']
)

flora(
	gbif['2733060'],
	'CHONTADURO',
	'Bactris gasipaes',
	"""El tallo alcanza aproximadamente 20 ms y un diámetro entre 15-30 cms. Su fruto es de color
	verde cuando está inmaduro, rojos o anaranjados cuando está maduro; es comestible al igual que la pulpa, la semilla 
	y los tallos.""",
	imgur['FnkMwjx.jpg'],
	dbpedia['Bactris_gasipaes'],
	eol['1130861'],
	'http://www.biodiversidad.co/fichas/312',
	uniprot['154467']
)

flora(
	gbif['2735560'],
	'PALMERA DE LORD BENTICK',
	'Bentinckia nicobarica',
	"""Se encuentra en el borde oriental de la Bahía de Bengala, en la isla de Nicobar. Es originaria del continente 
	asiático. Es una palma solitaria; los tallos son usados por las población local para la construccion de casas y cercas.""",
	imgur['200mfte.jpg'],
	dbpedia['Bentinckia_nicobarica'],
	eol['1128728'],
	'https://en.wikipedia.org/wiki/Bentinckia_nicobarica',
	uniprot['145673']
)

flora(
	gbif['2738902'],
	'COLA DE PESCADO',
	'Caryota mitis',
	"""Esta palma presenta tallos agrupados de hasta 15 cms de diámetro. Sus hojas miden de 2-3 ms de largo. Es una 
	especie ornamental y se puede encontrar en ambientes húmedos y suelos orgánicos.""",
	imgur['5gLq21x.jpg'],
	dbpedia['Caryota_mitis'],
	eol['1090464'],
	'http://www.biodiversidad.co/fichas/1291',
	uniprot['4714']
)

flora(
	gbif['2735935'],
	'PALMA ARECA',
	'Dypsis lutescens',
	"""Esta palma tiene un tallo cilíndrico de color gris, que alcanza los 5 ms de altura y los 15 cms de diámetro. Su 
	fruto es una baya de color amarillo oscuro a negro que mide hasta 1,5 cms de largo. Además sirve de alimento para la 
	avifauna y para la apicultura ya que es una especie melífera.""",
	imgur['mXJPnm1.jpg'],
	dbpedia['Dypsis_lutescens'],
	eol['1095187'],
	'http://www.biodiversidad.co/fichas/1297',
	uniprot['131267']
)

flora(
	gbif['3593724'],
	'PALMA DE MADAGASCAR',
	'Dypsis madagascariensis',
	"""Es una especie útil en la decoración de interiores. Puede medir de 7-8 ms de altura y 25 cms de grosor, con 
	el tronco liso y anillado, la hoja de esta especie tiene un aspecto plumoso. Se multiplica por semillas que tardan 
	casi 2 meses en germinar. Requiere buen suelo y humedad.""",
	imgur['pe9C4rl.jpg'],
	dbpedia['Dypsis_madagascariensis'],
	eol['5750674'],
	'http://www.biodiversidad.co/fichas/1298',
	uniprot['131266']
)

flora(
	gbif['5293281'],
	'PALMA DE CEILÁN',
	'Corypha umbraculifera',
	"""Es una especie endémica de la India, aunque también se puede encontrar en Sri Lanka, Tailandia y China. Fue 
	llevada a Surinam por inmigrantes del este de India. Es una de las palmas más grandes del mundo ya que pueden 
	alcanzar los 34 ms de altura con un tronco de 1.4 ms de diámetro.""",
	imgur['Ba9bJSi.jpg'],
	dbpedia['Corypha_umbraculifera'],
	eol['1092230'],
	'https://en.wikipedia.org/wiki/Corypha_umbraculifera',
	uniprot['115461']
)

flora(
	gbif['2731882'],
	'PALMA ACEITERA',
	'Elaeis guineensis',
	"""Es una especie nativa del continente africano, que se caracteriza por su grueso tronco cubierto con fragmentos de las 
	hojas ya caídas y por sus grandes racimos de frutos que presentan alto contenido de aceite. Es una palma de rápido 
	crecimiento con alta variabilidad genética, alto potencial reproductivo y larga expectativa de vida.""",
	imgur['DAOyYW7.jpg'],
	dbpedia['Elaeis_guineensis'],
	eol['1095470'],
	'http://www.biodiversidad.co/fichas/5346',
	uniprot['51953']
)

flora(
	gbif['2731920'],
	'PALMA NOLÍ',
	'Elaeis oleifera',
	"""Es una palma de tallo solitario que llega hasta los 3 ms de altura, se puede encontrar desde Nicaragua hasta el 
	noroccidente de Colombia, aunque tambien exiten ejemplares en menor medida en Surinam, Guayana Francesa,
	Perú, Ecuador y Brasil.""",
	imgur['ZiYbeZn.jpg'],
	dbpedia['Elaeis_oleifera'],
	eol['1098598'],
	'http://www.biodiversidad.co/fichas/1093',
	uniprot['80265']
)

flora(
	gbif['2739059'],
	'BOMBONA',
	'Iriartea deltoidea',
	"""Se encuentra en bosques primarios y bosques ribereños, puede alcanzar los 30 ms de altura y hasta 30 cms de diámetro, 
	tiene frutos de 2-3 cms de diámetro de color café amarillento al madurar, cáscara lisa, brillante y quebradiza.""",
	imgur['muCniYZ.jpg'],
	dbpedia.Iriartea,
	eol['1142669'],
	'http://www.biodiversidad.co/fichas/372',
	uniprot['101627']
)

flora(
	gbif['8286174'],
	'LICUALA DE MANGLAR',
	'Licuala spinosa',
	"""Es nativa de Indonesia, Filipinas, Península Malaya y Thailandia. Es una palma hermafrodita, sus troncos generalmente 
	forman grupos, cada uno de 3-4 ms de altura y 4-8 cm de grosor. Sus Frutos son esféricos u ovados y miden de 9-10 mms
	de longitud y son de color rojizo. Tolera suelos arenosos y sol o media sombra y necesita riegos abundantes.""",
	imgur['Iwvsknh.jpg'],
	dbpedia['Licuala_spinosa'],
	eol['1140901'],
	'https://en.wikipedia.org/wiki/Licuala_spinosa',
	uniprot['745111']
)

flora(
	gbif['5294777'],
	'PALMA DE MORICHE',
	'Mauritia flexuosa',
	"""Se encuentra en terrazas bajas, sobre terrenos inundados temporal o permanentemente, con drenaje muy deficiente. 
	Fruto de 7 cms de largo y 5 cms de diámetro, rojo-anaranjado oscuro a café-rojizo. Es muy rico en vitamina A, 
	se consume fresco o en bebidas, paletas o refrescos.""",
	imgur['kPcLY4D.jpg'],
	dbpedia['Mauritia_flexuosa'],
	eol['1138930'],
	'http://www.biodiversidad.co/fichas/383',
	uniprot['93293']
)

flora(
	gbif['2735462'],
	'PALMA BATAUA',
	'Oenocarpus bataua',
	"""Palma solitaria, llega a medir de 4-26 ms de alto y de 15-45 cms de diámetro. Se encuentra principalmente en zonas 
	húmedas pantanosas con inundaciones periódicas, el fruto es de color violáceo, pero negro cuando madura, este mide 
	de 2.5-4.5 cms de longitud y de 2-3 cms de diámetro.""",
	imgur['Sn2doC9.jpg'],
	dbpedia['Oenocarpus_bataua'],
	eol['1136856'],
	'http://www.biodiversidad.co/fichas/389',
	uniprot['169985']
)

flora(
	gbif['6109699'],
	'PALMA DÁTIL',
	'Phoenix dactylifera',
	"""Esta palma solitaria alcanza 30 ms de altura o más. Sus raíces son visibles en la base. Sus frutos de forma 
	cilíndrica miden hasta 5 x 1,5 cms son de color café amarillento a café rojizo, son comestibles y carnosos. Sus hojas 
	son útiles para la elaboración de una gran variedad de artículos como abanicos, recipientes y esteras. """,
	imgur['vkvSPL4.jpg'],
	dbpedia['Date_palm'],
	eol['1135088'],
	'http://www.biodiversidad.co/fichas/1306',
	uniprot['42345']
)

flora(
	gbif['2736747'],
	'PALMA RAFIS',
	'Rhapis excelsa',
	"""Esta palma alcanza de 90-120 cms de alto. La base de la hoja presenta una envoltura fibrosa café que cubre el tallo, 
	sus flores son de color amarillento. Es de uso ornamental, útil para el embellecimiento del espacio público y para la 
	decoración de exteriores e interiores.""",
	imgur['tIw7fa8.jpg'],
	dbpedia['Rhapis_excelsa'],
	eol['1131793'],
	'http://www.biodiversidad.co/fichas/1310',
	uniprot['115514']
)

flora(
	gbif['2733755'],
	'PALMA BOTELLA',
	'Roystonea regia',
	"""Puede llegar a medir 30 ms de altura y a tener 60 cms de diámetro. Los frutos son  de color marrón rojizo o morado 
	oscuro. Su tronco se emplea para obtener tablones, sus hojas para techar casas y sus frutos para la alimentación animal. 
	La raíz en bebidas se usa como diurético para expulsar calculos por la orina.""",
	imgur['ukBNjEu.jpg'],
	dbpedia['Roystonea_regia'],
	eol['1131526'],
	'http://www.biodiversidad.co/fichas/3739',
	uniprot['145709']
)

flora(
	gbif['2731766'],
	'SALAK',
	'Salacca edulis',
	"""Esta especie es nativa del continente oceánico y se encuentra en Borneo, Java, Malaya y Maluku. Requiere abundante agua 
	durante la mayor parte del año. Es relativamente pequeña y espinosa, sus tallos están agrupados y se ramifican en la base.
	Las raices no se extienden a gran profundidad.""",
	imgur['1Lj38Y1.jpg'],
	dbpedia.Salak,
	eol['1131455'],
	'https://es.wikipedia.org/wiki/Salacca',
	uniprot['145711']
)

flora(
	gbif['5293897'],
	'GERIVÁ',
	'Syagrus romanzoffiana',
	"""Esta palma de tallo largo y solitario alcanza de 10-15 ms de altura, sus frutos son de color amarillo a anaranjado y 
	comestibles; es una especie ornamental. El palmito es comestible y sus hojas son de alimento para el ganado y 
	las semillas trituradas son alimento para las gallinas.""",
	imgur['uD8dqYu.jpg'],
	dbpedia['Syagrus_romanzoffiana'],
	eol['1129524'],
	'http://www.biodiversidad.co/fichas/1287',
	uniprot['290277']
)


flora(
	gbif['2736139'],
	'FALSO CAMEDOR',
	'Synechanthus fibrosus',
	"""Tallo solitario, delgado, liso, verde. Puede alcanzar de 5-6 ms de altura. Está presente en Belice, Costa Rica, 
	Guatemala, Honduras, golfo de México, sureste y suroeste de México y Nicaragua.""",
	imgur['fENpyrd.jpg'],
	wikidata['Q15470681'],
	eol['1129508'],
	'https://es.wikipedia.org/wiki/Synechanthus_fibrosus',
	uniprot['348516']
)

flora(
	gbif['8700701'],
	'PALMA ABANICO',
	'Washingtonia filifera',
	"""Esta palma alcanza 24 ms de alto y 120 cms de diámetro y la parte superior de su tallo está cubierto por hojas muertas. 
	Sus flores son de color blanco. Sus frutos son pequeños y de color negro, es una especie ornamental. Se utiliza en las 
	calles y parques de muchas ciudades tropicales y subtropicales como decoración.""",
	imgur['WGJzE6S.jpg'],
	dbpedia['Washingtonia_filifera'],
	eol['1127834'],
	'http://www.biodiversidad.co/fichas/1315',
	uniprot['145714']
)

flora(
	gbif['2705753'],
	'BAMBÚ DE BEECHEYA',
	'Bambusa beecheyana',
	"""Es una especie tropical que crece mejor a pleno sol. No es invasivo, pero se puede convertir rápidamente en una planta 
	densa de numerosos tallos. Es muy común en China.""",
	imgur['4q9HzLU.jpg'],
	wikidata['Q15508512'],
	eol['1115604'],
	'https://en.wikipedia.org/wiki/Bambusa',
	uniprot['318053']
)

flora(
	gbif['2705764'],
	'MAHAL BAMBOO',
	'Bambusa longispiculata',
	"""Puede alcanzar una altura de 10-15 ms, con un diámetro de 7-10 cms, es de color verde con pelos blancos en algunas 
	partes. Esta planta es empleada como ornamental. Se encuentra en Colombia, Costa Rica, Ecuador, Salvador, Guatemala, Honduras,
	Puerto Rico, Nicaragua, Panamá, Estados Unidos e India. """,
	imgur['rCRDVDp.jpg'],
	dbpedia['Bambusa_longispiculata'],
	eol['1115606'],
	'http://www.biodiversidad.co/fichas/2394',
	uniprot['47448']
)

flora(
	gbif['4141692'],
	'GIANT TIMBER BAMBOO',
	'Bambusa oldhamii',
	"""Es una de las especies con mayor adaptabilidad, es de rápido crecimiento y no es invasor. Puede alcanzar de 
	12-18 ms de altura, cuando sus tallos se maduran son usados para la construcción de herramientas y decoración de interiores.""",
	imgur['fY9BDVa.jpg'],
	dbpedia['Bambusa_oldhamii'],
	eol['1115544'],
	'https://en.wikipedia.org/wiki/Bambusa_oldhamii',
	uniprot['58923']
)

flora(
	gbif['2705765'],
	'BAMBÚ BENGAL',
	'Bambusa tulda',
	"""SUs tallos forman grupos de 6-20 ms de altura. Es uno de los bambúes más importantes en Asia, especialmente en India, 
	Bangladesh y el norte de Tailandia, donde sirve como comida y material para la construcción. Lo ideal es que este 
	bambú se mantenga en un ambiente con una temperatura entre de 40 °F - 100 °F para su correcto crecimiento.""",
	imgur['eLa4VGS.jpg'],
	dbpedia['Bambusa_tulda'],
	eol['1115609'],
	'https://en.wikipedia.org/wiki/Bambusa_tulda',
	uniprot['292582']
)

flora(
	gbif['4140151'],
	'BAMBÚ DE BUDA',
	'Bambusa ventricosa McClure',
	"""Este bambú en sus condiciones ideales puede alcanzar una altura mayor a 15 ms. Durante su crecimiento disminuye los 
	entrenudos y forma una protuberancia característica. El tallo principal, como el de todo bambú es hueco. Las hojas son de 
	color verde.""",
	imgur['6c11eLT.jpg'],
	dbpedia['Bambusa_ventricosa'],
	eol['2905694'],
	'https://en.wikipedia.org/wiki/Bambusa_ventricosa',
	uniprot['323096']
)

flora(
	gbif['7661971'],
	'BAMBÚ',
	'Bambusa vulgaris',
	"""Es una especie de la familia de los pastos, y a su vez del grupo del bambú, presenta tallos muy gruesos en forma 
	de caña que pueden superar los 10 ms de altura y son huecos en su interior. Tiene múltiples usos artesanales, medicinales, 
	en el ámbito religioso, como planta ornamental; proporciona sombra y protección al suelo.""",
	imgur['lXk87cJ.jpg'],
	dbpedia['Bambusa_vulgaris'],
	eol['1114100'],
	'http://www.biodiversidad.co/fichas/5328',
	uniprot['58168']
)

flora(
	gbif['2703315'],
	'BAMBÚ GIGANTE',
	'Dendrocalamus asper',
	"""Tiene grandes tallos leñosos entre 20-30 ms de altura y de 8-20 cms de diámetro. Además sus paredes son relativamente 
	gruesas y se vuelven más delgadas hacia la parte superior del tallo, su color es verde pálido y está cubierto de pelos 
	cortos de color marrón. Crecen bien en diferentes tipos de suelo. """,
	imgur['ZXwBB1E.jpg'],
	dbpedia['Dendrocalamus_asper'],
	eol['1115595'],
	'https://es.wikipedia.org/wiki/Dendrocalamus_asper',
	uniprot['387743']
)

flora(
	gbif['2703312'],
	'BAMBÚ CADENA',
	'Gigantochloa apus',
	"""Es una especie nativa del Sureste asiático, es el bambú económicamente más importante en la isla de Java, especialmente 
	en la industria de la artesanía y muebles. Puede alcanzar de 8-22 ms de altura, con un  diámetro de 4-13 cms, sus tallos son 
	de color verde brillante o verde amarillento cuando es joven.""",
	imgur['N10KkE3.jpg'],
	wikidata['Q15517583'],
	eol['1115568'],
	'https://es.wikipedia.org/wiki/Gigantochloa',
	uniprot['1182957']
)

flora(
	gbif['2703311'],
	'BAMBÚ GOMBONG',
	'Gigantochloa verticillata',
	"""Este bambú puede crecer de 7-30 ms de altura y de 5-13 cms de diámetro, el centro de la planta se eleva de manera 
	irregular sobre el suelo. En Indonesia esta especie es la segunda más importante después Gigantochloa apus y desempeña 
	un papel destacado en la economía rural. A veces se usa con fines ornamentales.""",
	imgur['M9PRqrO.jpg'],
	wikidata['Q15245801'],
	eol['1115569'],
	'https://id.wikipedia.org/wiki/Bambu_gombong',
	uniprot['105183']
)

flora(
	gbif['4115908'],
	'BAMBÚ MULI',
	'Melocanna baccifera',
	"""Es el bambú que produce el fruto más grande de la familia de las gramíneas, es carnoso y en forma de pera. Es muy común 
	en la India, existe un evento en este país donde se celebra el florecimento de este tipo de bambú. Puede llegar a medir 
	de 10-25 ms de altura y de 3-7 cms de diámetro. De color verde cuando está jóven y más opaco cuando está viejo.""",
	imgur['Xc8UXTu.jpg'],
	dbpedia['Melocanna_baccifera'],
	eol['5843797'],
	'https://en.wikipedia.org/wiki/Melocanna_baccifera',
	uniprot['104005']
)

#Modeladas en otras rutas
g.add( (gbif['3152205'], RDF.type, WILDLIFE.TaxonName) ) #maiz cacao
g.add( (gbif['2962824'], RDF.type, WILDLIFE.TaxonName) ) #vuelta oriente Espino de mono
g.add( (gbif['2734435'], RDF.type, WILDLIFE.TaxonName) ) # vuelta oriente
g.add( (gbif['2957438'], RDF.type, WILDLIFE.TaxonName) ) #vuelta oriente
g.add( (gbif['5594205'], RDF.type, WILDLIFE.TaxonName) ) # vuelta oriente
g.add( (gbif['7141666'], RDF.type, WILDLIFE.TaxonName) ) #vuelta oriente
g.add( (gbif['4142909'], RDF.type, WILDLIFE.TaxonName) ) # vuelta oriente
g.add( (gbif['3190491'], RDF.type, WILDLIFE.TaxonName) ) #vuelta oriente
g.add( (gbif['4084063'], RDF.type, WILDLIFE.TaxonName) ) # vuelta oriente
g.add( (gbif['7269222'], RDF.type, WILDLIFE.TaxonName) ) #vuelta oriente
g.add( (gbif['3067261'], RDF.type, WILDLIFE.TaxonName) ) # vuelta oriente
g.add( (gbif['3086337'], RDF.type, WILDLIFE.TaxonName) ) # vuelta oriente
g.add( (gbif['8311514'], RDF.type, WILDLIFE.TaxonName) ) # vuelta oriente
g.add( (gbif['2767031'], RDF.type, WILDLIFE.TaxonName) ) #vuelta oriente
g.add( (gbif['3172537'], RDF.type, WILDLIFE.TaxonName) ) # vuelta oriente
g.add( (gbif['2962831'], RDF.type, WILDLIFE.TaxonName) ) #vuelta oriente
g.add( (gbif['5421429'], RDF.type, WILDLIFE.TaxonName) ) #vuelta oriente
g.add( (gbif['5420509'], RDF.type, WILDLIFE.TaxonName) ) #vuelta oriente
g.add( (gbif['3059672'], RDF.type, WILDLIFE.TaxonName) ) # vuelta oriente
g.add( (gbif['5421132'], RDF.type, WILDLIFE.TaxonName) ) # vuelta oriente
g.add( (gbif['3190087'], RDF.type, WILDLIFE.TaxonName) ) #vuelta oriente 
g.add( (gbif['3785984'], RDF.type, WILDLIFE.TaxonName) ) #vuelta oriente
g.add( (gbif['3152195'], RDF.type, WILDLIFE.TaxonName) ) # vuelta oriente
g.add( (gbif['2953986'], RDF.type, WILDLIFE.TaxonName) ) #vuelta oriente
g.add( (gbif['5417812'], RDF.type, WILDLIFE.TaxonName) ) # vuelta oriente
g.add( (gbif['5396865'], RDF.type, WILDLIFE.TaxonName) ) # vuelte oriente
g.add( (gbif['8138695'], RDF.type, WILDLIFE.TaxonName) ) #vuelta oriente
g.add( (gbif['3169446'], RDF.type, WILDLIFE.TaxonName) ) # vuelta oriente
g.add( (gbif['7649215'], RDF.type, WILDLIFE.TaxonName) ) # vuelta oriente
g.add( (gbif['3694437'], RDF.type, WILDLIFE.TaxonName) ) # vuelta oriente
g.add( (gbif['2984339'], RDF.type, WILDLIFE.TaxonName) ) #vuelta oriente

g.add( (gbif['8225137'], RDF.type, WILDLIFE.TaxonName) ) #vuelta oriente
g.add( (gbif['7262410'], RDF.type, WILDLIFE.TaxonName) ) #vuelta oriente

#print(g.serialize(format='pretty-xml'))
