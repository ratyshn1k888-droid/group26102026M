class BankAccount:
    def __init__(self,customer_name: str):
        self.owner = customer_name.strip().title()
        self.money = 0
        self.id = 987321


