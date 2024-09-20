class Club:
    def __init__(self, title):
        self._title = title

    def getTitle(self):
        return self.title
    
class ClubAssociation:
    def __init__(self):## takes no parameters to be initiated
        self._recognized_clubs =[]

    def add_new_club (self, title):
        new_club_object = Club(title) # adds newly created clubs to the recognized clubs list in the ClubAssociation object
        self._recognized_clubs.append(new_club_object)

    def list_available_club(self):
        print(self._recognized_clubs)
    
my_club_association = ClubAssociation()
my_club_association.add_new_club("Chess") # add clubs to the newly initialized object (association)
my_club_association.add_new_club("The Baker Street Irregular")
my_club_association.add_new_club("Food for Thought")

my_club_association.list_available_club()
        