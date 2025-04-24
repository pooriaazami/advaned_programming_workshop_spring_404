import sys
from enum import Enum

class Admin:
    def __init__(self, username, password):
        assert self.__chech_new_password(password)

        self.__username = username
        self.__password = password

    def __chech_new_password(self, password):
        return len(password) >= 8

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        assert self.__chech_new_password(new_password)
        self.__password = new_password
    
    def __str__(self):
        return f'Admin(username={self.__username})'

    def check_password(self, password):
        return self.__password == password

class Cashier:
    def __init__(self, username, password):
        assert self.__chech_new_password(password)

        self.__username = username
        self.__password = password

    def __chech_new_password(self, password):
        return len(password) >= 8

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        assert self.__chech_new_password(new_password)
        self.__password = new_password

    def __str__(self):
        return f'Cashier(username={self.__username})'

    def check_password(self, password):
        return self.__password == password

class Storekeeper:
    def __init__(self, username, password):
        assert self.__chech_new_password(password)

        self.__username = username
        self.__password = password

    def __chech_new_password(self, password):
        return len(password) >= 8

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        assert self.__chech_new_password(new_password)
        self.__password = new_password

    def __str__(self):
        return f'StoreKeeper(username={self.__username})'

    def check_password(self, password):
        return self.__password == password

class Product:
    def __init__(self, name, value, amount):
        self.__name = name
        self.__value = value
        self.__amount = amount

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value

    @property
    def amount(self):
        return self.__amount

    def __str__(self):
        return f'Product(name={self.__name}, value={self.__value}, amount={self.__amount})'

    def __repr__(self):
        return f'Product(name={self.__name}, value={self.__value}, amount={self.__amount})'

    def increase(self, amount):
        self.__amount += amount

    def decrease(self, amount):
        if amount <= self.__amount:
            self.__amount -= amount
            return True
        else:
            print('decrease ignored')
            return False

class ProductHolder:
    def __init__(self):
        self.__products = []

    def push(self, product):
        for p in self.__products:
            if p.name == product.name:
                p.increase(product.amount)
                return

        self.__products.append(product)

    def print_items(self):
        for i, product in enumerate(self.__products):
            print(f'{i + 1}- {product}')

    def remove_zeros(self):
        self.__products = list(filter(lambda x: x.amount != 0, self.__products))

    def __len__(self):
        return len(self.__product)

    def __getitem__(self, idx):
        return self.__products[idx]

    def show(self):
        print(self.__products)

class Invoice:
    def __init__(self):
        self.__products = []

    def push(self, product):
        for p in self.__products:
            if p.name == product.name:
                p.increase(1)
                return 
        
        self.__products.append(Product(product.name, product.value, 1))

    @property
    def total_value(self):
        total_amount = 0
        for product in self.__products:
            total_amount += produc.value * product.amount
    
    def show(self):
        print('=' * 100)
        total_amount = 0
        for i, product in enumerate(self.__products):
            print(f'{i + 1}- {product.name} {product.amount} {product.value}$')
            total_amount += product.value * product.amount

        print(f'Total Amount: {total_amount}$')
        print('=' * 100)

class LoginMenu:
    def __init__(self):
        pass

    def run(self):
        username = input('Enter your username (Enter 0 to exit): ')
        if username == '0':
            sys.exit(0)
        password = input('Enter your password: ')

        return username, password

class AdminMenuComands(Enum):
    REGISTER_NEW_CACHIER = 1
    REGISTER_NEW_STOREKEEPER = 2
    REPORTS = 3
    EXIT = 4
    ERROR = 5

class AdminMenu:
    def __init__(self, admin, app):
        self.__admin = admin
        self.__app = app

    def __print_menu(self):
        print('1- Register a new Cashier')
        print('2- Register a new StoreKeeper')
        print('3- Reports')
        print('4- Exit')
        
        command = input('Enter your command: ')

        match command:
            case '1':
                return AdminMenuComands.REGISTER_NEW_CACHIER
            case '2':
                return AdminMenuComands.REGISTER_NEW_STOREKEEPER
            case '3':
                return AdminMenuComands.REPORTS
            case '4':
                return AdminMenuComands.EXIT
            case _:
                return AdminMenuComands.ERROR

    def __read_new_cachier_data(self):
        username = input('Enter the username: ')
        while not self.__app.check_username(username):
            command = input('Invalid username, plese try again (enter 0 to exit): ')
            if command == '0':
                return None

        password = input('Enter the password: ')
        while True:
            try:
                cashier = Cashier(username, password)
                break
            except:
                command = input('Invalid password, plese try again (enter 0 to exit): ')
                if command == '0':
                    return None

        return cashier

    def __read_new_storekeeper_data(self):
        username = input('Enter the username: ')
        while not self.__app.check_username(username):
            command = input('Invalid username, plese try again (enter 0 to exit): ')
            if command == '0':
                return None

        password = input('Enter the password: ')
        while True:
            try:
                storekeeper = Storekeeper(username, password)
                break
            except:
                command = input('Invalid password, plese try again (enter 0 to exit): ')
                if command == '0':
                    return None

        return storekeeper

    def __reports(self):
        ...

    def __error(self):
        print('Invalid input, please try again.')

    def __process_command(self, command):
        match command:
            case AdminMenuComands.REGISTER_NEW_CACHIER:
                if cashier := self.__read_new_cachier_data():
                    self.__app.register_new_user(cashier)

            case AdminMenuComands.REGISTER_NEW_STOREKEEPER:
                if storekeeper := self.__read_new_storekeeper_data():
                    self.__app.register_new_user(storekeeper)
            case AdminMenuComands.REPORTS:
                reports = Reports()
                reports.run()
            case AdminMenuComands.EXIT:
                return
            case AdminMenuComands.ERROR:
                self.__error()

    def run(self):
        while True:
            command = self.__print_menu()
            if command == AdminMenuComands.EXIT:
                return

            self.__process_command(command)

class StorekeeperMenuCommands(Enum):
    LOAD_NEW_PRODUCT_TO_WAREHOUSE = 1
    LOAD_NEW_PRODUCT_TO_STORE = 2
    SHOW_WAREHOUSE_PRODUCST = 3
    SHOW_STORE_PRODUCST = 4
    REPORTS = 5
    CHANGE_PASSWORD = 6
    EXIT = 7
    ERROR = 8

class StorekeeperMenu:
    def __init__(self, storekeeper, warehouse, shop):
        self.__storekeeper = storekeeper
        self.__warehouse = warehouse
        self.__shop = shop

    def __print_menu(self):
        print('1- Load a new product to Warehouse')
        print('2- Load a product from warehouse to the shop')
        print('3- Show warehouse products')
        print('4- Show shop producst')
        print('5- Reports')
        print('6- Change Password')
        print('7- Exit')

        command = input('Enter your command: ')

        match command:
            case '1':
                return StorekeeperMenuCommands.LOAD_NEW_PRODUCT_TO_WAREHOUSE
            case '2':
                return StorekeeperMenuCommands.LOAD_NEW_PRODUCT_TO_STORE
            case '3':
                return StorekeeperMenuCommands.SHOW_WAREHOUSE_PRODUCST
            case '4':
                return StorekeeperMenuCommands.SHOW_STORE_PRODUCST
            case '5':
                return StorekeeperMenuCommands.REPORTS
            case '6':
                return StorekeeperMenuCommands.CHANGE_PASSWORD
            case '7':
                return StorekeeperMenuCommands.EXIT
            case _:
                return StorekeeperMenuCommands.ERROR

    def __load_new_product_to_warehouse(self):
        name = input('Enter the name of the new product: ')

        price = input('Enter the price of the product: ')
        while True:
            try:
                price = int(price)
                break
            except:
                price = input('Invalid value for price, please try again: ')

        amount = input('Ente number of the product: ')
        while True:
            try:
                amount = int(amount)
                break
            except:
                price = input('Invalid value for price, please try again: ')

        self.__warehouse.push(Product(name, price, amount))

    def __load_new_product_to_store(self):
        print('Choose the product you want to add to the store')
        self.__warehouse.print_items()

        item = input('Enter the id of the product you want to add to the shop: ')
        while True:
            try:
                item = int(item)
                break
            except:
                item = input('Invalid value for id(type error). (Enter 0 to return) Please try again: ')
                if item == '0':
                    return

            while 0 <= item <= len(self.__warehouse):
                item = input('Invalid valud for id(value error). (Enter 0 to return) Plese try again: ')
                if item == '0':
                    return
        
        item = self.__warehouse[item - 1]
        amount = input('Enter the amount you want to add to the shop: ')
        while True:
            try:
                amount = int(amount)
                break
            except:
                amount = input('Invalid value for amount(type error). (Enter 0 to return) Please try again: ')
                if amount == '0':
                    return

            while amount > item.amount or amount <= 0:
                amount = input('Invalid valud for amount(value error). (Enter 0 to return) Plese try again: ')
                if amount == '0':
                    return

        item.decrease(amount)
        self.__warehouse.remove_zeros()
        self.__shop.push(Product(name=item.name, value=item.value, amount=amount))

    def __reports(self):
        ...

    def __change_password(self):
        password = input('Enter your new password: ')
        while True:
            try:
                self.__storekeeper.password = password
                return
            except:
                password = input('Invalid password, please try again (enter 0 to exit): ')
                if password == '0':
                    return

    def __process_command(self, command):
        match command:
            case StorekeeperMenuCommands.LOAD_NEW_PRODUCT_TO_WAREHOUSE:
                self.__load_new_product_to_warehouse()
            case StorekeeperMenuCommands.LOAD_NEW_PRODUCT_TO_STORE:
                self.__load_new_product_to_store()
            case StorekeeperMenuCommands.REPORTS:
                self.__reports()
            case StorekeeperMenuCommands.CHANGE_PASSWORD:
                self.__change_password()
            case StorekeeperMenuCommands.SHOW_WAREHOUSE_PRODUCST:
                print('=' * 100)
                self.__warehouse.print_items()
                print('=' * 100)
            case StorekeeperMenuCommands.SHOW_STORE_PRODUCST:
                print('=' * 100)
                self.__shop.print_items()
                print('=' * 100)
            case StorekeeperMenuCommands.EXIT:
                return
            case StorekeeperMenuCommands.ERROR:
                self.__error()

    def __error(self):
        print('Invalid input, please try again.')

    def run(self):
        while True:
            command = self.__print_menu()
            if command == StorekeeperMenuCommands.EXIT:
                return

            self.__process_command(command)

class CashieMenuCommands(Enum):
    NEW_INVOICE = 1
    CHANGE_PASSWORD = 2
    EXIT = 3
    ERROR = 4

class CashierMenu:
    def __init__(self, cashier, shop, app):
        self.__cashier = cashier
        self.__shop = shop
        self.__app = app

    def __print_menu(self):
        print('1- New invoice')
        print('2- Change password')
        print('3- Exit')

        command = input('Enter your command: ')

        match command:
            case '1':
                return CashieMenuCommands.NEW_INVOICE
            case '2':
                return CashieMenuCommands.CHANGE_PASSWORD
            case '3':
                return CashieMenuCommands.EXIT
            case _:
                return CashieMenuCommands.ERROR

    def __error(self):
        print('Invalid input, please try again.')

    def __new_invoice(self):
        self.__shop.print_items()
        products = input('Provide a list of products that the customer wants to buy: ')
        products = map(int, products.strip().split())
        products = map(lambda x: x - 1, products)

        invoice = Invoice()
        for p in products:
            product = self.__shop[p]
            print(product)
            if product.decrease(1):
                invoice.push(Product(product.name, product.value, product.amount))
        
        invoice.show()
        return invoice

    def __change_password(self):
        password = input('Enter your new password: ')
        while True:
            try:
                self.__cashier.password = password
                return
            except:
                password = input('Invalid password, please try again (enter 0 to exit): ')
                if password == '0':
                    return

    def __process_command(self, command):
        match command:
            case CashieMenuCommands.NEW_INVOICE:
                invoice = self.__new_invoice()
                self.__app.new_invoice(invoice)
            case CashieMenuCommands.CHANGE_PASSWORD:
                self.__change_password()
            case CashieMenuCommands.EXIT:
                return
            case CashieMenuCommands.ERROR:
                self.__error()

    def run(self):
        while True:
            command = self.__print_menu()
            if command == CashieMenuCommands.EXIT:
                return

            self.__process_command(command)

class Reports:
    def __init__(self):
        ...

    def run(self):
        print('Showing some important report...')

class App:
    def __init__(self):
        self.__users = [
            Admin(username='admin', password='adminadmin'),
            # Storekeeper(username='s1', password='password'),
            # Cashier(username='c1', password='password'),
        ]

        self.__invoices = []
        self.__warehouse = ProductHolder()
        self.__shop = ProductHolder()
        self.__active_user = -1

        # self.__warehouse.push(Product(name='Chips', value=10, amount=50))
        # self.__warehouse.push(Product(name='Soda', value=2, amount=80))
        # self.__warehouse.push(Product(name='Apple', value=5, amount=20))

        # self.__shop.push(Product(name='Chips', value=10, amount=50))
        # self.__shop.push(Product(name='Soda', value=2, amount=20))
        # self.__shop.push(Product(name='Apple', value=5, amount=80))

    def __login(self, username, password):
        for i, user in enumerate(self.__users):
            if user.username == username:
                if user.check_password(password):
                    return i

        return -1

    def check_username(self, username):
        for user in self.__users:
            if username == user.username:
                return False

        return True

    def register_new_user(self, user):
        self.__users.append(user)

    def new_invoice(self, invoice):
        self.__invoices.append(invoice)

    def start(self):
        while True:
            login_menu = LoginMenu()
            while self.__active_user == -1:
                username, password = login_menu.run()
                self.__active_user = self.__login(username, password)
            
            user = self.__users[self.__active_user]
            if isinstance(user, Admin):
                admin_menu = AdminMenu(user, self)
                admin_menu.run()
            elif isinstance(user, Cashier):
                cashier_menu = CashierMenu(user, self.__shop, self)
                cashier_menu.run()
            elif isinstance(user, Storekeeper):
                storekeeper_menu = StorekeeperMenu(user, self.__warehouse, self.__shop)
                storekeeper_menu.run()
            
            self.__active_user = -1

def main():
    app = App()
    app.start()

if __name__ == '__main__':
    main()
