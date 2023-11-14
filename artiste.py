class Artiste:
    def __init__(self, artiste_id: int, nom: str):
        self._artiste_id = artiste_id
        self._nom = nom

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def artiste_id(self):
        return self._artiste_id

    @artiste_id.setter
    def artiste_id(self, value):
        self._artiste_id = value

