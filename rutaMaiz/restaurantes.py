#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, FOAF, RDFS
from utils.ontologias import GR, VCARD, UMBEL
from utils.namespaces import facebook, youtube, maps, imgur, twitter, alcaldiaTulua, rutaMaiz
from lugares import g

#g = Graph()

def restaurantes(uri, nombre, menu, telefono, direccion, webpage, imagen, mapa, uriatencion, abre, cierra, linkURI):
    if webpage != "No disponible":
        g.add( (URIRef(uri), FOAF.homepage, URIRef(webpage)) )
            
    g.add( (URIRef(uri), RDF.type, GR.Location) )
    g.add( (URIRef(uri), GR.name, Literal(nombre, lang='es')) )
    g.add( (URIRef(uri), GR.description, Literal(menu, lang='es')))
    g.add( (URIRef(uri), VCARD.tel, Literal(telefono)) )
    g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)) )
    g.add( (URIRef(uri), VCARD.adr, URIRef(mapa)))
    g.add( (URIRef(uri), GR.hasOpeningHoursSpecification, URIRef(uriatencion)) )
     
    #Dirección según vCard 2006
    g.add( (URIRef(mapa), RDF.type, VCARD.Address) )
    g.add( (URIRef(mapa), VCARD['country-name'], Literal('Colombia', lang='es')) )
    g.add( (URIRef(mapa), VCARD.locality, Literal('Tuluá', lang='es')) )
    g.add( (URIRef(mapa), VCARD['street-address'], Literal(direccion)) )

    #Horario de atencion
    g.add( (URIRef(uriatencion), RDF.type, GR.OpeningHoursSpecification) )
    g.add( (URIRef(uriatencion), GR.opens, Literal(abre, datatype=XSD.time)) )
    g.add( (URIRef(uriatencion), GR.closes, Literal(cierra, datatype=XSD.time)) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Monday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Tuesday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Wednesday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Thursday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Friday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Saturday) )
    g.add( (URIRef(uriatencion), GR.hasOpeningHoursDayOfWeek, GR.Sunday) )

    g.add(( URIRef(uri), UMBEL.isAbout, URIRef(rutaMaiz['Restaurantes.rdf'])))
    
    g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) ) #Link externo
    g.add( (URIRef(uri), VCARD.category, Literal("RESTAURANTES", lang='es')))


restaurantes(
    rutaMaiz['Restaurantes.rdf#laLeonora'],
    'HACIENDA LA LEONORA',
    """Tamal Valluno, subidos de maíz, cordero asado, chicha de maíz, ajiaco bogotano, manjar  blanco, 
    envueltos de choclo, natilla de maíz.""",
    '3116404505, 3152689558',
    'Campoalegre, Tuluá, Valle del Cauca',
    'No disponible',
    imgur['Y1JJa6b.png'],
    maps['xduJAL6Guy52'],
    youtube["q0UgTCZa1bE"],
    "09:00:00",
    "18:00:00",
    twitter['Ecodataset/status/715737460697931776']
)#con imagen por defecto

restaurantes(
    rutaMaiz['Restaurantes.rdf#elOcaso'],
    'EL OCASO',
    """Torta de maíz, chorizo campesino, chancarina, fiambre valluno.""",
    '3122502184',
    'Campoalegre, Tuluá, Valle del Cauca',
    'No disponible',
    imgur['GH1dzyy.png'],
    maps['negZQ2kbGjm'],
    youtube["q0UgTCZa1bE"],
    "09:00:00",
    "18:00:00",
    twitter['Ecodataset/status/741127397727162368']
)#con imagen por defecto

restaurantes(
    rutaMaiz['Restaurantes.rdf#losAlmendros'],
    'LOS ALMENDROS',
    """Ancas de rana, macho rucio, champús de maíz con frutas tropicales.""",
    '3152768355',
    'Campoalegre, Tuluá, Valle del Cauca',
    'No disponible',
    imgur['wOtGdsn.png'],
    maps['iPprdddk6AR2'],
    youtube["q0UgTCZa1bE"],
    "09:00:00",
    "18:00:00",
    twitter['Ecodataset/status/741129909305761794']
)#con imagen por defecto

restaurantes(
    rutaMaiz['Restaurantes.rdf#laCabanuela'],
    'LA CABAÑUELA',
    """cerdo de raza Zungo, plato con media gallina sudada, refrescante aperitivo sirope acompañado 
    con ricos platos mexicanos.""",
    '3175935835',
    'Campoalegre, Tuluá, Valle del Cauca',
    'No disponible',
    imgur['zl1BfDe.png'],
    maps['GoRsVqBHHKU2'],
    youtube["q0UgTCZa1bE"],
    "09:00:00",
    "18:00:00",
    twitter['Ecodataset/status/741132208879079424']
)#con imagen por defecto

restaurantes(
    rutaMaiz['Restaurantes.rdf#elJardin'],
    'EL JARDÍN',
    """Tradicional sancocho de gallina hecho en fogón de leña,  mazamorra de maíz.""",
    '3178767249',
    'Campoalegre, Tuluá, Valle del Cauca',
    'No disponible',
    imgur['ndNjAOf.png'],
    maps['iBs1aDqjjZt'],
    youtube["q0UgTCZa1bE"],
    "09:00:00",
    "18:00:00",
    twitter['Ecodataset/status/741133124176912384']
)#con imagen por defecto

restaurantes(
    rutaMaiz['Restaurantes.rdf#laBenilda'],
    'FINCA LA BENILDA',
    """Trasnochado de maíz, mazorcas de choclo asado, bandeja paisa, masato de maíz, arepas de choclo.""",
    '3104540005, 3182190336',
    'Campoalegre, Tuluá, Valle del Cauca',
    'No disponible',
    imgur['1RTtsR2.png'],
    maps['sgYUQMTqwwq'],
    youtube["q0UgTCZa1bE"],
    "09:00:00",
    "18:00:00",
    twitter['Ecodataset/status/741135052847874049']
)#con imagen por defecto

restaurantes(
    rutaMaiz['Restaurantes.rdf#americanPizza'],
    'AMERICAN PIZZA',
    """Jugos naturales, Lasañas, Churrasco, Ensaladas de Frutas, Sandwich, Malteadas, Pancerotes, 
    Ensaladas, Comidas Rápidas.""",
    '2240055, 2246515',
    'Carrera 28 Calle 30 Esquina, Tuluá, Valle del Cauca',
    'http://www.americanpizza.com.co/',
    imgur['c8eKdtZ.jpg'],#http://i.imgur.com/UoeDHRA.jpg
    maps['aD6R6DSjix62'],
    alcaldiaTulua['1475546'],
    "14:00:00",
    "23:00:00",
    facebook['American-Pizza-1608357502820958/']
)

restaurantes(
    rutaMaiz['Restaurantes.rdf#elPaisa'],
    'AQUÍ ES EL PAISA',
    """Lleva más de diecisiete años deleitando el paladar de los tulueños con comida típica, buena mesa y sazón paisa.
    Ofrece los mejores platos antioqueños, asados al carbón, comida gourmet, comidas rápidas, deliciosas y variadas picadas.""",
    '2256373, 3207113313, 3164788008',
    'Carrera 26 No. 38 - 144, Tuluá, Valle del Cauca',
    'http://www.aquieselpaisatulua.com/',
    imgur['F1yFg3a.jpg'], # http://i.imgur.com/y7LetOi.jpg
    maps['LzCHbGg7FVt'],
    alcaldiaTulua['1475518'],
    "17:00:00",
    "01:00:00",
    'http://www.aquieselpaisatulua.com/file/menu-aqui-es-el-paisa.pdf'
)

restaurantes(
    rutaMaiz['Restaurantes.rdf#la26'],
    'RESTAURANTE Y PANADERÍA LA 26',
    """Asadero y panadería. Expertos en la elaboración de gran variedad de productos alimenticios""",
    '2252791',
    'Carrera 26 No. 26 - 55, Tuluá, Valle del Cauca',
    'No disponible',
    imgur['LzYGArL.jpg'], # http://i.imgur.com/VeoLHUb.jpg
    maps['BSZnHjrLkW22'],
    "http://www.amarillascolombia.co/colombia/tulua/restaurantes/pollos-asados-mario-195432",
    "07:00:00",
    "20:00:00",
    alcaldiaTulua['1475516']
)#con imagen por defecto

restaurantes(
    #facebook['pages/Restaurante-El-Rincon-Costeño/1497339127212455'.decode('utf-8')],
    rutaMaiz['Restaurantes.rdf#rinconCosteno'],
    'RINCÓN COSTEÑO',
    """Ofrece deliciosa comida de mar, comida costeña, cazuela de mariscos.""",
    '2241054',
    'Calle 25 No. 22 - 51, Tuluá, Valle del Cauca',
    'No disponible',
    imgur['AXpED2P.jpg'],
    maps['f9yB84FSLT22'],
    alcaldiaTulua['1475514'],
    "09:30:00",
    "21:30:00",
    twitter['Ecodataset/status/760293709074366464']
)

restaurantes(
    rutaMaiz['Restaurantes.rdf#santaLucia'],
    'SANTA LUCÍA GOURMET RESTAURANTE BAR',
    """Ofrece la mejor cocina típica del Centro del Valle e internacional dentro de un ambiente campestre y familiar.""",
    '2244405, 3012295291',
    'Carrera 40 calle 17 B, Tuluá, Valle del Cauca',
    'No disponible',
    imgur['awE45sO.jpg'],
    maps['nNKSLnqPFVQ2'],
    alcaldiaTulua['1475527'],
    "07:00:00",
    "21:00:00",
    facebook['groups/57057973652']
)

restaurantes(
    rutaMaiz['Restaurantes.rdf#sebastianParrilla'],
    'SEBASTIÁN PARRILLA',
    """Asadero, deliciosos Chorizos de San Rafael los mejores de Tuluá.""",
    '2262697',
    'Carrera 28 No. 21 - 10, Tuluá, Valle del Cauca',
    'No disponible',
    imgur['Vawm18F.jpg'], #http://i.imgur.com/PapcNxf.jpg
    maps['QFEESFyNmsT2'],
    alcaldiaTulua['1475526'],
    "06:00:00",
    "22:00:00",
    facebook['pages/Sebastian-Parrilla/675857662453037']
)

restaurantes(
    rutaMaiz['Restaurantes.rdf#todoChuletas'],
    'TODO CHULETAS EXPRESS TULUÁ',
    """Restaurante a manteles. Ofrecemos sopas, carne, pollo, arroz, ensaladas.""",
    '2242979, 2255494',
    'Carrera 27A No. 42 - 184, Tuluá, Valle del Cauca',
    'No disponible',
    imgur['vCd5h8K.jpg'], #http://i.imgur.com/Ag2VbUV.jpg
    maps['5yQt2Tz5eeG2'],
    alcaldiaTulua['1475523'],
    "10:00:00",
    "15:00:00",
    facebook['Restaurante-Todo-Chuletas-Tulua-1636237983291640/']
)

restaurantes(
    rutaMaiz['Restaurantes.rdf#wagner'],
    'WAGNER`S COFFEE',
    """Delicioso café en la presentación que más te gusta, 
    acompañado de crepes, sandwich, hamburguesas, cheasecake, ... y otras delicias.""",
    '3164222259',
    'Carrera 32 No. 24 - 41, Tuluá, Valle del Cauca',
    'No disponible',
    imgur['MbOMDNi.jpg'], #http://i.imgur.com/p9b3Yyy.jpg
    maps['YPjRMLgFdS92'],
    alcaldiaTulua['1512189'],
    "10:00:00",
    "21:00:00",
    facebook['uban.wagner']
)

restaurantes(
    rutaMaiz['Restaurantes.rdf#yerbabuena'],
    'YERBABUENA RESTAURANTE VIVERO',
    """Combina la calidad gastronómica y un servicio de restaurante adecuado en medio de un ambiente 
    campestre con espacios amplios y cómodos. Exquisitos platos inspirados en la gastronomía nacional e internacional.""",
    '2262323, 2248999, 3146616634',
    'Carrera 40 # 17B - 28, Tuluá, Valle del Cauca',
    'http://restauranteyerbabuena.co/',
    imgur['qwKiXDM.png'],
    maps['1GTzW5tqFYD2'],
    alcaldiaTulua['1475521'],
    "08:00:00",
    "21:00:00",
    facebook['RestauranteYerbabuenaCo']
)

#print (g.serialize(format="pretty-xml"))   
