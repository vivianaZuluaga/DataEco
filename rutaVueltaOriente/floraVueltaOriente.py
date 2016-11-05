#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import WILDLIFE, CRUZAR, UMBEL, OWL
from utils.namespaces import rutaVueltaOriente, uniprot, dbpedia, wikidata, imgur, eol, gbif
from faunaVueltaOriente import g

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
    
    g.add( (URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaVueltaOriente.Flora)) )

flora(
	gbif['8138695'],
    "NACEDERO",
    "Trichanthera gigantea",
    """Árbol de hojas simples, opuestas, ápice acuminado, glabras o pubescentes en las venas, ovadas a oblongas, 
    pecíolo 1-5 cms de largo, limbo hasta 26 cms de largo por 14 cms de ancho. Inflorescencia en panícula terminal 5-15 cms 
    de largo. Flores con cáliz 10-12 mms de largo, tomentoso. El fruto es una cápsula de 1.5-2 cms de largo, pubescente.""",
    imgur['eGYfPLm.jpg'],
    dbpedia['Trichanthera'],
    eol['5637186'],
	'http://www.biodiversidad.co/fichas/3595',
	uniprot['681367']
)

flora(
    gbif['2767031'],
    "CABUYA",
    "Agave americana",
    """Planta perenne con distintos usos medicinales, alimenticios y textiles. Las hojas de entre 15 y 30 cms de ancho 
    y más de un metro de largo, salen todas desde el centro donde permanecen enrolladas a un tallo central y terminan 
    en el ápice en una aguja fina de unos 5 cms de longitud. Florece una sola vez en su vida.""",
    imgur['jPeW0t6.jpg'],
    dbpedia['Agave_americana'],
    eol['1083826'],
	'http://enciclopedia.us.es/index.php/Agave_americana',
	uniprot['39510']
)

flora(
    gbif['5407147'],
    "CHIRIMOYO",
    "Annona cherimola",
    """Árbol de hoja caduca, a excepción de aquellas zonas de invierno suave donde mantiene sus hojas ovaladas 
    hasta la primavera. Mide hasta 8 ms, es de tronco estrecho y copa ancha de forma redonda. Su fruto es la chirimoya, 
    en su interior contiene una pulpa comestible de color blanco con un sabor dulce, levemente ácido.""",
    imgur['tvWPVMm.jpg'],
    dbpedia['Annona_cherimola'],
    eol['1054913'],
	'http://www.lachirimoya.org/chirimoyo-arbol-chirimoya/',
	uniprot['49314']
)

flora(
    gbif['5407273'],
    "GUANÁBANA",
    "Annona muricata",
    """Árbol pequeño que llega a alcanzar hasta 10 ms de altura, de follaje compacto, hojas simples, coriáceas 
    verde oscuro, grandes y brillantes; muy susceptible al frío. Su fruto, la guanábana, mide entre 14 y 40 cms de 
    largo y entre 10 y 20 cms de ancho, la pulpa es blanca, jugosa, aromática y de sabor agridulce a dulce.""",
    imgur['o19PpMB.jpg'],
    dbpedia['Annona_muricata'],
    eol['1054863'],
	'https://encolombia.com/economia/agroindustria/cultivo/cultivodeguanabana/',
	uniprot['13337']
)

flora(
    gbif['2872695'],
    "ANTURIO",
    "Anthurium andraeanum",
    """Herbácea perenne de hojas verdes brillantes ovaladas o acorazonadas. Lo que se conoce como flor es una hoja 
    modificada llamada Espata que puede ser roja, blanca, amarilla, entre otros. La Espata rodea el espádice compuesto 
    por pequeñas flores que se agrupan alrededor de un eje central.""",
    imgur['6c0i38S.jpg'],
    dbpedia['Anthurium_andraeanum'],
    eol['1142454'],
	'https://es.wikipedia.org/wiki/Anthurium',
	uniprot['226677']
)

flora(
    gbif['2861312'],
    "FILODENDRO",
    "Philodendron spp",
    """Es una especie muy variable en su forma y su ecología. Presenta peciolos que miden de 283-108 cms de largo y de 
    4-17 mms de diámetro, de color verde oscuro. Sus hojas son de forma triangular ovada, miden de 27-101 cms de 
    largo por 25-90 cms de ancho, presentan ápice acuminado, haz de color verde oscuro y envés verde claro.""",
    imgur['QFt7Jif.jpg'],
    dbpedia['Philodendron'],
    eol['29342'],
	'http://www.biodiversidad.co/fichas/2197',
	uniprot['71613']
)

flora(
    gbif['114907430'],
    "MANO DE OSO",
    "Oreopanax floribundum",
    """Este árbol alcanza los 25 ms de altura. Su tronco recto y de corteza color gris pardusco ligeramente escamosa o 
    agrietada alcanza los 40 cms de diámetro. Su copa tiene forma de parasol, su follaje distribuido por 
    ramilletes es de color verde amarillento, sus ramas son gruesas, vidriosas.""",
    imgur['0zETXyz.jpg'],
    dbpedia['Dendropanax_colombianus'],
    eol['5056477'],
	'http://www.biodiversidad.co/fichas/1081',
	uniprot['52502']
)

flora(
    gbif['2734435'],
    "PALMA MOLINILLO",
    "Chamaedorea pinnatifrons",
    """Es una palma de tallo solitario de color verde, de hasta 2,5 ms de alto y entre 1-2 cms de diámetro. Sus hojas 
    tienen de 4 a 6 pinnas. Sus flores masculinas y femeninas son semejantes. Sus inflorescencias son de color naranja. 
    Sus frutos de forma elipsoide son de color naranja a negro según su madurez.""",
    imgur['DrULYAp.jpg'],
    wikidata['Q5764286'],
    eol['1091015'],
	'http://www.biodiversidad.co/fichas/1089',
	uniprot['348487']
)

flora(
    gbif['3170241'],
    "BENCENUCO",
    "Asclepias curassavica",
    """Es una hierba que alcanza hasta 1,5 ms de alto y tiene abundante exudado de color blanco, considerado tóxico. 
    Sus hojas son en forma de lanza miden hasta 12 cms de longitud y 2 cms de ancho. Sus flores de corola roja y 
    corona amarilla se disponen en umbelas. Su fruto es una cápsula que contiene numerosas semillas.""",
    imgur['6SuR7d7.jpg'],
    dbpedia['Asclepias_curassavica'],
    eol['581283'],
	'http://www.biodiversidad.co/fichas/1100',
	uniprot['52823']
)

flora(
    gbif['5391845'],
    "CADILLO",
    "Bidens pilosa",
    """Hierba pequeña, erecta anual que crece hasta 1 m de altura. Tiene hojas verde intenso dentadas, bordes 
    espinosos y produce pequeñas flores amarillas y fruto negro. Su raíz tiene un aroma distintivo similar al de 
    una zanahoria. Es originaria de la selva amazónica y otras áreas tropicales de América del Sur.""",
    imgur['f1339X1.jpg'],
    dbpedia['Bidens_pilosa'],
    eol['579063'],
	'http://www.biodiversidad.co/fichas/3516',
	uniprot['42337']
)

flora(
    gbif['3114910'],
    "SAUCE PLAYERO",
    "Tessaria integrifolia",
    """Árbol de 3-10 ms de altura de follaje persistente y copa pequeña. Se caracteriza por su silueta delgada. Sus 
    hojas simples son de color grisáceo y pubescentes. Sus flores son violáceas y se presentan en capítulos 
    terminales.""",
    imgur['KZlnfHV.jpg'],
    wikidata['Q6143507'],
    eol['5114705'],
	'http://www.biodiversidad.co/fichas/2100',
	uniprot['313942']
)

flora(
    gbif['5396865'],
    "OLIVÓN",
    "Vernonia brasiliana",
    """Arbusto de 1.50 ms de altura, bien ramificado, hojas oblongo–elípticas de 6x3 cms, que despiden un olor fuerte 
    al tocarlas. Inflorescencia en capítulos. Infrutescencias en forma de brochita.""",
    imgur['sjd3pJO.jpg'],
    wikidata['Q21302707'],
    eol['6181144'],
	'http://www.biovirtual.unal.edu.co/ICN/?controlador=ShowObject&accion=show&id=82852',
	uniprot['434694']
)

flora(
    gbif['5415081'],
    "TOTUMO",
    "Crescentia cujete",
    """Este árbol alcanza los 10 ms de altura. Sus ramas son largas y extendidas. Sus hojas tienen forma de espátula 
    y miden hasta 15 cms de largo. Sus flores son grandes de color púrpura amarillento. Su fruto de forma elipsoide tiene 
    una cáscara dura y no se abre por si solo, sus semillas son numerosas.""",
    imgur['wcKphwP.jpg'],
    dbpedia['Crescentia_cujete'],
    eol['578228'],
	'http://www.biodiversidad.co/fichas/1396',
	uniprot['1125401']
)

flora(
    gbif['3172537'],
    "GUAYACÁN ROSADO",
    "Tabebuia rosea",
    """Árbol de 15 a 30 ms de altura y de 90 cms de diámetro con un tronco recto. Sus hojas, compuestas de 5 folíolos 
    de borde liso y arreglados como los dedos de una mano, se caen durante la estación seca. Florece cuando ha perdido 
    las hojas; las flores son muy atractivas, se agrupan en racimos de color blanco o rosado.""",
    imgur['QFrVu0e.jpg'],
    dbpedia['Tabebuia_rosea'],
    eol['596778'],
	'https://biota.wordpress.com/2008/12/25/el-cultivo-del-roble-de-sabana-tabebuia-rosea/',
	uniprot['429709']
)

flora(
    gbif['3152240'],
    "BALSO",
    "Ochroma pyramidale",
    """Árbol de los bosques tropicales, puede alcanzar hasta 40 ms de altura. Flores de color blanco-amarillento. 
    Los frutos son cápsulas con numerosas semillas cubiertas por un algodón castaño claro. Es adecuado para recuperar 
    áreas degradadas. Produce la madera de menor densidad, empleada en la fabricación de juguetes.""",
    imgur['Yf3t4i0.jpg'],
    dbpedia['Ochroma_pyramidale'],
    eol['584793'],
	'http://www.biodiversidad.co/fichas/388',
	uniprot['66662']
)

flora(
    gbif['7649215'],
    "NOGAL CAFETERO",
    "Cordia alliodora",
    """Árbol de tamaño mediano a grande, que en estado maduro alcanza una altura superior a los 30 ms 
    y hasta 1 m de diámetro. De fuste recto, cilíndrico y con frecuencia limpio de ramas en un 50 a 60% de 
    la altura total. Corteza externa blancuzca, algo fisurada, dura y de grosor medio. Flores blancas.""",
    imgur['aUOYVfk.jpg'],
    dbpedia['Cordia_alliodora'],
    eol['580043'],
	'http://maderas.ut.edu.co/especies/pagina_especie.php?especie=LAUREL',
	uniprot['246517']
)

flora(
    gbif['7757322'],
    "QUICHES",
    "Bromelia spp",
    """Planta con hojas arrosetadas y sin tallo aparente. Crece encima de las ramas y troncos de los árboles. Las 
    hojas forman una especie de “estanque” en el centro de la roseta, donde se acumula agua. Lo más llamativo son las 
    flores que, en realidad, son hojas que toman un color diferente.""",
    imgur['jgbdHkv.jpg'],
    dbpedia['Bromelia'],
    eol['33260'],
	'http://www.opepa.org/index.php?option=com_content&task=view&id=236&Itemid=30',
	uniprot['4616']
)

flora(
    gbif['2956947'],
    "MARTIN GALVES",
    "Senna alata",
    """Arbusto de 1 a 7.5 ms de altura, con ramas robustas y el follaje joven pubescente. Hojas de 30 - 100 cms de 
    longitud; flores amarillas vistosas, en racimos terminales o situados en axilas superiores; semillas aplanadas. Las 
    hojas poseen propiedades laxantes, antimicrobianas y fungicidas, utilizadas para curar problemas de piel.""",
    imgur['MopkM3T.jpg'],
    dbpedia['Senna_alata'],
    eol['703879'],
	'https://es.wikipedia.org/wiki/Senna_alata',
	uniprot['53923']
)

flora(
    gbif['2957438'],
    "FLOR AMARILLO",
    "Senna spectabilis",
    """Árbol de 8 a 10 ms de altura y de 40 cms de diámetro en el tronco. Su copa tiene forma globosa. Su corteza es 
    marrón oscura y rugosa. Es de follaje caduco. Hojas compuestas, pinnadas, de color verde medio, discoloras y 
    pubescentes. Flores amarillas que forman inflorescencias terminales. Sus frutos son legumbres cilíndricas.""",
    imgur['YX0s7N2.jpg'],
    dbpedia['Senna_spectabilis'],
    eol['418255'],
	'http://lailahuber.blogspot.com.co/2011_01_01_archive.html',
	uniprot['347003']
)

flora(
    gbif['8474174'],
    "PAPAYUELA",
    "Carica goudotiana",
    """Planta que alcanza hasta 4 ms de altura, tallo grueso en la base y se adelgaza en la parte superior. Hojas 
    pecioladas de 17 a 34 cms, presenta flores de color amarillo-crema masculinas, femeninas y hermafroditas. El fruto 
    es una baya ovoide comestible de color amarillo al madurar, con múltiples semillas.""",
    imgur['2d6mzrP.jpg'],
    dbpedia['Vasconcellea_goudotiana'],
    eol['5731417'],
	'http://www.biodiversidad.co/fichas/5165',
	uniprot['262682']
)

flora(
    gbif['2984472'],
    "YARUMO",
    "Cecropia sp",
    """Árbol de 7 a 15 ms; tallo leñoso recto con anillos marcados, de color verde-grisáceo, algunas 
    veces ramificado desde la parte baja, pocas ramas y ubicadas en la parte alta. Hojas pecioladas, grandes, con 8-10 
    lóbulos, ásperas al tacto, palmeadas. Inflorescencias con espinas pendientes de un mismo pedúnculo.""",
    imgur['XkxkEpT.jpg'],
    dbpedia['Yarumo'],
    eol['61334'],
	'http://docplayer.es/6336435-Mangifera-indica-familia-anacardiaceae-mango.html',
	uniprot['77071']
)

flora(
    gbif['5421056'],
    "CUCHARO",
    "Clusia minor",
    """Árbol que alcanza hasta los 10 ms de altura; tiene ramitas algo angulosas; las hojas obovadas, 
    cartilaginosas, de 5-10 cms de largo, con peciolo delgado de 1-2 cms. Las inflorescencias con 4-5 pétalos 
    blancos o rosados. Fruto subgloboso u obovoide de 2 cms de longitud.""",
    imgur['4gOFj8B.jpg'],
    wikidata['Q5775222'],
    eol['584881'],
	'https://es.wikipedia.org/wiki/Clusia_minor',
	uniprot['156471']
)

flora(
    gbif['2874515'],
    "ZAPALLO",
    "Cucurbita maxima",
    """Las hojas de esta planta presentan 5 lóbulos, tienen vellos suaves, y margen dentado. Sus frutos son de forma 
    oval o redondeada, miden hasta 2 ms de diámetro, son carnosos, su interior es de color amarillo o rojo cuando maduros. 
    Sus semillas son de color blanco a café.""",
    imgur['03w1Evy.jpg'],
    dbpedia['Cucurbita_maxima'],
    eol['584406'],
	'http://www.biodiversidad.co/fichas/1342',
	uniprot['3661']
)

flora(
    gbif['3694437'],
    "COCA MONTAÑERA",
    "Erythroxylum ulei",
    """Arbusto muy ramificado que crece 1-5 ms de altura. La planta se cosecha en el medio silvestre para uso local 
    como medicina para las cefaleas, adontalgias y los resfriados. Se conoce también como Siona o Kofán.""",
    imgur['e0D1v7t.jpg'],
    wikidata['Q15379800'],
    eol['5404247'],
	'http://www.biodiversidad.co/fichas/3600',
	uniprot['13511']
)

flora(
    gbif['8033909'],
    "ACALIFA",
    "Acalypha macrostachya",
    """Árbol que alcalza 1–8 ms de altura, tallos jóvenes generalmente fuertes y con médula grande, densamente vellosos 
    a escasamente puberulentos. Hojas ovadas de 10–25 cms de largo y 6–18 cms de ancho, ápice generalmente acuminado. 
    Inflorescencias estaminadas con pubescencia como la de los tallos jóvenes.""",
    imgur['1REwEIV.jpg'],
    wikidata['Q9574549'],
    eol['1143557'],
	'http://hergol.biologia.ucr.ac.cr/taxa/index.php?taxon=1145&cl=Lista%20de%20plantas%20del%20Refugio%20de%20VS%20Golfito',
	uniprot['681401']
)

flora(
    gbif['3059672'],
    "SANGREGAO",
    "Croton gossypiifolius",
    """Árbol que alcanza hasta 16 ms de altura. Hojas color verde claro. Corteza externa café, interna blanca, 
    desprende en placa. Inflorescencias con tomento amarillo. Conocido como sangre de drago, debido a la savia 
    roja y viscosa que exuda su corteza, ampliamente utilizada en la medicina tradicional Latinoamericana.""",
    imgur['OWQrNxM.jpg'],
    wikidata['Q3004383'],
    eol['1146430'],
	'http://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S0370-59432013000300003',
	uniprot['323053']
)

flora(
    gbif['3067261'],
    "LECHERO (CAUCHO)",
    "Euphorbia cotinifolia",
    """Árbol semicaducifolio muy ramificado, llega a alcanzar 4-5 ms de altura, con la corteza clara y lisa. Hojas 
    simples, opuestas, base redondeada, intenso colorido al exponerse al sol. Flores amarillentas de escasa 
    importancia ornamental. Especie venenosa en todas sus partes, especialmente el látex.""",
    imgur['QESKUE8.jpg'],
    dbpedia['Euphorbia_cotinifolia'],
    eol['1145074'],
	'http://www.biodiversidad.co/fichas/921',
	uniprot['457243']
)

flora(
    gbif['5380041'],
    "HIGUERILLA",
    "Ricinus communis",
    """Arbusto perenne muy ramificado que alcanza entre 2 y 4 metros de altura, de raíz superficial y 
    tallo erecto, color rojo-vinoso, recubierto por una tenue capa de cera. Hojas grandes, alternas, pigmentación 
    rosada. Florece casi todo el año, pero sobre todo en verano. De las semillas se obtiene "aceite de ricino".""",
    imgur['iKojJu1.jpg'],
    dbpedia['Ricinus_communis'],
    eol['1151096'],
	'http://www.herbotecnia.com.ar/exo-ricino.html',
	uniprot['3988']
)

flora(
    gbif['8311514'],
    "PÍSAMO",
    "Erythrina poeppigiana",
    """Árbol grande que puede alcanzar hasta 35 ms de altura. Presenta aguijones gruesos. Las flores son de color 
    rojo-anaranjado y se encuentran en racimos erectos. Los frutos son legumbres de hasta 25 cms de largo. Produce gran 
    cantidad de follaje que sirve como abono en cultivos, regenera suelos al fijar nitrógeno.""",
    imgur['vYig5sj.jpg'],
    wikidata['Q5837321'],
    eol['416279'],
	'http://aprendeenlinea.udea.edu.co/ova/?q=node/455',
	uniprot['647292']
)

flora(
    gbif['2953986'],
    "MATARRATÓN",
    "Gliricidia sepium",
    """Árbol perenne, con raíces profundas; crece de 10–15 ms de altura y 40 cms de diámetro en el tallo, produce 
    muchas  ramificaciones. Hojas compuestas de 2–6 cms de largo, de forma elíptica y de color verde en la 
    superficie. Flores en racimos de 2 cms de largo, color entre rosa y púrpura claro.""",
    imgur['9fCUTaf.jpg'],
    dbpedia['Gliricidia_sepium'],
    eol['642632'],
	'http://www.tropicalforages.info/Multiproposito/key/Multiproposito/Media/Html/Gliricidia%20sepium.htm',
	uniprot['167663']
)

flora(
    gbif['2951499'],
    "CONGOLO",
    "Mucuna pruriens",
    """Planta anual, arbusto trepador con largos zarcillos que le permiten llegar a más de 15 ms. Sus granos son 
    blancos, lavanda o púrpura; flores y vainas cubiertas de pelos anaranjados, causantes de severa hinchazón y alergia
    si se ponen en contacto con la piel. Se usa en la medicina tradicional.""",
    imgur['bie0GOH.jpg'],
    wikidata['Q953611'],
    eol['645045'],
	'https://es.wikipedia.org/wiki/Mucuna_pruriens',
	uniprot['157652']
)

flora(
    gbif['2880642'],
    "ROBLE",
    "Quercus humboldtii",
    """Árbol monoico caducifolio, de aproximadamente 25 ms de altura, con copa amplia y redondeada. Hojas glabras 
    deciduas agrupadas al final de las ramas. Flores pequeñas, apétalas de color amarillento. El fruto es una nuez o 
    bellota ovoide sostenida en la base por una cúpula escamosa. Su madera es de baja calidad, pero muy resistente.""",
    imgur['gxKVrLI.jpg'],
    dbpedia['Quercus_humboldtii'],
    eol['1151543'],
	'http://www.uco.edu.co/floraorienteantioquia/fagaceae/Quercus-humboldtii-Bonpl/Paginas/default.aspx',
	uniprot['3511']
)

flora(
    gbif['7898917'],
    "CUERNO VENADO",
    "Xylosma prunifolium",
    """Árbol con espinas de hasta 5 cms, ramificadas en la base del tronco y luego se hacen simples y muy agudas en 
    las ramas, a veces ausentes, hojas de base cuneada a redondeada, glabras.""",
    imgur['ZE9vHOS.jpg'],
    wikidata['Q17562923'],
    eol['5731214'],
	'https://books.google.com.co/books?id=Omzm3LW0mZUC&pg=PA291&lpg=PA291&dq=luego+se+hacen+simples+y+muy+agudas+enlas+ramas,+a+veces+ausentes,+hojas+de+base+cuneada+a+redondeada,+glabras&source=bl&ots=uF5rXApwK9&sig=-mw17zF-AVrKieGSFcKcMRSJ02E&hl=es&sa=X&redir_esc=y#v=onepage&q=luego%20se%20hacen%20simples%20y%20muy%20agudas%20enlas%20ramas%2C%20a%20veces%20ausentes%2C%20hojas%20de%20base%20cuneada%20a%20redondeada%2C%20glabras&f=false',
	uniprot['179718']
)

flora(
    gbif['2760842'],
    "PLATANILLO",
    "Heliconia griggsiana",
    """Heliconia de tamaño mediano, con inflorescencias colgantes, espiraladas, las cuales tienen brácteas 
    rojizo-rosadas,amarillas o verdes, con quillas de color morado oscuro, cubiertas por un estrato fino, ceroso, 
    de tonalidad blanca. Las hojas tienen la vena central marrón y el envés blancuzco.""",
    imgur['KmDXQiB.png'],
    wikidata['Q15329832'],
    eol['1118024'],
	'http://www.rarepalmseeds.com/es/pix/HelGri.shtml',
	uniprot['796949']
)

flora(
    gbif['8708187'],
    "LAUREL JIGUA",
    "Cinnamomum cinnamomifolia",
    """Árbol que alcanza los 18 ms de altura y 40 cms de diámetro en su tronco; su copa es globosa; su follaje de 
    color verde oscuro y brillante; su ramificación es abundante. Las hojas son simples, alternas, dispuestas en forma 
    de hélices. Las flores son de color blanco, pequeñas y fragantes. La madera y las hojas poseen un agradable olor.""",
    imgur['RDUpfjg.jpg'],
    wikidata['Q6074391'],
    eol['488334'],
	'https://es.wikipedia.org/wiki/Phoebe_cinnamomifolia',
	uniprot['13428']
)

flora(
    gbif['3033969'],
    "AGUACATILLO",
    "Licaria sp",
    """Árbol de hoja perenne con una copa amplia y redondeada; puede alcanzar hasta 16 ms de altura. El tronco puede 
    ser de 20 cms de diámetro. Todas las partes de la planta tienen un aroma picante. El árbol se extrae de la 
    naturaleza por su madera, que se utiliza a nivel local en la fabricación de muebles.""",
    imgur['hUD4xVp.jpg'],
    wikidata['Q5226729'],
    eol['61876'],
	'https://es.wikipedia.org/wiki/Licaria',
	uniprot['128634']
)

flora(
    gbif['5421429'],
    "HUESITO",
    "Malpighia glabra",
    """Alcanza los 8 ms de altura. El tronco es usualmente bajo y torcido, la copa es baja y densa. Las hojas son 
    pequeñas y sus flores de color rosado. El fruto mide entre 1-25 cms de diámetro; es redonda con tres costillas, 
    su color varía entre amarillo anaranjado y rojo oscuro de acuerdo al grado de madurez.""",
    imgur['OKgpAfF.jpg'],
    dbpedia['Malpighia_glabra'],
    eol['398658'],
	'http://www.biodiversidad.co/fichas/1522',
	uniprot['71611']
)

flora(
    gbif['3188585'],
    "NIGUITO",
    "Miconia sp",
    """Arbusto con copa redondeada, hojas simples opuestas, el borde es finamente aserrado, haz verde oscuro. 
    Inflorescencias muy tupidas en panículas terminales, de color verde pálido. Las flores son pequeñas y amarillentas, 
    blancas o rosadas. El fruto es una baya de color rojo al madurar. Se utiliza como leña.""",
    imgur['703ZLjF.jpg'],
    dbpedia['Miconia'],
    eol['60394'],
	'http://www.biodiversidad.co/fichas/4918',
	uniprot['263288']
)

flora(
    gbif['3190504'],
    "CEDRO MACHO",
    "Guarea trichilioides",
    """Árbol que presenta una base estriada, el tronco recto y sin ramificaciones. Alcanza una altura entre 25-30 ms 
    y un diámetro de hasta 1 m. Las hojas son de gran tamaño, de 20-60 cms de largo y se encuentran dispuestas de manera 
    alterna. La corteza es áspera, con muchas fisuras longitudinales y de color pardo, con un evidente matiz rojizo.""",
    imgur['gqHHXy3.jpg'],
    dbpedia['Guarea_guidonia'],
    eol['581915'],
	'http://www.biodiversidad.co/fichas/669',
	uniprot['43908']
)

flora(
    gbif['3190491'],
    "TROMPILLO",
    "Trichilia pallida",
    """Árbol de hasta 20 ms de altura, de madera blanda, corteza viva quebradiza, fibrosa y delgada. Hojas de 15 cms 
    de largo por 10 cms de ancho, compuestas, alternas, dispuestas en forma de hélice. Flores pequeñas, de color crema y 
    dispuestas en inflorescencias axilares sobre sus ramitas. Frutos capsulares dehiscentes, con pelitos cortos y suaves.""",
    imgur['IGn4Hl0.jpg'],
    wikidata['Q15526615'],
    eol['592301'],
	'http://www.biodiversidad.co/fichas/2271',
	uniprot['597422']
)

flora(
    gbif['8225137'],
    "AROMO",
    "Acacia farnesiana",
    """Arbusto muy ramificado desde la base que alcanza 3-5 m de altura. Tronco de corteza oscura y ramaje tortuoso 
    en zig-zag. Follaje semicaduco en ocasiones. Hojas con dos espinas blancas y rectas de 2-3 cms de 
    longitud en la base de las mismas. Flores de color amarillo dorado, fragantes, de 1-1.5 cms de diámetro.""",
    imgur['WqonGiJ.jpg'],
    dbpedia['Acacia_farnesiana'],
    eol['684149'],
	'http://www.biodiversidad.co/fichas/2237',
	uniprot['72368']
)

flora(
    gbif['2981948'],
    "CARBONERO",
    "Calliandra pittieri",
    """Árbol de unos 5 ms de altura, su follaje y copa en forma de parasol, al igual que sus flores en pomos 
    blanco-rosados, ayudan a reconocerlo. La hoja es pequeña; el fruto es una vaina o legumbre que al calentar el sol 
    expulsa las semillas. Casi todo el año se observa esta especie con flores y frutos.""",
    imgur['lxjvAyg.jpg'],
    wikidata['Q15492902'],
    eol['647621'],
	'http://www.biodiversidad.co/fichas/3559',
	uniprot['226080']
	
)

flora(
    gbif['5357677'],
    "GUAMO",
    "Inga edulis",
    """Árbol con 8-15 ms de altura, tronco bajo, ramificando algunas veces casi desde la base, copa algo rala. Hojas 
    compuestas; flores con cáliz verdoso y corola blanquecina, perfumadas. El fruto es una vaina cilíndrica 
    indehiscente, de color verde. Las semillas son negras, cubiertas por una pulpa blanca, suave y azucarada.""",
    imgur['mqQyaGg.jpg'],
    dbpedia['Inga_edulis'],
    eol['8685157'],
	'https://es.wikipedia.org/wiki/Guama_(fruta)',
	uniprot['199163']
)

flora(
    gbif['2969284'],
    "DORMIDERA",
    "Mimosa pudica",
    """Planta herbácea de unos 50 cms de altura y perennifolia. Tallo espinoso, ramificado, leñoso, con pelos rígidos en 
    dirección a la parte terminal. Capacidad de plegar las hojas cuando las tocan; esto  se debe a un mecanismo de 
    defensa de la planta. Flores lilas claras o rosado brillante con estambres prominentes y vistosos.""",
    imgur['DR3zxji.jpg'],
    dbpedia['Mimosa_pudica'],
    eol['417449'],
	'http://www.biodiversidad.co/fichas/3636',
	uniprot['76306']
)

flora(
    gbif['2962831'],
    "CHIMINANGO",
    "Pithecellobium dulce",
    """Árbol de 5-20 ms, espinoso; hojas compuestas. Las flores son amarillentas o blanco verdosas y se producen 
    en cabezuelas como de 1 cm de diámetro, dispuestas en racimos axilares o terminales. La legumbre mide unos 15 
    cms es retorcida y encorvada, con semillas negras y brillantes, rodeadas de un arilo carnoso, comestible.""",
    imgur['rVRJY0L.jpg'],
    dbpedia['Pithecellobium_dulce'],
    eol['642629'],
	'http://www.biodiversidad.co/fichas/3546',
	uniprot['404691']
)

flora(
    gbif['2962824'],
    "ESPINO DE MONO",
    "Pithecellobium lanceolatum",
    """Arbustos de 0.75-12 ms de altura, corteza estriada. Hojas bipinnadas, cada pinna exactamente con 2 
    foliolos. Flores fragantes con perianto verde pálido con pelos densos, agrupadas en inflorescencias, 
    largas, laxas, solitarias o en parejas. Frutos 1-2 por espiga, pedunculados, valvas curvadas, rojos en la madurez, lampiños.""",
    imgur['I3dpH20.jpg'],
    wikidata['Q15459116'],
    eol['642793'],
	'http://www.biodiversidad.co/fichas/2153',
	uniprot['1129495']
)

flora(
    gbif['2972961'],
    "SAMÁN",
    "Pithecellobium saman",
    """Árbol grande y umbraculiforme que llega a medir 60 ms de altura. La densa y simétrica copa puede alcanzar 80 
    ms de ancho. Cuenta con un tronco corto, grueso y una corteza gris oscura. Las hojas son perennes y 
    de disposición alternada, de 25–40 cms de largo. Las flores de color entre rosado y verde.""",
    imgur['9oRNcJq.jpg'],
    dbpedia['Pithecellobium_saman'],
    eol['46244366'],
	'http://documents.mx/documents/arbol-emblematicos-de-los-estados.html',
	uniprot['76910']
)

flora(
    gbif['2984660'],
    "GUAIMARO",
    "Brosimum alicastrum",
    """Árbol de gran porte que puede alcanzar 45 ms, y alcanza un diámetro aproximado de 1.5 ms en su tronco. Su copa 
    es generalmente piramidal y densa. las flores son numerosas. La infrutescencias es globosa, mide de 1.5-2 cms de 
    diámetro, al madurar son amarillas, parduscas o anaranjadas.""",
    imgur['RSCjvMG.jpg'],
    dbpedia['Brosimum_alicastrum'],
    eol['596209'],
	'http://www.biodiversidad.co/fichas/1368',
	uniprot['194253']
)

flora(
    gbif['7262619'],
    "HIGUERÓN",
    "Ficus glabrata",
    """Árbol grande de hasta 40 ms de altura, con follaje vistoso. Las hojas son alargadas y grandes. Los frutos tienen 
    forma de higo y son verdes. Planta con uso medicinal, sus frutos son laxantes y alimento para avifauna, la madera 
    es usada en cajonería y formaleta. Además, esta especie es empleada en la protección de fuentes de agua.""",
    imgur['Vw76IUy.jpg'],
    dbpedia['Ficus_glabrata'],
    eol['46243853'],
	'http://www.biodiversidad.co/fichas/1026',
	uniprot['182113']
)

flora(
    gbif['7262410'],
    "MATAPALOS",
    "Ficus involuta",
    """Árbol "estrangulador", que suele crecer encima de otros árboles, abrazándolos con sus fuertes raíces. Puede 
    alcanzar hasta 20 ms de altura. Hojas alternas, algo gruesas, brillantes, con venas notorias. "Frutos" (siconos) 
    normalmente pequeños y redondos, usualmente rojizos o amarillentos adornados con motas.""",
    imgur['2YhtzfX.jpg'],
    dbpedia['Ficus_aurea'],
    eol['594677'],
	'https://elmundoenimagenes13.wordpress.com/2014/11/29/ficus-estrangulador-en-monteverde-costa-rica/',
	uniprot['319808']
	#http://www.biodiversidad.co/fichas/1056
)

flora(
    gbif['3169446'],
    "CHAGUALO",
    "Myrsine guianensis",
    """Árbol de todos los climas, está adaptado para prosperar en circunstancias difíciles, de 6-21 ms de altura. Hojas 
    alternas, lustrosas por el haz, claras por el envés, son duras. Flores y frutos (bayas pequeñas) crecen agrupados 
    en bolitas apretadas a lo largo de las ramas. Los pequeños frutos maduran en negro.""",
    imgur['GEQ3Wfq.jpg'],
    wikidata['Q6035263'],
    eol['486714'],
	'https://sites.google.com/site/reservachagualos/biota-en-los-chagualos/myrsine-guianensis',
	uniprot['681410']
)

flora(
    gbif['5417812'],
    "ARRAYÁN",
    "Eugenia biflora",
    """Arbolito de 3-5 ms de altura, frutos aromáticos, de color rojizo pasando a negro. se distribuye en paises como
    Belice, Bolivia, Brasil, República Dominicana, Jamaica, Puerto Rico, Islas Virginias, Colombia, Costa Rica, Ecuador, 
    El Salvador, Guayanas Francesa, Guatemala, Guyanas, Honduras, México, Panamá, Perú, Surinam, Venezuela.""",
    imgur['2USVhtl.jpg'],
    wikidata['Q15357705'],
    eol['2508566'],
	'http://www.biodiversidad.co/fichas/3779',
	uniprot['1453369']
)

flora(
    gbif['5420509'],
    "GUAYABO CIMARRÓN",
    "Psidium guineense",
    """Árbol pequeño que alcanza un tamaño de 1-7 ms de altura, una planta de crecimiento relativamente lento. Las 
    hojas son angostas en los extremos y a veces los bordes están enroscados. Las flores son blancas y los frutos 
    globosos, de color verde-amarillento.""",
    imgur['Zmy88xF.jpg'],
    dbpedia['Psidium_guineense'],
    eol['2508601'],
	'https://es.wikipedia.org/wiki/Psidium_guineense',
	uniprot['260140']
)

flora(
    gbif['3084012'],
    "ANAMÚ",
    "Petiveria alliacea",
    """Planta herbácea perenne, crece hasta aproximadamente 1 m de altura. En algunos lugares se le conoce como 
    "yerba de ajo" debido al fuerte olor a ajo que emana, especialmente de las raíces. La raíz posee propiedades 
    anestésicas y analgésicas y se considera más poderosa que las hojas.""",
    imgur['ApOc6ry.jpg'],
    dbpedia['Petiveria_alliacea'],
    eol['594860'],
	'http://www.saludparati.com/anamu.htm',
	uniprot['46142']
)

flora(
    gbif['3086337'],
    "CORDONCILLO",
    "Piper aduncum",
    """Árbol pequeño de 2-6 ms de alto, profusamente ramificado, con nudos hinchados y prominentes, a menudo de color 
    rojizo, tallos verde pálidos, amarillentos o de color marrón. Inflorescencias curvadas en flor y/o fruto; flores 
    densamente agrupadas sobre el raquis. Fruto redondeado-obpiramidal, glabro, de color marrón cuando seco.""",
    imgur['230L7S7.jpg'],
    dbpedia['Piper_aduncum'],
    eol['486213'],
	'http://www.biodiversidad.co/fichas/3577',
	uniprot['130377']
)

flora(
    gbif['4155046'],
    "GUADUA RAYADA",
    "Guadua angustifolia bicolor",
    """Bambú gigante, espinoso, con culmos erectos y huevos que alcanzan alturas hasta de 25 ms y diámetros entre 10-25 
    cms. Sus entrenudos tienen paredes hasta de 2 cms de espesor. Se diferencia de la especie tipo por tener rayas 
    longitudinales amarillas sobre el culmo verde. Tiene gran potencial para la fabricación de artesanías.""",
    imgur['D5VIXzt.jpg'],
    wikidata['Q1491422'],
    eol['5846334'],
	'https://guaduabambucolombia.com/guadua-inmunizada/vivero/',
	uniprot['323898']
)

flora(
    gbif['4142909'],
    "CARRIZO",
    "Rhipidocladum racemiflorum",
    """Bambú de 10–15 ms de largo y 5–10 mms de ancho, erecto en la base, tallo hueco, generalmente decumbente en 
    la vegetación aledaña. Un promedio de 50 ramas por nudo, no verticiladas sino creciendo en forma de abanico en la 
    base. Las ramas primarias de 35 cms de largo; cúlmeas lisas y brillantes. Más bien delgado y frágil.""",
    imgur['fFAovYc.jpg'],
    wikidata['Q15521956'],
    eol['5822829'],
	'www.bambumex.org/paginas/Rracemiflorum.pdf',
	uniprot['464972']
)

flora(
    gbif['5594205'],
    "CIPRÉS DE ESTACÓN",
    "Amyris pinnata",
    """Árbol que crece hasta 10 ms de altura, 4 ms de fuste y 30 cms de diámetro. Corteza verdosa por fuera y 
    amarillenta por dentro; sin exudado pero con olor a limón o ruda. Hojas compuestas, de 15-25 cms. Flores 
    blanco–verdosas, pequeñas que dan lugar a frutos en un folículo marrón, con una semilla negra.""",
    imgur['gUuiZB0.jpg'],
    wikidata['Q15387993'],
    eol['5619428'],
	'http://www.biodiversidad.co/fichas/3772',
	uniprot['1123434']
)

flora(
    gbif['3190087'],
    "JUSTARRAZÓN",
    "Zanthoxylum monophyllum",
    """Árbol pequeño alcanza un tamaño de 3-8 ms de altura, generalmente con ramitas y tronco espinosos. 
    Flores pequeñas blancuzcas. Corteza de color gris a castaño, untanto lisa y con grietas verticales. Hojas
    lampiñas, de color verde, lustrosas en el haz y más pálidas en el envés.""",
    imgur['ceJ3yfH.jpg'],
    wikidata['Q6170902'],
    eol['582230'],
	'https://books.google.com.co/books?id=76LnQRyBNS4C&pg=PA273&lpg=PA273&dq=Muchas+flores+peque%C3%B1as+blancuzcas.+Corteza+de+color+gris+a+casta%C3%B1o+es+un+tanto+lisa+y+tiene+grietas+verticales&source=bl&ots=cO6FbZyRBj&sig=50szGhYLic-cmIZYtuzDr0GI9zA&hl=es&sa=X&redir_esc=y#v=onepage&q=Muchas%20flores%20peque%C3%B1as%20blancuzcas.%20Corteza%20de%20color%20gris%20a%20casta%C3%B1o%20es%20un%20tanto%20lisa%20y%20tiene%20grietas%20verticales&f=false',
	uniprot['43887']
)

flora(
    gbif['7269222'],
    "TACHUELO",
    "Zanthoxylum rhoifolium",
    """Árbol de 5-9 ms de altura, copa aplanada, fuste recto y corto, tronco grisáceo o castaño, acanalado en la base, 
    fuertes aguijones, aguijones en rámulas y hojas. Ramificaciones largas, ascendentes. Follaje siempreverde, hojas 
    compuestas, alternas, pinnadas, con espinas rectas dorsales, raquis canaliculado, con pelos estrellados.""",
    imgur['itfk4vL.jpg'],
    dbpedia['Zanthoxylum_rhoifolium'],
    eol['39954266'],
	'https://es.wikipedia.org/wiki/Zanthoxylum_rhoifolium',
	uniprot['549434']
)

flora(
    gbif['3785984'],
    "MESTIZO",
    "Cupania cinerea",
    """Árbol de hasta 20 ms de altura y 60 cms de diámetro en su tronco, de corteza lisa. Hojas de 20 a 32 cms de largo, 
    compuestas, alternas, dispuestas en forma de hélice, borde aserrado. Flores de 7 mms de diámetro, blancas, agrupadas 
    en inflorescencias terminales. Frutos redondos, pubescentes café, con 3 semillas negras brillantes.""",
    imgur['JhBECIF.jpg'],
    wikidata['Q15547475'],
    eol['5627731'],
	'http://www.biodiversidad.co/fichas/1413',
	uniprot['298314']
)

flora(
    gbif['5421132'],
    "CHAMBIMBE",
    "Sapindus saponaria",
    """Árbol de unos 15 ms de alto, hojas alternas pinnadas; flores pequeñas, fragantes, muy abundantes en 
    inflorescencia terminal paniculada, 5 pétalos blancos que alternan con los sépalos; frutos globosos, amarillentos, 
    de 2 cms de diámetro, de envoltura translúcida; semillas duras, de color negro lustroso.""",
    imgur['NLfHDfp.jpg'],
    dbpedia['Sapindus_saponaria'],
    eol['582237'],
	'http://www.biodiversidad.co/fichas/1471',
	uniprot['171222']
)

flora(
    gbif['7333251'],
    "AZAFRÁN DE RAÍZ",
    "Escobedia scabrifolia",
    """Hierba perenne, erecta, que alcanza un tamaño de 40–100 cms de alto, glabra; tallo simple. Hojas opuestas. Flores 
    solitarias en las axilas de las hojas. Uso de sus raíces anaranjadas como colorante natural de los alimentos y uso 
    en la medicina popular; se ha comprobado que las flores tienen sustancias antibacteriales.""",
    imgur['zQoark4.jpg'],
    wikidata['Q21399372'],
    eol['5676853'],
	'http://agrodiversos.blogspot.com.co/p/blog-page.html?view=timeslide',
	uniprot['374682']
)

flora(
    gbif['2932389'],
    "FRIEGAPLATOS",
    "Solanum torvum",
    """Arbusto de hasta 2.5 ms de altura, cubierto de pelos estrellados (con las ramas libres, es decir unidas 
    únicamente en la base), armado de espinas dispersas rectas o algunas recurvadas. Hojas escasamente lobadas, 
    cubiertas con pelos estrellados; flores blancas. Frutos globosos, verdes, sin pelillos.""",
    imgur['n9zVGBJ.jpg'],
    dbpedia['Solanum_torvum'],
    eol['581201'],
	'http://www.conabio.gob.mx/malezasdemexico/solanaceae/solanum-torvum/fichas/ficha.htm',
	uniprot['119830']
)

flora(
    gbif['3152195'],
    "GUACIMO",
    "Guazuma ulmifolia",
    """Árbol de 2-20 ms con un tallo de 45 cms de diámetro, corteza externa agrietada. Hojas simples, agudas a acuminadas, 
    aserradas, estrellado-tomentosas; flores amarillentas, fragantes, enzimas axilares pequeñas; cáliz estrellado - 
    tomentoso, pétalos de 3 mms, fruto leñoso, globolo u oval, de 2-4 cms con tubérculos duros.""",
    imgur['RLlU52L.jpg'],
    dbpedia['Guazuma_ulmifolia'],
    eol['584815'],
	'http://www.biodiversidad.co/fichas/1243',
	uniprot['93772']
)

flora(
    gbif['7141666'],
    "ZURRUMBO",
    "Trema micrantha",
    """Árbol perennifolio, de 5-13 ms de altura con un diámetro de 6-20 cms. Copa en forma de sombrilla, abierta e 
    irregular. Hojas estipuladas, simples, alternas; de 5-12 cms de largo por 2-4 cms de ancho. Los árboles se 
    reconocen por sus ramas que crecen con una orientación típicamente horizontal o ligeramente colgantes.""",
    imgur['PXakwq0.jpg'],
    dbpedia['Trema_micrantha'],
    eol['231353'],
	'http://www.conabio.gob.mx/conocimiento/info_especies/arboles/doctos/69-ulmac2m.pdf',
	uniprot['28954']
)

flora(
    gbif['2984339'],
    "ORTIGA BRAVA",
    "Urera baccifera",
    """Arbusto de 1-6 ms de altura, tallos suculentos, con pelos urticantes. Hojas alternas, anchas, ovadas, base cordada 
    redondeada, borde irregularmente dentado con dientes grandes, envés pubescente con pelos urticantes sobre las nervaduras. 
    Flores masculinas globosas; flores femeninas en cimas escorpioides. Fruta con drupa jugosa.""",
    imgur['IVimLXQ.jpg'],
    dbpedia['Urera_baccifera'],
    eol['594148'],
	'http://www.biodiversidad.co/fichas/1247',
	uniprot['681502']
)

flora(
    gbif['4084063'],
    "PALO BLANCO",
    "Citharexylum kunthianum",
    """Arbusto que alcanza hasta 10 ms de altura, con ramas largas y extendidas. Frutos verdes y de color anaranjado 
    o morado intenso al madurar. Flores en racimos sencillos, blancos y fragantes, tubulosas, pequeñas, que producen 
    frutos abayados de 4 mms con el cáliz persistente, con 2 semillas aplanadas redondas.""",
    imgur['IrOLx8Z.jpg'],
    wikidata['Q15493663'],
    eol['5387105'],
	'http://www.biodiversidad.co/fichas/3777',
	uniprot['222864']
)

flora(
    gbif['8688754'],
    "VENTUROSA",
    "Lantana canescens",
    """Arbusto de hasta 2.5 ms de altura; tallos y ramas más o menos densamente canescente-estrigosos. Hojas lanceoladas, 
    la nervadura prominente. Flores densamente agrupadas, primero aglomeradas, pero alargándose y 
    generalmente oblongas en el fruto. Crece en selvas bajas caducifolias, en rocas calizas y sitios alterados.""",
    imgur['eDKstWg.jpg'],
    wikidata['Q15430229'],
    eol['487147'],
	'http://www1.inecol.edu.mx/publicaciones/resumeness/FLOVER/41-nash_II.pdf',
	uniprot['662443']
)

#Plantas presentes en la Ruta del Maíz
g.add( (gbif['3190638'], RDF.type, WILDLIFE.TaxonName) )
g.add( (gbif['5406697'], RDF.type, WILDLIFE.TaxonName) )
g.add( (gbif['2874484'], RDF.type, WILDLIFE.TaxonName) )
g.add( (gbif['5420380'], RDF.type, WILDLIFE.TaxonName) )
g.add( (gbif['4155017'], RDF.type, WILDLIFE.TaxonName) )
g.add( (gbif['5289743'], RDF.type, WILDLIFE.TaxonName) )
g.add( (gbif['8206387'], RDF.type, WILDLIFE.TaxonName) )
g.add( (gbif['2932944'], RDF.type, WILDLIFE.TaxonName) )
g.add( (gbif['5289798'], RDF.type, WILDLIFE.TaxonName) )
g.add( (gbif['3093023'], RDF.type, WILDLIFE.TaxonName) )
g.add( (gbif['2760874'], RDF.type, WILDLIFE.TaxonName) )
g.add( (gbif['3173930'], RDF.type, WILDLIFE.TaxonName) )

#print(g.serialize(format='pretty-xml'))
