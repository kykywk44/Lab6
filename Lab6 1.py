class UserAccount:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
        print(f'Объект создан. \nname: {self.name} \nemail: {self.email} \npassword: {self.password} \n')

    def set_password(self, new_password):
        self.password = new_password
        p = ''
        for a in range (len(self.password)):
            p = p + '*'
        print('Пароль был изменен: ',p)

    def check_password(self, password):
        print(self.password == password)

user1 = UserAccount('Kazimir','kazimirovich@gmail.com','zalupko')
user1.set_password('zalupenko!')

i = input('Введите пароль для проверки: ')
user1.check_password(i)
