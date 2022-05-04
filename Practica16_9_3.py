class Client:
    def __init__(self,first_name,second_name,city,balance):
        self.first_name=first_name
        self.second_name=second_name
        self.city=city
        self.balance=balance
    def get_guest(self):
       return f"{self.first_name} {self.second_name}. {self.city}."
    def __str__(self):
        return f"{self.first_name} {self.second_name}. {self.city}. Баланс: {self.balance}руб."
client_1=Client("Иван","Петров","Москва",50)
client_2=Client("Петр","Иванов","Казань",300)
print(client_1)
print("-----------------------")
guests=(client_1,client_2)
for guest in guests:
    print(guest.get_guest())