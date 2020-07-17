# Ratespiel, Tiere erraten, einfacher Code mit einer einfachen Funktion
# Funktion für die Bewertung der Frage und das addieren von Punkten bei richtiger Antwort
def pruef_quest(quest, antwort) :
    global points
#mehrere Versuche für den Teilnehmer einräumen, durch die Funktion "noch_quest" in der Funktion "pruef_quest"
    noch_quest = True
    versuch = 0
    while noch_quest and versuch < 3 :
        if quest.lower() == antwort.lower() :
            print("Korrekt")
#weniger Punkte für Antwort nach mehr Versuchen
            points = points + 3 - versuch
            noch_quest = False
        else :
            if versuch < 2 :
                quest = input("Leider falsch. Vesuche es erneut! ")
            versuch = versuch + 1
# nach 3 Versuchen wird die richtge Antwort angegeben und kein Punkt vergeben
    if versuch == 3 :
        print("Die richtige Antwort ist " + antwort)
    # Ingnorieren der Groß/Kleinschreibung für die Antworten
    #if quest.lower() == antwort.lower() :
     #   print("Korrekt")
      #  points = points + 1


# Zuerst werden die Punkte auf 0 gesetzt.
#Variable "punkte" wird erstellt
points = 0
# Das Spiel wird vorgestellt
print("Errate das Tier")
# erste Frage für das Spiel
quest1 = input("Welcher Bär lebt am Nordpol? ")
# Prüfung der Antwort mit oben ersteller Funktion pruef_quest
pruef_quest(quest1, "Eisbär")
#weitere Fragen hinzufügen
quest2 = input("Welches ist das schnellste Landtier? ")
pruef_quest(quest2, "Gepard")
quest3 = input("Welches ist das größte Tier? ")
pruef_quest(quest3, "Blauwal")
#Muliple choice Fragen mit Zeilenumbruch \n
quest4 = input("Welches Tier ist ein Fisch? \n A) Wal\n B) Delphin\n C) Hai\n D) Tintenfisch\n Schreibe A, B, C oder D? ")
pruef_quest(quest4, "C")
#Fragen mit 2 Antwort - Möglichkeiten - Ja oder Nein
quest5 = input("Mäuse sind Säugetiere. Richtig oder Falsch? ")
pruef_quest(quest5, "Richtig")

#Gesamtanzahl der Punkte anzeigen
print("Deine Punktezahl ist " + str(points))




