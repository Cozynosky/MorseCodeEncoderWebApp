Introduction
============
MorseCodeEncoder is a Web app, where you can encode and decode text messages with morse code. I started from a console app which is also in my repos, but I wanted to show it to my friends
so I've found free bootstrap template and made some modifications.

How it works
-------------
All app works on Heroku platform under [https://morse-code-encoder.herokuapp.com/](https://morse-code-encoder.herokuapp.com/). In Input you can write almost any text message
(limited with morse code alphabet) or already encoded message. In Output you will see your result depending od which button you pressed. After encoding there also apperas audio player
with your encoded message and download option.

Technologies
===========
* Python 3.9
* Flask 2.0.1
* Pydub
* (and all other dependencies in requirements.txt)
