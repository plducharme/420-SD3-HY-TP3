class Genre:
    def __init__(self, genre_id: int, nom: str):
        self._genre_id = genre_id
        self._nom = nom

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def genre_id(self):
        return self._genre_id

    @genre_id.setter
    def genre_id(self, value):
        self._genre_id = value

