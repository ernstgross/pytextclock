#!/usr/bin/env python

# Importiere Zeit-Modul
import time

# Definiere "dictionary" für die "Text-Uhr"
dict_text_clock={}
    

def init():
    """Öffnet die Datei Uhrprojekt_Zeitanzeige_Zeitansage.csv
    und liest den Key und den Value aus und speichert diese im Ditctionary
    dict_text_clock.
    """
    with open("Uhrprojekt_Zeitanzeige_Zeitansage.csv", encoding="utf-8") as f:
        for line in f:
            line = line.replace("\n", "")
            (key,val) = line.split(",")
            dict_text_clock[key] = val

def get_text_time(hour, minute):
    """ Make out of hour and minute a readable text.
    hour:    hours in range 0..23
    minutes: minutes in range 0..59 """

    # Erstelle den "key". Beachte dabei die führenden Nullen für Stunden und Minuten.
    hour   = hour%24    # Damit können wir "fehlerhafte" Eingaben über 23 Stunden behandeln.
    minute = minute%60  # Damit können wir "fehlerhafte" Eingaben über 59 Minuten behandeln.
    minute = minute - minute%5 # Damit regeln wir den Fünf-Minuten-Takt
    dict_text_clock_key = "{0:02d}:{1:02d}".format(hour, minute)
    #print(dict_text_clock_key

    # Gebe den Text der Uhrzeit aus dem Dictionary zurück.
    return dict_text_clock[dict_text_clock_key]


# HAUPTPROGRAMM 

def hautprogramm():
    
    # Initialisiere dictionary
    init()

    # Eine Schleife welche die Ausgabe der aktuellen Zeit für immer wiederholt.
    while True:
        # Echte/Reale Zeit
        # Hole aktuelle, lokale Zeit
        zeit=time.localtime()

        # Gebe Zeit aus
        print(get_text_time(zeit.tm_hour, zeit.tm_min))

        # Berechne Zeit bis zum nächsten Aufwachen.
        delta_minuten_schlafen  = 4 - zeit.tm_min%5
        delta_sekunden_schlafen = 60 - zeit.tm_sec
        delta_sekunden_gesamt_schlafen = delta_minuten_schlafen*60 + delta_sekunden_schlafen

        # Debug-Info als Test (kann später auskommentiert werden)
        print("\t\tAktuelle Zeit: " + time.asctime())
        print("\t\tIch schlafe "+str(delta_minuten_schlafen)+" Minuten und "+str(delta_sekunden_schlafen)+" Sekunden (insgesamt "+ str(delta_sekunden_gesamt_schlafen)+" Sekunden) bis zum nächsten 'Gong'")

        # Schlafe bis zum nächsten "Gong"
        time.sleep(delta_sekunden_gesamt_schlafen)
        
        
if __name__ == '__main__':
    hautprogramm()
