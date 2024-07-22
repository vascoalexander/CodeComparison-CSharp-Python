# 1 Grundlagen
---
#### 1.1 Variablen

##### Übung 1.1.1
Schreiben Sie eine Reihe von Anweisungen, um 3 Variablen a, b und c zu deklarieren und ihnen die Werte **1**, **'France'** bzw. **36.2** zuzuweisen. Die Werte dieser Variablen sollen dann auf der Konsole angezeigt werden.

##### Übung 1.1.2
Schreiben Sie eine Reihe von Anweisungen, um eine Variable namens **message** zu deklarieren und mit dem Wert „hello“ zu initialisieren. Ändern Sie dann diese Variable so, dass sie den Wert „how are you“ enthält. Das Programm sollte den Inhalt der Variable nach der Änderung auf der Konsole ausgeben.

##### Übung 1.1.3
Schreiben Sie eine Reihe von Anweisungen, um 2 Variablen **x** und **y** zu deklarieren und ihnen die Werte 3 und 8.5 zuzuweisen. Konvertieren Sie dann den Typ dieser Variablen in Strings.
Das Programm soll nach der Umwandlung den Typ dieser Variablen am Ende anzeigen.

##### Übung 1.1.4
Schreiben Sie ein Programm, das den Benutzer nach seinem Gewicht in Kilogramm fragt und dieses in einer Variablen speichert. Das Programm soll am Ende das vom Benutzer eingegebene Gewicht anzeigen.

##### Übung 1.1.5
Schreiben Sie ein Programm, das zwei Zahlen vom Benutzer annimmt, die Zahlen addiert und das Ergebnis auf der Konsole ausgibt.

##### Übung 1.1.6
Schreiben Sie ein Programm, das zwei Zahlen vom Benutzer annimmt, die Zahlen dividiert und das Ergebnis auf der Konsole anzeigt. Was passiert, wenn der Divisor 0 ist?

##### Übung 1.1.7
Schreiben Sie ein Programm, das zwei Gleitkommazahlen x = 22.0 und y = 7.0 dividiert und das Ergebnis auf der Konsole anzeigt. Verwenden Sie den Modulo-Operator, um das Ergebnis auf drei Dezimalstellen genau zu formatieren.

#### 1.2 Bedingte Anweisungen

##### Übung 1.2.1
Erstellen Sie ein Programm mit dem Sie überprüfen können, ob eine eingegebene Integer größer ist als 5. Wenn ja, dann erfolgt eine Ausgabe auf dem Bildschirm.

##### Übung 1.2.2
Schreibe ein Programm das eine Zahl vom Nutzer entgegennimmt und auf der Konsole ausgibt ob die Zahl gerade oder ungerade ist.

##### Übung 1.2.3
Bei einem Wettbewerb müssen alle Teilnehmer in der Schwergewichtsklasse zwischen 235 und 265 Pfund wiegen. Schreiben Sie ein Programm, das nach dem Gewicht des Teilnehmers fragt und dann ausgibt, ob er zum Wettbewerb zugelassen ist.

##### Übung 1.2.4
Sie geben per Tastur 7 Zahlen ein. Das Programm gibt am Ende die größte Zahl aus.

##### Übung 1.2.5
Schreiben Sie ein Programm das überprüft, ob das Alter des Benutzers über 18 liegt oder nicht. Wenn das Alter des Benutzers größer oder gleich 18 ist, soll das Programm 'Der Benutzer ist volljährig' anzeigen, andernfalls 'Der Benutzer ist minderjährig'.

##### Übung 1.2.6
Eine Bank verfährt nach folgender Regel:
Wenn ein Kunde auf seinem Girokonto ein Guthaben von mehr als 1.000 Euro oder auf seinem Sparkonto ein Guthaben von mehr als 1.500 Euro hat, wird keine Scheckgebühr erhoben. Andernfalls wird eine Gebühr von 0,15 Euro erhoben. Schreiben Sie ein Programm, das nach dem Kontostand der beiden Konten fragt und dann ausgibt, wie hoch die Gebühr ist.

##### Übung 1.2.7
Ein Paketdienst berechnet 3,00 Euro Versandkosten bis zu einem
Gewicht von 10 Kilo (inklusive). Darüber sind für jedes Kilo zusätzlich 0,25 Euro zu bezahlen. Schreiben Sie ein Programm, das den Anwender nach dem Gewicht der Sendung fragt und dann die Versandkosten ausgibt.

Gewicht der Sendung: 11 
Versandkosten: 3,25 Euro

##### Übung 1.2.8
Schreiben Sie ein Programm, mit dem Sie Werte von Euro nach DM und umgekehrt ausrechnen können. Der Anwender soll dabei nach dem Betrag gefragt werden und in welche Währung der Betrag umgerechnet werden soll. Dabei soll das Zeichen 'e' für die Berechnung DM -> Euro ausgewertet werden. Ist das eingegebene Zeichen ein anderes, soll die Berechnung Euro -> DM erfolgen.

Die Formel die Sie dazu benötigen sind:
Euro = DM/1,95583 bzw.  DM = Euro * 1,95583

##### Übung 1.2.9
Verändern Sie das Programm aus Übung 1.2.8 so, dass ab einem Gewicht von 20 Kilo 0.50 Euro für jedes Kilo über 10 Kilo zu bezahlen sind.

Gewicht der Sendung: 25
Versandkosten: 10,50 Euro

##### Übung 1.2.10
Schreiben Sie ein Programm, das den Anwender nach seinem Geburtsjahr fragt, kodiert mit zwei Ziffern, und nach dem aktuellen Jahr fragt, ebenfalls kodiert mit zwei Ziffern. Das Programm soll das richtige Alter des Anwenders in Jahren ausgeben.

Geburtsjahr: 62 
Aktuelles Jahr: 09 
Ihr Alter ist: 47

##### Übung 1.2.11
Schreiben Sie ein Programm zur Berechnung von Schaltjahren.
Ob ein Jahr ein Schaltjahr ist, hängt von mehreren Bedingungen ab:
Ist ein Jahr durch 400 ohne Rest teilbar, ist es immer ein Schaltjahr. Ist ein Jahr durch 4, jedoch nicht durch 100 teilbar, ist es ein Schaltjahr. In allen anderen Fällen ist es kein Schaltjahr. Schreiben Sie ein Programm „Schaltjahr", das nach einer Jahreszahl fragt und danach überprüft, ob es sich bei dem Jahr um ein Schaltjahr handelt. Nach der Prüfung soll ausgegeben werden, ob es ein Schaltjahr ist oder nicht.

##### Übung 1.2.12
Der Hersteller eines Mikrowellenherds empfiehlt beim Erhitzen von zwei Portionen 50% mehr Erhitzungszeit und beim Erhitzen von drei Portionen, die Erhitzungszeit zu verdoppeln. Das Erhitzen von mehr als drei Portionen wird nicht empfohlen. Schreiben Sie ein Programm, das den Anwender nach der Anzahl der Portionen und nach der Erhitzungszeit für eine Portion fragt. Das Programm gibt dann die empfohlene Erhitzungszeit aus. Hinweis: Verwenden Sie vier aufeinander folgende if-Abfragen ohne else-Zweig, wobei jede von ihnen einen von vier Fällen testet: eine Portion, zwei Portionen, drei Portionen, mehr als drei Portionen.

##### Übung 1.2.13
Sepps Tanke befindet sich an der A565 in Bonn am Rande der Eifel. Die nächsten 200 Kilometer gibt es keine weitere Tankstelle. Schreiben Sie ein Programm, das den Fahrern hilft zu entscheiden, ob sie tanken sollen oder nicht.

Das Programm fragt nach:
-	Der Tankkapazität in Litern
-	Der Benzinanzeige in Prozent (voll = 100, dreiviertel voll = 75, usw.)
-	Dem Benzinverbrauch des Fahrzeugs in km pro Liter.

Die Ausgabe des Programms ist „Tanken!" oder „Weiterfahren", je nachdem, ob das Fahrzeug genug Benzin für 200 Kilometer hat oder nicht.

    Beispiel:
    Tankkapazität: 12 
    Benzinanzeige in %: 50
    Benzinverbrauch km/l: 30 
    Tanken!

#### 1.3 Schleifen


# 2 Datenstrukturen
---
#### 2.1 Arrays

#### 2.2 Listen

#### 2.3 Wörterbücher

#### 2.4 Stack

#### 2.5 Queues

#### 2.6 Verknüpfte Listen


# Nr. 3 Algorithmen
---
#### 3.1 Sortieren

#### 3.2 Suchen

#### 3.3 Rekursion

#### 3.4 Dynamische Programmierung

#### 3.5 Graphenalgorithmen


# 4 Fortgeschrittene Themen
---
#### 4.1 Objektorientierte Programmierung (OOP)

#### 4.2 Datei-I/O

#### 4.3 Behandlung von Ausnahmen

#### 4.4 Reguläre Ausdrücke

#### 4.5 Datum und Uhrzeit

#### 4.6 Unit-Tests

#### 4.7 Web Scraping