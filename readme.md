#TODO Alex:

Lösch die Szenarien Outputs vom Ende der txt Dateien.

script.py so anpassen, das aus dem Szenario Ordner innerhalb von files/Modell()/ jeweils 
eins der beiden Szenarios iteriert wird und für eine der 4 Phasen die preprompt ausgeführt.

Die erstellte Szenariobeschreibung, dann ans ende der txt Dateien ran und nochmal an die API. 

Also ungefähr so:

for Szenario in model_folder:
	for phase in phases:
		...