<img src="icon.png" align="right" />

# Dier en Zorg README [![Dier en Zorg](https://badgen.net/badge/dier-en-zorg-py-script/beta/cyan?icon=terminal)](https://github.com/tvdsluijs/translogger#readme)

Gek werd ik er van. Het formulier van de verzekering "Dier en Zorg". Ik was altijd het polis nummer en relatie nummer kwijt. Ook de juiste naam van mijn dierenarts en het telefoon nummer moest ik opzoeken.

Dan al die gegevens die ik moest invullen.... Terwijl het vaak op de nota staat.

Mijn hond heeft altijd de zelfde behandeling / medicatie.... en het invullen van het zeer klantonvriendelijke formulier was ik zat.

Dus daarom dit script.

## Belangrijke opmerking!!!

- Aan dit script kunnen geen rechten worden ontleent, niet qua werking en niet qua ondersteuning;
- Het script is gemaakt door mij en ik heb geen relatie (behalve dat ik een verzekerde ben) met de verzekerings maatschappij achter "Dier en Zorg";
- Het script is dus niet van het bedrijf achter "Dier en Zorg";
- Ik verkoop het script niet en ik verdien dus niet aan dit script;
- Het script mag je gratis gebruiken, als er iets fout gaat door het gebruik van het script (in de ruimste zin van het woord) is dat jouw probleem.
- Het script vult in wat jij normaal zou invullen, mits je de config.yml juist invult. Het automatiseert dus je type-werk. Niets meer niets minder. Het volgt de normale formulier route die je als bezoeker ook zou volgen.
- Mocht Dier en Zorg dit script toch niet leuk vinden, haal ik het offline. Ik hoop het niet, ik hoop dat ik koffie en gebak van ze krijg :-)

## Hoe starten

**Stap 1:**

Download dit script via `git clone git@github.com:tvdsluijs/dier-en-zorg-py-script.git`

**Stap 2:**

Maak een config.yml file aan in de config folder. Er staat een voorbeeld bestand.

Vul jouw gegevens in het config formulier

Je moet wel even 1x de juiste getallen uit de selectboxen halen van het formulier. Misschien pas ik dat ooit nog wel aan.

Stap 3

Zet je nota in de declaratie map (jpg of iets)

Stap 4

Klaar en runnen maar

`python dierenzorg_formulier.py`

Tijdens het draaien van het script worden vragen gesteld (zoals: wanneer was de bahandel datum), deze worden daarna automatisch in het formulier ingevuld.

Het Dier en Zorg formulier wordt niet automatisch verstuurd. Je dient zelf even alles te controleren en daarna op verzenden te klikken.

### Systeem vereisten

Het geheel gebruikt chrome drivers. Je hebt dus chrome nodig en de drivers. Die vind je [hier](https://chromedriver.chromium.org/)


### Commits & Update

![code coverage](https://badgen.net/github/status/tvdsluijs/dier-en-zorg-py-script/master/coverage/coveralls)

![Commits](https://badgen.net/github/commits/tvdsluijs/dier-en-zorg-py-script)

![Update](https://badgen.net/github/last-commit/tvdsluijs/dier-en-zorg-py-script) 


## Gebouwd met 

* Python 3.7.x
* [Pycharm](https://www.jetbrains.com/pycharm/)

> en

[<img src="https://img.youtube.com/vi/uel8ToMHGBM/maxresdefault.jpg" width="50%">](https://youtu.be/uel8ToMHGBM)

## Koffie tijd!

Denk je, nou die gast gun ik best een bak koffie voor zijn werk, sponsor me dan 1 of 2 bakken!

[![Coffee](https://badgen.net/badge/Buy%20me/a%20Coffee/orange)](https://www.buymeacoffee.com/itheo)


## License


![MIT](https://badgen.net/github/license//tvdsluijs/translogger)
