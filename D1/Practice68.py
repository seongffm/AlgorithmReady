#객체지향 3
class Student:
    name='홍길동'
class GraduateStudent(Student):
    name = '이순신'
    major = '컴퓨터'
print(f"이름: {Student.name}")
print(f"이름: {GraduateStudent.name}, 전공: {GraduateStudent.major}")

#올바른 구현
class Student:
    def __init__(self,name):
        self.name = name
class GraduateStudent(Student):
    def __init__(self, name,major):
        super().__init__(name)
        self.major = major
student = Student('홍길동')
graduate_student = GraduateStudent('이순신','컴퓨터')
print(f"이름: {student.name}")
print(f"이름: {graduate_student.name}, 전공: {graduate_student.major}")