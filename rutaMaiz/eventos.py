#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS, DC, FOAF
from utils.ontologias import GR, VCARD, EVENT, UMBEL, TIME, GEONAMES
from utils.namespaces import facebook, twitter, youtube, imgur, maps, rutaMaiz
from empresas import g

#g = Graph()

rutaMaizEventos = Namespace('http://190.14.254.237/dataseteco/RutaDelMaiz/Eventos/')

def eventos(uri, nombre, fecha, descripcion, lugar, media, image, uriTime, mapa, duracion):
	if media != "No disponible":
		g.add(( URIRef(uri), EVENT.illustrate, URIRef(media)) )

	g.add(( URIRef(uri), RDF.type, EVENT.Event ) )
	g.add( (URIRef(uri), FOAF.depiction, URIRef(image)) )
	g.add(( URIRef(uri), RDFS.label, Literal(nombre, lang='es')) )
	g.add(( URIRef(uri), RDFS.comment, Literal(descripcion, lang='es')) )
	
	#Fecha y duracion
	g.add( ( URIRef(uri), EVENT.time, URIRef(uriTime) ) )
	g.add( ( URIRef(uriTime), RDF.type, TIME.Interval) )
	g.add( ( URIRef(uriTime), TIME.at, Literal(fecha, datatype=XSD.dateTime) ))
	g.add( ( URIRef(uriTime), TIME.duration, Literal(duracion, datatype=XSD.duration) ))
	
	#Lugar	
	g.add( ( URIRef(uri), EVENT.place, URIRef(mapa)) )#http://www.geonames.org/3666646	
	g.add( ( URIRef(mapa), RDFS.label, Literal(lugar, lang='es')) ) # datatype=XSD.string
	
	g.add(( URIRef(uri), UMBEL.isRelatedTo, URIRef(rutaMaiz.Eventos)) )

eventos(
	'https://www.facebook.com/events/179078442487780/',
	'FIESTA DE LOS AÑOS DORADOS',
	'2016-05-27T14:00:00Z',#fecha CCYY-MM-DDThh:mm:ss Mes de Junio de todos los años
	"""Evento celebrado como antesala de la feria, un espacio para el adulto mayor con
	música, animación y refrigerios.""",#lugar
	#'Polideportivo de la I.E. Corazón del Valle Sede Tomás Uribe Uribe, Tuluá',
	'Carrera 27 con Calle 22, Tuluá, Valle del Cauca', #verificar  Cr 30 Cl 19 Esq
	#rutaMaizEventos['FIESTADORADOS.mp4'],
	youtube['gQn35OZVAM0'],
	imgur['OPWm9Vc.jpg'],
	twitter['775688832356327424'],
	maps['J5v7a2a8A842'], ## Geo no deja ubicar direcciones asi que se usa la uri de maps
	"P1D"#PnYn MnDTnH nMnS
)

eventos(
	'https://www.facebook.com/feriadetuluaoficial/posts/1716500381962189',
	'DESFILE DE BANDAS MÚSICO-MARCIALES',
	'2016-05-29T18:00:00Z',#Mes de Junio de todos los años
	'Con la participación de bandas provenientes del municipio de Tuluá y de otros municipios.',
	'Calle 25 con Carrera 5, Tuluá, Valle del Cauca',
	#rutaMaizEventos['bandas.mp4'],
	youtube['RmGl4ritx7M'],
	imgur['yus7d2D.jpg'],
	twitter['775696473652592640'],
	maps['PHgJvbo2VrL2'],
	"P1D"#PnYn MnDTnH nMnS
)

eventos(
	'https://www.facebook.com/feriadetuluaoficial/posts/1723882454557315',
	'DESFILE DE CABALLITOS DE PALO Y COMPARSAS INFANTILES',
	'2016-05-29T14:30:00Z',#Mes de Junio de todos los años
	'Evento celebrado como antesala de la feria de Tuluá.',
	'Plaza Cívica Boyacá, Tuluá, Valle del Cauca',
	#rutaMaizEventos['carnavalOrejitas.mp4'],
	youtube['Lf25yOUEnbM'],
	imgur['mF90nnF.jpg'],
	twitter['775699774334988288'],
	maps['gFUQC5kTjuC2'],
	"P1D"#PnYn MnDTnH nMnS
)

eventos(
	'https://www.facebook.com/feriadetuluaoficial/posts/1725394204406140',
	'VELADA BOXÍSTICA',
	'2016-06-01T00:00:00Z',#Mes de Junio, todos los años
	'Evento celebrado como antesala de la feria de Tuluá.',
	'Coliseo Manuel Victoria Rojas, Tuluá, Valle del Cauca',
	#rutaMaizEventos['Boxeo.mp4'],
	youtube['peed56xYCIw'],
	imgur['duRIvGC.jpg'],
	twitter['775704156095057920'],
	maps['QoiP3PhsN6S2'],
	"P1D"#PnYn MnDTnH nMnS
)

eventos(
	'http://www.eltabloide.com.co/carnaval-de-orejones/',
	'DESFILE DE COMPARSAS',
	'2016-05-30T18:00:00Z',
	'Evento celebrado como antesala de la feria de Tuluá.',
	'Transversal 12 con Calle 25, Tuluá, Valle del Cauca',
	#rutaMaizEventos['carnavalOrejones.mp4'],
	youtube['Fp14F3_JMQ8'],
	imgur['f7hcZMr.jpg'],
	twitter['775734225316241408'],
	maps['eqKGUWzZJjw'],
	"P1D"#PnYn MnDTnH nMnS
)

eventos(
	'https://www.facebook.com/feriadetuluaoficial/posts/1725381304407430',
	'JUEGOS PIROTÉCNICOS',
	'2016-06-01T20:00:00Z',
	'Evento celebrado como antesala de la feria de Tuluá.',
	#'Polideportivo Barrio Alameda y Avenida Jorge Eliécer Gaitán, Tuluá',
	'Barrio Alameda, Tuluá, Valle del Cauca',
	#rutaMaizEventos['juegosArtificiales.mp4'],
	youtube['MF0FJNXKRFc'],
	imgur['uZW2eJj.jpg'],
	twitter['775754957131747328'],
	GEONAMES['3666646'],
	"P1D"#PnYn MnDTnH nMnS
)

eventos(
	'https://www.facebook.com/feriadetuluaoficial/posts/1725601521052075',
	'CABALGATA FERIA DE TULUÁ',
	'2016-05-28T14:30:00Z',
	'Evento de apertura de la feria de Tuluá.',
	#'Estación de Servicio Terpel vía Aguaclara, Tuluá',
	'Av Principal Aguaclara, Tuluá, Valle del Cauca',
	#rutaMaizEventos['cabalgataTulua.mp4'],
	youtube['2vli_5pwWhE'],
	imgur['I0aaPIy.jpg'],
	twitter['775771646573572096'],
	GEONAMES['3666646'],
	"P1D"#PnYn MnDTnH nMnS
)

eventos(
	'https://www.facebook.com/feriadetuluaoficial/',
	'FERIA DE TULUÁ',
	'2016-06-02T00:00:00Z',
	"""La programación es variada, desde lo agropecuario, ganadero, artesanal hasta las presentaciones de 
	artistas nacionales e internacionales de manera simultánea en cinco escenarios diferentes de la ciudad.""",
	'Tuluá, Valle del Cauca',
	#rutaMaizEventos['feriaTulua.mp4'],
	youtube['Tu24OPFWFIE'],
	imgur['Q9EgLz2.jpg'],
	'http://www.eltabloide.com.co/huele-a-feria/',
	GEONAMES['3666646'],
	"P4D"#PnYn MnDTnH nMnS
)

eventos(
	'https://www.facebook.com/encuentro.deestudiantinas.94/',
	"ENCUENTRO NACIONAL DE ESTUDIANTINAS 'HECTOR CEDEÑO'",
	'2016-11-13T00:00:00Z',
	"""Tiene como objetivo preservar la memoria del Maestro Hector Cedeño y difundir la música andina
	colombiana interpretada por estudiantinas. La programación del evento incluye la presentación de
	las Estudiantinas participantes en diferentes espacios públicos con acceso gratuito.""",
	'Parque Céspedes, Tuluá, Valle del Cauca',
	#rutaMaizEventos['estudiantinas.mp4'],
	youtube['bBNXc5diBQc'],
	imgur['ziCJBhU.jpg'],
	twitter['775782302861389824'],
	maps['V99seUN68Bm'],
	"P2D"#PnYn MnDTnH nMnS
)

eventos(
	'https://www.facebook.com/events/1850449368500266/',
	'FESTIVAL DEL MATE, EL GUARAPO Y LA MÚSICA AUTÓCTONA',
	'2016-10-14T00:00:00Z',#Segunda semana del mes de Agosto de cada año
	"""Tradicional evento tulueño que rescata y preserva las raíces culturales cultivando el amor por nuestra música, 
	además reúne a buena parte de los grupos de música andina y latinoamericana de la región en un solo concierto.""",
	'Calle 42 Cra 32, Tuluá, Valle del Cauca',
	#rutaMaizEventos['mate.mp4'],
	youtube['Wpr0u16-tlE'],
	imgur['w7uDnPD.jpg'],
	twitter['775783573018316800'],
	maps['TaAGeYoxZFo'],
	"P2D"#PnYn MnDTnH nMnS
)

eventos(
	'http://www.tulua.gov.co/sitio.shtml?apc=B1--1481401-1481401&x=1480722',
	'FESTIVAL DEL RÍO TULUÁ',
	'2016-03-16T00:00:00Z',#Segunda semana del mes de octubre de cada año
	"""Venta de platos típicos de la región, bebidas y dulces típicos. Campeonatos de voley playa, ciclomontañismo, 
	competencias en triciclos y en patines, concurso de pintura para los niños, competencias en neumáticos por el lecho del río 
	Tuluá, se presentan artistas en tarima y se realizan actividades de limpieza.""",
	#'Costado del lecho del Río Tuluá, entre las calles 38 y 42 del barrio Fátima, Tuluá, Valle del Cauca',
	'Calles 38 y 42, Tuluá, Valle del Cauca',
	#rutaMaizEventos['festiRio.mp4'],
	youtube['voluzOZjDEU'],
	imgur['jSRvxep.jpg'],
	twitter['775784947407810560'],
	maps['7CgYpqsvSvM2'],
	"P1D"#PnYn MnDTnH nMnS
)

eventos(
	'http://www.tulua.gov.co/sitio.shtml?apc=B1-1--&x=1480719',
	'FESTIVAL REGIONAL DE COMETAS CLUB ROTARIO TULUÁ',
	'2016-08-07T00:00:00Z',#Segundo Domingo del mes de Agosto
	"""Cada año acuden cerca de 1.000 expositores de cometas y aproximadamente 12.000 visitantes y 
	observadores. En el marco del festival se hace una exposición de paracaidistas y ultralivianos, por parte 
	de la Fuerza Aérea Colombiana.""",
	'Departamento Administrativo De Tránsito, Tuluá, Valle del Cauca',#lugar cercano
	#rutaMaizEventos['festivalCometas.mp4'],
	youtube['CNbl8ERcuW0'],
	imgur['8fIkCUN.jpg'],
	twitter['775806976097816576'],
	maps['E1aZrAQbDkT2'],
	"P1D"#PnYn MnDTnH nMnS
)

eventos(
	'http://www.sancochofest.co/',
	'SANCOCHO FEST',
	'2016-02-05T00:00:00Z',#Primer fin de semana del mes de febrero de cada año
	"""Evento gratuito que intenta mostrar lo mejor de propuestas emergentes en el área de la música, cine, fotografía, 
	poesía donde pueden participar y asistir todas las personas amantes de la cultura.""",
	'Parque Céspedes, Tuluá, Valle del Cauca',
	#rutaMaizEventos['sancochoFest.mp4'],
	youtube['4c_Tj-pfebs'],
	imgur['CcGKhZF.jpg'],
	twitter['775813581631725568'],
	maps['CxALtR6eg3o'],
	"P3D"#PnYn MnDTnH nMnS
)

eventos(
	'http://www.tulua.gov.co/sitio.shtml?apc=C1v16--&x=1517450',
	'FIESTAS DE LA RUTA DEL MAÍZ',
	'2016-05-18T10:30:00Z',
	"""Comprenden la gastronomía en torno a productos hechos a base de maíz.""",
	'Campoalegre, Tuluá, Valle del Cauca',
	#rutaMaizEventos['fiestasMaiz.mp4'],
	youtube['D7rWW6TwIrQ'],
	imgur['KikTRxw.png'],
	twitter['775822493596647424'],
	maps['DGoj5ahqmem'],
	"P1D"#PnYn MnDTnH nMnS
)

eventos(
	'https://www.facebook.com/XVIII-Carrera-Atl%C3%A9tica-y-Recreativa-Fenalco-R%C3%ACo-Tulu%C3%A0-962006747253233/',
	'CARRERA ATLÉTICA Y RECREATIVA FENALCO RÍO TULUÁ',
	'2016-07-24T07:00:00Z',#hasta las 2:30
	"""Este evento se ha realizado desde hace 18 años, siendo el segundo evento más importante de la ciudad, 
	declarado por el concejo municipal como interés deportivo y cultural.""",
	#'Carreras 28 y 30 Frente a Industria de Harinas Tuluá',
	'Industrias De Harinas Tuluá, Tuluá, Valle del Cauca',
	#rutaMaizEventos['carreraAtletica.mp4'],
	youtube['fNK21W2k6hQ'],
	imgur['OyVpEFV.jpg'],
	twitter['775828352833847296'],
	maps['ZQLF915NyA82'],
	"P1D"#PnYn MnDTnH nMnS
)

eventos(
	'https://www.facebook.com/events/454437778093456',
	'ROTARY RUN',
	'2016-10-09T08:00:00Z',#hasta las 2:30
	"""Carrera atlética incluyente organizada por el Club Rotario Tuluá El Lago, los competidores recorren 
	entre 4-12 kms. El dinero recaudado se destina a obras sociales. Valor de la inscripción $30000""",
	#'Carreras 28 y 30 Frente a Industria de Harinas Tuluá',
	'Parque Céspedes, Tuluá, Valle del Cauca',
	#rutaMaizEventos['carreraAtletica.mp4'],
	youtube['dMowaObVXyM'],
	imgur['MQ2962y.png'],
	twitter['786720513901092864'],
	maps['DkW2w3rnnh82'],
	"PT5H"#PnYn MnDTnH nMnS
)

#print (g.serialize(format="pretty-xml")) 	
