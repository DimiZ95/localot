
"""
Das folgende Skript zeigt auf, welche KPI´s relevant sind, um eine nachhaltige CO2-Wirtschaft
für das vorliegende Projekt:"localot" darzustellen.

Hierzu wird auf verschiedene Faktoren eingegangen, welche sowohl bezugnehmend auf die CO2 Werte, 
als auch auf weitere Indikatoren stützen.

Folgende Faktoren, werden als wichtig angesehen.

#1 CO2 Verbrauch, wenn der Endkunde mit dem Auto in die Stadt fährt
#2 Wasserverbrauch, zur Herstellung eines Kartons 
#3 Energieverbrauch in KW/h, zum herstellen eines Kartons 
#4 Gesamtvolumen des Kartons

"""
import xml.etree.ElementTree as ET
import urllib.request
import urllib.parse
import urllib
global c
global db


'''
   #1 CO2 Verbrauch, wenn der Endkunde mit dem auto in die Stadt fährt

   :param float fromlat_Einzelhändler1: Breitengrad des EInzelhändlers, welcher üblicherweise als Stammdaten bei erstellung des Profils in eine Datenbank eingepflegt werden 
   :param float fromlong_Einzelhändler1: Längengrad des EInzelhändlers, welcher üblicherweise als Stammdaten bei erstellung des Profils in eine Datenbank eingepflegt werden 
   :param float tolat_Endkunde1: Breitengrad des Endkunden, welcher üblicherweise als Stammdaten bei erstellung des Profils in eine Datenbank eingepflegt werden 
   :param float tolong_Endkunde1: Längengrad des Endkunden, welcher üblicherweise als Stammdaten bei erstellung des Profils in eine Datenbank eingepflegt werden   
   :param str url: Gesamt-URL, zur Abfrage der API Daten
   :param float routeDistance: Komplette Distanz in Meilen
   :param float routeDistanceKm: Komplette Distanz in Km
   :param float co2Verbrauch_auto: Endverbrauch der Strecke hin und zurück

   '''
fromlat_Einzelhändler1 = 49.473388
fromlong_Einzelhändler1 = 8.474956
tolat_Endkunde1 = 49.478059
tolong_Endkunde1 = 8.472934

#Extrahiere die Daten der API 
url= "http://yournavigation.org/api/dev/route.php?flat=" + str(fromlat_Einzelhändler1) + "&flon=" + str(fromlong_Einzelhändler1) + "&tlat=" + str(tolat_Endkunde1) + "&tlon=" + str(tolong_Endkunde1) +"&v=motorcar&fast=1&instructions=1" 
connection = urllib.request.urlopen(url)
js = connection.read()
root = ET.fromstring(js)
for child in root:
    for c in child:
        global distance
        if c.tag == "{http://earth.google.com/kml/2.0}distance":
            distance= c.text
routeDistance = float(distance)
routeDistanceKm = routeDistance * 1.60934

#Hin- und Rückfahrt 
gesamtstrecke = routeDistanceKm *2 
#700m werden für die Parkplatzsuche verwendet abgeleitet durch http://inrix.com/press-releases/parking-pain-de/
gesamtstrecke = gesamtstrecke + 0.7

"""
Seit 2015 müssen die Hersteller einen CO2-Grenzwert von durchschnittlich 130 Gramm 
pro Kilometer (g/km) einhalten, ab 2021 sind dann 95 g/km festgeschrieben.
Quelle: bund.net/themen/mobilitaet/autos/co2-emissionen/?wc=21735

Gemäß dieser Annahme, wird von ausgegangen, dass durchschnittlich ein KFZ 130g CO2 pro km verbraucht. 
"""
co2Verbrauch_auto = gesamtstrecke * 130
print(co2Verbrauch_auto)


