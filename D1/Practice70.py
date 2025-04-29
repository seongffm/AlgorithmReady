#객체지향 7
class Person:
    sex = 'Unknown'
    @classmethod
    def getGender(cls):
        print(cls.sex)
class Male(Person):
    sex = 'Male'
class Female(Person):
    sex = 'Female'
Male.getGender()
Female.getGender()

#getGender() 자체를 오버라이딩 하기 
class Person:
    def getGender(self):
        return 'Unknown'
class Male(Person):
    def getGender(self):
        return 'Male'
class Female(Person):
    def getGender(self):
        return 'Female'
print(Male().getGender())
print(Female().getGender())