class Dog:
    def __init__(self, breed:str, name:str, age:int):
        self.breed = breed
        self.name = name
        self.age = age
        self.update_weight()

        self.days = 0
        self.eg = self.newday()
        self.full = False
        breed2color = {
            "Poodle" : "black",
            "Maltese" : "white"
        }
        self.color = breed2color[breed]

    def amounts(self):
        amount = round(self.weight * 1000 * 0.01, 2)
        print(f"{self.name}은(는) 하루에 {amount}g의 사료를 먹습니다.")
        return amount

    def newday(self):
        self.days += 1
        self.eg = 0
        return self.eg

    def withdays(self):
        print(f"{self.name}와(과) 함께한 날은 {self.days}일 입니다.")

    def eat(self, g):
        amount = self.amounts()
        self.eg += g
        if self.eg < amount:
            print(f"{self.name}은(는) 오늘 {self.eg}g의 사료를 먹었습니다. 더 먹을 수 있어요!")
            self.full = False
        else:
            print(f"{self.name}은(는) 오늘 {self.eg}g의 사료를 먹었습니다. 이제 배불러요!")
            self.full = True
        return self.eg, self.full

    def isfull(self):
        if self.full:
            print(f"배불러요!")
        else:
            print(f"배부르지 않아요!")

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