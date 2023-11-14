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

#### Utilisation de Pyglet
[Documentation (en anglais)](https://pyglet.readthedocs.io/en/latest/programming_guide/media.html)
Pyglet a parfois quelques difficultés avec les chemins absolus de fichiers. La façon la plus simple d'utiliser Pyglet
est de bâtir l'équivalent d'un "PATH" (séries de répertoires où chercher le fichier) et d'appeler le fichier avec juste
le nom:
>repertoire_courant = os.path.dirname(os.path.realpath(__file__))  
>chemins = os.path.join(chemins, nouveau_chemin)   
>chemins_musique = os.path.join(repertoire_courant, chemins)    
pyglet.resource.path = [chemins_musique]  
pyglet.resource.reindex()  
>musique = pyglet.resource.media("mon_fichier.mp3")   
>musique.play()

Il est possible de mettre les medias (ex: musique) dans une file pour faire une liste de lecture. Au lieu la chanson
directement, on créer un lecteur et on ajoute les médias
>player = pyglet.media.Player()  
>player.queue(media)  
>player.play()  
>player.pause()  
>player.next_source() # joue la prochaine chanson  
>player.seek() # joue la chanson à un temps spécifique

>player.time # position courante dans la chanson (le temps)  
>player.playing # True si en train de jouer  
>player.volume # Volume entre 0 et 1 (float)  
>player.source # Le media courant en train de jouer  
>player.loop # Si True, joue la chanson en boucle 

## Requis
Vous devez faire une application de lecture de mp3s avec PySide6
### Requis interface graphique
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
          - Boucle
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
   3) L'utilisateur doit pouvoir supprimer la piste de la BD
      - Une fenêtre de confirmation doit apparaître
4) La fenêtre principale devra avoir un menu avec les éléments suivants
   - "Fichier"
     - "Reset"
       - Permet de recréer une BD vide
     - "Quitter"
       - Doit fermer l'application
   - "Aide"
     - "À propos"
       - Ajouter vos noms et toutes notices légales
5) L'application doit pouvoir jouer, mettre en pause, jouer la prochaine


### Requis BD
1) Lors de l'importation des chansons, toutes valeurs non-existantes dans la Bd devra être insérées (Piste,
Artiste, Genre, Album)
2) L'application devra donner la possibilité de mettre-à-jour les informations de la piste
3) L'application doit pouvoir retourner l'information sur les autres pistes de l'album
4) L'application doit pouvoir supprimer une piste de la BD
5) L'application doit pouvoir faire une RESET de la BD

## Éléments graphiques
Vous pouvez créer vos propres icônes ou utiliser des icônes existantes. Certains sites comme
[flaticon](https://www.flaticon.com/) permettent d'utiliser des icônes en ajoutant la notice légale dans l'application.

## MP3 
Vous pouvez utiliser vos propres mp3 pour tester. Certains mp3 seront inclus comme exemples. Ce sont des mp3 libres de
droits obtenus sur [Pixbay](https://pixabay.com/fr/music/).

Les mp3s d'exemples contiennent des tags modifiés manuellement pour simuler des données réelles.
Pour modifier les tags rapidement, vous pouvez utiliser [MP3TAG](https://www.mp3tag.de/en/) ou Tinytag


## Classes fournies
Les classes Album, Genre, Piste et Artiste sont définies dans leurs propres fichiers. Pour ces fichiers, vous devez
respecter l'encapsulation.

RecolteurBD permet l'interaction avec la BD. Cette classe contient la méthode qui fait la création de la BD.
Les requêtes de cette méthode ne doivent pas être modifiées. En d'autres mots, à moins d'instructions contraires,
ne pas modifier la structure de ces tables de la BDs. Cependant, vous pouvez ajouter des tables au besoin.

RecolteurInfos permet de récolter les informations à partir du mp3 et d'appeler RecolteurBD pour intéragir avec la BD.

## Critères d'évaluation
Ce TP compte pour 30% de la note finale et fait partie de l'évaluation sommative avec l'examen final. Faire attention
au double seuil.

La répartition des points est comme suit:
- 10% pour les requis interface graphique
- 8% pour les requis BD
- 4% pour la gestion des exceptions
- 5% pour l'usabilité et l'esthétisme de l'interface graphique
- 3% pour le respect des normes Python et la documentation 

Pour ce TP, les détails de l'interface sont laissés à votre discrétion. Vous avez la chance de faire l'interface comme
bon ils vous semblent. Cependant, ne pas oublier les principes de bases:
- Doit être clair et intuitif
- Doit être agréable à regarder

## Extras / Bonis
- Ajouter le mode aléatoire pour la liste de lecture 1%
- Possibilité de réarranger la liste de lecture 2%
- D'autres points bonis pourraient s'ajouter

## Application dans le monde réelle
En industrie, la majorité des applications/jeux/etc vont tenter de ramasser un maximum d'information sur un utilisateur.
Dans un cas comme celui-ci, on utiliserait plus une base de données document déployé dans le cloud. Ces informations
pour cerner le comportement d'un utilisateur et ses intérêts pour améliorer un produit, mais parfois, elles sont
simplement revendues à des tierces parties.

On pourrait imaginer une version de l'application qui permet de créer un profil. À partir du profil et des choix de
lectures, on pourrait faire un algorithme de recommendation de musique (artistes connexes, styles connexes, etc).

Aussi, en SQL, on écrit rarement les requêtes directement. Habituellement, on utilise un ORM (Object Relation Mapping).
Un ORM est une bibliothèque qui créée un mapping entre les objets et la BD. L'ORM créer automatiquement les requêtes
nécessaires pour l'insertion, la mise-à-jour, supression, recherche, etc.
