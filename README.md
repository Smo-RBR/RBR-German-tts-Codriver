# RBR-German-tts-Codriver
Deutscher Janne v2 kompatibler Beifahrer fürs Pacenote Plugin von Richard Burns Rally

Enstanden aus der Vorarbeit von Workerbee und den Notes Erweiterungen von Janne Laahanen.

Kompatibel mit den Notes auf Basis von Workerbees IDs und zusätzlich derer aus Jannemod v2.

# Work in Progress
- Frontend aufräumen, wer das oft zum editieren der Notes benutzt: lieber abwarten, das sieht noch aus wie Kraut und Rüben, oder man nimmt halt Roadbook

# Installation

Zuerst oben links unter dem grün unterlegtem "Code" die Dateien als .zip herunterladen

**Backup machen: Im deinem RBR-Ordner den Ordner "Audio" und im Ordner Plugins den Ordner "Pacenote" folgendermassen kopieren: Rechte Maustaste auf den Verzeichnisnamen, dann kopieren, dann einfügen. Jetzt sollten sich im RBR Ordner ein neuer Eintrag "Audio-Kopie" und im Plugins Ordner eim Eintrag "Pacenote-Kopie" befinden.**

Danach das heruntergeladene zip in Dein RBR Verzeichnis entpacken. Bei der Nachfrage ob Dateien überschrieben werden sollen mit "Ja" antworten.

Jetzt kannst du in RBR eine Stage starten, zwei mal links klicken und im erscheinenden Fenster im oberen Dropdown deine gewünschtes Ansageschema auswählen. Neben den originalen Schema stehen dir jetzt folgende Ansageschemata zur Verfügung:
```
Smo-Nummern_und_90:  	Smo-Nummern:            Smo-Mix:	Smo-Richtung:	
Kehre l/r		Kehre l/r		Kehre l/r	l/r Kehre
2 l/r			1 l/r			90 l/r		l/r 1 
90 l/r			2 l/r			Scharf l/r	l/r 2
3 l/r			3 l/r			3 l/r		l/r 3
4 l/r			4 l/r			4 l/r		l/r 4
5 l/r			5 l/r			5 l/r		l/r 5
6 l/r			6 l/r			Leicht l/r	l/r 6
Voll l/r		Voll l/r		Voll l/r	l/r Voll
```
Wenn du dein bevorzugtes Ansageschema gefunden hast, kannst du die Datei Richard_Burns_Rally Verzeichnis\Plugins\Pacenote\config\pacenotes\rbr.ini so ändern, dass diese auf dein bevorzugtes Schma verweist. Voreingestellt ist gerade Smo-Mix, und es sollte eigenlich selbsterklärend sein. Du musst nur die Zeile "file0" ändern. Sonst nichts. 

# De-Installation
Den Ordner RBR-Ordner\Audio und RBR-Ordner\Plugins\Pacenote löschen und dann die bei der Installation kopierten Ordner wieder in Audio und Pacenote umbenennen
