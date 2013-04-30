konRuStra
=========

Ein Rundenbasiertes Strategiespiel in der Konsole.
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
Der Code soll aus drei einfachen Klassen bestehen:

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

<h5>play</h5>
<p>
Reduziert sich auf die für das Spiel wichtigen Funktionen <br>
play soll nur Funktionen, die aus test oder main <br>
stammen, sinnvoll aufrufen. Wenn möglich auch wieder schön in <br>
eine Klasse verpackt. 
</p>

