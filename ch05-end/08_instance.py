class Student:
    def __init__(self):
        pass

# 클래스 사용해 객체 생성(선언)
student = Student()

print(isinstance(student, Student))

print('--------------------------------')

class Circle:              
    def __init__(self, radius): 
        self.radius = radius
    def get_circumference(self):
        return 2 * 3.14 * self.radius
    def get_area(self):
        return 3.14 * (self.radius ** 2)
    
# 원 둘레, 넗이 구하기
circle = Circle(10)
print('둘레: ', circle.get_circumference())
print('넓이: ', circle.get_area())


