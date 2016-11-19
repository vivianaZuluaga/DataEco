#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph, BNode
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import WILDLIFE, UMBEL, OWL, VCARD
from utils.namespaces import rioFrio, rutaVueltaOriente, dbpedia, wikidata, imgur, eol, gbif, uniprot
from eventosRiofrio import g

#g = Graph()

def fauna(uri, nombre_comun, nombre_cientifico, descripcion, imagen, uriLink1, uriLink2, ref, uriLink3, linkURI):
	g.add( (URIRef(uri), RDF.type, WILDLIFE.TaxonName) )
	g.add( (URIRef(uri), WILDLIFE.commonName, Literal(nombre_comun, lang='es') ) )
	g.add( (URIRef(uri), WILDLIFE.scientificName, Literal(nombre_cientifico, lang='la')) )
	g.add( (URIRef(uri), WILDLIFE.shortDescription, Literal(descripcion, lang='es')) )
	g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)))
	g.add( (URIRef(uri), WILDLIFE.kingdomName, Literal('Animal', lang='es')) )
	g.add( (URIRef(uri), FOAF.isPrimaryTopicOf, URIRef(ref)) ) #Sitio web
	
	g.add( (URIRef(uri), OWL.sameAs, URIRef(uriLink1)) ) #Link RDF
	g.add( (URIRef(uri), OWL.sameAs, URIRef(uriLink3)) ) #Link RDF
	
	g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) ) #Links externos
	g.add( (URIRef(uri), RDFS.seeAlso, URIRef(uriLink2)) )
	
	g.add( (URIRef(uri), VCARD.category, Literal("FAUNA", lang='es')))
	g.add( ( URIRef(uri), UMBEL.isAbout, URIRef(rioFrio['Fauna.rdf'])) )

fauna(
 	rioFrio['Fauna.rdf#ortalisRuficauda'],
 	'GUACHARACA',
 	'Ortalis ruficauda',
 	"""Mide aproximadamente 53 cms; carece de plumas en la garganta cuya piel es roja y las plumas de la cola forman un 
 	penacho largo y delgado. Es principalmente herbívora y furgívora, se alimenta de frutos, brotes y hojas. Las hembras 
 	de esta especie ponen entre dos y cuatro huevos.""",
 	imgur['bmlBCxg.jpg'],
 	dbpedia['Rufous-vented_chachalaca'],
 	eol['1050075'],
	'http://www.biodiversidad.co/fichas/4256',
	uniprot['301604'],
	gbif['5229447']
 )

fauna(
 	rioFrio['Fauna.rdf#edalorhinaPerezi'],
 	'RANA VAQUITA',
 	'Edalorhina perezi',
 	"""Se la puede encontrar en los bosques húmedos y zonas inundables. La piel sobre el vientre es lisa, el pecho y vientre 
 	son negros, es una especie pequeña y está presente en Ecuador, Colombia, Brasil y Perú.""",
 	imgur['YTwHFDS.jpg'],
 	dbpedia['Edalorhina_perezi'],
 	eol['1036652'],
	'http://www.biodiversidad.co/fichas/2735',
	uniprot['318278'],
	gbif['2423530']
 )

fauna(
 	rioFrio['Fauna.rdf#salamandraSalamandra'],
 	'SALAMANDRA',
 	'Salamandra salamandra',
 	"""Esta especie se puede encontrar en zonas húmedas, se oculta durante el día bajo las piedras, troncos caídos y hojas. 
 	Puede llegar a medir entre 12-23 cms de longitud y vivir hasta los 20 años.""",
 	imgur['cJ86d4t.jpg'],
 	dbpedia['Fire_salamander'],
 	eol['333311'],
	'https://en.wikidatapedia.org/wikidata/Salamandra',
	uniprot['57571'],
	gbif['2431776']
 )	

fauna(
 	rioFrio['Fauna.rdf#pumaConcolor'],
 	'PUMA',
 	'Puma concolor',
 	"""Esta especie ha sido reportada en los departamentos de Vaupés, Vichada, Amazonas, Antioquia, Bolivar y Casanare. 
 	El puma concolor caza principalmente de noche y puede adapatarse a varios tipos de hábitat.""",
 	imgur['31kUvXJ.jpg'],
 	dbpedia['Cougar'],
 	eol['311910'],
	'http://www.biodiversidad.co/fichas/348',
	uniprot['9696'],
	gbif['2435099']
 )

fauna(
 	rioFrio['Fauna.rdf#lutrinae'],
 	'NUTRIA',
 	'Lutrinae',
 	"""Animal de costumbres acuáticas, con abundante pelaje impermeable, esto le permite manter su calor corporal. Se alimenta 
 	principalmente de peces, aunque también de anfibios e invertebrados acuáticos.""",
 	imgur['rqc4d42.jpg'],
 	dbpedia['Otter'],
 	eol['2849553'],
	'https://en.wikidatapedia.org/wikidata/Otter',
	uniprot['169417'],
	gbif['2433750']
 )

fauna(
 	rioFrio['Fauna.rdf#nasuaNasua'],
 	'CUSUMBO',
 	'Nasua nasua',
 	"""Partes superiores rojizo encendido; cola con anillos blanquecinos y negros. Se encuentra en Colombia, Ecuador, Perú, 
 	Argentina y las Guayanas. Su alimentación consiste principalmente de frutas y raíces, pero también consume pequeños 
 	invertebrados. Habita bósques de zona tropical y sub-tropical.""",
 	imgur['CD9AIqw.jpg'],
 	dbpedia['South_American_coati'],
 	eol['328601'],
	'http://www.biodiversidad.co/fichas/3490',
	uniprot['9651'],
	gbif['2433536']
 )

fauna(
 	rioFrio['Fauna.rdf#tremarctosOrnatus'],
 	'OSO DE ANTEOJOS',
 	'Tremarctos ornatus',
 	"""En comparación con otros osos del mundo, es de tamaño mediano. La coloración del pelaje es uniforme, negra o café 
 	negruzca, con pelo áspero de 55-120 mms de largo. Consume hierbas y brotes.""",
 	imgur['6Ugecli.jpg'],
 	dbpedia['Spectacled_bear'],
 	eol['328076'],
	'http://www.biodiversidad.co/fichas/281',
	uniprot['9638'],
	gbif['2433401']
 )

fauna(
 	rioFrio['Fauna.rdf#soricidae'],
 	'MUSARAÑAS',
 	'Soricidae',
 	"""Son insectívoros y de cuerpo pequeño, el hocico es alargado y en forma de punta y sus orejas se esconden tras su 
 	pelaje, los ojos son minúsculos. La fecundidad de estos animales es asombrosa.""",
 	imgur['GAFfFru.jpg'],
 	dbpedia['Shrew'],
 	eol['8714'],
	'https://es.wikidatapedia.org/wikidata/Soricidae',
	uniprot['9376'],
	gbif['5534']
 )

fauna(
 	rioFrio['Fauna.rdf#caenolestes'],
 	'RUNCHOS',
 	'Caenolestes',
 	"""Estos animales son insectívoros y nocturnos, son buenos trepadores de árboles y se pueden encontrar en Colombia, 
 	Ecuador y al noroeste de Venezuela, es considerada una especie solitaria.""",
 	imgur['G9BPwh7.jpg'],
 	dbpedia['Caenolestes'],
 	eol['15588'],
	'https://en.wikidatapedia.org/wikidata/Caenolestes',
	uniprot['37886'],
	gbif['2433359']
 )

fauna(
 	rioFrio['Fauna.rdf#hydrochoerusHydrochaeris'],
 	'CHIGÜIRO',
 	'Hydrochoerus hydrochaeris',
 	"""Se encuentra en los valles de los principales ríos de Suramérica: Magdalena, Orinoco, Amazonas, Rio de la plata y 
 	Panamá. Se alimenta de hierbas, considerada una especie social. Es el roedor más grande del mundo, su coloración varía entre 
 	gris oliváceo, pardo rojizo y marrón.""",
 	imgur[''],
 	dbpedia['Capybara'],
 	eol['326517'],
	'http://www.biodiversidad.co/fichas/294',
	uniprot['10149'],
	gbif['5786666']
 )

fauna(
 	rioFrio['Fauna.rdf#anasPlatyrhynchosDomesticus'],
 	'PATO',
 	'Anas platyrhynchos domesticus',
 	"""La cabeza verde del macho contrasta con su pico amarillo, collar blanco, pecho castaño, flancos grises y flecos 
 	rizados negros en la punta de la cola. La hembra es moteada con manchas negras en el pico anaranjado. Consume una gran 
 	variedad de alimentos entre ellos artrópodos, gusanos, insectos, caracoles y algunos productos dados por las personas.""",
 	imgur['loEy21I.jpg'],
 	dbpedia['Domestic_duck'],
 	eol['45886553'],
	'http://www.biodiversidad.co/fichas/4502',
	uniprot['8839'],
	gbif['2498056']
 )

fauna(
 	rioFrio['Fauna.rdf#trochilidae'],
 	'COLIBRÍ',
 	'Trochilidae',
 	"""También se le conoce como picaflor; el más pequeño de los colibrís mide aproximadamente 6 cms y el más grande 
 	conocido mide 25 cms. Se alimenta del néctar de las flores principalmente rojas o naranjas brillantes, también come 
 	algunos insectos como arañas, avispas, hormigas y escarabajos.""",
 	imgur['sCgxVN4.jpg'],
 	dbpedia['Hummingbird'],
 	eol['8021'],
	'https://en.wikidatapedia.org/wikidata/Category:Trochilidae',
	uniprot['9244'],
	gbif['5289']
 )

fauna(
 	rioFrio['Fauna.rdf#caprimulgidae'],
 	'CHOTACABRAS',
 	'Caprimulgidae',
 	"""Presenta patas débiles, pico pequeño, cerdas rictales conspicuas, ojos grandes ubicados en los lados de la 
 	cabeza y boca grande con paladar muy sensible, la cual puede abrir horizontal y verticalmente utilizando un mecanismo 
 	de extensión de su mandíbula inferior.""",
 	imgur['mLHt0HH.jpg'],
 	dbpedia['Nightjar'],
 	eol['7971'],
	'http://www.icesi.edu.co/wikidata_aves_colombia/tiki-index.php?page=CAPRIMULGIDAE+-+Chotacabras+y+Guardacaminos',
	uniprot['48286'],
	gbif['5225']
 )

fauna(
 	rioFrio['Fauna.rdf#ardeidae'],
 	'GARZA',
 	'Ardeidae',
 	"""Aves de tamaño medio a grande y la mayoría de sus miembros presentan cuellos y patas largas. Sus patas largas y fuertes 
 	les permiten cruzar ríos poco profundos. Se encuentran en regiones tropicales principalmente, se pueden reproducir en 
 	colonias bastante grandes o bien en algunas mas modestas.""",
 	imgur['iPehz0A.jpg'],
 	dbpedia['Heron'],
 	eol['8013'],
	'http://www.icesi.edu.co/wikidata_aves_colombia/tiki-index.php?page=ARDEIDAE+-+Garzas',
	uniprot['8901'],
	gbif['3685']
 )

fauna(
 	rioFrio['Fauna.rdf#ajaiaAjaja'],
 	'GARZA PALETA',
 	'Ajaia ajaja',
 	"""Se alimenta principalmente de peces pequeños y en menor medida de insectos acuáticos y camarones. Mide entre 65.8-81.0 
 	cms. El pico tiene forma de cuchara y presenta manchas pequeñas de color verdoso. La cabeza y la parte superior de 
 	la garganta son descubiertas y de color verdoso.""",
 	imgur['hU5VYB8.jpg'],
 	dbpedia['Roseate_spoonbill'],
 	eol['46390584'],
	'http://www.biodiversidad.co/fichas/4221',
	uniprot['371920'],
	gbif['2480804']
 )

fauna(
 	rioFrio['Fauna.rdf#columbidae'],
 	'PALOMAS',
 	'Columbidae',
 	"""Se alimentan de legumbres, granos, semillas, desechos de comida que busca en la basura en zonas urbanas, mide 
 	de 29 a 35 cm de largo, son descendientes de las palomas bravías salvajes del sur de Europa. Tienen patas rojizas, 
 	ojos rojos anaranjados, y picos grises.""",
 	imgur['PPPKQQv.jpg'],
 	dbpedia['Columbidae'],
 	eol['7978'],
	'http://www.biodiversidad.co/fichas/4464',
	uniprot['8930'],
	gbif['5233']
 )

fauna(
 	rioFrio['Fauna.rdf#momotusMomota'],
 	'BARRANQUEROS',
 	'Momotus momota',
 	"""Se alimenta de pequeños insectos, también captura pequeños lagartos y serpientes. Se conoce por su cabeza voluminosa, 
 	con una banda azul clara que rodea su coronilla negra y se vuelve morada en la nuca; se encuentra en bosques húmedos y 
 	secos.""",
 	imgur['dc5K3Nd.jpg'],
 	dbpedia['Blue-crowned_motmot'],
 	eol['1050064'],
	'http://www.biodiversidad.co/fichas/3452',
	uniprot['57426'],
	gbif['2475290']
 )

fauna(
 	rioFrio['Fauna.rdf#spizaetusIsidori'],
 	'ÁGUILA',
 	'Spizaetus isidori',
 	"""Mide entre 64-74 cms de largo. Es grande y robusta con cabeza, cuello y dorso negros. Con una cresta aguda. Tiene 
 	las alas anchas pero proporcionalmente largas y por debajo son color crema con puntas negras y coberteras rufas. Prefiere 
 	los bosques húmedos montanos. Se alimenta de aves de gran tamaño y también de mamíferos.""",
 	imgur['Bapm5Vn.jpg'],
 	dbpedia['Black-and-chestnut_eagle'],
 	eol['1048938'],
	'http://www.icesi.edu.co/wikidata_aves_colombia/tiki-index.php?page=%C3%81guila+crestada',
	uniprot['214437'],
	gbif['5788512']
 )

fauna(
 	rioFrio['Fauna.rdf#accipiterNisus'],
 	'GAVILÁN',
 	'Accipiter nisus',
 	"""Cuerpo pequeño, con alas redondeadas, patas largas y un pico fuerte y poderoso. La cola siempre es más larga que las 
 	alas, y en el macho adulto presenta unas cuatro a cinco franjas onduladas. Las hembras pueden ser hasta un 25% más 
 	grandes que los machos.""",
 	imgur['XyvXEUa.jpg'],
 	dbpedia['Eurasian_sparrowhawk'],
 	eol['1048393'],
	'https://es.wikidatapedia.org/wikidata/Accipiter_nisus',
	uniprot['993372'],
	gbif['2480637']
 )

fauna(
 	rioFrio['Fauna.rdf#falcoPeregrinus'],
 	'HALCÓN',
 	'Falco peregrinus',
 	"""Está presente en todos los continentes, menos en la Antártida. En Colombia se puede observar a lo largo de todo 
 	el país. Se alimenta de una gran variedad de aves de diferentes tamaños, sus presas más comunes son patos o palomas. Es uno 
 	de los halcones de mayor tamaño de casi todo el continente americano.""",
 	imgur['0lD8LSP.jpg'],
 	dbpedia['Peregrine_falcon'],
 	eol['1049164'],
	'http://www.biodiversidad.co/fichas/4543',
	uniprot['8954'],
	gbif['2481047']
 )

fauna(
 	rioFrio['Fauna.rdf#gallinulaChloropus'],
 	'GALLINETA',
 	'Gallinula chloropus',
 	"""En Colombia se distribuye en Bogotá, La Guajira y Valle del Cauca. Suele medir entre 33-36 cms; su plumaje es de color 
 	gris, más oscuro en la cabeza y el cuello. Las patas se tornan de un color verdoso. Se la puede encontrar en climas 
 	húmedos y tropicales.""",
 	imgur['Odiee1N.jpg'],
 	dbpedia['Common_moorhen'],
 	eol['1049299'],
	'http://www.biodiversidad.co/fichas/4238',
	uniprot['9123'],
	gbif['5228199']
 )

fauna(
 	rioFrio['Fauna.rdf#turdusMerula'],
 	'MIRLA',
 	'Turdus merula',
 	"""El macho es de color negro, con el pico de color amarillo y un anillo del mismo color alrededor del ojo, tiene un 
 	vasto repertorio de cantos. La hembra es parda en la parte de arriba, con tintes rojizos en el pecho y mentón gris. 
 	Se alimenta de una gran variedad de insectos, gusanos también consume frutas y, a veces, semillas.""",
 	imgur['zEgRzcm.jpg'],
 	wikidata['Q21348750'],
 	eol['1177498'],
	'https://es.wikidatapedia.org/wikidata/Turdus_merula',
	uniprot['9187'],
	gbif['2490719']
 )

fauna(
 	rioFrio['Fauna.rdf#manacusManacus'],
 	'SALTARÍN',
 	'Manacus manacus',
 	"""Se distribuye en la región Amazónica, Orinoquía y en toda la región del Caribe. Se alimenta principalmente de bayas y 
 	en menor proporción de insectos. Es una de las especies más ruidosos, es diurna y arbórea. Además de Colombia, también se 
 	la puede encontrar en Argentina, Paraguay, Brasil, Ecuador, Guayanas, Trinidad y Tobago y Venezuela.""",
 	imgur['AGz0NXW.jpg'],
 	dbpedia['White-bearded_manakin'],
 	eol['919301'],
	'http://www.biodiversidad.co/fichas/2609',
	uniprot['196037'],
	gbif['2487672']
 )

fauna(
 	rioFrio['Fauna.rdf#onychorhynchusCoronatus'],
 	'ATRAPAMOSCAS',
 	'Onychorhynchus coronatus',
 	"""Su longitud es de 16.5 cms. El patrón de coloración es poco notable excepto en las raras ocasiones cuando despliega 
 	la cresta de una forma espectacular. En condiciones naturales se le ha visto abrirla durante el acicalamiento. La 
 	cola es naranja y el cuerpo café claro.""",
 	imgur['zUmhKr3.jpg'],
 	dbpedia['Royal_flycatcher'],
 	eol['1053240'],
	'http://www.icesi.edu.co/wikidata_aves_colombia/tiki-index.php?page=Atrapamoscas+Real',
	uniprot['360224'],
	gbif['2483680']
 )

fauna(
 	rioFrio['Fauna.rdf#podicepsMajor'],
 	'ZAMBULLIDOR',
 	'Podiceps major',
 	"""Mide 44 cms de largo. Se lo encuentra en cuerpos de agua como lagunas, lagos, arroyos, también en costas de mar. Se 
 	alimenta de peces que pesca sumergiéndose en el agua. Su cuello es largo, de color café rojizo; el pico es largo, 
 	puntiagudo y ligeramente encorvado hacia arriba.""",
 	imgur['hoEnP7x.jpg'],
 	dbpedia['Great_grebe'],
 	eol['1049444'],
	'http://www.icesi.edu.co/wikidata_aves_colombia/tiki-index.php?page=Podicipediformes',
	uniprot['555330'],
	gbif['2482062']
 )

fauna(
 	rioFrio['Fauna.rdf#amazonaOchrocephala'],
 	'LORO',
 	'Amazona ochrocephala',
 	"""Esta especie se distribuye en La Guajira, Magdalena, Cesar, Chocó, Amazonas, Bolívar, Caldas, Caquetá, Guaviare, 
 	Antioquia, Atlántico, Córdoba, Meta, Huila y Norte de Santander. Mide 36 cms, pico es pálido, cuerpo es de color 
 	verde principalmente.""",
 	imgur['MDcEBUq.jpg'],
 	dbpedia['Yellow-crowned_amazon'],
 	eol['1178062'],
	'http://www.biodiversidad.co/fichas/4151',
	uniprot['151761'],
	gbif['2479612']
 )

fauna(
 	rioFrio['Fauna.rdf#melopsittacusUndulatus'],
 	'PERICO',
 	'Melopsittacus undulatus',
 	"""Se alimenta preferiblemente de semillas de gramíneas y cultivos. Esta ave puede vivir hasta los 21 años de edad 
 	aproximadamente, es muy común en Autralia pero se ha introducido en otras regiones porque es usada como mascota.""",
 	imgur['9Iv5waw.jpg'],
 	dbpedia['Budgerigar'],
 	eol['914969'],
	'http://www.biodiversidad.co/fichas/5340',
	uniprot['13146'],
	gbif['2479798']
 )

fauna(
	rioFrio['Fauna.rdf#strigiformes'],
	'BÚHO',
	'Strigiformes',
	"""Tienen grandes ojos mirando hacia adelante lo que les da la visión amplia y poderosa, algunas especies tienen los 
	oídos dispuestos asimétricamente en la cabeza, es un ave nocturna que se alimenta de insectos y pequeños roedores.""",
	imgur['bsN0NdG.jpg'],
	dbpedia['Owl'],
	eol['696'],
	'https://es.wikidatapedia.org/wikidata/Strigiformes',
	uniprot['772159'],
	gbif['1450']
)

g.add( (rutaVueltaOriente['Fauna.rdf#bubulcusIbis'], UMBEL.isAbout, URIRef(rioFrio['Fauna.rdf'])) ) # Garza del ganado
g.add( (rutaVueltaOriente['Fauna.rdf#musMusculus'], UMBEL.isAbout, URIRef(rioFrio['Fauna.rdf'])) ) # Ratón casero

#print(g.serialize(format='pretty-xml'))	
