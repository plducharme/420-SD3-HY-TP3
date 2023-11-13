# TP3 - Récolteur3000
## Contexte
En informatique, les données sont le "nerf de la guerre". Si le produit est gratuit, c'est que vous êtes le produit.
On retourne dans le temps lorsque la musique était numérisée en format mp3. Vous devez concevoir un lecteur de mp3 qui
ramassera de l'information sur les pistes et les artistes à partir d'une liste de lecture.

## Comprendre le mp3
Lorsque de la musique est enregistrée, un dispositif analogique est généralement utilisé (e.g. un micro) et le résultat
est numérisé dans un format brut appelé WAV. Ce format enregistre la hauteur de la fréquence captée par le dispositif.
Cependant, étant un format brut, il nécessite beaucoup d'espace (environ 10Mo par minute). C'est une des raisons qui a
amené la création du format MPEG-2 layer III ou mp3. Le mp3 est un format compressé qui donne un bon ratio de
compression avec peu de perte de qualité sonore. 

Le mp3 contient aussi un entête nommé ID3 permettant d'enregistrement des informations sur la piste, l'artiste,
le débit, une image, etc. C'est ce que nous allons interroger pour populer notre base de données.

## ID3v2 Tag
Les éléments contenus dans l'entête ID3 se nomme tags (étiquettes). On va utiliser une bibliothèque qui nous donnera
facilement accès à ses tags: [TinyTag](https://pypi.org/project/tinytag/)

Les tags suivants sont disponibles:

>tag.album        # album  
tag.albumartist   # artiste de l'album   
tag.artist        # nom d'artiste  
tag.audio_offset  # nombres d'octets avant que les données audio commencent  
tag.bitdepth      # nombre de bits par échantillon (sample)  
tag.bitrate       # débit en kBits/s  
tag.comment       # commentaire  
tag.composer      # compositeur  
tag.disc          # no de disque  
tag.disc_total    # nombre total de disques  
tag.duration      # durée de la chanson en secondes  
tag.filesize      # grosseur du fichier en octets  
tag.genre         # genre  
tag.samplerate    # échantillons par seconde  
tag.title         # titre de la chanson  
tag.track         # numéro de piste  
tag.track_total   # nombre total de pistes  
tag.year          # année  

>Exemple:  
> 
>tag = TinyTag.get(chemin_mp3)   
> print(tag.artist)

## Bibliothèque Audio
Plusieurs bibliothèques audio Python existent pour manipuler, convertir, jouer des fichiers médias (audio/vidéo). 

### VLC (python-bindings)
C'est une bibliothèque qui délègue les appels aux bibliothèques dynamiques (e.g. .dll, .so)
- Nécessite que [VLC](https://www.videolan.org/vlc/) soit installé
- Peu de documentation et exemples
- Très puissante

### PyDub
Bibliothèque idéale pour la manipulation de fichiers audios. Permet de convertir, séparer une chanson en plusieurs
segments, jouer, mixer, etc
- Nécessite libAv ou ffmpeg pour certaines opérations
- Écrit entièrement en Python

### Pyglet
Bibliothèque graphique (un peu comme PySide6) qui comprend des composantes média
C'est la bibliothèque utilisée par défaut dans le TP
- Relativement simple d'utilisation pour la lecture 

## Requis
Vous devez faire une application de lecture de mp3s avec PySide6
### Requis interface
1) L'application se constituera de plusieurs "zones" qui seront contenues dans des QDockWidget.
   1) Zone d'affichage de lecture
      - Permet l'affichage des informations sur le mp3 en cours de lecture
        - Titre
        - Artiste
        - Album
        - Genre
        - Débit en KBits/s
        - année
      - Ces informations doivent provenir de la BD
   2) Zone de contrôles (Joueur, Pause, Suivant, Précédent)
        - Permet l'affichage des contrôles du lecteur
          - Jouer/Pause
          - Suivant
          - Précédent
          - Volume
   3) Zone liste de lecture
        - Contient la liste des chansons
        - Doit contenir aussi une façon d'ajouter des chansons (ex: un widget qui ouvre un QFileDialog)
2) La fenêtre principale devra s'appeler "Récolteur3000"
3) Dans la zone d'affichage de lecture
   1) L'utilisateur doit pouvoir être capable de consulter les informations sur l'album (autres pistes de l'album, etc)
      - L'implémentation (bouton, nouvelle fenêtre, même fenêtre, etc) est laissée à votre discrétion
   2) L'utilisateur doit pouvoir modifier les informations de la piste
      - Les changements doivent être persistés dans la BD
4) La fenêtre principale devra avoir un menu avec les éléments suivants
   - "Fichier"
     - "Reset"
       - Permet de recréer une BD vide
     - "Quitter"
       - Doit fermer l'application
   - "À propos"
     - Ajouter vos noms et toutes notices légales


### Requis BD
1)


## Éléments graphiques


## MP3 

## Critères d'évaluation


## Extra
- Random
- Réarranger la liste de lecture

## Application dans le monde réelle
En industrie, la majorité des applications/jeux/etc vont tenter de ramasser un maximum d'information sur un utilisateur.
Dans un cas comme celui-ci, on utiliserait plus une base de données document déployé dans le cloud. Ces informations
pour cerner le comportement d'un utilisateur et ses intérêts pour améliorer un produit, mais parfois, elles sont
simplement revendues à des tierces parties.

On pourrait imaginer une version de l'application qui permet de créer un profil. À partir du profil et des choix de
lectures, on pourrait faire un algorithme de recommendation de musique (artistes connexes, styles connexes, etc).

