# SWISS100
Python Scripts zur Automatisierung von Aufgaben im Bezug auf die schweizerische Hundertjährigen Studie SWISS100  
## Anwendung der Scripts
Die Anwendung der Scripts ist einfach. Das Script beinhaltet 2 Funktionen move_actigraph und move_EAR. Wie der Name der Funktionen schon sagt, werden entweder Actigraph oder EAR Dateien bewegt. Um eine Funktion auszuführen, entfernt die # Kommentarzeichen (unter ## Usage example). Danach muss man nur noch den Pfad des Ursprungsordner (source_folder) und den Pfad des Zielordners (destination_folder) angeben.  
Die Funktionen sind so geschrieben, dass bei den Actigraph Dateien zuerst, falls noch nicht vorhanden, ein neuer Ordner (Fall-ID) erstellt wird im Zielordner und dann erst die Datei verschoben wird. Da EAR Dateien für jeden Fall bereits in Ordner strukturiert sind, werden die Ordner mitsamt den Dateien verschoben. Neue Ordner im Zielordner werden nur dann erstellt, falls im Zielordner keine mit der Fall-ID korrespondierenden Ordner gefunden wurden.  
Bitte beachtet: **Die Funktionen basieren darauf, dass die Dateien/Ordner in einer bestimmten Reihenfolge benannt wurden. Dateien, die nicht den richtigen Benennungsregeln entsprechen, werden nicht bewegt, sondern bleiben im Ursprungsordner.** Diese Funktionen sollen somit den Grossteil der Dateien verschieben und falsch benannte oder andere Dateien unbewegt lassen. Diese unbewegten Dateien müssen dann manuell verschoben werden. Dadurch können auch Benennungsfehler der Datei erkannt werden.
