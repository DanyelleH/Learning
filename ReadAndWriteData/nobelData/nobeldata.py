import json

class NobelData:
    def __init__(self):
        with open("/Users/danyelleridley/Documents/Learning/ReadAndWriteData/nobelData/nobels.json",'r') as nobelfile:
            self._noble_data = json.load(nobelfile)
        

    def search_nobel(self, year,category):
        surname_list=[]
        for prize_obj in  self._noble_data['prizes']:
            if prize_obj['year'] == year:
                if prize_obj['category'] == category:
                    for awardies in prize_obj["laureates"]:
                        surname_list.append(awardies['surname'])
        sorted_surnames = sorted(surname_list)
        return sorted_surnames
    
nobel_object = NobelData()
print(nobel_object.search_nobel('2001', 'economics'))