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


class StreamingGuide:

    def __init__(self) :
        self._streaming_services_list = []

    def add_streaming_service(self, service_object):
        self._streaming_services_list.append(service_object)

    def delete_streaming_service(self, serviceName):
        for service in self._streaming_services_list:
            if service.getName() == serviceName:
                self._streaming_services_list.remove(service)
            
    
    def where_to_watch_movie (self, movie_title):
        result = []
        for services in self._streaming_services_list:
            catalog = services.getCatalog()
            if movie_title in catalog:
                movie = catalog[movie_title]
                if len(result) == 0:
                    result.append(f"{movie.getTitle()}, {movie.getYear()}")
                    result.append(services.getName())
                else:
                    result.append(services.getName())
        return result if result else None




movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

stream_serv_1 = StreamingService('Netflick')
# print(movie_1.getTitle())
stream_serv_1.addMovie(movie_2)
# print(stream_serv_1.getName())

stream_serv_2 = StreamingService('Hula')
stream_serv_2.addMovie(movie_1)
stream_serv_2.addMovie(movie_4)
stream_serv_2.deleteMovie('The Seventh Seal')
stream_serv_2.addMovie(movie_2)

stream_serv_3 = StreamingService('Dizzy+')
stream_serv_3.addMovie(movie_4)
stream_serv_3.addMovie(movie_3)
stream_serv_3.addMovie(movie_1)

stream_guide = StreamingGuide()
stream_guide.add_streaming_service(stream_serv_1)
stream_guide.add_streaming_service(stream_serv_2)
stream_guide.add_streaming_service(stream_serv_3)
stream_guide.delete_streaming_service('Hula')
search_results = stream_guide.where_to_watch_movie('Little Women')
print(search_results)