from PySide6.QtWidgets import (QApplication, QMainWindow, QFrame, QWidget, QVBoxLayout, QDockWidget, QPushButton,
                               QFileDialog)
from PySide6.QtCore import Qt
import pyglet
from tinytag import TinyTag
import sqlite3
from piste import Piste
from album import Album
from artiste import Artiste
from genre import Genre
import os


class Recolteur3000(QMainWindow):
    def __init__(self):
        super().__init__()


class RecolteurDB:
    def __init__(self):
        self.connexion = sqlite3.connect("infos_musique.db")
        self.curseur = self.connexion.cursor()


    def reset(self):
        # Exécuter les DROP TABLE

        # Recréer la BD
        self.creer_bd()

    def creer_bd(self):
        self.curseur.execute("CREATE TABLE Genre(genreId INTEGER PRIMARY KEY autoincrement, nom NOT NULL UNIQUE)")
        self.curseur.execute("CREATE TABLE Artiste(artisteId INTEGER PRIMARY KEY autoincrement, nom NOT NULL UNIQUE)")
        self.curseur.execute("CREATE TABLE Album(albumId INTEGER PRIMARY KEY autoincrement, nom NOT NULL UNIQUE, "
                             "artisteId, FOREIGN KEY(artisteId) REFERENCES Artiste(artisteId))")
        self.curseur.execute("CREATE TABLE Piste(pisteId INTEGER PRIMARY KEY autoincrement, titre NOT NULL UNIQUE, "
                             "artisteId, bitdepth, bitrate, duration, genreId, albumId, sample_rate, annee, file_size,"
                             "no_piste, FOREIGN KEY(artisteId) REFERENCES Artiste(artisteId), "
                             "FOREIGN KEY(genreId) REFERENCES Genre(genreId), "
                             "FOREIGN KEY(albumId) REFERENCES Album(albumId))")


class RecolteurInfos:

    def __init__(self):
        self._recolteur_db = RecolteurDB()

    @property
    def recolteur_db(self):
        return self._recolteur_db

    @recolteur_db.setter
    def recolteur_db(self, value):
        self._recolteur_db = value

    def recolter(self, chemin_mp3: str):
        pass


app = QApplication()
recolteur = Recolteur3000()
recolteur.show()
app.exec()