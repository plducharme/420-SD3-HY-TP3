from artiste import Artiste


class Album:
    def __init__(self, album_id: int, nom: str, artiste: Artiste):
        self._album_id = album_id
        self._nom = nom
        self._artiste = artiste
    @property
    def album_id(self):
        return self._album_id

    @album_id.setter
    def album_id(self, album_id):
        self._album_id = album_id

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @property
    def artiste(self):
        return self._artiste

    @artiste.setter
    def artiste(self, artiste):
        self._artiste = artiste

