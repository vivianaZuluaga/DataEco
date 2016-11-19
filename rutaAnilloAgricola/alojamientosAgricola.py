#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS, FOAF
from utils.ontologias import GR, VCARD, ACCO, UMBEL
from utils.namespaces import rutaAnillo, facebook, twitter, imgur, maps, youtube, alcaldiaTulua
from rutaAnilloAgricola import g

#g = Graph()

def alojamientos(uri, nombre, webpage, telefono, email, direcc, mapa, descripcion, uriRoom, uriValue, 
    uriBed, numHabitaciones, numCamas, imagen, linkURI):
    if webpage != "No disponible":
        g.add( (URIRef(uri), FOAF.homepage, URIRef(webpage)))
            
    g.add( (URIRef(uri), RDF.type, ACCO.Hotel))
    g.add( (URIRef(uri), RDF.type, GR.Individual) )
    g.add( (URIRef(uri), GR.name, Literal(nombre, lang='es')) )
    g.add( (URIRef(uri), GR.description, Literal(descripcion, lang='es')) )
    g.add( (URIRef(uri), VCARD.tel, Literal(telefono)))
    g.add( (URIRef(uri), VCARD.email, Literal(email)))
    g.add( (URIRef(uri), FOAF.depiction, URIRef(imagen)))
    g.add( (URIRef(uri), VCARD.adr, URIRef(mapa)))

    #Dirección según vCard 2006
    g.add( (URIRef(mapa), RDF.type, VCARD.Address) )
    g.add( (URIRef(mapa), VCARD['country-name'], Literal('Colombia', lang='es')) )
    g.add( (URIRef(mapa), VCARD.locality, Literal('Tuluá', lang='es')) )
    g.add( (URIRef(mapa), VCARD['street-address'], Literal(direcc)) )

    #Horario de Atención
    g.add( (URIRef(uri), ACCO.feature, ACCO.AccommodationFeature) )
    g.add( (ACCO.AccommodationFeature, ACCO.availabilityTimes, Literal("24 Horas")) )

    #Habitaciones
    g.add( (URIRef(uriRoom), RDF.type, ACCO.HotelRoom))
    g.add( (URIRef(uriRoom), RDF.type, GR.SomeItems) )
    g.add( (URIRef(uriRoom), ACCO.partOf, URIRef(uri)) )

    #Value
    g.add( (URIRef(uriValue), RDF.type, GR.QuantitativeValue))
    g.add( (URIRef(uriRoom), ACCO.numberOfRooms, URIRef(uriValue)) )
    g.add( (URIRef(uriValue), GR.hasUnitOfMeasurement, Literal("C62"))) #No hay unidades
    g.add( (URIRef(uriValue), GR.hasValue, Literal(numHabitaciones, datatype=XSD.int)))

    #Camas
    g.add( (URIRef(uriBed), RDF.type, ACCO.BedDetails))
    g.add( (URIRef(uriRoom), ACCO.bed, URIRef(uriBed)))
    g.add( (URIRef(uriBed), ACCO.quantity, Literal(numCamas, datatype=XSD.int)))
    
    g.add( (URIRef(uri), RDFS.seeAlso, URIRef(linkURI)) ) #Link externo
    g.add( (URIRef(uri), VCARD.category, Literal("ALOJAMIENTOS", lang='es')))
    
    g.add((URIRef(uri), UMBEL.isAbout, URIRef(rutaAnillo['Alojamientos.rdf'])))
    


alojamientos(
    rutaAnillo['Alojamientos.rdf#miCabana'],#uri
    "CLUB BALNEARIO MI CABAÑA",#nombre
    "No disponible",#webpage
    "3182230849",#telefono
    "No disponible",#email
    "Narino, Tuluá, Valle del Cauca",#direccion
    maps['vrmxo7Rz8M72'],#mapa
    """Dedicados a la realización de reuniones sociales, sancocho de gallina. Cuenta con piscina, cabañas, restaurante, 
    discoteca. Ubicado en el Km 5 Vía Riofrío""",#descripcion
    facebook['eventos.micabana'],#uriroom
    "http://www.nexdu.com/co/Mi-Cabana-Club-Balneario-Tulua",#urivalue
    "http://www.amarillasinternet.com/balneariomicabana/",#uriBed
    "",#numHab
    "",#numCamas
    imgur['DnVGwKO.jpg'],#imagen
    youtube['FwF0DNd-qOQ']
)

alojamientos(
    rutaAnillo['Alojamientos.rdf#villaJacob'],#uri
    "FINCA VILLA JACOB",#nombre
    "No disponible",#webpage
    "3104951792, 3146560061, 3044117513",#telefono
    "No disponible",#email
    "Narino, Tuluá, Valle del Cauca",#direccion
    maps['Y9wRrEzBSGT2'],#mapa
    """Sitio campestre para recrearse y descansar, habitaciones con baño privado, además cocina, 
    piscina, una amplia zona verde, fogón de leña, kiosco de juegos. Ubicada por el callejón de la Capilla a 10 
    minutos de Tuluá.""",#descripcion
    imgur['QsK17rv.jpg'],#uriroom
    "http://www.mivalledecompras.com/servicios/stulua/alquileres/fincas/fincavillajacob/",#urivalue
    imgur['H7FEhFm.jpg'],#uriBed
    "4",#numHab
    "4",#numCamas
    imgur['USKW6kJ.jpg'],#imagen
    facebook['Finca-VillaJacob-1533300763660562/']
)

alojamientos(
    rutaAnillo['Alojamientos.rdf#piedraRoja'],#uri
    "PIEDRA ROJA COMPLEJO TURÍSTICO",#nombre
    "http://www.complejopiedraroja.com",#webpage
    "3174030301, 3174783629, 3103701115",#telefono
    "piedrarojatulua@hotmail.com",#email
    "Tres Esquinas, Tuluá, Valle del Cauca",#direccion
    maps['xp8uxKxpR7L2'],#mapa
    """Cuenta con alquiler de cabañas, canchas de fútbol, servicio de piscina, salón para eventos sociales, juegos y 
    un ambiente acogedor que no puede dejar de visitar. Ubicado en la Vereda Papayal.""",#descripcion
    facebook['piedrarojatulua'],#uriroom
    imgur['XITlQoT.jpg'],#urivalue
    imgur['fmqTZ94.jpg'],#uriBed
    "",#numHab
    "",#numCamas
    imgur['fXKwhIT.jpg'],#imagen
    facebook['Piedra-Roja-Tulua-222463944443876']
)

alojamientos(
    rutaAnillo['Alojamientos.rdf#fincaHerradura'],#uri
    "FINCA LA HERRADURA",#nombre
    "No disponible",#webpage
    "3103747120",#telefono
    "No disponible",#email
    "Tres Esquinas, Tuluá, Valle del Cauca",#direccion
    maps['9UQfQtZPmmE2'],#mapa
    """Alquiler de cabañas. Ubicada en la Vereda Gato Negro""",#descripcion
    "http://amarillasaz.com/co/finca-la-herradura/tulua/anuncio-37317",#uriroom
    "http://www.nexdu.com/co/Finca-La-Herradura-Tulua",#urivalue
    "http://tulua.linkbyme.co/finca-la-herradura-if232497/",#uriBed
    "",#numHab
    "",#numCamas
    imgur['z7Sj7ag.jpg'],#imagen
    facebook['fincalaherradura.tuluavalle']
)

alojamientos(
    rutaAnillo['Alojamientos.rdf#villaStamford'],#uri
    "FINCA VILLA STAMFORD",#nombre
    "No disponible",#webpage
    "3136132871, 3105417776, 2324843",#telefono
    "No disponible",#email
    "Tres Esquinas, Tuluá, Valle del Cauca",#direccion
    maps['56rMdnXS6Yw'],#mapa
    """Sitio campestre para recrearse y descansar, habitaciones con baño privado, cocina interna, piscina adultos y niños, 
    amplia zona verde, fogón de leña, asador, kiosco y más. Ubicada en el callejón de las Viudas.""",#descripcion
    facebook['villastamford.soto'],#uriroom
    "http://mivalledecompras.com/servicios/stulua/alquileres/fincas/fincavillastamfort",#urivalue
    imgur['hReO1On.jpg'],#uriBed
    "4",#numHab
    "29",#numCamas
    imgur['qfz0H56.jpg'],#imagen
    youtube['0qJR4UNfqrQ']
)

'''alojamientos(
    twitter['770219551191687168'],#uri
    "VILLA ADRIANA",#nombre
    "No disponible",#webpage
    "2251615, 2251817, 316 420 84 14",#telefono
    "No disponible",#email
    "Vía Nariño - La Palmera cruce hacia Los Caimos",#direccion
    maps['LNWJ8JVHChw'],#mapa
    """Ofrece pasadías y hospedaje, capacidad para 9 personas, zona de camping, piscina para niños, kiosco pequeño para eventos, 
    contacto con animales de granja: patos, gallinas y otros.""",#descripcion
    facebook[''],#uriroom
    valleCompras[''],#urivalue
    imgur[''],#uriBed
    "3",#numHab
    "7",#numCamas
    imgur['']#imagen
)'''

'''alojamientos(
    twitter['770221231530442752'],#uri
    "Villa Lozano",#nombre
    "No disponible",#webpage
    "310 470 48 24",#telefono
    "No disponible",#email
    "Corregimiento de Nariño - vía a La palmera  Callejón Maldonado",#direccion
    maps['paMt6nKByNz'],#mapa
    """Ofrece pasadías y hospedaje, capacidad para 12 personas, zona de camping, zona para asados, piscina, kiosco pequeño para 
    eventos, senderos ecológicos, cultivos de cítricos.""",#descripcion
    "http://186.116.11.66/suimweb/ARCHIVOS/ADMINISTRATIVO/SISTEMAS%20DE%20INFORMACI%C3%93N/OTROS%20-%20MODELO%20EXPEDIENTE%20MUNICIPAL%20-%20TULUA,%20VALLE%20-%202005.PDF",#uriroom
    valleCompras[''],#urivalue
    imgur[''],#uriBed
    "4",#numHab
    "8",#numCamas
    imgur['']#imagen
)'''

alojamientos(
    rutaAnillo['Alojamientos.rdf#genesis'],#uri
    "VILLA GÉNESIS",#nombre
    "No disponible",#webpage
    "3122064128, 3128881294, 3123467429",#telefono
    "ORLA.0822@gmail.com",#email
    "Narino, Tuluá, Valle del Cauca",#direccion
    maps['iiRh1N7xQE92'],#mapa
    """Para eventos empresariales y familiares, dos cabañas para alojamiento los fines de semana (con o sin alimentación).""",#descripcion
    imgur['sh6Sy2R.jpg'],#uriroom
    "http://mivalledecompras.com/servicios/stulua/alquileres/fincas/fincaennarino",#urivalue
    imgur['N5engS1.jpg'],#uriBed
    "5",#numHab
    "25",#numCamas
    imgur['kOINh1e.jpg'],#imagen
    facebook['Genesis.finca/']
)


alojamientos(
    rutaAnillo['Alojamientos.rdf#miRubi'],#uri
    "VILLA MI RUBÍ",#nombre
    "No disponible",#webpage
    "2253083, 2312366, 3128472553",#telefono
    "No disponible",#email
    "Tres Esquinas, Tuluá, Valle del Cauca",#direccion
    maps['gwfwM1bw2b72'],#mapa
    """Ofrece pasadías y hospedaje. Capacidad para 7 personas, zona de camping, piscina, kiosco pequeño para eventos, 
    senderos ecológicos, juegos, mesa de billar y mesa de ping pong. Ubicada en el callejón Las Viudas""",#descripcion
    alcaldiaTulua['1475507'],#uriroom
    "http://www.tulua-valle.gov.co/sitio.shtml?apc=B---1475507-1481399-1475507&x=1475507",#urivalue
    "http://www.furniturekraft.com/uploads/products/910e-bed%20copy.jpg",#uriBed
    "3",#numHab
    "7",#numCamas
    imgur['PcYSh4U.jpg'],#imagen
    twitter['770222399069511680']
)

'''alojamientos(
    twitter['770227640611512321'],#uri
    "Villa Carmela",#nombre
    "No disponible",#webpage
    "2313439, 3113152765",#telefono
    "No disponible",#email
    "Corregimiento Tres Esquinas - callejón Gato Negro",#direccion
    maps['8vP2fgEYYTR2'],#mapa
    """Ofrece pasadías y hospedaje. Capacidad para 12 personas, zona de camping, piscina, kiosco pequeño para eventos, 
    cancha de microfútbol.""",#descripcion
    alcaldiaTulua['1475508'],#uriroom
    valleCompras[''],#urivalue
    imgur[''],#uriBed
    "4",#numHab
    "7",#numCamas
    imgur['']#imagen
)'''

'''alojamientos(
    twitter[''],#uri
    "Villa La Mami",#nombre
    "No disponible",#webpage
    "2232 07 14",#telefono
    "No disponible",#email
    "Corregimiento Tres esquinas - Callejón La Soledad",#direccion
    maps['8vP2fgEYYTR2'],#mapa
    """Ofrece pasadías y hospedaje. Capacidad para 10 personas, piscina.""",#descripcion
    "http://www.tulua-valle.gov.co/sitio.shtml?apc=m-r-1475510-1475510&x=1475510",#uriroom
    valleCompras[''],#urivalue
    imgur[''],#uriBed
    "3",#numHab
    "5",#numCamas
    imgur['']#imagen
)'''

'''alojamientos(
    twitter[''],#uri
    "Villa Patricia",#nombre
    "",#webpage
    "3136611037, 3103733585, 3167017653",#telefono
    "No disponible",#email
    "Sobre la vía principal corregimiento Tres Esquinas",#direccion
    maps[''],#mapa
    """Ofrece pasadías y hospedaje. Capacidad para 12 personas, zona de camping, zona deportiva y recreativa con capacidad para 
    200 personas, piscina recreativa y piscina infantil, jacuzzi, sauna, kiosco, juegos infantiles, cancha de microfútbol, 
    cancha de voleibol playa, mesa de billar, bar junto a la piscina, interacción con animales de granja: avícola.""",#descripcion
    facebook[''],#uriroom
    valleCompras[''],#urivalue
    imgur[''],#uriBed
    "3",#numHab
    "6",#numCamas
    imgur['']#imagen
)'''

'''alojamientos(
    twitter[''],#uri
    "Villa Consuelo",#nombre
    "",#webpage
    "231 80 40",#telefono
    "No disponible",#email
    "Corregimiento Tres Esquinas - vereda El Cairo",#direccion
    maps[''],#mapa
    """Ofrece pasadías y hospedaje. Capacidad para 42 personas, zona de camping, piscina para niños y adultos, kiosco pequeño 
    para eventos, interacción con animales de granja: caballos pony, ganzos, pavo real, micos y perros, visita a cultivos 
    de cítricos.""",#descripcion
    "http://www.tulua.gov.co/sitio.shtml?apc=B1--1475512-1475512",#uriroom
    valleCompras[''],#urivalue
    imgur[''],#uriBed
    "6",#numHab
    "21",#numCamas
    imgur['']#imagen
)'''

##############################################3
alojamientos(
    rutaAnillo['Alojamientos.rdf#laCalenita'],#uri
    "FINCA LA CALEÑITA CASA BANQUETERA",#nombre
    "No disponible",#webpage
    "3183456354",#telefono
    "No disponible",#email
    "Narino, Tuluá, Valle del Cauca",#direccion
    maps['iiRh1N7xQE92'],#mapa
    """Finca campestre para eventos sociales y familiares. Piscina, kiosko y una hermosa casa a tu servicio. 
    Ubicada en el callejón Mejoral.""",#descripcion
    facebook['pages/Finca-La-Calenita/1431019867115336'],#uriroom
    facebook['pages/Narino-Finca-La-Calenita/1535586643352277'],#urivalue
    facebook['profile.php?id=100009334215790'],#uriBed
    "",#numHab
    "",#numCamas
    imgur['CuyuQUz.png'],#imagen
    youtube['fUycJ_7Zacg']
)

alojamientos(
    rutaAnillo['Alojamientos.rdf#laIsabella'],#uri
    "FINCA CAMPESTRE LA ISABELLA",#nombre
    "No disponible",#webpage
    "3175174964, 3167999472",#telefono
    "info@livevalledelcauca.com",#email
    "Tres Esquinas, Tuluá, Valle del Cauca",#direccion
    maps['azbNQKuB2K42'],#mapa
    """Capacidad para 20 personas, mesa de billar, juegos de mesa, 
    piscina, asador, kiosko, zona de camping, zona de hamacas, eventos sociales.""",#descripcion
    imgur['w3QswAp.jpg'],#uriroom
    "http://www.livevalledelcauca.com/tulua/finca-campestre-la-isabella.html",#urivalue
    imgur['dDu5y6d.jpg'],#uriBed
    "",#numHab
    "20",#numCamas
    imgur['R3SkKFT.jpg'],#imagen
    twitter['796178416772988929']
)

#print (g.serialize(format='pretty-xml'))
