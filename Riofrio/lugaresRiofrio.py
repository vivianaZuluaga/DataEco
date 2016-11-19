#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, FOAF, RDFS
from utils.ontologias import CRUZAR, VCARD, UMBEL
from utils.namespaces import rioFrio, facebook, youtube, maps, imgur, alcaldiaRiofrio
from floraRiofrio import g

#g = Graph()

def lugares(uri, nombre, descripcion, direccion, telefono, email, imagen, video, mapa, linkURI): 
    if video != "No disponible":
        g.add( (URIRef(uri), FOAF.depiction, URIRef(video)) )#puede ser usado para indicar contenido multimedia         
          
    g.add( (URIRef(uri), RDF.type, VCARD.Location) )
    g.add( (URIRef(uri), FOAF.name, Literal(nombre, lang="es")) )
    g.add( (URIRef(uri), RDFS.comment, Literal(descripcion, lang="es")) )
    g.add( (URIRef(uri), VCARD.tel, Literal(telefono))  )
    g.add( (URIRef(uri), VCARD.email, Literal(email)) ) #agente
    g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)) ) #revisar
    g.add( (URIRef(uri), VCARD.adr, URIRef(mapa)))

    #Dirección segun vCard 2006
    g.add( (URIRef(mapa), RDF.type, VCARD.Address) )
    g.add( (URIRef(mapa), VCARD['country-name'], Literal('Colombia', lang="es")) )
    g.add( (URIRef(mapa), VCARD.locality, Literal('Tuluá', lang="es")) )
    g.add( (URIRef(mapa), VCARD['street-address'], Literal(direccion)) )
    
    g.add(( URIRef(uri), UMBEL.isAbout, URIRef(rioFrio['Lugares.rdf']))) 
    g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) ) #Link externo
    g.add( (URIRef(uri), VCARD.category, Literal("LUGARES", lang='es')))

lugares(
     rioFrio['Lugares.rdf#liverpool'],
     'RESERVA LIVERPOOL',
     """Reserva natural privada del Ingenio Carmelita, ubicada en la Vereda El Rubí entre 2.500 y 2.700 m.s.n.m. 
     (340 Has. De Extensión)""",
     'El Rubí, Riofrío, Valle del Cauca',
     '2268216, 2268518',
     'contactenos@riofrio-valle.gov.co',
     imgur['ZFsI0Cg.jpg'],#imagen
     youtube["AuWsKQC1Jhc"],
     maps['JJktYcue2Zt'],
     'http://noticiasasopromay.blogspot.com.co/2012_06_01_archive.html'
 )


lugares(
     rioFrio['Lugares.rdf#paramoDelDuende'],
     'PARQUE NATURAL REGIONAL PÁRAMO DEL DUENDE',
     """Con una caida promedio de 17 metros, río Volcanes, se observan aves Asomas. Área ideal para la investigación y 
     la observación de flora y fauna.""",
     'Fenicia, Riofrío, Valle del Cauca',
     '2268216',
     'secretariadevivienda@riofrio-valle.gov.co',
     imgur['8xxvoXr.jpg'],#img Duende
     youtube['Sp533NukCt8'],
     maps['qziatSoJ9Y32'],
     'http://www.rutasdelpaisajeculturalcafetero.com/publicaciones/parque_natural_regional_paramo_del_duende_pub'
 )

lugares(
     rioFrio['Lugares.rdf#madrigal'],
     'MADRE VIEJA MADRIGAL',
     """Integrada por 2 municipios (Riofrío y Trujillo), cultivo de peces en jaula, avistamiento de aves, pesca deportiva, 
     camping, paseos en bote. Más información en www.humedalmadrigal.com""",
     'Riofrío, Valle del Cauca',
     '3177194645, 3158679031',
     'sogorronesmadrigal@hotmail.com',
     imgur['03Pemo9.png'],#img Madrigal
     youtube['DHC-jWC5vfo'],
     maps['Ze5wUxVTuDp'],
     'http://bibliotecadigital.icesi.edu.co/biblioteca_digital/handle/10906/41280?locale=de'
 )

lugares(
     rioFrio['Lugares.rdf#cantarrana'],
     'HUMEDAL CANTARRANA',
     """Regula los cauces de las quebradas Madrigal y Cascajal que surten los acueductos de esas 
     dos veredas. Ubicado a 3 Kms desde la cabecera municipal.""",
     'Riofrío, Valle del Cauca',
     '2268216, 2268518',
     'contactenos@riofrio-valle.gov.co',
     imgur['CDEVm8e.jpg'],#laguna catarra
     youtube['xUt92wqHkXg'],
     maps['aQnRwhYV7PS2'],
     alcaldiaRiofrio['index.shtml?apc=bjxx-2-&x=2720839']
 )

lugares(
     rioFrio['Lugares.rdf#parqueRicardoCruz'],
     'PARQUE RECREACIONAL RICARDO ALVARADO CRUZ',
     """Hermoso parque recreacional ubicado a 500 ms de la cabecera municipal de Riofrío.""",
     'Riofrío, Valle del Cauca',
     '2268216, 2268518',
     'contactenos@riofrio-valle.gov.co',
     imgur['QeXkX3q.jpg'],
     "No disponible",
     maps['Ye2zWFPtpMM2'],
     alcaldiaRiofrio['directorio_turisrico.shtml?apc=blxx-1-&x=2721146']
 )

lugares(
     rioFrio['Lugares.rdf#laVigoroza'],
     'VEREDA LA VIGOROZA',
     """Ciclomontañismo, venta de agua de panela con queso y sancocho de gallina. Ubicada a 11.5 kms de la cabecera municipal.""",
     'Gato Cansado, Riofrío, Valle del Cauca',
     '2268216, 2268518',
     'contactenos@riofrio-valle.gov.co',
     imgur['ku8zAMo.jpg'],
     youtube['c63bDwCiJqg'],
     maps['daQ8kovQ15S2'],
     'http://mapasamerica.dices.net/colombia/mapa.php?nombre=Vereda-Vigorosa&id=4582'
 )
 
lugares(
     rioFrio['Lugares.rdf#vayju'], #uri
     'VAYJÚ ECOTURISMO',#nombre
     """Ofrece a sus visitantes, avistamiento de aves, muros para escalar, canopy en el río Riofrío, pista de habilidades, 
     senderos ecológicos, cabalgatas, piscina con agua natural, contacto con animales, camping y cabañas. Acceso por vía 
     pavimentada en carro particular o en el bus de Tuluá a Salónica. Abierto de lunes a jueves 
     a partir de las 9:00 am hasta las 5:30 pm; viernes, sábado y domingo jornada continua. Más información 
     en http://www.vayju.com/""",#descripcion
     'Km 6 Via Riofrío - Salonica, Riofrío, Valle Del Cauca',#direccion
     '3146977558, 3116035261﻿',#telefono
     'info@vayju.com',#email
     imgur['2kG9Yv6.png'],#imagen
     youtube['saWfPiVCj6E'],#video
     maps['FpogG14WkaQ2'],
     facebook['VAYJUFincaEcoturistica/']
)
 
lugares(
     rioFrio['Lugares.rdf#cascadaSanAlfonso'], #uri
     'CASCADA DE SAN ALFONSO',#nombre
     """Hermosa cascada con una caída de unos cien metros, para llegar hay que tomar la vía que va hacia la vereda Alfonso-Alto 
     (Salónica) hasta la finca El Avenazo; a partir de allí caminar unos veinte minutos por la ribera de una quebrada. 
     Cuando se acaba el camino de tierra, continuar cien metros aproximadamente.""",#descripcion
     'Salónica - Riofrío, Valle Del Cauca',#direccion
     '0',#telefono
     'No disponible',#email
     imgur['iY8pkul.png'],#imagen
     youtube['oPsdlaKcNgg'],#video
     maps['cBJ1RgE7KbM2'],
     alcaldiaRiofrio['index.shtml?apc=bjxx-2-&x=2719492']
)

lugares(
     rioFrio['Lugares.rdf#cuancua'], #uri
     'BALNEARIO CUANCUA',#nombre
     """Centro recreacional con piscina natural de aguas provenientes del río Cuancua, ricas en sabaletas, jetudos, boca chicos, 
     y barbudos que lo hacen ser un gran atractivo para amantes de la pesca, presentaciones artísticas, senderos ecológicos, 
     servicio de parqueadero vigilado y cabañas. ENTRADA: $1000 COP""",#descripcion
     'km 4 vía Riofrío - Trujillo, Valle Del Cauca',#direccion
     '3103742201',#telefono
     'No disponible',#email
     imgur['9sfJnNc.png'],#imagen
     youtube['Ih9BDZRBINs'],#video
     maps['4KFK9Y79afH2'],#2pDcxzA2ojN2
     facebook['Balneario-Cuancua-236420123136159']
)
 
#print (g.serialize(format="pretty-xml"))
