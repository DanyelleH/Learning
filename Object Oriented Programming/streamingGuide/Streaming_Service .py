class StreamingService:
    def __init__(self, name):
        self._name = name
        self._catalog = {} # key: movie title  value: movieObject

    def getName(self):
        return self._name
    
    def getCatalog(self):
        return self._catalog
    
    def addMovie(self, movieObject):
        self._catalog[movieObject.getTitle()]=movieObject

    def deleteMovie(self,movieTitle ):
        if movieTitle in self._catalog:
            del self._catalog[movieTitle]
