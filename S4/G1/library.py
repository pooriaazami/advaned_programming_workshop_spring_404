from enum import Enum

class User:
    def __init__(self, username, password):
        assert self.__check_new_password(password)

        self.__username = username
        self.__password = password

    def __check_new_password(self, new_password):
        return len(new_password) >= 8

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        assert self.__check_new_password(new_password)
        self.__password = new_password

    def __str__(self):
        return f'User(username={self.__username})'

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

class Librarian(User):
    def __init__(self, username, password):
        super().__init__(username, password)

class Customer(User):
    def __init__(self, username, password):
        super().__init__(username, password)

class Publication:
    def __init__(self, name, year, number):
        self.__name = name
        self.__year = year
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def year(self):
        return self.__year

    @property
    def number(self):
        return self.__number

    def __convert_to_str(self):
        return f'Publication(name={self.__name}, year={self.__year})'

    def __str__(self):
        return self.__convert_to_str()

    def __repr__(self):
        return self.__convert_to_str()

class Book:
    def __init__(self, name, author, publication):
        self.__name = name
        self.__author = author
        self.__publication = publication

    @property
    def name(self):
        return self.__name

    def author(self):
        return self.__author

    def publication(self):
        return self.__publication

    def __convert_to_str(self):
        return f'Book(name={self.__name}, author={self.__author}, pub={self.__publication})'

    def __str__(self):
        return self.__convert_to_str()

    def __repr__(self):
        return self.__convert_to_str()

class AdminMenuCommands(Enum):
    REGISTER_NEW_BOOKKIPPER = 1
    REPORT_ACTIVE_BOOKS = 2
    REPORT_BORROWED_BOOKS = 3
    REPORT_BOOKS = 4
    SEARCH_BOOK = 5
    REPORT_ACTIVE_USERS = 6
    EXIT = 7
    ERROR = 8

class AdminMenu:
    def __init__(self):
        ...

    def print_menu(self):
        print('1- register a new book keeper')
        print('2- report active books')
        print('3- report borrowed books')
        print('4- book report')
        print('5- search for a book')
        print('6- active users')
        print('7- exit')

        command = input('Enter your command: ')

        match command:
            case '1':
                return AdminMenuCommands.REGISTER_NEW_BOOKKIPPER
            case '2':
                return AdminMenuCommands.REPORT_ACTIVE_BOOKS
            case '3':
                return AdminMenuCommands.REPORT_BORROWED_BOOKS
            case '4':
                return AdminMenuCommands.REPORT_BOOKS
            case '5':
                return AdminMenuCommands.SEARCH_BOOK
            case '6':
                return AdminMenuCommands.REPORT_ACTIVE_USERS
            case '7':
                return AdminMenuCommands.EXIT
            case _:
                return AdminMenuCommands.ERROR
            
    def parse_user_input(self, user_input):
        match user_input:
            case AdminMenuCommands.REGISTER_NEW_BOOKKIPPER:
                ...
            case AdminMenuCommands.REPORT_ACTIVE_BOOKS:
                ...
            case AdminMenuCommands.REPORT_BORROWED_BOOKS:
                ...
            case AdminMenuCommands.REPORT_BOOKS:
                ...
            case AdminMenuCommands.SEARCH_BOOK:
                ...
            case AdminMenuCommands.REPORT_ACTIVE_USERS:
                ...
            case AdminMenuCommands.EXIT:
                ...
            case AdminMenuCommands.ERROR:
                ...

    def run(self):
        while True:
            command = self.print_menu()
            self.parse_user_input(command)

            if command == AdminMenuCommands.EXIT:
                break

class App:
    def __init__(self):
        self.__users = [
            Admin('admin', 'adminadmin'),
        ]

        self.__active_user = -1

    def __login(self, username, password):
        for i, user in enumerate(self.__users):
            if user.username == username and user.password == password:
                return i

        return -1
            
    def run(self):
        while True:
            username = input('Enter your username (Entet 0 to exit): ')

            if username == '0':
                break
            
            password = input('Enter your password: ')

            # idx = self.__login(username, password)
            # if idx == -1:
            if (idx := self.__login(username, password)) == -1:
                print('Invalid username or password. Please try again.')
            else:
                self.__active_user = idx
                
                if isinstance(self.__users[self.__active_user], Admin):
                    menu = AdminMenu()
                    menu.run()

            # some tasks

            self.__active_user = -1

def main():
    app = App()
    app.run()

if __name__ == '__main__':
    main()
