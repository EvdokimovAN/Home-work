class Uni:
    def __init__(self, name, age, uni):
        self.name = name
        self.age = age
        self.uni = uni

    def mesto_ob(self):
        if self.uni == "МФТИ":
            print(f"Привет физтех {self.name} ")
        else:
            print(f"Привет {self.name} из {self.uni}")

class Facultet(Uni):
    def __init__(self, name, age, uni, coures, facultet ):
        super().__init__(name, age,uni)
        self.coures = coures
        self.facultet = facultet

    def inf(self):
        print(f"имя: {self.name}, возраст: {self.age}, место обучения: {self.uni}, курс: {self.coures}, факультет: {self.facultet} ")
        if self.facultet == "ФЭФМ":
            print("Наш слон")

    def curs(self):
        if self.coures >= 2:
            print("Привет старшекурсник")
        else:
            print("Здарова пекус")

Alex = Uni("Alex", 18, "МГУ")
Sasha = Facultet("Sasha", 20, "МФТИ", 3, "ФЭФМ")
Egor = Facultet("Egor", 18, "ВШЭ", 1, "Матфак" )
Fedy = Facultet("Fedy", 21, "МГУ", 4, "Мех-мат" )
Nekita = Facultet("Nekita", 19, "Бауманка", 2, "ИУ-9")
Alex.mesto_ob()
Sasha.inf()
Egor.curs()
        