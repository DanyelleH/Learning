class Movie:

    def __init__(self, title, genre, director, year):
        self._title = title
        self._genre = genre
        self._director = director
        self._year = int(year)

    def getTitle(self):
        return self._title
    def getGenre(self):
        return self._genre
    def getDirector(self):
        return self._director
    def getYear (self):
        return self._year
    