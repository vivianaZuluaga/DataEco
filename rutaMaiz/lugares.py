#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, FOAF, RDFS
from utils.ontologias import CRUZAR, VCARD, UMBEL
from utils.namespaces import facebook, youtube, maps, imgur, rutaMaiz
from flora import g

#g = Graph()

def lugares(uri, nombre, descripcion, direccion, telefono, email, imagen, video, mapa, linkURI): 
    if video != "No disponible":
        g.add( (URIRef(uri), FOAF.depiction, URIRef(video)) )#puede ser usado para indicar contenido multimedia           
    
    g.add( (URIRef(uri), RDF.type, VCARD.Location) )
    g.add( (URIRef(uri), FOAF.name, Literal(nombre, lang='es')) )
    g.add( (URIRef(uri), RDFS.comment, Literal(descripcion, lang='es')))
    g.add( (URIRef(uri), VCARD.tel, Literal(telefono))  )
    g.add( (URIRef(uri), VCARD.email, Literal(email)) ) #agente
    g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)) ) #revisar
    g.add( (URIRef(uri), VCARD.adr, URIRef(mapa)))

    #Dirección según vCard 2006
    g.add( (URIRef(mapa), RDF.type, VCARD.Address) )
    g.add( (URIRef(mapa), VCARD['country-name'], Literal('Colombia', lang='es'))) 
    g.add( (URIRef(mapa), VCARD.locality, Literal('Tuluá', lang='es'))) 
    g.add( (URIRef(mapa), VCARD['street-address'], Literal(direccion))) 
    
    g.add(( URIRef(uri), UMBEL.isAbout, URIRef(rutaMaiz['Lugares.rdf']))) 
    
    g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) ) #Link externo
    g.add( (URIRef(uri), VCARD.category, Literal("LUGARES", lang='es')))


lugares(
    rutaMaiz['Lugares.rdf#parqueGuadua'],
    'PARQUE DE LA GUADUA',
    """Cultivos de guadua y heliconias, senderos ecológicos, una cascada y una piscina natural de agua tibia son algunos 
    de los atractivos del parque. En este sitio de 51.000 m2 los turistas descansan en zonas verdes y disfrutan con 
    sus hijos en un espacio adecuado con juegos infantiles.""",
    #'Avenida Kenedy diagonal a la Productora de Jugos',
    'Entrada sur, Tuluá, Valle del Cauca',
    '22251548',
    'parqueguadua@hotmail.com',
    imgur['2r8lJWt.jpg'],
    #univalleLugares['ParqueGuadua.mp4'],
    youtube['kIMOBo6uqm4'],
    maps['wr9jbYdmt742'],
    facebook['pages/Parque-De-La-Guadua/118949828184599']
)

lugares(
    rutaMaiz['Lugares.rdf#lagoChilicote'],
    'LAGO CHILICOTE',
    """Lago ubicado en el área urbana del municipio hacia el sur-occidente de la ciudad en el cual se pueden apreciar 
    hermosos aterdeceres y una gran cantidad de ""Garzas Blancas"" que anidan en un arbol ubicado en el centro del lago.""",
    #'Barrios Sajonia y el Lago, Tuluá, Valle del Cauca',
    'Lago Chilicote, Tuluá, Valle del Cauca',
    '0',#No disponible
    'No disponible',
    imgur['BYqy4hZ.jpg'],
    #univalleLugares['lagoChilicote.mp4'],
    youtube['dW7QH47c898'],
    maps['CeSudK2K98S2'],
    'http://www.tulua.gov.co/sitio.shtml?apc=m1G5--&x=1475586'
)

lugares(
    rutaMaiz['Lugares.rdf#parqueCarlosSarmiento'],
    'PARQUE CARLOS SARMIENTO LORA',
    """Ofrece una gran piscina para niños y un área de piscina semi olímpica para adultos, restaurante, 
    refugios, zona de juegos y el Parque Universalmente Accesibe RUA.""",
    #'Entrada Variante Sur',
    'Parque Carlos Sarmiento Lora, Tuluá, Valle del Cauca',
    '2244853, 2241677',
    'parquecarlosarmientolora@hotmail.com',
    imgur['hVhPc5m.png'],
    'No disponible',
    maps['eMYDXk6nBzk'],
    facebook['parquecarlossarmientolora?fref=ts']
)

lugares(
    rutaMaiz['Lugares.rdf#parqueCespedes'],
    'PARQUE LINEAL JUAN MARÍA CÉSPEDES',
    """Punto tradicional preferido por propios y extraños para el encuentro, la tertulia, el esparcimiento en familia 
    y el descanso.""",
    'Carreras 27 y 28, Tuluá, Valle del Cauca',
    #'Parque Céspedes, Tuluá, Valle del Cauca',
    '0',#No disponible
    'No disponible',
    imgur['3Nxt5Ra.jpg'],
    'No disponible',
    maps['M5i5NihUe1Q2'],
    facebook['pages/Parque-Lineal-Cespedes/473779859367621']
)

lugares(
    rutaMaiz['Lugares.rdf#parqueDeBoyaca'],
    'PLAZA CÍVICA PARQUE DE BOYACÁ',
    """Cuenta con espacios para la preservación de la flora y la fauna,  plaza cívica  para la celebración de los 
    acontecimientos de la comunidad tulueña.""",
    'Calle 26 con Carrera 25, Tuluá, Valle del Cauca',
    '0',#No disponible
    'No disponible',
    imgur['vjn1yxv.jpg'],
    'No disponible',
    maps['ne9gP1wbxK92'],
    'http://tulua.gov.co/?apc=m1G-1484013-1484013&x=1484013'
)

lugares(
    rutaMaiz['Lugares.rdf#museoBernalEsquivel'],
    'MUSEO VIAL INTERNACIONAL BERNAL ESQUIVEL',
    """Se pueden observar al lado del río algunas obras del pintor y escultor tulueño Angel Bernal Esquivel.""",
    'Cra. 28, Tuluá, Valle del Cauca',
    '0',#No disponible
    'No disponible',
    imgur['RwG1Ft2.jpg'],
    'No disponible',
    maps['vxqvZiA8qZk'],
    'http://www.eltiempo.com/archivo/documento/MAM-689648'
)

lugares(
    rutaMaiz['Lugares.rdf#ranchoPanorama'],
    'RANCHO PANORAMA',
    """Pesca deportiva, juegos infantiles, kioscos para reuniones sociales y restaurante. Abierto de 7 am a 11 pm""",
    'Carrera 40, Tuluá, Valle del Cauca',
    '2257838, 3006194147, 3164474977',
    'No disponible',
    imgur['cbMVHSc.png'],
    youtube['4shX_UVhbuE'],
    maps['GpBCXuJiqZ82'],
    facebook['rancho.panorama/']
)

'''lugares(
    'http://wikimapia.org/31342856/es/Humedal-Charco-de-Oro',
    'HUMEDAL CHARCO DE ORO',
    """Humedal afectado por la expansión de las fronteras agrícolas""",
    'Campoalegre, Tuluá, Valle del Cauca',
    'No disponible',
    'No disponible',
    imgur['b0aTDPQ.png'],
    'No disponible',
    maps['T33fhUWuf3x']
)

lugares(
    'http://wikimapia.org/31342849/es/Humedal-La-Bolsa',
    'HUMEDAL LA BOLSA',
    """Humedal afectado por la expansión de las fronteras agrícolas""",
    'Campoalegre, Tuluá, Valle del Cauca',
    'No disponible',
    'No disponible',
    imgur['boarCCq.png'],
    'No disponible',
    maps['T33fhUWuf3x']
)'''

#print (g.serialize(format="pretty-xml")) 