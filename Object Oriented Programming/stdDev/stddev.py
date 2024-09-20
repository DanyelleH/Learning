class Person():

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def getAge(self):
        return self._age

def stdDev(arr):
    age_list = []
    variance_numbers =[]
    for people in arr:
            age_list.append(people.getAge())
    average_age = sum(age_list) / len(age_list)
    for age in age_list:
         variance_numbers.append((age - average_age) ** 2)
    variance = sum(variance_numbers) / len(variance_numbers)
    deviation = variance ** 0.5
    return deviation

p1 = Person("Kyoungmin", 73)
p2 = Person("Mercedes", 24)
p3 = Person("Beatrice", 48)
person_list = [p1, p2, p3]
p1.getAge()

print(stdDev(person_list))