class User:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    
    def get_email(self):
        return self.__email

    
    def set_email(self, email):
        if "@" in email and "." in email:  
            self.__email = email
        else:
            print("Невірний формат емейлу")

    
    def __authenticate(self, input_password):
        return self.__password == input_password

    
    def change_password(self, old_password, new_password):
        if self.__authenticate(old_password):  
            self.__password = new_password
            print("Пароль успішно змінено")
        else:
            print("Помилка: старий пароль введено неправильно")

    
    def display_info(self):
        print(f"Email: {self.__email}")


user = User("user@example.com", "password123")

user.display_info()

user.set_email("newuser@example.com")
print("Оновлений емейл:", user.get_email())

user.change_password("wrongpassword", "newpassword123")

user.change_password("password123", "newpassword123")

user.display_info()