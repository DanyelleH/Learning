import statistics
class Student:

    def __init__(self, name, grade):
        self._name = name
        self._grade = grade 
    def getGrade(self):
        return self._grade
    
def basic_stats(student_object_list):
    # grades = []
    grades =[student.getGrade() for student in student_object_list]
    # for student in student_object_list:
    #     grades.append(student.getGrade())
    mean=statistics.mean(grades)
    median = statistics.median(grades)
    mode = statistics.mode(grades)
    basic_stats= (mean, median, mode)
    return basic_stats

s1 = Student("Kyoungmin", 73)
s2 = Student("Mercedes", 74)
s3 = Student("Avanika", 78)
s4 = Student("Marta", 74)
student_list = [s1, s2, s3, s4]
print(basic_stats(student_list))