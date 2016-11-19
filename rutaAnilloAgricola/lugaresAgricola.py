#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, FOAF, RDFS
from utils.ontologias import CRUZAR, VCARD, UMBEL
from utils.namespaces import rutaAnillo, facebook, twitter, imgur, maps, youtube
from empresasAgricola import g

#g = Graph()

def lugares(uri, nombre, descripcion, direccion, telefono, email, imagen, video, mapa, linkURI): 
    if video != "No disponible":
        g.add( (URIRef(uri), FOAF.depiction, URIRef(video)) )#puede ser usado para indicar contenido multimedia 
                  
    g.add( (URIRef(uri), RDF.type, VCARD.Location) )
    g.add( (URIRef(uri), FOAF.name, Literal(nombre, lang="es")) )
    g.add( (URIRef(uri), RDFS.comment, Literal(descripcion, lang="es")) )
    g.add( (URIRef(uri), VCARD.tel, Literal(telefono))  )
    g.add( (URIRef(uri), VCARD.email, Literal(email)) ) #agente
    g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)) ) 
    g.add( (URIRef(uri), VCARD.adr, URIRef(mapa)))

    #Dirección según vCard 2006
    g.add( (URIRef(mapa), RDF.type, VCARD.Address) )
    g.add( (URIRef(mapa), VCARD['country-name'], Literal('Colombia', lang="es")) )
    g.add( (URIRef(mapa), VCARD.locality, Literal('Tuluá', lang="es")) )
    g.add( (URIRef(mapa), VCARD['street-address'], Literal(direccion)) )
    
    g.add(( URIRef(uri), UMBEL.isAbout, URIRef(rutaAnillo['Lugares.rdf'])))
    g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) ) #Link externo
    g.add( (URIRef(uri), VCARD.category, Literal("LUGARES", lang='es')))
    
lugares(
    rutaAnillo['Lugares.rdf#santoAparecido'],#uri
    'CAPILLA DEL SANTO APARECIDO',#nombre
    """En la capilla se conserva una escultura de porcelana que refleja el Cristo descendido de la Cruz. Dicha escultura 
    fue encontrada hace más de 100 años por una campesina tulueña y es venerada por los milagros que ha concedido a sus 
    creyentes. Ubicada antes de la vereda El Cairo, sobre la vía principal.""",#descripcion
    'Vía Tres Esquinas, Tuluá, Valle del Cauca',#direccion
    '0',#telefono
    'No disponible',#email
    imgur['iG762nC.png'],#imagen
    youtube['WeQNXoFSjL0'],#video
    maps['2qhg5w2iAjk'],#mapa
    facebook['pages/Capilla-Santo-Aparecido/161137537424017']
)

lugares(
    rutaAnillo['Lugares.rdf#humedalSapera'],#uri
    'HUMEDAL BOCAS DE TULUÁ - LA SAPERA',#nombre
    """Se trata de un humedal cubierto en gran porcentaje por macrófitas; la zona amortiguadora en su mayoría son pastos 
    utilizados para el ganado; se encuentra aledaño al río Tuluá, el cual lo surte constantemente. Ubicado en las Haciendas 
    Bilbao y Normandía.""",#descripcion
    'Bocas de Tuluá, Tuluá, Valle del Cauca',#direccion
    '0',#telefono
    'cuentosverdes@cvc.gov.co',#email
    imgur['vNIj2k4.png'],#imagen
    youtube['cncHUYEsr2k'],#video
    maps['8jXReqSHzkA2'],#mapa
    "https://issuu.com/natucreativa/docs/humedales_del_valle_geogr__fico_del/177"
)

#print (g.serialize(format='pretty-xml'))
