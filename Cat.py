class Cat:
    def __init__(self, name,gender, age):
        self.name=name
        self.gender=gender
        self.age=age
    def get_name(self):
        return f"Имя- {self.name}"
    def get_gender(self):
        return f"Пол- {self.gender}"
    def get_age(self):
        return f"Возраст- {self.age}"
