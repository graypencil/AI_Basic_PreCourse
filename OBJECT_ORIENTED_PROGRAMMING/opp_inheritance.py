class Person(object): 
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def about_me(self):
        print("저의 이름은 ", self.name, "이구요, 제 나이는 ", str(self.age), "살 입니다.")
        
    def __str__(self):
        print("저의 이름은 ", self.name, "이구요, 제 나이는 ", str(self.age), "살 입니다.")

class Employee(Person):
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender) # 부모 클래스 객체를 그대로 받아옴
        self.salary = salary
        self.hire_date = hire_date
        
    def do_work(self):
        print("열심히 일을 합니다.")
            
    def about_me(self): # 부모 클래스 함수 재 정의
        super().about_me() # 부모클래스 함수 받음
        print("제 급여는 ", self.salary, "원 이구요, 제 입사일은 ", self.hire_date, "입니다.")

myPerson = Person("John", 34, "Male")
myPerson.about_me()

myEmployee = Employee("Daeho", 48, "Male", 300000, "2012/03/02")
myEmployee.about_me() 