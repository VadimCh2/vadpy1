

class Person:
    def __init__(self, name: str):
        self.name = name.strip().title()

    def __str__(self):
        return f"{self.name}"

class bankAccount:
    def __init__(self, owner: Person, bank: "Bank"):
        self.balance = 0
        self.owner = owner
        self.bank = bank

    def deposit(self, amount: int):
        self.balance += amount

    def widthraw(self, amount: int):
        self.balance -= amount


    def __str__(self):
        return f"Account was oppened in {self.bank.title} for {self.owner.name}"

class Bank:
    def __init__(self, title: str):
        self.title = f'LTD{title.strip().upper()}'

    def open_account(self, client: Person) -> bankAccount:
        bank_Account = bankAccount(owner=client, bank=self)

    def __str__(self):
        return f"{self.title}"