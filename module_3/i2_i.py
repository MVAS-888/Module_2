class User:
    def __init__(self, email, password):
        self.__email = email  
        self.__password = password  

    
    def get_email(self):
        return self.__email

    
    def set_email(self, new_email):
        self.__email = new_email


    def __authenticate(self, password):
        return self.__password == password


    def change_password(self, old_password, new_password):
        if self.__authenticate(old_password):  
            self.__password = new_password
            print("Пароль успішно змінено!")
        else:
            print("Помилка: Старий пароль введено неправильно!")

user1 = User("user@example.com", "secure123")

print("Поточний емейл користувача:", user1.get_email())
user1.set_email("new_user@example.com")
print("Оновлений емейл користувача:", user1.get_email())

user1.change_password("wrongpassword", "newpassword123")
user1.change_password("secure123", "newpassword123")
