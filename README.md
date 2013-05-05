konRuStra
=========
<p>
Projektname:                        konRuStra <br>
Projektinitiator/Projekturheber:    dodo <br>
Projektlizenz:                      GPLv3 <br>
</p>
Ein Rundenbasiertes Strategiespiel in der Konsole.<br>
<h3>Zielsetzung:</h3>
* mehrere verschiedene Spielerklassen: Soldat (soldier) Schurke (robber) Magier (wizard)
* Erfahrungspunktesystem (Funktion: experienceGen, giveEP)
* Handel (Funktion: trade)
* 10*10 Feld
* einfach zu verstehender Code
* leicht anzupassender Code
* am besten als Packet gepackt
* einfache Bedienung
* Lokalisierte Versionen
* eine Konfigurationsdatei, welche die Werte für play enthält und kommentiert ist <br>
<br>
<strong>Der Code soll aus drei einfachen Klassen bestehen: </strong>

<h5>main</h5> 
<p>
Liefert die Funktionen für den Spielablauf <br>
</p>

<h5>test</h5> 
<p>
Testet die Funktionen von main <br>
test war für Entwickler gedacht, die ein wenig rumspielen <br>
wollen
</p>

<h5>userInput</h5>
<p>
Regelt die Interaktion mit dem User und benutzt dabei main und test. <br>
Wird in play verwendet. <br>
</p>

<h5>play</h5>
<p>
Reduziert sich auf die für das Spiel wichtigen Funktionen <br>
play soll nur Funktionen, die aus test oder main <br>
stammen, sinnvoll aufrufen. Wenn möglich auch wieder schön in <br>
eine Klasse verpackt. 
</p>
<p>
Für Entwickler gibt es die Datei notes.txt. In ihr werden die Ideen
des Initiators beschrieben. Außerdem dient die Datei als Handbuch
für das Projekt.
</p>


