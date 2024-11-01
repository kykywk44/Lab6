class UserAccount:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
        print(f'Объект создан. \nname: {self.name} \nemail: {self.email} \npassword: {self.password} \n')

    def set_password(self, new_password):
        self.password = new_password
        print('Пароль был изменен')

    def check_password(self, password):
        print(self.password == password)

user1 = UserAccount('Denis','dbykov1307@gmail.com','denis2010')
user1.set_password('denis2025')

i = input('Введите пароль для проверки: ')
user1.check_password(i)
