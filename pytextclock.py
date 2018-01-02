#!/usr/bin/env python

# Importiere Zeit-Modul
import time

# Definiere "dictionary" für die "Text-Uhr"
dict_text_clock = {
    "00:00" : "null",
    "00:05" : "fünf nach null",
    "11:55" : "fünf vor zwölf",
    "12:00" : "zwölf",
    "12:05" : "fünf nach zwölf",
    "12:10" : "zehn nach zwölf",
    "12:15" : "fünfzehn nach zwölf",
    "12:20" : "zwanzig nach zwölf",
    "12:25" : "fünfundzwanig nach zwölf",
    "12:30" : "dreißig nach zwölf",
    }
 

def get_text_time(hour, minute):
    """Make out of hour and minute a readable text.
    hour:    hours in range 0..12
    minutes: minutes in range 0..59 """

    # Erstelle den "key". Beachte dabei die führenden Nullen für Stunden und Minuten.
    dict_text_clock_key = "{0:02d}:{1:02d}".format(hour, minute-minute%5)
    #print(dict_text_clock_key)

    # Gebe den Text der Uhrzeit aus dem Dictionary zurück.
    return dict_text_clock[dict_text_clock_key]


# HAUPTPROGRAMM 

# Teste get_text_time(hour, minute)
assert(get_text_time(00, 00) == "null")
assert(get_text_time(11, 55) == "fünf vor zwölf")
assert(get_text_time(11, 59) == "fünf vor zwölf")
assert(get_text_time(12, 0)  == "zwölf")
assert(get_text_time(12, 4)  == "zwölf")
assert(get_text_time(12, 5)  == "fünf nach zwölf")


# Echte/Reale Zeit
# Hole aktuelle, lokale Zeit
#zeit=time.localtime()

# Gebe Zeit aus
#print(get_text_time(zeit.tm_hour, zeit.tm_min))

