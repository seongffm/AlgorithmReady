#객체지향 2
# def printNationality(Korean):
#     if Korean=="Korean":
#         return '대한민국'
# print(printNationality("Korean"))

#그냥 함수 정의 -> 클래스 안에 메서드 정의
#인자로 Korean문자열 받음 -> 인자없이 클래스 안에 고정 동작
#함수호출 -> 클래스 이름으로 메서드 호출

#클래스 정보를 다루고 싶을때 사용 -> 클래스 속성 수정가능 
# class Korean:
#     nationality = '대한민국'
#     @classmethod
#     def getNationality(cls):
#         print(cls.nationality)
# print(Korean.nationality)
# Korean.getNationality()

# class Human:
#     nationality = '지구인'
#     @classmethod
#     def getNationality(cls):
#         print(cls.nationality)
# class Korean(Human):
#     nationality = '대한민국'
# class Unite(Human):
#     nationality = '미국'
# Korean.getNationality()
# Unite.getNationality()
# Human.getNationality()

#정적메서드로 구현해라 
class Korean:
    nationality = '대한민국'
    @staticmethod
    def prinNationality():
        print(Korean.nationality)
print(Korean.nationality)
Korean.prinNationality()