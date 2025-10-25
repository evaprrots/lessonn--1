class Animal:
    def __init__(self, name, species):
        self.name = name        
        self.species = species  

    def make_sound(self):
        """Звук, який видає тварина (за замовчуванням — невідомий)"""
        return "Якась тварина видає звук."

    def get_info(self):
        """Повертає інформацію про тварину"""
        return f"{self.species} на ім'я {self.name}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Собака")  
        self.breed = breed                

    def get_info(self):
        return f"{self.species} породи {self.breed} на ім'я {self.name}"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Кіт")
        self.color = color           

    def get_info(self):
        return f"{self.species} кольору {self.color} на ім'я {self.name}"

dog = Dog("Рекс", "Німецька вівчарка")
cat = Cat("Мурчик", "білий")
print(dog.get_info())   
print(cat.get_info())    



