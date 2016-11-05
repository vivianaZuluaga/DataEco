#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, FOAF, RDFS
from utils.ontologias import CRUZAR, VCARD, UMBEL
from utils.namespaces import rutaJardin, facebook, maps, youtube, imgur
from floraJardinBotanico import g

#g = Graph()

def lugares(uri, nombre, descripcion, direccion, telefono, email, imagen, video, mapa): 
    if video == "No disponible":
        g.add( (URIRef(uri), FOAF.depiction, Literal('No disponible')) )
    else:
        g.add( (URIRef(uri), FOAF.depiction, URIRef(video)) )#puede ser usado para indicar contenido multimedia           
    
    g.add( (URIRef(uri), RDF.type, CRUZAR['Recurso-turistico']) )
    g.add( (URIRef(uri), RDF.type, VCARD.Location) )
    g.add( (URIRef(uri), FOAF.name, Literal(nombre, lang='es')) )
    g.add( (URIRef(uri), RDFS.comment, Literal(descripcion, lang='es')) )
    g.add( (URIRef(uri), VCARD.tel, Literal(telefono))  )
    g.add( (URIRef(uri), VCARD.email, Literal(email)) )

    g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)) ) #revisar
    g.add( (URIRef(uri), VCARD.adr, URIRef(mapa)))

    #Dirección según vCard 2006
    g.add( (URIRef(mapa), RDF.type, VCARD.Address) )
    g.add( (URIRef(mapa), VCARD['country-name'], Literal('Colombia', lang='es')) )
    g.add( (URIRef(mapa), VCARD.locality, Literal('Tuluá', lang='es')) )
    g.add( (URIRef(mapa), VCARD['street-address'], Literal(direccion)) )
    
    g.add(( URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaJardin.Lugares)))


lugares(
    'http://inciva.gov.co/cespedesia/itemlist/category/17-jardin-botanico',
    'JARDÍN BOTÁNICO JUAN MARÍA CÉSPEDES',
    """Guarda un tesoro destinado para investigadores, científicos, amantes de la
    flora y la fauna y del paisaje que ofrecen los bosques secos tropicales.""",
    'Mateguada, Valle del Cauca',
    '3206888271, 3156361319',
    'jardinbotanico@inciva.gov.co',
    imgur['QIthGO2.jpg'],#imagen
    youtube['QuhYS8KmnEs'],#video
    maps['hRdkwZBgae22']
)

lugares(
    'http://www.ciudadguru.com.co/empresas/cascada-de-la-arenosa-en-mateguadua/tulua/15951514',
    'CASCADA LA ARENOSA',
    """Hermoso sitio natural, agua muy fria, con arenas blancas y grandes piedras que la circundan.
    Los lugareños ofrecen la práctica del Rapell sobre la cascada y Rafting por el Río Tuluá hasta
    llegar al Jardín Botánico. A 7 kms de la cabecera municipal.""",
    'Mateguada, Valle del Cauca',
    '2260975, 2339300',
    'turismo@tulua.gov.co',
    imgur['mJd34Ks.jpg'],
    youtube['gChA97Gc1xs'],#video
    maps['wefveCHtHxG2']
)

lugares(
    'http://www.ciudadguru.com.co/empresas/semillero-de-guadua-y-bambu/tulua/15952774',
    'SEMILLERO DE GUADUA Y BAMBÚ',
    """Vivencie los túneles que forman las guaduas y bambúes en el semillero más grande de Latinoamérica
    en el número de especies. Cierre los ojos y disfrute de los olores de las guaduas y los sonidos
    de los pájaros que despiertan los sentidos. Ubicado en el Jardín Botánico.""",
    'Mateguada, Valle del Cauca',
    '2260975, 3002202211',
    'No disponible',
    imgur['lOZmXmJ.jpg'],#imagen
    'No disponible', #VIDEO
    maps['DiGWwzkH2kx']
)

#print(g.serialize(format='pretty-xml'))    
