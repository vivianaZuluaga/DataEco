#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import WILDLIFE, UMBEL, OWL, VCARD
from utils.namespaces import rutaAnillo, rutaMaiz, rutaVueltaOriente, rioFrio, dbpedia, wikidata, eol, imgur, gbif, uniprot
from lugaresAgricola import g

#g = Graph()

def fauna(uri, nombre_comun, nombre_cientifico, descripcion, imagen, uriLink1, uriLink2, ref, uriLink3, linkURI):
    g.add( (URIRef(uri), RDF.type, WILDLIFE.TaxonName) )
    g.add( (URIRef(uri), WILDLIFE.commonName, Literal(nombre_comun, lang="es") ) )
    g.add( (URIRef(uri), WILDLIFE.scientificName, Literal(nombre_cientifico, lang="la")) )
    g.add( (URIRef(uri), WILDLIFE.shortDescription, Literal(descripcion, lang="es")) )
    g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)))
    g.add( (URIRef(uri), WILDLIFE.kingdomName, Literal('Animal', lang="es")) )  
    g.add( (URIRef(uri), FOAF.isPrimaryTopicOf, URIRef(ref)) ) #Sitio web
    
    g.add( (URIRef(uri), OWL.sameAs, URIRef(uriLink1)) ) #Link RDF a DBpedia  
    g.add( (URIRef(uri), OWL.sameAs, URIRef(uriLink3)) ) #Link RDF a UniProt
    
    g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) ) #Links externos
    g.add( (URIRef(uri), RDFS.seeAlso, URIRef(uriLink2)) )
    
    g.add( ( URIRef(uri), UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) )
    g.add( (URIRef(uri), VCARD.category, Literal("FAUNA", lang='es')))
 
fauna(
    rutaAnillo['Fauna.rdf#lepidodactylusLugubris'],#uri
    "GUECO ENLUTADO, GUECO, GECO",#nombre comun
    "Lepidodactylus lugubris",#nombre cientifico
    """Mide aproximadamente 45 mms de longitud. Tiene un color de fondo pálido cremoso con un marrón oscuro o beige 
    superpuesto en zigzag. Pueden cambiar tonos de color entre blanco, marrón, rojizo-marrón, beige y gris. Sus partes 
    inferiores son siempre de color beige y, a veces moteado. Las crías son réplicas en miniatura de los adultos.""",#descrip
    imgur['wnDBsv4.jpg'],#imagen
    dbpedia['Lepidodactylus_lugubris'],#link
    eol['8832483'],
    'http://tuatera.com/fororeptiles/gecko-cuidados/lepidodactylus-lugubris-cuidados-informacion-terrario/',
    uniprot['47724'],
    gbif['5221610']
)

fauna(
    rutaAnillo['Fauna.rdf#basiliscusBasiliscus'],#uri
    "IGUANA JESUCRISTO",#nombre comun
    "Basiliscus basiliscus",#nombre cientifico
    """Alcanza una longitud total de aproximadamente 80 cms y pesa entre 200-500 gr. El color del dorso va desde el verde al 
    oliva-marrón, a marrón con rayas oscuras. El vientre es de color amarillo. Sus dedos son muy largos y tienen garras 
    afiladas. Los machos están adornados por una cresta y por una papada de color.""",#descrip
    imgur['x07f7b9.jpg'],#imagen
    dbpedia['Basiliscus_basiliscus'],
    eol['795614'],
    'http://www.waza.org/es/zoo/zoologico-virtual-galeria/basiliscus-basiliscus',
    uniprot['161134'],
    gbif['5221813']
)

fauna(
    rutaAnillo['Fauna.rdf#cercosauraArgulus'],#uri
    "LISA DE HOJARASCA",#nombre comun
    "Cercosaura argulus",#nombre cientifico
    """Lagartija de longitud máxima de 45 mms en machos y 41 mms en hembras. Dorso sepia o café, tornándose más pálido 
    hasta la altura de la cola, donde se vuelve habano, rojizo o anaranjado. Tiene una hilera de círculos oscuros con centros 
    claros, semejantes a pequeños ojos, a cada lado del cuerpo.""",#descrip
    imgur['KzXznVz.jpg'],#imagen
    wikidata['Q5313776'],
    eol['1053458'],
    'http://zoologia.puce.edu.ec/Vertebrados/reptiles/FichaEspecie.aspx?Id=1669',
    uniprot['174802'],
    gbif['2450419']
)

fauna(
    rutaAnillo['Fauna.rdf#dendrophidionBivittatus'],#uri
    "GUARDACAMINO, ESTERILLA, JARRETERA",#nombre comun
    "Dendrophidion bivittatus",#nombre cientifico
    """Se distribuye en la cordillera central y occidental de Colombia. Es una serpiente inofensiva que cumple un importante rol 
    dentro de la cadena alimenticia, ya que se alimenta de roedores y anfibios.""",#descrip
    imgur['IofqAh1.jpg'],#imagen
    wikidata['Q5124943'],
    eol['815721'],
    'http://abc.finkeros.com/serpientes-en-nuestras-fincas-jarretera/',
    uniprot['699575'],
    gbif['2452613']
)

fauna(
    rutaAnillo['Fauna.rdf#lampropeltisTriangulum'],#uri
    "CORAL, FALSA CORAL, MATA GANADO",#nombre comun
    "Lampropeltis triangulum",#nombre cientifico
    """Tiene una longitud entre 80-180 cms. Serpiente delgada y esbelta, cabeza ovalada y algo puntiaguda. Su cuerpo está 
    cubierto por anillos de colores rojo, negro y amarillo. El amarillo puede variar desde tonos muy vivos o pasteles 
    (a veces casi blancos) a tonos más anaranjados. El rojo suele ser más vivo.""",#descrip
    imgur['f34QpnV.jpg'],#imagen
    dbpedia['Lampropeltis_triangulum'],
    eol['792617'],
    'https://www.ecured.cu/Lampropeltis_triangulum',
    uniprot['140017'],
    gbif['5224503']
)

fauna(
    rutaAnillo['Fauna.rdf#dendrocygnaAutumnalis'],#uri
    "PISINGO, IGUAZA COMÚN",#nombre comun
    "Dendrocygna autumnalis",#nombre cientifico
    """Ave acuática espectacularmente colorida, sociable y ruidosa; tiene un pico rosa brillante, cuello y patas largas, 
    pecho castaño y vientre negro. Prefiere los lagos de agua dulce poco profundos; puede llegar a los que están 
    en medio del campo. Se alimenta principalmente de semillas de varias hierbas e insectos.""",#descrip
    imgur['5yZLaEG.jpg'],#imagen
    dbpedia['Dendrocygna_autumnalis'],
    eol['1267835'],
    'http://www.audubon.org/es/guia-de-aves/ave/pijije-alas-blancas',
    uniprot['8873'],
    gbif['2498393']
)

fauna(
    rutaAnillo['Fauna.rdf#rhynchortyxCinctus'],#uri
    "PERDIZ SELVÁTICA",#nombre comun
    "Rhynchortyx cinctus",#nombre cientifico
    """Perdiz de color café y pecho gris, raya negra desde el ojo hasta un lado del cuello, la hembra con pecho estriado, 
    la perdiz más pequeña de Colombia. Mide entre 17-20 cms, pesa aproximadamente 150 grs. """,#descrip
    imgur['CDgCEPE.jpg'],#imagen
    dbpedia['Rhynchortyx_cinctus'],
    eol['1047258'],
    'http://colombiacuriosa.blogspot.com.co/2016/05/pava-y-afines.html',
    uniprot['1356621'],
    gbif['2474165']
)

fauna(
    rutaAnillo['Fauna.rdf#phalacrocoraxBrasilianus'],#uri
    "CORMORÁN NEOTROPICAL",#nombre comun
    "Phalacrocorax	brasilianus",#nombre cientifico
    """Mide entre 58-73 cms y pesa alrededor de 1800 grs. El adulto es negro brillante con pico negro, largo y delgado con 
    un gancho en el extremo. Sus patas también son negras y presenta una bolsa gular y piel facial desnuda de color amarillo 
    opaco delineado en su parte posterior por una estrecha banda blanca.""",#descrip
    imgur['cHMcMp7.jpg'],#imagen
    dbpedia['Phalacrocorax_brasilianus'],
    eol['1065006'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Cormor%C3%A1n+Neotropical+-+Phalacrocorax+brasilianus',
    uniprot['37046'],
    gbif['2481868']
)

fauna(
    rutaAnillo['Fauna.rdf#nycticoraxNycticorax'],#uri
    "GUACO COMÚN",#nombre comun
    "Nycticorax nycticorax",#nombre cientifico
    """Ave robusta que mide de 61-69cms, con cuello corto y pico grande, y ojos de gran tamaño. Puede llegar a pesar más de 
    650 grs. Pico negro, patas amarillas verdoso. Coronilla y espalda negro lustroso; alas y cola gris; frente y lados de 
    la cabeza en partes inferiores blanquecinas; ojos rojos.""",#descrip
    imgur['8XCZd5O.jpg'],#imagen
    dbpedia['Nycticorax_nycticorax'],
    eol['1048731'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Guaco+Com%C3%BAn+-+Nycticorax+nycticorax',
    uniprot['8901'],
    gbif['2480863']
)

fauna(
    rutaAnillo['Fauna.rdf#butoridesStriata'],#uri
    "GARCITA RAYADA",#nombre comun
    "Butorides striata",#nombre cientifico
    """Ave robusta de 35-48 cms y un peso que oscila entre 135-250 grs. Su cuerpo es predominantemente azul grisáceo con la 
    coronilla negra y los lados de la cabeza, cuello y pecho de color gris. Tiene una raya blanca que va desde la garganta y 
    se hace más ancha en el pecho, la espalda es gris verdoso y la cola y alas verde oscuro.""",#descrip
    imgur['APOXbvi.jpg'],#imagen
    dbpedia['Butorides_striata'],
    eol['1065041'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Garcita+Rayada+-+Butorides+striata',
    uniprot['433628'],
    gbif['2480824']
)

fauna(
    rutaAnillo['Fauna.rdf#ardeaCocoi'],#uri
    "GARZÓN AZUL",#nombre comun
    "Ardea cocoi",#nombre cientifico
    """Ave grande de 102-130 cms de longitud. Presenta el alto pecho, los muslos y el cuello blancos, este último con estrías 
    en su parte frontal. La coronilla es negra con dos plumas largas que cuelgas sobre el cuello, el abdomen también es negro 
    y la espalda y cola son azul grisáceo. Es la garza más grande y esbelta de todas las garzas en Colombia.""",#descrip
    imgur['4VB1RoI.jpg'],#imagen
    dbpedia['Ardea_cocoi'],
    eol['1048971'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Garz%C3%B3n+Azul',
    uniprot['399589'],
    gbif['2480951']
)
  
fauna(
    rutaAnillo['Fauna.rdf#egrettaThula'],#uri
    "GARZA PATIAMARILLA",#nombre comun
    "Egretta thula",#nombre cientifico
    """Mide entre 47.5-67 cms y pesa cerca de 370 grs. Se caracteriza por tener el cuerpo totalmente blanco con el pico y las 
    patas negras con los dedos amarillos. Tiene los ojos amarillos y una pequeña banda amarilla que se extiende por delante 
    de estos hasta la base del pico. En plumaje nupcial es igualmente blanca pero con plumas más largas y recurvadas.""",#descrip
    imgur['tYXpH2E.jpg'],#imagen
    dbpedia['Egretta_thula'],
    eol['1048667'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Garza+Patiamarilla',
    uniprot['110681'],
    gbif['2480873']
)

fauna(
    rutaAnillo['Fauna.rdf#phimosusInfuscatus'],#uri
    "COQUITO, GALLINAZO NEGRO",#nombre comun
    "Phimosus infuscatus",#nombre cientifico
    """Mide entre 46-56 cms, con un peso promedio de 559 grs. Los adultos presentan su plumaje negro característico con trazos 
    de verde azuloso metálico oscuro sobre todo en las alas, tiene el pico rojizo curvado al igual que su cara o región 
    desnuda de la cabeza y patas.""",#descrip
    imgur['j6i05MZ.jpg'],#imagen
    dbpedia['Phimosus_infuscatus'],
    eol['1049667'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Coquito+-+Phimosus+infuscatus',
    uniprot['555323'],
    gbif['2480812']
)

fauna(
    rutaAnillo['Fauna.rdf#rostrhamusSociabilis'],#uri
    "CARACOLERO, CARACORELO COMÚN",#nombre comun
    "Rostrhamus sociabilis",#nombre cientifico
    """Mide entre 41-46 cms. Cuenta con alas medianas a largas, anchas hacia los extremos y cola cuadrada. Posee un pico delgado 
    y fuertemente curvado. Su piel facial y patas son de color rojo-naranja. Los machos adultos manifiestan uniformemente un 
    color negro pizarra. Las hembras adultas por encima tienen un color café negruzco.""",#descrip
    imgur['0C3UnfY.jpg'],#imagen
    dbpedia['Rostrhamus_sociabilis'],
    eol['1049023'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Caracolero+Com%C3%BAn',
    uniprot['156764'],
    gbif['2480415']
)

fauna(
    rutaAnillo['Fauna.rdf#milvagoChimachima'],#uri
    "PIGUA",#nombre comun
    "Milvago chimachima",#nombre cientifico
    """Mide 41 cms de largo y pesa 330 grs. Es de tamaño pequeño, de constitución liviana, cola más bien larga, y “ventana” grande 
    de color ante en las primarias. En los adultos la cabeza, región inferior y el forro de las alas son de color ante claro. 
    La línea postocular es negra. El pico y las patas son entre azul claro y verdoso.""",#descrip
    imgur['2oR826R.jpg'],#imagen
    dbpedia['Milvago_chimachima'],
    eol['1049220'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Pigua',
    uniprot['56337'],
    gbif['2481066']
)

fauna(
    rutaAnillo['Fauna.rdf#aramusGuarauna'],#uri
    "CARRAO, RASCÓN CAUCANO",#nombre comun
    "Aramus guarauna",#nombre cientifico
    """Mide de 61-71 cms y pesa de 1130-1370 grs el macho y de 1050-1170 grs la hembra. Presenta alas anchas y redondeadas, 
    pico largo ligeramente decurvado y patas largas. El macho es de color café aceitoso con estrías blanquecinas en cabeza, 
    cuello y alta espalda. La hembra es similar al macho pero levemente más pequeña.""",#descrip
    imgur['5TkiAuS.jpg'],#imagen
    dbpedia['Aramus_guarauna'],
    eol['1049274'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Carrao+-+Aramus+guarauna',
    uniprot['54356'],
    gbif['2474337']
)

fauna(
    rutaAnillo['Fauna.rdf#vanellusChilensis'],#uri
    "PELLAR, GALLINAZO COMÚN",#nombre comun
    "Vanellus chilensis",#nombre cientifico
    """Mide de 32-38 cms. Ambos sexos son similares. Presenta pico rosa con punta negra, patas rosa y una cresta occipital 
    larga y aguda de color negro. Por encima es principalmente de color gris pardusco con hombros color verde broncíneo. 
    Tiene la frente, parche gular y pecho negros. Su vientre y rabadilla son blancos y su cola negra.""",#descrip
    imgur['Lqw4muO.jpg'],#imagen
    dbpedia['Vanellus_chilensis'],
    eol['1049062'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Pellar+Com%C3%BAn+-+Vanellus+chilensis',
    uniprot['50404'],
    gbif['5229146']
)

fauna(
    rutaAnillo['Fauna.rdf#himantopusMexicanus'],#uri
    "CIGÜEÑUELA, CIGÜEÑUELA AMERICANA",#nombre comun
    "Himantopus mexicanus",#nombre cientifico
    """Mide de 35-40 cms y pesa de 166-205 grs. Presenta patas muy largas y pico largo, delgado y negro. El macho en estado 
    reproductivo tiene las patas y el iris rojo brillante y su nuca, espalda, alas y parte posterior de la cabeza son de 
    color negro. El resto de sus partes son blancas menos la parte superior del pecho que presenta tinte rosa.""",#descrip
    imgur['F3hows7.jpg'],#imagen
    dbpedia['Himantopus_mexicanus'],
    eol['1049561'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Cigue%C3%B1uela+-+Himantopus+mexicanus',
    uniprot['227231'],
    gbif['5229128']
)

fauna(
    rutaAnillo['Fauna.rdf#actitisMacularius'],#uri
    "ANDARRÍOS MANCHADO, ANDARRÍOS MACULADO",#nombre comun
    "Actitis macularius",#nombre cientifico
    """Mide de 18-20 cms, pesa de 19-64 grs y presenta una envergadura de 37-40 cms. En plumaje no reproductivo presenta 
    pico de color negro con la mandíbula amarillenta, patas amarillo opaco, cuerpo de color café oliva por encima con una 
    línea superciliar blanquecina y partes inferiores blancas con borrón pardusco en los lados del pecho.""",#descrip
    imgur['nQye6qQ.jpg'],#imagen
    dbpedia['Actitis_macularius'],
    eol['1064984'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Andarr%C3%ADos+Maculado+-+Actitis+macularius',
    uniprot['190659'],
    gbif['2481798']
)

fauna(
    rutaAnillo['Fauna.rdf#jacanaJacana'],#uri
    "GALLITO DE CIÉNAGA",#nombre comun
    "Jacana jacana",#nombre cientifico
    """Mide de 21-25 cms, los machos pesan de 88-119 grs aproximadamente y las hembras de 140-151 grs. Presenta pico amarillo 
    con escudo frontal bilobulado de color rojo y carúnculas laterales del mismo color. Sus patas son largas con dedos también 
    largos, ambos de color verdoso. Su cabeza, cuello y partes inferiores son negros.""",#descrip
    imgur['6oLpRzy.jpg'],#imagen
    dbpedia['Jacana_jacana'],
    eol['1049284'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Gallito+de+Ci%C3%A9naga+-+Jacana+jacana',
    uniprot['54508'],
    gbif['2481846']
)

fauna(
    rutaAnillo['Fauna.rdf#aratingaWagleri'],#uri
    "PERICO FRENTIRROJO",#nombre comun
    "Aratinga wagleri",#nombre cientifico
    """Ave que mide cerca de 36 cms y pesa de 162-217 grs. Es de color verde con las partes inferiores un poco más amarillentas. 
    Su frente y coronilla son rojas con algunas manchas del mismo color en la garganta y lados del cuello. Su cola es larga y 
    aguda con la superficie inferior amarillo oliva, al igual que el interior de sus alas.""",#descrip
    imgur['r5i1z4v.jpg'],#imagen
    dbpedia['Aratinga_wagleri'],
    eol['1177979'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Perico+Chocolero+-+Psittacara+wagleri',
    uniprot['867391'],
    gbif['2479159']
)

fauna(
    rutaAnillo['Fauna.rdf#pionusMenstruus'],#uri
    "COTORRA CABECIAZUL, COTORRA CHEJA",#nombre comun
    "Pionus menstruus",#nombre cientifico
    """Mide entre 24-28 cms y pesa de 209-295 grs. Presenta cabeza y pecho azul, y cobertoras auriculares negruzcas. Su pico 
    es pardusco con la base rosácea y tiene el área ocular desnuda blanquecina. El resto del cuerpo es principalmente verde 
    con las plumas infracaudales y la base de la superficie inferior de la cola rojas.""",#descrip
    imgur['2ucGhZ9.jpg'],#imagen
    dbpedia['Pionus_menstruus'],
    eol['1178041'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Cotorra+Cheja+-+Pionus+menstruus',
    uniprot['13214'],
    gbif['2479902']
)

fauna(
    rutaAnillo['Fauna.rdf#crotophagaMajor'],#uri
    "GARRAPATERO GRANDE, GARRAPATERO MAYOR",#nombre comun
    "Crotophaga major",#nombre cientifico
    """Mide alrededor de 46 cms, los machos pesan en promedio 162 grs y las hembras 145 grs. Presenta ojos blancos, patas negras 
    y pico negro comprimido lateralmente con culmen arqueado en la base de la mandíbula superior. El adulto es de color negro-azul 
    lustroso con los bordes de las plumas de las alas verde broncíneo y cola con lustre púrpura.""",#descrip
    imgur['g4c7YiA.jpg'],#imagen
    dbpedia['Crotophaga_major'],
    eol['914612'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Garrapatero+Mayor+-+Crotophaga+major',
    uniprot['48617'],
    gbif['2496210']
)

fauna(
    rutaAnillo['Fauna.rdf#megascopsCholiba'],#uri
    "CURRUCUTÚ, CURRUCUTÚ COMÚN",#nombre comun
    "Megascops choliba",#nombre cientifico
    """Mide de 20-24 cms y pesa de 97-160 grs. Presenta iris amarillo, pico gris verdoso con punta gris y patas de color café 
    grisáceo. Tiene disco facial gris claro con bordes negros prominentes, coronilla y partes superiores con estrías 
    oscuras, plumas de vuelo y cola barradas de ante pálido y café. Por debajo es principalmente blanco.""",#descrip
    imgur['9ghzI8b.jpg'],#imagen
    dbpedia['Megascops_choliba'],
    eol['1025097'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Currucut%C3%BA+Com%C3%BAn+-+Megascops+choliba',
    uniprot['507958'],
    gbif['2497365']
)

fauna(
    rutaAnillo['Fauna.rdf#amaziliaTzacatl'],#uri
    "AMAZILIA COLIRRUFO",#nombre comun
    "Amazilia tzacatl",#nombre cientifico
    """Mide aproximadamente 9.1 cms. Se reconoce fácilmente por su pico rojizo con la punta negra y su cola café-rojiza oscura. 
    Emite silbidos agudos y una serie rápida de “tsip” propios de estas aves. El colibrí colirrufo caza insectos durante vuelos 
    cortos. También busca sus presas en hojas, ramas y telas de araña.""",#descrip
    imgur['edFZpRK.jpg'],#imagen
    dbpedia['Amazilia_tzacatl'],
    eol['1273441'],
    'https://www.medellin.gov.co/biodiversidad/seccion.hyg?seccion=5&submenu=1',
    uniprot['57392'],
    gbif['2476441']
)

fauna(
    rutaAnillo['Fauna.rdf#megaceryleTorquata'],#uri
    "MARTÍN PESCADOR GRANDE, MARTÍN PESCADOR MEDIANO",#nombre comun
    "Megaceryle torquata",#nombre cientifico
    """Mide alrededor de 40 cms, los machos pesan entre 254-330 grs y las hembras entre 274-325 grs.  El macho es de color azul 
    grisáceo en las partes superiores, presenta pecho y vientre rufo. En frente de los ojos tiene dos manchas 
    semicirculares blancas. Sus plumas primarias son negras y las cobertoras infracaudales blancas con barras grises.""",#descrip
    imgur['46KDzC8.jpg'],#imagen
    dbpedia['Megaceryle_torquata'],
    eol['1049955'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Mart%C3%ADn+Pescador+Mayor+-+Megaceryle+torquata',
    uniprot['488310'],
    gbif['2475466']
)

fauna(
    rutaAnillo['Fauna.rdf#chloroceryleAmericana'],#uri
    "MARTÍN PESCADOR CHICO",#nombre comun
    "Chloroceryle americana",#nombre cientifico
    """Mide aproximadamente 20 cms, la hembra pesa entre 33-35 grs y el macho de 29-40 grs. El macho es verde oscuro en las 
    partes superiores con algo de bronze en la coronilla. Presenta collar blanco y manchas del mismo color en las plumas 
    primarias, secundarias y en las cobertoras alares. Tiene una banda pectoral rufa y su garganta y vientre son blancos.""",#descrip
    imgur['OMbLt4u.jpg'],#imagen
    dbpedia['Chloroceryle_americana'],
    eol['917144'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Mart%C3%ADn+Pescador+Chico+-+Chloroceryle+americana',
    uniprot['57406'],
    gbif['2475486']
)

fauna(
    rutaAnillo['Fauna.rdf#melanerpesRubricapillus'],#uri
    "CARPINTERO HABADO",#nombre comun
    "Melanerpes rubricapillus",#nombre cientifico
    """Los adultos son de 205 mms de largo y pesan 48 grs. Tienen un lomo blanco con negro parecido al color de las cebras, 
    alas y los muslos blancos. La cola es negra con algo de blanco y las partes inferiores pardo oscuro. El macho tiene 
    un parche de corona roja en la nuca; la hembra tiene una corona color beige y la nuca pálida.""",#descrip
    imgur['85VGq9C.jpg'],#imagen
    dbpedia['Melanerpes_rubricapillus'],
    eol['1177502'],
    'https://ecojugando.wordpress.com/2015/08/20/carpintero-habado-melanerpes-rubricapillus/',
    uniprot['56082'],
    gbif['2478125']
)

fauna(
    rutaAnillo['Fauna.rdf#veniliornisKirkii'],#uri
    "CARPINTERO CULIRROJO",#nombre comun
    "Veniliornis kirkii",#nombre cientifico
    """Mide 15-16.5 cms de longitud y pesa 28-30 grs. El plumaje de sus partes superiores es verde oliva, con un 
    lustre dorado a anaranjado en el lomo y las coberteras alares. El macho tiene la cara color oliva fusco, la coronilla 
    y la parte posterior del cuello color gris pizarra. La hembra presenta la corona y la nuca color marrón oscuro.""",#descrip
    imgur['qAYQro9.jpg'],#imagen
    dbpedia['Veniliornis_kirkii'],
    eol['1177616'],
    'http://www.naturalista.mx/taxa/18020-Veniliornis-kirkii',
    uniprot['315388'],
    gbif['2478367']
)

fauna(
    rutaAnillo['Fauna.rdf#colaptesPunctigula'],#uri
    "CARPINTERO PECHIPUNTEADO, CARPINTERO BUCHIPECOSO",#nombre comun
    "Colaptes punctigula",#nombre cientifico
    """Mide 20 cms de longitud. La frente es negra, la coronilla roja, lados de la cabeza blancos, bordeados por debajo de 
    un bigote rojo (solo en los machos). Garganta manchada de negro y blanco. Pecho y abdomen amarillo claro oliva, con 
    puntos negros. La espalda es de color amarillo oliva oscuro barrado de negro.""",#descrip
    imgur['1UPyRnQ.jpg'],#imagen
    dbpedia['Colaptes_punctigula'],
    eol['1177467'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Carpintero+Buchipecoso',
    uniprot['381865'],
    gbif['2478237']
)

fauna(
    rutaAnillo['Fauna.rdf#campephilusMelanoleucos'],#uri
    "CARPINTERO MARCIAL",#nombre comun
    "Campephilus melanoleucos",#nombre cientifico
    """Mide de 33-38 cms y pesa de 181-284 grs. Presenta pico largo de color grisáceo a blancuzco con punta cincelada y 
    culmen levemente curvo. Tiene iris blanco a amarillento pálido, piel ocular grisácea y patas gris a gris-verde. El 
    macho presenta plumas de color ante blanquecino alrededor de la base  del pico.""",#descrip
    imgur['piiWNiz.jpg'],#imagen
    dbpedia['Campephilus_melanoleucos'],
    eol['1177548'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Carpintero+Marcial+-+Campephilus+melanoleucos',
    uniprot['315367'],
    gbif['2478564']
)

fauna(
    rutaAnillo['Fauna.rdf#synallaxisAlbescens'],#uri
    "RASTROJERO PÁLIDO, CHAMICERO PÁLIDO",#nombre comun
    "Synallaxis albescens",#nombre cientifico
    """Mide entre 14-17 cms de longitud y pesa 13-15 grs. Es un pájaro esbelto con una cola de 9,3 cms longitud. El plumaje de 
    sus partes superiores es principalmente de color marrón claro, con las alas y cola más oscuras. Tienen el píleo de color 
    castaño rojizo al igual que la nuca y las coberteras alares. Sus partes inferiores son blanquecinas.""",#descrip
    imgur['LBHfbd5.jpg'],#imagen
    dbpedia['Synallaxis_albescens'],
    eol['1050187'],
    'https://ecojugando.wordpress.com/2015/12/17/pijui-pechiblanco-o-chamicero-palido-synallaxis-albescens/',
    uniprot['88181'],
    gbif['2484936']
)

fauna(
    rutaAnillo['Fauna.rdf#lepidocolaptesSouleyetii'],#uri
    "TREPATRONCOS CAMPESTRE, TREPADOR CAMPESTRE",#nombre comun
    "Lepidocolaptes souleyetii",#nombre cientifico
    """Posee un largo total promedio de 20 cms. Pico delgado, ligeramente decurvado (25 mms), coronilla y nuca café negruzco 
    y finalmente estriado de blanco ante; a veces alto manto también estriado finamente; espalda café rufo uniforme; 
    rabadilla, alas y colas rufa; garganta ante; resto de partes inferiores café.""",#descrip
    imgur['8qWrKJG.jpg'],#imagen
    dbpedia['Lepidocolaptes_souleyetii'],
    eol['917806'],
    'http://www.biodiversidad.co/fichas/2590',
    uniprot['75977'],
    gbif['2486044']
)

fauna(
    rutaAnillo['Fauna.rdf#cercomacraNigricans'],#uri
    "HORMIGUERO YEGUA",#nombre comun
    "Cercomacra nigricans",#nombre cientifico
    """Forma una especie de grupo con otros tres hormigueros cuyos machos son en gran parte negro con unas marcas blancas 
    (Carbonaria, Melanaria, Ferdinandi). De este grupo, el Hormiguero Yegua es el más extendido geográficamente. Las hembras 
    son muy oscuras con marcas blancas en las alas y garganta.""",#descrip
    imgur['isv6Iob.jpg'],#imagen
    dbpedia['Cercomacra_nigricans'],
    eol['1052462'],
    'http://neotropical.birds.cornell.edu/portal/species/overview?p_p_spp=386611',
    uniprot['722450'],
    gbif['2490135']
)

fauna(
    rutaAnillo['Fauna.rdf#todirostrumCinereum'],#uri
    "ESPATULILLA, ESPATULILLA COMÚN",#nombre comun
    "Todirostrum cinereum",#nombre cientifico
    """Mide de 8.8-10.2 cms y pesa entre 4.4-8 grs. El macho tiene la frente, lados de la cabeza y la coronilla negro 
    lustroso con un tono gris pizarra en el occipucio y oliva en la espalda y la rabadilla. Sus alas son negras con los bordes 
    y puntas de las cobertoras de color amarillo.""",#descrip
    imgur['P2dpbXd.jpg'],#imagen
    dbpedia['Todirostrum_cinereum'],
    eol['1053321'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Espatulilla+Com%C3%BAn',
    uniprot['196049'],
    gbif['2483274']
)

fauna(
    rutaAnillo['Fauna.rdf#sayornisNigricans'],#uri
    "GUARDA PUENTES",#nombre comun
    "Sayornis nigricans",#nombre cientifico
    """Mide entre 15-19 cms y pesa alrededor de 18 grs. Su cabeza, pecho, partes superiores y alas son color negro hollín, 
    mientras que su abdomen es blanco, al igual que los márgenes de las cobertoras alares, rémiges internas y rectríces 
    externas. Presenta iris café oscuro y pico y patas negras.""",#descrip
    imgur['me2Raon.jpg'],#imagen
    dbpedia['Sayornis_nigricans'],
    eol['1046718'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Atrapamoscas+Guardapuentes',
    uniprot['183530'],
    gbif['2483612']
)
 
fauna(
    rutaAnillo['Fauna.rdf#pyrocephalusRubinus'],#uri
    "PECHIRROJO, ATRAPAMOSCAS PECHIRROJO",#nombre comun
    "Pyrocephalus rubinus",#nombre cientifico
    """Mide 14cms. Cresta corta. El macho tiene coronilla y partes inferiores escarlata brillante; lista ocular, occipucio 
    y partes superiores café hollin. La hembra es muy diferente: por encima café ceniza oscuro; garganta y pecho blancos 
    estrecha y difusamente barrados de negruzco; bajas partes inferiores salmon rosáceo; centro del abdomen a menudo blanco.""",#descrip
    imgur['pLQ00lY.jpg'],#imagen
    dbpedia['Pyrocephalus_rubinus'],
    eol['1050412'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Atrapamoscas+Pechirrojo',
    uniprot['371933'],
    gbif['2483647']
)

fauna(
    rutaAnillo['Fauna.rdf#machetornisRixosa'],#uri
    "SIRIRÍ BUEYERO, ATRAPAMOSCAS GANADERO",#nombre comun
    "Machetornis rixosa",#nombre cientifico
    """Tamaño aproximado de 19 cms. Tiene los ojos rojos y  patas largas que le facilitan caminar sobre el suelo. 
    Es principalmente café oliva pálido por encima, su coronilla es más gris y con la cresta naranja encendido usualmente 
    oculta (en el macho únicamente); una estrecha línea ocular negruzca, alas y cola parduscas.""",#descrip
    imgur['4QvEWMG.jpg'],#imagen
    dbpedia['Machetornis_rixosa'],
    eol['285035'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Atrapamoscas+Ganadero',
    uniprot['495241'],
    gbif['2482934']
)

fauna(
    rutaAnillo['Fauna.rdf#myiozetetesCayanensis'],#uri
    "SUELDA CRESTINEGRA",#nombre comun
    "Myiozetetes cayanensis",#nombre cientifico
    """Mide cerca de 16.5 cms. Tiene pico negro y corto, sus partes superiores son de tonalidad café en contraste con su 
    coronilla y lados de la cabeza que son negros, posee un parche naranja dorado oculto en la coronilla. Tiene garganta blanca 
    y el resto de partes inferiores son de matiz amarillo brillante.""",#descrip
    imgur['sThcSOC.jpg'],#imagen
    dbpedia['Myiozetetes_cayanensis'],
    eol['1053224'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Suelda+Crestinegra',
    uniprot['478635'],
    gbif['2482921']
)

fauna(
    rutaAnillo['Fauna.rdf#tyrannusSavana'],#uri
    "SIRIRÍ TIJERETA, SIRIRÍ TIJERETÓN",#nombre comun
    "Tyrannus savana",#nombre cientifico
    """El tamaño de los machos es de 38 cms y el de las hembras de solo 28 cms. Tiene la cola muy larga y profundamente 
    ahorquillada (más corta en la hembra). Presentan la coronilla, nuca y lados de la cabeza hasta debajo de los ojos, 
    de color negro. La espalda es gris claro, las alas más oscuras, cola negra.""",#descrip
    imgur['KJO2DtD.jpg'],#imagen
    dbpedia['Tyrannus_savana'],
    eol['917500'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Sirir%C3%AD+Tijereta',
    uniprot['137541'],
    gbif['5229693']
)

fauna(
    rutaAnillo['Fauna.rdf#neochelidonTibialis'],#uri
    "GOLONDRINA SELVÁTICA",#nombre comun
    "Neochelidon tibialis",#nombre cientifico
    """Mide 12 cms de longitud y pesa entre 9.1 y 10.5 grs. Su plumaje es gris opaco, gris parduzco a negro parduzco, con 
    el pecho y el vientre más claros, grisáceos a blacuzcos y penachos blancos en los muslos. El oído, los lados del cuello, 
    el iris, el pico y las patas son de color castaño oscuro.""",#descrip
    imgur['Ixpldaw.jpg'],#imagen
    dbpedia['Neochelidon_tibialis'],
    eol['1050800'],
    'https://es.wikipedia.org/wiki/Neochelidon_tibialis',
    uniprot['1740326'],
    gbif['2489212']
)

fauna(
    rutaAnillo['Fauna.rdf#stelgidopteryxRuficollis'],#uri
    "GOLONDRINA BARRANQUERA",#nombre comun
    "Stelgidopteryx ruficollis",#nombre cientifico
    """Mide 13 cms y pesa entre 14-18 grs. Es principalmente café grisáceo, sus alas y cola son café negruzcas y las barbas 
    de la plumas primarias externas son rigidas. Presenta garganta café y el resto de partes inferiores café grisáceo 
    oscuro las cuales se vuelven amarillentas hacia el abdomen.""",#descrip
    imgur['h0D1RCC.jpg'],#imagen
    dbpedia['Stelgidopteryx_ruficollis'],
    eol['1050747'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Golondrina+Barranquera+-+Stelgidopteryx+ruficollis',
    uniprot['72878'],
    gbif['2489203']
)

fauna(
    rutaAnillo['Fauna.rdf#hirundoRustica'],#uri
    "GOLONDRINA TIJERETA",#nombre comun
    "Hirundo rustica",#nombre cientifico
    """Mide alrededor de 18 cms y pesa de 16-24 grs. El macho presenta frente y garganta rufa, coronilla y partes altas 
    azul lustroso y cola negra con parches blancos. Las plumas externas de la cola son notoriamente elongadas. Presenta 
    una amplia banda pectoral azul y el resto de las partes inferiores de color crema.""",#descrip
    imgur['4a0HLx2.jpg'],#imagen
    dbpedia['Hirundo_rustica'],
    eol['917688'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Golondrina+Tijereta+-+Hirundo+rustica',
    uniprot['43150'],
    gbif['5230791']
)

fauna(
    rutaAnillo['Fauna.rdf#turdusIgnobilis'],#uri
    "MIRLA OLLERA",#nombre comun
    "Turdus ignobilis",#nombre cientifico
    """Mide alrededor de 24 cms. Es de color café sucio con pico negro. Por encima es de color café oscuro opaco uniforme 
    a café oliva opaco, su garganta es blanca estriada de negruzco y gradualmente café oliva pálido en el pecho. El centro 
    del abdomen e infracaudales son blancos.""",#descrip
    imgur['qowJLGA.jpg'],#imagen
    dbpedia['Turdus_ignobilis'],
    eol['922675'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Mirla+Ollera',
    uniprot['411541'],
    gbif['2490722']
)

fauna(
    rutaAnillo['Fauna.rdf#sicalisFlaveola'],#uri
    "CANARIO CORONADO, SICALIS CORONADO",#nombre comun
    "Sicalis flaveola",#nombre cientifico
    """Mide aproximadamente 14 cms su color es amarillo brillante. El Macho por encima tiene color amarillo oliva débilmente 
    estriado de pardusco en la espalda; la coronilla anterior es naranja brillante la cabeza y partes inferiores tienen 
    amarillo dorado. La hembra es más opaca y menos naranja en la coronilla.""",#descrip
    imgur['6yNqA10.jpg'],#imagen
    dbpedia['Sicalis_flaveola'],
    eol['922690'],
    'http://www.avesyturismo.com/canario-criollo-sicalis-coronado.html',
    uniprot['163868'],
    gbif['2491862']
)

fauna(
    rutaAnillo['Fauna.rdf#volatiniaJacarina'],#uri
    "ESPIGUERO SALTARÍN, CANARIO CORONADO, VOLATINERO NEGRO",#nombre comun
    "Volatinia jacarina",#nombre cientifico
    """Mide de 8.7-10.9 cms y pesa de 8-12 grs. Presenta pico cónico con culmen levemente decurvado. El macho tiene la 
    cabeza, el cuello, partes superiores y partes inferiores de color negro con azul oscuro iridiscente. La hembra es de color 
    marrón, más oscuro por encima que por debajo.""",#descrip
    imgur['aKmiHzx.jpg'],#imagen
    dbpedia['Volatinia_jacarina'],
    eol['1050405'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Volatinero+Negro+-+Volatinia+jacarina',
    uniprot['135452'],
    gbif['2491741']
)

fauna(
    rutaAnillo['Fauna.rdf#sporophilaNigricollis'],#uri
    "ESPIGUERO CAPUCHINO",#nombre comun
    "Sporophila nigricollis",#nombre cientifico
    """Mide de 8.5-10.3 cms y pesa de 8.5-11.2 grs. El macho presenta iris café, pico azul grisáceo y patas negruzcas. Su 
    cabeza hasta la nuca y el pecho son de color negro y el resto de partes altas son de color oliva pálido. La hembra es de 
    color café cálido en gran parte de su cabeza, nuca, manto y baja espalda.""",#descrip
    imgur['5GP58vb.jpg'],#imagen
    dbpedia['Sporophila_nigricollis'],
    eol['917113'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Espiguero+Capuchino+-+Sporophila+nigricollis',
    uniprot['138930'],
    gbif['2491335']
)

fauna(
    rutaAnillo['Fauna.rdf#setophagaPetechia'],#uri
    "REINITA DORADA, REINITA AMARILLA",#nombre comun
    "Setophaga petechia",#nombre cientifico
    """Mide 11.4 cms. El macho es amarillo encendido con oliva-amarillento en partes superiores. Las alas y cola son 
    negruzcas fuertemente marginadas de amarillo. El pecho y los lados tienen estrías de color rufo. La hembra es más 
    opaca y con más oliva por encima. Es una de las reinitas más comunes de Colombia.""",#descrip
    imgur['Bi54eBO.jpg'],#imagen
    dbpedia['Setophaga_petechia'],
    eol['918547'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Reinita+amarilla',
    uniprot['123634'],
    gbif['7341834']
)

fauna(
    rutaAnillo['Fauna.rdf#icterusNigrogularis'],#uri
    "TURPIAL AMARILLO",#nombre comun
    "Icterus nigrogularis",#nombre cientifico
    """Mide entre 20-21 cms. Los machos tienen un peso promedio de 39.5 grs y las hembras 37.4 grs. Su plumaje principalmente 
    es de color amarillo limón con la región ocular, babero, alas y cola color negro. Presenta una barra alar blanca 
    estrecha pero nítida y las márgenes de las rémiges internas son blanquecinos.""",#descrip
    imgur['f43frzM.jpg'],#imagen
    dbpedia['Icterus_nigrogularis'],
    eol['1050858'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Turpial+Amarillo',
    uniprot['84827'],
    gbif['5229939']
)

fauna(
    rutaAnillo['Fauna.rdf#chrysomusIcterocephalus'],#uri
    "MONJITA CABECIAMARILLA, MONJITA",#nombre comun
    "Chrysomus icterocephalus",#nombre cientifico
    """El macho mide alrededor de 18 cms y la hembra 16.5 cms. El peso promedio para los machos es de 35.9 grs y el peso de 
    las hembras es de 37.4 grs. Tienen pico cónico y agudo. El macho es negro con cabeza, garganta y alto pecho color 
    amarillo brillante. La hembra presenta por encima un color oliva pardusco opaco.""",#descrip
    imgur['Yza4Mpv.jpg'],#imagen
    dbpedia['Chrysomus_icterocephalus'],
    eol['284088'],
    'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Turpial+Cabeciamarillo',
    uniprot['993346'],
    gbif['2484103']
)

fauna(
    rutaAnillo['Fauna.rdf#cerdocyonThous'],#uri
    "ZORRO CAÑERO",#nombre comun
    "Cerdocyon thous",#nombre cientifico
    """Es un canino de tamaño mediano (5-7 Kgs.), la cola es moderadamente peluda, con la punta negra y oscura en la base. 
    El rostro es largo y puntiagudo, la cabeza es relativamente corta y estrecha. El pelaje generalmente es gris oscuro a negro 
    a lo largo del dorso, la línea media en el vientre incluyendo las patas son gris a negro.""",#descrip
    imgur['8hK48Hw.jpg'],#imagen
    dbpedia['Cerdocyon_thous'],
    eol['328685'],
    'http://www.biodiversidad.co/fichas/421',
    uniprot['9620'],
    gbif['2434584']
)

fauna(
    rutaAnillo['Fauna.rdf#pumaYagouaroundi'],#uri
    "PUMA, LEÓN, YAGUARUNDI",#nombre comun
    "Puma yagouaroundi",#nombre cientifico
    """Presenta dos formas en la coloración de su pelaje: una de color castaño rojizo, y otra parda casi negra o 
    grisácea. Alcanza una longitud de 50-70 cms de largo, más la cola que mide de 30-60 cms. Mide en promedio 
    33 cms de altura. Los adultos alcanzan un peso entre los 3.5-9.1 kgs. Se alimenta de pequeños mamíferos y aves.""",#descrip
    imgur['vRm3s3s.jpg'],#imagen
    dbpedia['Puma_yagouaroundi'],
    eol['1053885'],
    'http://www.naturalista.mx/taxa/74989-Puma-yagouaroundi',
    uniprot['1608482'],
    gbif['2435146']
)

fauna(
    rutaAnillo['Fauna.rdf#oreochromisNiloticus'],#uri
    "TILAPIA NILÓTICA, MOJARRA",#nombre comun
    "Oreochromis niloticus",#nombre cientifico
    """Puede medir hasta 60 cms y pesar 4 Kgs. Fácilmente reconocible debido a su cuerpo comprimido, a las líneas verticales 
    separadas de color oscuro y a la barra en la aleta caudal. En época reproductiva el color de las aletas se vuelve 
    rojizo. Se alimenta de algas bentonicas, fitoplancton, huevos de otras especies de peces y larvas.""",#descrip
    imgur['6YTmwYK.jpg'],#imagen
    dbpedia['Oreochromis_niloticus'],
    eol['356343'],
    'http://www.biodiversidad.co/fichas/585',
    uniprot['8128'],
    gbif['4285694']
)

fauna(
    rutaAnillo['Fauna.rdf#tilapiaRendalli'],#uri
    "MOJARRA HERBÍVORA, TILAPIA HERBÍVORA",#nombre comun
    "Tilapia rendalli",#nombre cientifico
    """Alcanza los 45 cms y los 2 kgs. De color verde oliva a marrón, a menudo con escamas azules dispersas; bases de escamas 
    en el cuerpo con crecientes marcas oscuras; aleta dorsal oliva, con un delgado borde exterior entre amarillento a rojo; 
    aleta caudal oliva con puntos nacarados en la porción superior, de rojo a amarillento por debajo.""",#descrip
    imgur['rBjlcu4.jpg'],#imagen
    dbpedia['Tilapia_rendalli'],
    eol['212062'],
    'http://biogeodb.stri.si.edu/caribbean/es/thefishes/species/4505',
    uniprot['8129'],
    gbif['2370605']
)

fauna(
    rutaAnillo['Fauna.rdf#poeciliaMexicana'],#uri
    "PIPONA",#nombre comun
    "Poecilia mexicana",#nombre cientifico
    """Mide entre los 6-9 cms los machos y entre 10-12 cms las hembras. En estado salvaje va del pardo al grisáceo, pasando 
    por el verde oliva y morado tenue, encontrándose en ocasiones individuos melánicos, y presentando los machos dominantes 
    y algunas hembras alfa tonalidades que van del amarillo al naranja en los bordes de las aletas caudal y dorsal.""",#descrip
    imgur['YIukHx0.jpg'],#imagen
    dbpedia['Poecilia_mexicana'],
    eol['211878'],
    'http://www.pezadicto.com/poecilia-mexicana-molly-mexicano/',
    uniprot['48701'],
    gbif['8400492'] 
)

fauna(
    rutaAnillo['Fauna.rdf#astyanaxMicrolepis'],#uri
    "SARDINA, SARDINITA",#nombre comun
    "Astyanax microlepis",#nombre cientifico
    """Es una especie de colores muy variados dependiendo del sitio de captura. Presenta una mancha caudal negra  
    bien  marcada. Aletas anaranjadas, cuerpo plateado con visos amarillos. La línea predorsal es completamente escamada 
    y la línea lateral con 50 o más escamas las cuales son pequeñas y finas.""",#descrip
    imgur['rn4LoLr.jpg'],#imagen
    wikidata['Q6398228'],
    eol['211218'],
    'https://www.cortolima.gov.co/sites/default/files/images/stories/centro_documentos/pom_coello/diagnostico/apendices/ap_peces.pdf',
    uniprot['642543'],
    gbif['5204264']
)

fauna(
    rutaAnillo['Fauna.rdf#sternopygusMacrurus'],#uri
    "VERINGO, PEZ CUCHILLO",#nombre comun
    "Sternopygus macrurus",#nombre cientifico
    """Puede medir más de 38 cms de longitud total. El ojo característicamente presenta el borde orbital libre. Es de color 
    oscuro con una banda blanca. Encima de la aleta pectoral posee una mancha oscura verticalmente alargada. La 
    aleta anal es larga dejando libre un pedúnculo largo en forma de filamento.""",#descrip
    imgur['wX8oLGa.jpg'],#imagen
    wikidata['Q5611023'],
    eol['205876'],
    'http://izt.ciens.ucv.ve/mbucv/peces/Proyecto%20Atlas/PaginaWeb/GYMNOTIFORMES_STERNOPYGIDAE_Familia_Sternopygus%20macrurus.htm',
    uniprot['77841'],
    gbif['2402060']
)

# Modelado en otras rutas
g.add( (rutaMaiz['Fauna.rdf#rhinellaMarina'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) ) #ruta maiz
g.add( (rutaMaiz['Fauna.rdf#colostethusFraterdanieli'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) )
g.add( (rutaMaiz['Fauna.rdf#leptodactylusFragilis'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) )
g.add( (rutaMaiz['Fauna.rdf#leptodactylusColombiensis'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) )
g.add( (rutaMaiz['Fauna.rdf#iguanaIguana'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) )
g.add( (rutaVueltaOriente['Fauna.rdf#micrurusMipartitus'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) ) #vuelta oriente
g.add( (rutaVueltaOriente['Fauna.rdf#dendrocygnaBicolor'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) )
g.add( (rutaMaiz['Fauna.rdf#anasCyanoptera'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) ) #ruta maiz
g.add( (rutaVueltaOriente['Fauna.rdf#bubulcusIbis'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) ) #vuelta oriente
g.add( (rutaMaiz['Fauna.rdf#ardeaAlba'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) ) # maiz
g.add( (rutaMaiz['Fauna.rdf#coragypsAtratus'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) )
g.add( (rutaVueltaOriente['Fauna.rdf#zenaidaAuriculata'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) ) #vuelta oriente
g.add( (rutaVueltaOriente['Fauna.rdf#columbinaTalpacoti'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) )
g.add( (rutaVueltaOriente['Fauna.rdf#forpusConspicillatus'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) )
g.add( (rutaVueltaOriente['Fauna.rdf#crotophagaAni'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) )
g.add( (rutaVueltaOriente['Fauna.rdf#taperaNaevia'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) )
g.add( (rutaMaiz['Fauna.rdf#thamnophilusMultistriatus'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) ) #maiz
g.add( (rutaVueltaOriente['Fauna.rdf#pitangusSulphuratus'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) ) #vuelta oriente
g.add( (rutaVueltaOriente['Fauna.rdf#tyrannusMelancholicus'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) )
g.add( (rutaVueltaOriente['Fauna.rdf#fluvicolaPica'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) )
g.add( (rutaVueltaOriente['Fauna.rdf#notiochelidonCyanoleuca'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) )
g.add( (rutaVueltaOriente['Fauna.rdf#troglodytesAedon'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) )
g.add( (rutaVueltaOriente['Fauna.rdf#thraupisEpiscopus'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) )
g.add( (rutaVueltaOriente['Fauna.rdf#didelphisMarsupialis'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) )
g.add( (rutaVueltaOriente['Fauna.rdf#dasypusNovemcinctus'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) )
g.add( (rutaVueltaOriente['Fauna.rdf#artibeusLituratus'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) )
g.add( (rutaVueltaOriente['Fauna.rdf#glossophagaSoricina'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) )
g.add( (rutaMaiz['Fauna.rdf#sciurusGranatensis'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) ) #maiz
g.add( (rioFrio['Fauna.rdf#hydrochoerusHydrochaeris'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) ) #riofrio
g.add( (rutaVueltaOriente['Fauna.rdf#sylvilagusBrasiliensis'], UMBEL.isAbout, URIRef(rutaAnillo['Fauna.rdf'])) ) #vuelta oriente

#print (g.serialize(format='pretty-xml'))
