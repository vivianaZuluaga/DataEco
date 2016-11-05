#Ontologias definidas para modelar el ambito del ecoturismo y geografia
from rdflib import Namespace
OWL = Namespace('http://www.w3.org/2002/07/owl#')

#Turismo
CRUZAR = Namespace('http://idi.fundacionctic.org/cruzar/turismo#')
ACCO = Namespace('http://purl.org/acco/ns#') #Alojamientos
WILDLIFE = Namespace('http://purl.org/ontology/wo/')

#Geografia
GEONAMES = Namespace('http://www.geonames.org/') #dataset
GEOPOS = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#')
GEOES = Namespace('http://geo.linkeddata.es/ontology/') #

#Otros
GR = Namespace('http://purl.org/goodrelations/v1#')#ontologia del e-comerce
VCARD = Namespace('http://www.w3.org/2006/vcard/ns#')
EVENT = Namespace('http://purl.org/NET/c4dm/event.owl#')#eventos
UMBEL = Namespace('http://umbel.org/umbel#')
TIME = Namespace('http://purl.org/NET/c4dm/timeline.owl#')#indicar lapsos de tiempo

#Proyecto
DOAP = Namespace('http://usefulinc.com/ns/doap#')
VoID = Namespace('http://rdfs.org/ns/void#')
dcterms = Namespace('http://purl.org/dc/terms/')
