# py07_person.py

class Person:
    # 명사(속성)인 멤버변수
    name = '유고'
    age = 49
    weight = 76.2
    gender = 'male'

    # 초기화 메서드(파이썬 기본으로 포함)
    def __init__(self, name, age, weight, gender):
        self.name = name
        self.age = age
        self.weight = weight
        self.gender = gender

    def __str__(self): # 객체 출력을 문자열 포맷팅!
        retStr = f'{self.name}\n{self.age}\n{self.weight}\n{self.gender}'
        return retStr

    # 동사(기상)인 멤버함수(메서드)
    def getup(self):  # myself
        print(f'{self.name}이(가) 일어납니다.')

    def setWeight(self, weight):
        print(f'{self.name}의 몸무게가 변경됩니다.')
        print(f'현재 {self.weight}kg')
        self.weight = weight
        print(f'변경 후 {self.weight}kg')

    def getGender(self):
        return self.gender


man = Person('명건', 50, 76.5, 'man') # __init__() 특수함수를 실행.
man.getup()
man.setWeight(80.1)
print(f'{man.name}의 성별은 {man.getGender()}.')
print('----------------------------')
print('객체 정보')
print(man)
