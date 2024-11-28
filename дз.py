from functools import total_ordering
def raising(cls):
    def up(self):
        print(f"{self.name}-{self.post}, повышен до начальника")
    cls.up = up
    return cls
def NDS(func):
    def wrapper(self):
        print("Без вычета НДС:",end=' ')
        result = func(self)
        print(f"После вычета НДС: Maky получает {self.salary*0.87}")
        return result
    return wrapper

@total_ordering
@raising
class company:
    def __init__(self, name, age, post, salary):
        self.name = name
        self.age = age
        self.post = post
        self.salary = salary
    def inf(self):
        print(f"имя: {self.name}, возраст: {self.age}, должность: {self.post}, зарплата: {self.salary}")
    @NDS
    def sal(self):
        K=self.salary
        print(f"{self.name} получает {K}")
    def __eq__(self, other):
        return self.salary == other.salary
    def __lt__(self,other):
        return self.salary < other.salary
worker1 = company("Tom", 22,"сварщик",100)
worker2 = company("Bob", 25,"слесарь",80)
worker3 = company("Ron", 29,"главный инженер",110)  
worker4 = company("Maky",44,"разнорабочий",90)
print(worker1 < worker2)  
worker3.up()
worker4.sal()









    
    
