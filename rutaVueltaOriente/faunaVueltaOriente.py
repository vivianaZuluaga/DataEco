#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import WILDLIFE, CRUZAR, UMBEL, OWL
from utils.namespaces import rutaVueltaOriente, uniprot, dbpedia, wikidata, imgur, eol, gbif
from eventosvueltaOriente import g

#g = Graph()

def fauna(uri, nombre_comun, nombre_cientifico, descripcion, imagen, uriLink1, uriLink2, ref, uriLink3):
    g.add( (URIRef(uri), RDF.type, WILDLIFE.TaxonName) )
    g.add( (URIRef(uri), WILDLIFE.commonName, Literal(nombre_comun, lang='es') ) )
    g.add( (URIRef(uri), WILDLIFE.scientificName, Literal(nombre_cientifico, lang='la')) )
    g.add( (URIRef(uri), WILDLIFE.shortDescription, Literal(descripcion, lang='es')) )
    g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)))
    g.add( (URIRef(uri), WILDLIFE.kingdomName, Literal('Animal', lang='es')) )
    
    g.add( (URIRef(uri), FOAF.isPrimaryTopicOf, URIRef(ref)) ) #Sitio web del que se tomo la des
    g.add( (URIRef(uri), OWL.sameAs, URIRef(uriLink1)) ) #Link RDF a DBpedia
    g.add( (URIRef(uri), RDFS.seeAlso, URIRef(uriLink2)) ) #Link a EOL
    g.add( (URIRef(uri), OWL.sameAs, URIRef(uriLink3)) ) #Link RDF a UniProt
    
    g.add( ( URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaVueltaOriente.Fauna)) )

fauna(
    gbif['5777723'],
    "ZORRO GRIS",
    "Dusicyon thous",
    """Cánido de tamaño mediano (5-7 Kgs), la cola es moderadamente peluda, con la punta negra y oscura en la base. El 
    rostro es largo y puntiagudo, la cabeza es relativamente corta y estrecha. El pelaje generalmente es gris oscuro a 
    negro a lo largo del dorso, la línea media en el vientre incluyendo las patas son gris a negro.""",
    imgur['qYFO2lk.jpg'],
    dbpedia['Dusicyon_thous_azarae'],
    eol['328685'],
	'http://www.biodiversidad.co/fichas/421',
	uniprot['9620']
)

fauna(
    gbif['2433270'],
    "MURCIÉLAGO CARA RAYADA",
    "Artibeus lituratus",
    """Murciélago de tamaño grande, con el cuerpo grueso y macizo. Tiene la cabeza ancha y corta; la hoja nasal es pequeña 
    en forma de punta de lanza y con la base redondeada; las orejas son medianas y redondeadas; el labio inferior posee 
    verrugas. Tiene cuatro bandas blancas en la cara, muy notorias. El pelaje dorsal es muy largo pero sedoso, de color café.""",
    imgur['RAsubX0.jpg'],
    dbpedia['Artibeus_lituratus'],
    eol['327359'],
	'http://www.biodiversidad.co/fichas/2452',
	uniprot['27634']
)

fauna(
    gbif['2433176'],
    "MURCIÉLAGO FRUGÍVORO",
    "Carollia perspicillata",
    """Pelaje color pardo oscuro a pardo grisáceo, generalmente tricoloreado oscuro-claro-oscuro .Abdomen de color 
    pardo grisáceo. Presenta el uropatagio desnudo y la cola no excede la mitad del mismo. No posee líneas faciales 
    ni dorsales. El 50% de su alimentación se basa en frutos de arbustos y pequeños árboles.""",
    imgur['H7kfU1x.jpg'],
    dbpedia['Carollia_perspicillata'],
    eol['327438'],
	'https://www.cortolima.gov.co/sites/default/files/images/stories/centro_documentos/pom_prado/diagnostico/apendices/ap_quiropteros.pdf',
	uniprot['40233']
)

fauna(
    gbif['2433194'],
    "MURCIÉLAGO NECTIVORO",
    "Glossophaga soricina",
    """Presenta orejas cortas y redondeadas, trago triangular con la punta aguda. Labio inferior con un surco profundo 
    bordeado de pequeñas verrugas, membrana alar ligada al metatarso, uropatagio bien desarrolado, 
    calcáneo menor que el pie, pulgar grande. La coloración de las partes superiores varía del café oscuro al claro.""",
    imgur['bwWMWxz.jpg'],
    dbpedia['Glossophaga_soricina'],
    eol['327431'],
	'http://www.biodiversidad.co/fichas/3463',
	uniprot['27638']
)

fauna(
    gbif['2438073'],
    "RATÓN SILVESTRE",
    "Oryzomys alfaroi",
    """De tamaño pequeño. Hocico largo y pronunciado, ojos grandes, orejas medianas pero bien evidentes, de color 
    negruzco a marrón oscuro y de apariencia desnuda. Pelaje suave y uniforme. Dorso de color marrón rojizo oscuro a 
    marrón negruzco. Su dieta llega a incluir hojas verdes, frutas, semillas e insectos.""",
    imgur['uFjpu60.jpg'],
    dbpedia['Oryzomys_alfaroi'],
    eol['1179993'],
	'http://zoologia.puce.edu.ec/Vertebrados/mamiferos/FichaEspecie.aspx?Id=2126',
	uniprot['530171']
)

fauna(
    gbif['2440779'],
    "ARMADILLO, GURRE",
    "Dasypus novemcinctus",
    """Cuerpo cubierto con un caparazón formado por pequeñas placas óseas unidas entre sí; en su parte media, este 
    caparazón tiene una serie de bandas verticales que le dan flexibilidad, permitiendo que el animal doble su cuerpo. 
    La cola y la parte superior de la cabeza también están cubiertas con placas óseas.""",
    imgur['ZZWQB6s.jpg'],
    dbpedia['Dasypus_novemcinctus'],
    eol['328482'],
	'http://www.opepa.org/index.php?option=com_content&task=view&id=708&Itemid=29',
	uniprot['9361']
)

fauna(
    gbif['5219955'],
    "CHUCHA DE AGUA",
    "Chironectes minimus",
    """Partes superiores de color gris; cabeza marrón oscura o negruzca, con sendas manchas grisáceas a los lados de 
    la frente; línea media dorsal angosta, marrón oscura o negruzca que se dilata a nivel de las paletas; partes 
    inferiores incluyendo labios y garganta, blancos; manos y pies blanco-rosado; pulgar de los pies sin garra.""",
    imgur['7NmK2l6.jpg'],
    dbpedia['Chironectes_minimus'],
    eol['289603'],
	'http://www.biodiversidad.co/fichas/3489',
	uniprot['91500']
)

fauna(
    gbif['2439920'],
    "CHUCHA COMÚN",
    "Didelphis marsupialis",
    """Puede llegar a medir entre 45-60 cms de largo. Cuerpo de color negro, gris o amarillo, con dos capas de pelo. 
    Las orejas son puntiagudas y negras; cola desprovista de pelo. Las hembras son generalmente más pequeñas que los machos, anidan 
    en una cavidad o madriguera de un árbol, después de un período de gestación de 14 días dan a luz hasta ocho crías.""",
    imgur['TNuNdEz.jpg'],
    dbpedia['Didelphis_marsupialis'],
    eol['328504'],
	'http://www.biodiversidad.co/fichas/2509',
	uniprot['9268']
)

fauna(
    gbif['2436860'],
    "CONEJO SABANERO",
    "Sylvilagus brasiliensis",
    """Más pequeño que los conejos domesticados de origen europeo. Tiene un pelaje bastante uniforme, café oscuro 
    con algunas manchas café-anaranjadas, diferente de los colores y patrones que suelen mostrar los conejos 
    domésticos. Es más frecuente verlo en las horas del amanecer y del atardecer, cuando es más activo.""",
    imgur['UXzUUrS.jpg'],
    dbpedia['Sylvilagus_brasiliensis'],
    eol['118008'],
	'http://www.opepa.org/index.php?option=com_content&task=view&id=709&Itemid=29',
	uniprot['483865']
)

fauna(
    gbif['5218725'],
    "MURCIÉLAGO DE COLA LIBRA",
    "Molossus molossus",
    """Posee la base del pelaje pálida, la parte dorsal es negra, marrón oscuro o castaño. Tiene un hocico 
    ancho con mentón redondeado, las orejas son cortas y redondeadas. La cola generalmente es del 50% a 60% de 
    la longitud del cuerpo. se alimentan de insectos, mariposas nocturnas, hormigas voladoras y escarabajos.""",
    imgur['IDrZUo4.jpg'],
    dbpedia['Molossus_molossus'],
    eol['327951'],
	'http://www.biodiversidad.co/fichas/2504',
	uniprot['27622']
)

fauna(
    gbif['7429082'],
    "RATÓN CASERO",
    "Mus musculus",
    """Roedor pequeño, no rebasa los 21 cms de largo total y se caracteriza por poseer una cola aparentemente desnuda, 
    pero con vellosidades finas. El color puede variar mucho, desde el gris claro hasta el café o negro y 
    combinaciones de los anteriores. Olfato muy desarrollado, lo ayuda en encontrar los alimentos.""",
    imgur['Ov6b29i.jpg'],
    wikidata['Q2683493'],
    eol['328450'],
	'https://www.ecured.cu/Rat%C3%B3n_casero',
	uniprot['10090']
)

fauna(
    gbif['2439270'],
    "RATA COMÚN",
    "Rattus rattus",
    """Mide aproximadamente entre 14-20 cms y pesa entre 100-240 grs. La parte dorsal es negro rayado con pelos 
    negros y blancos sobre los costados. Las orejas son medianas y desnudas. La trompa es larga y punteada. La cola es 
    robusta, ligeramente más larga que la longitud de la cabeza y el cuerpo. Las patas son largas y gruesas.""",
    imgur['1Siv2Yv.jpg'],
    dbpedia['Rattus_rattus'],
    eol['328447'],
	'http://www.biodiversidad.co/fichas/5394',
	uniprot['10117']
)

fauna(
    gbif['5218919'],
    "COMADREJA",
    "Mustela frenata",
    """Las plantas de las patas están cubiertas con pelos, la cola es larga con el borde distal de color negro, 
    presenta manchas faciales excepto en ejemplares muy jóvenes. Suele alimentarse de aves de corral y cuyes de los cuales 
    únicamente devora el cerebro. Se ha reportado que emite un olor desagradable cuando se siente acorralada.""",
    imgur['TfQw5uP.jpg'],
    wikidata['Q20907812'],
    eol['328589'],
	'http://www.biodiversidad.co/fichas/4332',
	uniprot['55048']
)

fauna(
    gbif['2433573'],
    "PERRO DE MONTE",
    "Potos flavus",
    """Cuerpo alargado y musculoso, cabeza redondeada, rostro corto y ojos grandes y separados. Piernas y brazos 
    cortos, pero hábiles para sujetarse. Pelaje corto, aterciopelado y muy tupido, de un color marrón en la espalda 
    que se va oscureciendo al llegar a la cola y la cabeza y amarillento por la parte inferior.""",
    imgur['xgjy7vU.jpg'],
    dbpedia['Potos_flavus'],
    eol['328067'],
	'https://es.wikipedia.org/wiki/Potos_flavus',
	uniprot['29067']
)

fauna(
    gbif['2480518'],
    "GAVILÁN CAMINERO",
    "Buteo magnirostris",
    """Pequeño de 33-41 cms de longitud total. Los ojos, base de la mandíbula superior y patas son amarillos. Presenta 
    un parche rufo en la base de las plumas primarias. La cabeza, el dorso, la garganta y el pecho  en su parte 
    superior son gris pardusco y el vientre es barrado de color blanco y café. La cola es gris a rufa.""",
    imgur['6N47kRq.jpg'],
    dbpedia['Buteo_magnirostris'],
    eol['1049099'],
	'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Gavil%C3%A1n+Caminero',
	uniprot['223488']
)

fauna(
    gbif['2498402'],
    "IGUAZA MARÍA",
    "Dendrocygna bicolor",
    """Mide de 45-53 cms y pesa de 621-755 grs. Es principalmente de color café canela con una línea a lo largo de 
    la nuca de color café oscuro. Sus alas y espalda son negruzcas con un notorio escamado marrón claro.  Al vuelo 
    resaltan sus alas negruzcas, internamente cafés y una banda blanca en la base dorsal de la cola.""",
    imgur['MBgH4Dh.jpg'],
    dbpedia['Dendrocygna_bicolor'],
    eol['914528'],
	'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Iguaza+Mar%C3%ADa+-+Dendrocygna+bicolor',
	uniprot['8874']
)

fauna(
    gbif['2480830'],
    "GARZA DEL GANADO",
    "Bubulcus ibis",
    """Mide entre 46-56 cms y pesa de 340-390 grs. Tiene un aspecto rechoncho y su cuerpo es completamente blanco con 
    el pico amarillo y las patas verde opaco. Durante el período reproductivo también es blanca con la coronilla, la 
    espalda y el pecho amarillentos y el pico y las patas rojizos.""",
    imgur['vdQzk2p.jpg'],
    dbpedia['Bubulcus_ibis'],
    eol['1048666'],
	'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Garcita+del+Ganado+-+Bubulcus+ibis',
	uniprot['110668']
)


fauna(
    gbif['5231804'],
    "TORCAZA MORADA",
    "Columba cayennensis",
    """Alcanza unos 30 cms de longitud, es muy arisca y vuela alto. Plomiza, tiene la frente, cubiertas, espalda y 
    pecho castaño violáceos. Las patas rojas y el pico negro. Se mantiene solitaria, en parejas y en bandadas de hasta 
    500 individuos.""",
    imgur['gfEc6JL.jpg'],
    dbpedia['Columba_cayennensis'],
    eol['46281203'],
	'https://www.ecured.cu/Paloma_colorada',
	uniprot['8931']
)

fauna(
    gbif['2495858'],
    "TORTOLITA COMÚN",
    "Columbina talpacoti",
    """Tiene un largo total promedio de 16.5 cms. El macho es principalmente rufo canela, con las partes inferiores más 
    pálidas y la coronilla contrastante gris clara, la hembra es mucho más opaca especialmente por debajo y con la 
    espalda rojiza. Se alimenta principalmente de semillas.""",
    imgur['g2ws5Rr.jpg'],
    dbpedia['Columbina_talpacoti'],
    eol['914637'],
	'http://www.biodiversidad.co/fichas/2516',
	uniprot['504887']
)

fauna(
    gbif['2495358'],
    "TORCAZA NAGUIBLANCA",
    "Zenaida auriculata",
    """Mide 25 cms. Café oliváceo uniforme por encima, excepto la coronilla gris azulada: lados del cuello con visos 
    rosados y algo de verde iridiscentes; cara anteada con tinte vináceo; puntas de las plumas de la cola rufo 
    acanelado, contrastando con una banda medial negra. Por debajo anteado vináceo, la garganta más pálida.""",
    imgur['hxq6Rw2.jpg'],
    dbpedia['Zenaida_auriculata'],
    eol['1049710'],
	'http://www.biodiversidad.co/fichas/4608',
	uniprot['115703']
)

fauna(
    gbif['2496209'],
    "GARRAPATERO COMÚN",
    "Crotophaga ani",
    """Mide cerca de 35 cms, los machos pesan alrededor de 115 grs y las hembras cerca de 95 grs. El adulto es de color 
    negro lustroso con iris café a negro y piel alrededor del ojo negra. Su pico es arqueado, lateralmente comprimido 
    con quilla delgada, ancho en la base y curvado hacia abajo hasta la frente. Sus patas son negras y su cola larga.""",
    imgur['3NdIvQi.jpg'],
    dbpedia['Crotophaga_ani'],
    eol['915111'],
	'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Garrapatero+Com%C3%BAn+-+Crotophaga+ani',
	uniprot['103947']
)

fauna(
    gbif['5231932'],
    "TRESPIÉS",
    "Tapera naevia",
    """Mide de 26-29 cms y pesa alrededor de 52 grs. Presenta iris café a verdoso, pico café a café naranja, patas 
    café grisáceas y piel desnuda alrededor del ojo de color amarillo. Color café por encima con estriado ante y 
    negro y álula negra prominente. Presenta cresta rufa estriada de negro.""",
    imgur['z5mzfMS.jpg'],
    dbpedia['Tapera_naevia'],
    eol['913248'],
	'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Tres+Pies+-+Tapera+naevia',
	uniprot['78212']
)

fauna(
    gbif['5231103'],
    "GORRIÓN DE COLLAR RUFO",
    "Zonotrichia capensis",
    """Mide entre 11.8-13.4 cms y pesa de 16.8-31 grs. Es ligeramente crestado y con pico cónico de tamaño medio. 
    Presenta cabeza gris; nuca y lados del cuello rufos, formando un collar que se extiende hacia los lados 
    del pecho. Las plumas de su cola son cafés con los bordes rufos. Su garganta es blanca y el pecho blanco grisáceo.""",
    imgur['LeBUJrL.jpg'],
    dbpedia['Zonotrichia_capensis'],
    eol['916840'],
	'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Copet%C3%B3n+Com%C3%BAn+-+Zonotrichia+capensis',
	uniprot['44391']
)

fauna(
    gbif['2489208'],
    "GOLONDRINA AZUL",
    "Notiochelidon cyanoleuca",
    """Mide 13 cms aproximadamente; por encima es azul lustroso debajo blanco inmaculado, infracaudales negras; cola 
    ligeramente ahorquillada. Las migratorias del sur son ligeramente más grandes; el interior de las alas es gris. Las 
    jóvenes son de color verduzco con lustre azul en partes superiores.""",
    imgur['fNUpbf3.jpg'],
    dbpedia['Notiochelidon_cyanoleuca'],
    eol['1178581'],
	'http://www.biodiversidad.co/fichas/4697',
	uniprot['72892']
)

fauna(
    gbif['2484396'],
    "CHAMÓN PARÁSITO",
    "Molothrus bonariensis",
    """Mide alrededor de 22 cms. Tiene un pico corto, cónico y ojos oscuros en ambos sexos. Los machos son totalmente 
    negros púrpura lustroso. La hembra es café grisáceo opaco por encima, mucho más pálido debajo. Vive en áreas 
    abiertas, como parques y potreros. Es un ave parásita de cría, pone sus huevos en los nidos de otros pájaros.""",
    imgur['3PD6Rbw.jpg'],
    dbpedia['Molothrus_bonariensis'],
    eol['1052069'],
	'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Cham%C3%B3n+Par%C3%A1sito',
	uniprot['84836']
)

fauna(
    gbif['5228112'],
    "PERDIZ COMÚN",
    "Colinus cristatus",
    """Presenta un tamaño entre 20-23 cms. Cresta aguda conspicua. Macho: cara y garganta blanquecinos; nuca negra 
    punteada de blanco; partes inferiores café punteado; puntos blancos grandes en pecho y flancos; vientre barrado de 
    negro. Hembra: más opaca, cresta café, garganta estriada de negro.""",
    imgur['WnuKXZc.jpg'],
    dbpedia['Colinus_cristatus'],
    eol['1047228'],
	'http://www.biodiversidad.co/fichas/3456',
	uniprot['114915']
)

fauna(
    gbif['5228831'],
    "CARPINTERO REAL",
    "Dryocopus lineatus",
    """Carpintero de gran tamaño, aproximadamente 36 cms de longitud. Cresta prominente de color rojo, al igual que el 
    "bigote" y la coronilla. Lados de la cabeza y partes superiores de color negro. La espalda es negra con dos líneas 
    blancas que no se unen. Garganta con estrías de blanco y negro, pecho negro y abdomen barrado.""",
    imgur['klbmpwY.jpg'],
    dbpedia['Dryocopus_lineatus'],
    eol['1177478'],
	'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Carpintero+Real',
	uniprot['121135']
)

fauna(
    gbif['2479071'],
    "PERIQUITO DE ANTEOJOS",
    "Forpus conspicillatus",
    """Mide alrededor de 13 cms con el pico marfil. El macho es principalmente verde, más claro y más amarillento debajo, 
    región ocular azul, coberturas alares superiores e inferiores y rabadillas azul violeta. La hembra es completamente 
    verde (no azul), más brillante, verde esmeralda alrededor de los ojos, frente y rabadilla.""",
    imgur['cYGuZOk.jpg'],
    dbpedia['Forpus_conspicillatus'],
    eol['1178012'],
	'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Periquito+de+Anteojos+-+Forpus+conspicillatus',
	uniprot['1265750']
)

fauna(
    gbif['2481721'],
    "TIGUE CHICO",
    "Tringa flavipes",
    """Mide de 23-25 cms, pesa de 48-114 grs. La hembra es un poco más grande que el macho. Presenta patas amarillas y 
    pico de color negro, delgado y recto. En plumaje reproductivo presenta partes superiores moteadas de gris pardusco. 
    En plumaje no reproductivo sus partes superiores son de color gris pálido.""",
    imgur['t9NEsPh.jpg'],
    dbpedia['Tringa_flavipes'],
    eol['1049439'],
	'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Andarrios+Patiamarillo+-+Tringa+flavipes',
	uniprot['161739']
)

fauna(
    gbif['2481720'],
    "TIGUE GRANDE",
    "Tringa melanoleuca",
    """Mide de 29-33 cms, pesa de 111-235 grs. Presenta patas amarillas y pico negro ligeramente decurvado. El adulto 
    en condición no reproductiva presenta partes altas de color gris parduzco con puntos y márgenes blancos. En plumaje 
    reproductivo presenta estrías oscuras en la cabeza y el cuello y puntos negruzcos en el pecho.""",
    imgur['vJuNFpu.jpg'],
    dbpedia['Tringa_melanoleuca'],
    eol['1049431'],
	'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Andarr%C3%ADos+Mayor+-+Tringa+melanoleuca',
	uniprot['161682']
)

fauna(
    gbif['2488602'],
    "AZULEJO COMÚN",
    "Thraupis episcopus",
    """Largo total promedio de 16.5 cms. Cabeza, cuello y partes inferiores gris azul pálido, en contraste con alta espalda 
    más oscura y más azul; alas y cola marginadas de azuloso, hombros azul claro a oscuro. Su alimentación consiste 
    mayoritariamente de frutas, y puede complementarse con flores, insectos y pequeños invertebrados.""",
    imgur['lBS8Gds.jpg'],
    dbpedia['Thraupis_episcopus'],
    eol['1052952'],
	'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Azulejo+Com%C3%BAn',
	uniprot['58209']
)

fauna(
    gbif['2477507'],
    "PONCHITA",
    "Crypturellus soui",
    """Mide aproximadamente 21.5-24 cms de largo, se trata de una especie tímida, reservada y solitaria. Es un ave 
    regordeta reconocida por su pequeño tamaño, su  plumaje es de color marrón “hollín” con una sombra gris en la 
    cabeza,  su cuello es parduzco, con la garganta blanquecina, su vientre es de color canela brillante.""",
    imgur['ZBqTreQ.jpg'],
    dbpedia['Crypturellus_soui'],
    eol['1178390'],
	'https://es.wikipedia.org/wiki/Crypturellus_soui',
	uniprot['458187']
)

fauna(
    gbif['2476195'],
    "COLIBRÍ NUCA BLANCA",
    "Florisuga mellivora",
    """Tiene un largo total promedio de 10.2 cms, pico corto (20 mms) y decurvado en la punta. El macho con 
    cabeza, garganta y pecho azul lustroso, bajas partes interiores blancas, cola principalmente blanca con ápice negro. 
    La hembra verde broncíneo por encima, pecho moreno a verdoso y escamado blanco, cola verde oscura.""",
    imgur['gB61cJv.jpg'],
    dbpedia['Florisuga_mellivora'],
    eol['1048777'],
	'http://www.biodiversidad.co/fichas/2554',
	uniprot['304640']
)

fauna(
    gbif['5231459'],
    "CUCARACHERO COMÚN",
    "Troglodytes aedon",
    """Mide 11.4 cms. Café grisáceo por encima, con barrado negruzco indistinto en alas y cola; débil superciliar 
    blanco; por debajo más o menos rosáceo, usualmente más pálido en garganta y abdomen; infracaudales uniformes o 
    barradas. Mantiene la cola erecta mientras salta activamente a lo largo de setos o matorrales.""",
    imgur['qjJcsqN.jpg'],
    dbpedia['Troglodytes_aedon'],
    eol['1050659'],
	'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Cucarachero+Com%C3%BAn',
	uniprot['58211']
)

fauna(
    gbif['2482802'],
    "ATRAPA MOSCAS COPETE VERDE",
    "Empidonax virescens",
    """Mide entre 13-14.5 cms de longitud y pesa de 12.2-14 grs. Los adultos presentan corona, cuello y partes 
    superiores verde oliva, alas negruzcas. El vientre y las plumas infracaudales son amarillo pálido, su pico es largo 
    y plano con mandibula superior negra e inferior naranja pálido y sus patas son grises.""",
    imgur['BQtSLjr.jpg'],
    dbpedia['Empidonax_virescens'],
    eol['1046721'],
	'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Atrapamoscas+Verdoso',
	uniprot['209628']
)

fauna(
    gbif['5229564'],
    "VIUDITA COMÚN",
    "Fluvicola pica",
    """Su longitud es de 13 cms. Es blanco con occipucio y centro de la espalda negros: presenta alas y cola de color 
    negro; márgenes de las primarias internas y ápice de la cola de color blanco. Los jóvenes son similares a los 
    adultos pero más opacos. Ha sido observado alimentándose de mariposas y libélulas.""",
    imgur['qOTvZ37.jpg'],
    dbpedia['Fluvicola_pica'],
    eol['1053132'],
	'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Viudita+Com%C3%BAn',
	uniprot['196030']
)

fauna(
    gbif['2482755'],
    "BICHOFUÉ GRITÓN",
    "Pitangus sulphuratus",
    """Atrapamoscas que mide 22 cms y pesa aproximadamente 65 grs, es grande y robusto con un pico grande 
    y fuerte, cola relativamente corta, patas negras; coronilla negra circundada por amplia banda blanca; parche amarillo 
    oculto en la coronilla; lados de la cabeza negros; pequeña mancha amarilla en la mejilla.""",
    imgur['fEdFf4L.jpg'],
    dbpedia['Pitangus_sulphuratus'],
    eol['916841'],
	'http://www.biodiversidad.co/fichas/4535',
	uniprot['371930']
)

fauna(
    gbif['5229662'],
    "SIRIRÍ COMÚN",
    "Tyrannus melancholicus",
    """Mide cerca de 22 cms y pesa 40 grs. Tiene la cabeza gris con una máscara negruzca, posee un parche naranja oculto 
    en la coronilla. Su espalda es oliva grisáceo, sus alas y cola son de un tono café negruzco, su garganta es gris 
    pálido, las partes bajas inferiores son amarillas. El pico y las patas son negros.""",
    imgur['B50ISOf.jpg'],
    dbpedia['Tyrannus_melancholicus'],
    eol['917493'],
	'http://www.icesi.edu.co/wiki_aves_colombia/tiki-index.php?page=Sirir%C3%AD+Com%C3%BAn',
	uniprot['121427']
)

fauna(
    gbif['5226883'],
    "RABO DE AJÍ",
    "Micrurus mipartitus",
    """Cuerpo cilíndrico que puede alcanzar hasta 120 cms. De 34-84 anillos negros alternados con anillos amarillo 
    claro o blanco más pequeños. En la cola tiene entre 1-9 anillos, el negro se alterna con el rojo. La cabeza es 
    negra y cubre hasta la parte posterior de los ojos, luego inicia un anillo rojo o anaranjado amplio. Es venenosa.""",
    imgur['0Lh0LY3.jpg'],
    wikidata['Q5079828'],
    eol['1055830'],
	'http://www.serpientes-snakes.com.ar/superfamilias/micrurus_mipartitus.htm',
	uniprot['430902']
)

fauna(
    gbif['5223229'],
    "CAZADORA",
    "Clelia clelia",
    """Alcanza una longitud máxima de 22.80 cms. La coloración del dorso en juveniles es rojo profundo, la cabeza es 
    negra con una banda nucal de color crema o blanco; los adultos presentan una coloración gris oscura en el 
    dorso, las escamas labiales son mas pálidas y la región ventral es de color crema grisáceo.""",
    imgur['7N4mN4Z.jpg'],
    dbpedia['Clelia_clelia'],
    eol['454628'],
	'http://www.biodiversidad.co/fichas/2796',
	uniprot['121322']
)

fauna(
    gbif['2456089'],
    "FALSA CORAL",
    "Erythrolamprus bizona",
    """Longitud máxima de 100 cms. Presenta anillos rojos y negros, los últimos en pares, inclusive el primer anillo 
    nucal. Entre los anillos negros hay un anillo de color blanco o amarillo. La cabeza clara arriba, pero el hocico 
    y la región parietal manchados de negro. Banda ocular negra.""",
    imgur['CCodOyF.jpg'],
    dbpedia['Erythrolamprus_bizona'],
    eol['794729'],
	'http://www.biodiversidad.co/fichas/2843',
	uniprot['121327']
)

fauna(
    gbif['2454954'],
    "GUAMERA",
    "Leptodeira annulata",
    """Longitud de 19.4 cms en machos y 86.9 cms en hembras. La coloración dorsal va de café claro a café más 
    oscuro con una serie de manchas dorsales también de color café, que algunas veces pueden fusionarse dando la 
    apariencia de una línea recta o en zigzag en la región medio dorsal; la cabeza es café oscuro.""",
    imgur['hrXCrrS.jpg'],
    dbpedia['Leptodeira_annulata'],
    eol['792206'],
	'http://www.biodiversidad.co/fichas/2847',
	uniprot['121346']
)

fauna(
    gbif['2456438'],
    "TIERRERA",
    "Tantilla melanocephala",
    """Cabeza alargada y no diferenciada del cuello, ojos pequeños y el cuerpo cilíndrico y delgado. Presenta un color 
    pardo amarillento o rojizo, cada escama dorsal posee pigmentos pardos, la cabeza es de color negro, el abdomen es 
    de color blanco y sin manchas. Esta serpiente logra medir aproximadamente 50 cms de longitud, incluyendo la cola.""",
    imgur['IOAAUil.jpg'],
    dbpedia['Tantilla_melanocephala'],
    eol['2816562'],
	'http://www.serpientesdevenezuela.net/web/index.php/component/content/article?id=124',
	uniprot['121370']
)

fauna(
    gbif['2437581'],
    "GUATÍN",
    "Dasyprocta fuliginosa",
    """El dorso puede ser de color café rojizo, café amarillo o amarillo grisáceo. Puede presentar finas estrías negras 
    en el pelaje. Las partes anteriores del dorso pueden ser cafés o negras. La parte posterior del dorso tiene pelos largos 
    de color negro con las puntas amarillas. El vientre varía desde café hasta negro.""",
    imgur['pWHRfbT.jpg'],
    dbpedia['Dasyprocta_fuliginosa'],
    eol['127456'],
	'http://www.biodiversidad.co/fichas/665',
	uniprot['193455']
)

# Fauna presente en la Ruta del Maíz
g.add( (gbif['5219666'], RDF.type, WILDLIFE.TaxonName) ) # Ardilla
g.add( (gbif['2481942'], RDF.type, WILDLIFE.TaxonName) ) # Gallinazo
g.add( (gbif['2459658'], RDF.type, WILDLIFE.TaxonName) ) # Iguana Comun
g.add( (gbif['2467661'], RDF.type, WILDLIFE.TaxonName) ) # Lagarto
g.add( (gbif['5216933'], RDF.type, WILDLIFE.TaxonName) ) # Sapo Comun
g.add( (gbif['2433536'], RDF.type, WILDLIFE.TaxonName) ) # Cusumbo

#print (g.serialize(format="pretty-xml")) 
