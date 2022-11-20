class Dog:
    def __init__(self, breed:str, name:str, age:int):
        self.breed = breed
        self.name = name
        self.age = age
        self.update_weight()

        self.days = 0
        breed2color = {
            "Poodle" : "black",
            "Maltese" : "white"
        }
        self.color = breed2color[breed]

    def amounts(self):
        amount = round(self.weight * 1000 * 0.01, 2)
        print(f"{self.name}은(는) 하루에 {amount}g의 사료를 먹습니다.")
        return self.amount

    def day(self):
        self.days += 1
        g = 0
        print(f"{self.name}와(과) 함께한 날이 하루 더 늘었습니다.")
        return g

    def eat(self, g):
        g += g
        self.amounts()
        if g < self.amount:
            print(f"{self.name}은(는) 오늘 {g}g의 사료를 먹었습니다. 더 먹을 수 있어요!")
            full = False
        else:
            print(f"{self.name}은(는) 오늘 {g}g의 사료를 먹었습니다. 이제 배불러요!")
            full = True
        return g, full

    def get_color(self):
        return self.color

    def get_n_year_old(self, n:int):
        self.age += n
        self.update_weight()
        return self.age, self.weight

    def update_weight(self):
        if self.age < 4:
            self.weight = self.age * 1.2
        else:
            self.weight = 3