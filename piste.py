from artiste import Artiste
from genre import Genre
from album import Album


class Piste:
    def __init__(self, piste_id: int, titre: str, artiste: Artiste, bit_depth: int, bit_rate: float, duration: float,
                 genre: Genre, album: Album, sample_rate: int, annee: int, file_size: int, no_piste: int):
        self._piste_id = piste_id
        self._titre = titre
        self._artiste = artiste
        self._bit_depth = bit_depth
        self._bit_rate = bit_rate
        self._duration = duration
        self._genre = genre
        self._album = album
        self._sample_rate = sample_rate
        self._annee = annee
        self._file_size = file_size
        self._no_piste = no_piste

    @property
    def titre(self):
        return self._titre

    @titre.setter
    def titre(self, value):
        self._titre = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        self._genre = value

    @property
    def annee(self):
        return self._annee

    @annee.setter
    def annee(self, value):
        self._annee = value

    @property
    def album(self):
        return self._album

    @album.setter
    def album(self, value):
        self._album = value

    @property
    def artiste(self):
        return self._artiste

    @artiste.setter
    def artiste(self, value):
        self._artiste = value

    @property
    def piste_id(self):
        return self._piste_id

    @piste_id.setter
    def piste_id(self, value):
        self._piste_id = value

    @property
    def bit_rate(self):
        return self._bit_rate

    @bit_rate.setter
    def bit_rate(self, value):
        self._bit_rate = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value

    @property
    def sample_rate(self):
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, value):
        self._sample_rate = value

    @property
    def bit_depth(self):
        return self._bit_depth

    @bit_depth.setter
    def bit_depth(self, value):
        self._bit_depth = value

    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, value):
        self._file_size = value

    @property
    def no_piste(self):
        return self._no_piste

    @no_piste.setter
    def no_piste(self, value):
        self._no_piste = value






