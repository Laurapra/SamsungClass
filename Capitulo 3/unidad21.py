#q1
class Dog:
    def bark(self):
        print('woof woof')

my_dog = Dog()
my_dog.bark()

#q2
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name}: woof woof")

my_dog = Dog('Bingo')
my_dog.bark()

#programacion por parejas
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.math_quiz = []
        self.science_quiz = []
        self.eng_quiz = []

    def __str__(self):
        return f"Student name: {self.name}\nStudent ID: {self.student_id}\nMath quiz: {self.math_quiz}\nScience quiz: {self.science_quiz}\nEnglish quiz: {self.eng_quiz}"
    
    def set_eng_quiz(self, score):
        self.eng_quiz.append(score)

    def set_math_quiz(self, score):
        self.math_quiz.append(score)

    def set_science_quiz(self, score):
        self.science_quiz.append(score)

    def get_name(self):
        return self.name

    def get_student_id(self):
        return self.student_id

    def get_eng_quiz(self):
        return self.eng_quiz

    def get_math_quiz(self):
        return self.math_quiz

    def get_science_quiz(self):
        return self.science_quiz

    def get_total_score(self):
        return sum(self.math_quiz) + sum(self.science_quiz) + sum(self.eng_quiz)

    def get_avg_score(self):
        num_quizzes = len(self.math_quiz) + len(self.science_quiz) + len(self.eng_quiz)
        total_score = self.get_total_score()
        return total_score / num_quizzes
my_student = Student("Juan Perez", 20210001)
my_student.set_eng_quiz(85)
my_student.set_math_quiz(90)
my_student.set_science_quiz(92)
print(my_student)