#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import WILDLIFE, UMBEL, OWL
from utils.namespaces import rioFrio, dbpedia, wikidata, imgur, eol, gbif, uniprot
from faunaRiofrio import g

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
    
    g.add( (URIRef(uri), UMBEL.isRelatedTo, rioFrio.Flora) )


flora(
 	gbif['3129176'],
 	'CHILCA',
 	'Baccharis dracunculifolia',
 	"""Arbusto leñoso, en general de 2-3 ms de altura, de hojas perennes y forma globosa. Sus tallos son cilíndricos y 
 	con pequeños pelos.""",
 	imgur['DmS28Yc.png'],
 	dbpedia['Baccharis_dracunculifolia'],
 	eol['6181269'],
	'https://en.wikipedia.org/wiki/Baccharis_dracunculifolia',
	uniprot['72900']
 )

flora(
 	gbif['3105048'],
 	'FRAILEJONES',
 	'Espeletia',
 	"""Se encuentra en áreas de páramo; con una altura máxima de 4 ms, tallos delgados. Está presente en la región Andina en 
 	la Cordillera Central.""",
 	imgur['oaanuoD.jpg'],
 	dbpedia['Espeletia'],
 	eol['6260580'],
	'http://www.biodiversidad.co/fichas/4855',
	uniprot['185152']
 )    

flora(
 	gbif['5405976'],
 	'ARNICA',
 	'Arnica montana',
 	"""Esta especie se encuentra presente en áreas de páramo; mide 1 m de altura, sus flores tienen tonalidades de 
 	fucsia a violeta.""",
 	imgur['DQ3ct3t.jpg'],
 	dbpedia['Arnica_montana'],
 	eol['482128'],
	'http://www.biodiversidad.co/fichas/4998',
	uniprot['436207']
 )    

flora(
 	gbif['2698931'],
 	'QUICHE',
 	'Guzmania gloriosa',
 	"""Conocida por sus hojas largas, rígidas y arqueadas de un intenso color verde, no alcanza una gran altura. Es una 
 	planta originaria de regiones suroccidentales de América del sur y de las Antillas.""",
 	imgur['mx5bC8K.jpg'],
 	dbpedia['Guzmania_gloriosa'],
 	eol['1118453'],
	'https://en.wikipedia.org/wiki/Guzmania_gloriosa',
	uniprot['49489']
 )    

flora(
 	gbif['5414222'],
 	'ACEBO',
 	'Ilex aquifolium',
 	"""Generalmente mide de 2-5 ms, pero en algunas ocasiones pueden alcanzar hasta 12 ms de altura. Las hojas son brillantes 
 	y miden de 4-7.5 cms de longitud, estas son usadas como antipirético, diurético suave y tónico.""",
 	imgur['dgFG7WA.jpg'],
 	dbpedia['Ilex_aquifolium'],
 	eol['46322600'],
	'http://www.biodiversidad.co/fichas/1797',
	uniprot['4298']
 )    

flora(
 	gbif['3036520'],
 	'MANO DE OSO',
 	'Oreopanax floribundum',
 	"""Es fácil de reconocer por la forma de sus hojas, que parecen los dedos de una mano abierta. Es usada como una especie 
 	ornamental, debido a su forma característica; sus flores son de color crema y sus frutos de color verde, pero cuando maduran 
 	se tornan de un color violeta.""",
 	imgur['lmG0BYj.jpg'],
 	dbpedia['Oreopanax'],
 	eol['5056477'],
 	'http://www.biodiversidad.co/fichas/1081',
 	uniprot['52502']
 )        

flora(
 	gbif['2754207'],
 	'CORTAPICO',
 	'Bomarea multiflora',
 	"""Es una planta con frutos de color púrpura; sus hojas son de un color marrón ténue. Sus flores tienen un color entre 
 	rojo, amarillo y a veces violáceo. Está presente en Ecuador, Colombia, Bolivia y Venezuela.""",
 	imgur['5MTUlYV.jpg'],
 	dbpedia['Bomarea_multiflora'],
 	eol['1086318'],
	'https://es.wikipedia.org/wiki/Bomarea_multiflora',
	uniprot['488910']
 )    

flora(
 	gbif['4170835'],
 	'MORTIÑO',
 	'Vaccinium meridionale',
 	"""Esta planta crece hasta 3.5 ms de altura y su tallo alcanza 50 cms de diámetro; sus hojas tienen forma elíptica y 
 	miden entre 1-3.5 cms de largo por 0.6-1.4 cms de ancho. Sus flores son pequeñas, de color blanco y sus frutos son bayas 
 	de color morado oscuro a negro al madurar.""",
 	imgur['42u4szJ.jpg'],
 	wikidata['Q15395050'],
 	eol['6946968'],
	'http://www.biodiversidad.co/fichas/1603',
	uniprot['57538']
 )    

flora(
 	gbif['3861855'],
 	'SIETECUEROS',
 	'Tibouchina lepidota',
 	"""Esta planta puede medir hasta 20 ms de altura, su corteza desprende escamas rojizas. Las flores son de color violeta 
 	y muy llamativas. El fruto es de un color café claro, posee muchas semillas en su interior.""",
 	imgur['1v1n1El.jpg'],
 	wikidata['Q6146392'],
 	eol['5434731'],
	'http://www.biodiversidad.co/fichas/1021',
	uniprot['1160661']
 )    

flora(
 	gbif['7359544'],
 	'ENCENILLO',
 	'Weinmannia tomentosa',
 	"""Este árbol se encuentra en la cordillera oriental colombiana, alcanza los 25 ms de altura; tiene corteza lisa y de 
 	color gris. Sus flores son blancas y pequeñas. Su madera es usada para la construccion de vigas, columnas y cercas. 
 	Las hojas sirven para aliviar la fiebre al ganado.""",
 	imgur['VXiVsOm.jpg'],
 	wikidata['Q5405356'],
 	eol['5552584'],
	'http://www.biodiversidad.co/fichas/1761',
	uniprot['189904']
 )    

flora(
 	gbif['2753090'],
 	'AZUCENA',
 	'Lilium candidum',
 	"""Planta bulbosa de tamaño grande, presenta flores blancas agrupadas en ramilletes terminales. Algunos afirman 
 	que procede de oriente; es usada en la medicina alternativa como antiespasmódico, tisanas para la hidropesia, entre otras.""",
 	imgur['kbENh3v.jpg'],
 	dbpedia['Lilium_candidum'],
 	eol['1003297'],
	'https://en.wikipedia.org/wiki/Lilium_candidum',
	uniprot['83802']
 )    

flora(
 	gbif['7930239'],
 	'MATAPALO',
 	'Ficus trigona',
 	"""Árbol de hasta 15 ms de altura, con hojas de 10-19 cms de largo por 6-9 cms de ancho, lisas y rígidamente acartonadas 
 	cuando están secas.""",
 	imgur['kiNSCaD.jpg'],
 	dbpedia['Lilium_candidum'],
 	eol['6958325'],
	'http://www.biodiversidad.co/fichas/3801',
	uniprot['378037']
 )    

flora(
 	gbif['3022502'],
 	'ALMENDROS',
 	'Prunus dulcis',
 	"""Árbol que puede alcanzar 10 ms de talla, con tronco rara vez derecho. Hojas simples de 7.5-12.5 cms de longitud. Frutos 
 	de color verde, carnosos que miden unos 3-6 cms de longitud. Soporta muy bien la sequía y le perjudica el exceso de agua.""",
 	imgur['doRSxmc.jpg'],
 	dbpedia['Almond'],
 	eol['46326125'],
	'http://www.granada.org/internet/arboles.nsf/bus/14?OpenDocument',
	uniprot['3755']
 )    

flora(
 	gbif['5338267'],
 	'UÑA DE GATO',
 	'Uncaria tomentosa',
 	"""Es típica de bosques fuertemente intervenidos, trochas y ríos pequeños. Estudios farmacológicos han mostrado que los 
 	alcaloides de esta especie tienen efecto antitumoral. Es antidiabética, antirreumática y antiinflamatoria, además se utiliza 
 	en el tratamiento contra gastritis, enfermedades hepáticas, reumatismo, artritis y cirrosis.""",
 	imgur['GILTCS7.jpg'],
 	dbpedia['Uncaria_tomentosa'],
 	eol['1096909'],
	'http://www.biodiversidad.co/fichas/382',
	uniprot['128375']
 )    

flora(
 	gbif['3180085'],
 	'ARRAYÁN',
 	'Myrtus communis',
 	"""Planta aromática que mide entre 1-3 ms de altura, las hojas son de color verde oscuro y tienen de 3-5 cm de largo. Las 
 	flores son de color blanco, pero a veces se tornan rosadas, con cinco pétalos. Se usa como anticatarral.""",
 	imgur['O0UYO0X.jpg'],
 	dbpedia['Myrtus_communis'],
 	eol['2508590'],
	'http://www.biodiversidad.co/fichas/1617',
	uniprot['119949']
 )    

flora(
 	gbif['3190647'],
 	'CRUCETO',
 	'Quassia amara',
 	"""Arbusto que llega a alcanzar los 5 ms de altura. El extracto de la madera es usado como insecticida natural. Puede 
 	traer efectos segundarios en humanos si se usa como pesticida en los cultivos.""",
 	imgur['ZK1mr7z'],
 	dbpedia['Myrtus'],
 	eol['46326128'],
	'https://en.wikipedia.org/wiki/Quassia_amara',
	uniprot['43725']
 )    
    

flora(
 	gbif['3083750'],
 	'CHAMISO',
 	'Atriplex canescens',
 	"""Es un arbusto nativo de California y también se encuentra en otras partes de Norteamérica y Suramérica. Las flores en 
 	verano no son tan llamativas, pero cuando florecen son muy vistosos. Nuevas especies y variedades de este genero 
 	continuan surgiendo.""",
 	imgur['u4bWdpt.jpg'],
 	dbpedia['Atriplex_canescens'],
 	eol['586526'],
	'https://en.wikipedia.org/wiki/Atriplex_canescens',
	uniprot['35922']
 )    

flora(
 	gbif['5421144'],
 	'HAYUELO',
 	'Dodonaea viscosa',
 	"""Vive en bósques húmedos y secos, alcanza los 7 ms de altura. Las hojas miden 7 cms de largo por 2,5 cms de ancho. 
 	Frutos de 1.5 cms de diámetro, rojizos cuando juveniles y café claro cuando están maduros.""",
 	imgur['OyW1Lbw.jpg'],
 	dbpedia['Dodonaea_viscosa'],
 	eol['582326'],
	'http://www.biodiversidad.co/fichas/1415',
	uniprot['151065']
 )    

flora(
 	gbif['5349620'],
 	'PÍZAMO',
 	'Erythrina fusca',
 	"""Es una especie originaria de Norte América; actualmente se encuentra en Centro y Sur América. Este árbol alcanza los 15 
 	ms de altura, sus flores son de color naranja, agrupadas. Es una planta fijadora de nitrógeno y, por lo tanto, sirve 
 	para recuperación de suelos. La bebida del cocimiento de sus flores es sedativa.""",
 	imgur['602pK3r.jpg'],
 	dbpedia['Erythrina_fusca'],
 	eol['644276'],
	'http://www.biodiversidad.co/fichas/3538',
	uniprot['556509']
 )    

flora(
 	gbif['5406086'],
 	'ÁRBOLOCO',
 	'Montanoa quadrangularis',
 	"""Árbol propio de la zona andina de Colombia y Venezuela; de 8-10 ms de altura. Sus flores son blancas a manera 
 	de margaritas. Crece en áreas intervenidas donde se constituye en un valioso constructor del ecosistema y formador 
 	del nicho para promover el desarrollo de otras especies.""",
 	imgur['bjnH5BU.jpg'],
 	dbpedia['Q15564996'],
 	eol['6247581'],
	'http://www.biodiversidad.co/fichas/3513',
	uniprot['167003']
 )    

flora(
 	gbif['3120946'],
 	'ALTAMISA',
 	'Artemisia vulgaris',
 	"""Hierba de 40-80 cms de altura. El fruto de esta planta es de color negro. La ingestión de infusión de la planta se usa 
 	para evitar hemorragias durante la menstruación.""",
 	imgur['RFQGzwx.jpg'],
 	dbpedia['Artemisia_vulgaris'],
 	eol['850415'],
	'http://www.biodiversidad.co/fichas/3888',
	uniprot['4220']
 )    

flora(
 	gbif['5354656'],
 	'ESCOBO',
 	'Cytisus scoparius',
 	"""Alcanza los 2 ms de altura; las flores son solitarias y de color amarillo. El fruto tiene pelos pequeños. 
 	Crece en márgenes de caminos y cultivos abandonados a menudo es cultivado como una planta ornamental.""",
 	imgur['LwKNXmi.jpg'],
 	dbpedia['Cytisus_scoparius'],
 	eol['703895'],
	'https://en.wikipedia.org/wiki/Cytisus_scoparius',
	uniprot['3835']
 )    

flora(
 	gbif['5544303'],
 	'CARACOLÍ',
 	'Anacardium excelsum',
 	"""Alcanza hasta 40 ms de altura, su tronco produce un líquido de color rojizo, sus ramas son gruesas y abundantes. 
 	Sus flores miden 3 mms de diámetro aproximadamente, son de color rosado blancuzco y crecen agrupadas en inflorescencias 
 	terminales.""",
 	imgur['00ML9MC.jpg'],
 	dbpedia['Anacardium_excelsum'],
 	eol['6935004'],
	'http://www.biodiversidad.co/fichas/1070',
	uniprot['638922']
 )

flora(
 	gbif['3084014'],
 	'GUAGUA',
 	'Phytolacca rivinoides',
 	"""Es una planta leñosa en la base con brotes de hasta 5 ms de largo, se puede encontrar en la Amazonía, 
 	cerca de los establecimientos de los indios Yanomami; tambien tiene uso medicinal.""",
 	imgur['t1vbei6.jpg'],
 	wikidata['Q12219768'],
 	eol['482121'],
	'https://es.wikipedia.org/wiki/Phytolacca_rivinoides',
	uniprot['1580009']
 )    

flora(
 	gbif['2901294'],
 	'CASCARILLA',
 	'Cinchona pubescens',
 	"""Árbol que puede alcanzar hasta 15 ms de altura, copa mediana densa con follaje verde; sus flores son de color 
 	rosado-violáceo y sus frutos son de color negruzco cuando estan maduros. El tronco es algo torcido.""",
 	imgur['UY24rUo.jpg'],
 	dbpedia['Cinchona_pubescens'],
 	eol['1110181'],
	'http://www.biodiversidad.co/fichas/3665',
	uniprot['50278']
 )    

flora(
 	gbif['3183534'],
 	'POMO',
 	'Syzygium jambos',
 	"""Es una especie de copa globosa, amplia, redondeada de follaje denso, verde obscuro y con hojas jóvenes rojizas. 
 	Se distribuye en las laderas de la Sierra Nevada de Santa Marta y las tres cordilleras, es usada como planta ornamental 
 	en  parques, avenidas, separadores. El fruto es consumido por aves y mamíferos silvestres.""",
 	imgur['cqjBG6A.jpg'],
 	dbpedia['Cinchona_pubescens'],
 	eol['2508661'],
	'http://www.biodiversidad.co/fichas/3565',
	uniprot['334483']
 )      
       
flora(
 	gbif['2984476'],
 	'YARUMO',
 	'Cecropia peltata',
 	"""Árbol de 30 ms de altura con tronco recto y hueco. Se encuentra en las Antillas Mayores y Menores y en América Central, 
 	tambien en America del Sur en los países de Venezuela, Colombia, Brasil y las Guayanas.""",
 	imgur['ueMusmv.jpg'],
 	dbpedia['Cecropia_peltata'],
 	eol['46242436'],
	'http://www.biodiversidad.co/fichas/5108',
	uniprot['210352']
 )    

flora(
 	gbif['5304469'],
 	'DRAGO',
 	'Dracaena draco',
 	"""Árbol con el tronco grisáceo y ramificado, sus frutos son de color rojo anaranjado. Las flores poseen un color 
 	blanco-verdoso. La resina de esta especie es llamada "Sangre de dragón" y es comercializada y usada medicinalmente.""",
 	imgur['EahW9fX.jpg'],
 	dbpedia['Dracaena_draco'],
 	eol['46321891'],
	'https://en.wikipedia.org/wiki/Dracaena_draco',
	uniprot['100532']
 )    

flora(
 	gbif['2721307'],
 	'TOTE',
 	'Rhynchospora nervosa',
 	"""Puede alcanzar una altura de 30-40 cms. Las hojas son de color verde oliva y llegan a medir entre 25-35 cms de 
 	longitud por 1 mm de ancho. Los frutos son de color pardo-anaranjado a pardo-oscuro. Se puede encontrar desde México 
 	hasta el sur de Brasil y norte de Argentina.""",
 	imgur['ENxnztV.jpg'],
 	wikidata['Q15555289'],
 	eol['249178'],
	'http://www.biodiversidad.co/fichas/3625',
	uniprot['76499']
 )    

flora(
 	gbif['2878688'],
 	'ROBLE',
 	'Quercus robur',
 	"""Éste árbol alcanza de 15-20 ms de altura. Las ramas más viejas son de color cenizo; sus flores son de color 
 	verde amarillento. La cocción de la corteza se usa para curar la diarrea, para enjuagues bucales, para 
 	combatir la gengivitis y las inflamaciones entre otras aplicaciones medicinales.""",
 	imgur['6zla8xY.jpg'],
 	dbpedia['Quercus_robur'],
 	eol['1151323'],
	'http://www.biodiversidad.co/fichas/1726',
	uniprot['38942']
 )    

flora(
 	gbif['5358205'],
 	'TACHUELO',
 	'Pictetia aculeata',
 	"""Árbol caduco pequeño, común en áreas secas. Las ramitas son espinosas y las hojas casi redondas tienen punta 
 	espinosa. Florece y fructifica todo el año. Produce una madera muy fina, pero debido a las pequeñas dimensiones sólo 
 	se utiliza para postes de cercas. Tambiés es usado con fines ornamentales.""",
 	imgur['lt9YxZy.jpg'],
 	wikidata['Q6075171'],
 	eol['415795'],
	'https://es.wikipedia.org/wiki/Pictetia_aculeata',
	uniprot['77292']
 )    

flora(
 	gbif['2685742'],
 	'CEDRO',
 	'Cedrus',
 	"""Este árbol tiene una forma pulcra y piramidal en su juventud, con rígidas ramas ascendentes, pero con la edad se 
 	extiende formando un árbol ancho y plano con ramas enormes de 30 ms o más de altura.""",
 	imgur['w1Qz4fK.jpg'],
 	wikidata['Q128550'],
 	eol['34221'],
	'http://www.biodiversidad.co/fichas/2242',
	uniprot['3321']
 )    

flora(
 	gbif['5384064'],
 	'TUNO',
 	'Opuntia ficus-indica',
 	"""Este cactus puede crecer hasta 4 ms de altura. Sus frutos o “higos” tienen un bello color amarillo-rojo y un sabor 
 	muy agradable, además contienen un alto valor nutritivo: proteínas, calorías, grasa, calcio y fósforo son algunos de los 
 	componentes de este fruto.""",
 	imgur['6zpl1XS.jpg'],
 	dbpedia['Opuntia_ficus-indica'],
 	eol['479484'],
	'http://www.biodiversidad.co/fichas/1548',
	uniprot['371859']
 )
  
#Modelada en otra ruta 
g.add( (gbif['3152240'], RDF.type, WILDLIFE.TaxonName) ) # vuelta oriente
g.add( (gbif['2926634'], RDF.type, WILDLIFE.TaxonName) ) #MAIZ

#print (g.serialize(format="pretty-xml"))
