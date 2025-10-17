import datetime

class ExpensesManager:
    def __init__(self):
        self.date = datetime.datetime.now().strftime("%x")
        self.category = ["food", "bills", "shopping"]

    def user(self):
        username = input("Whats your name? ").lower()
        with open("users.txt", mode="a+") as users:
            users.seek(0)
            if username not in users.read():
                users.write(f"{username}\n")
        return username

    def choose_category(self):
        while True:
            choice = input("What type of expense? 'food', 'bills', 'shopping': ").lower()
            if choice in self.category:
                return choice
            print("Invalid category, try again.")

    def description(self):
        info = input("Describe it: ").lower()
        return info

    def price(self):
        while True:
            amount = input("How much was it? ")
            try:
                float(amount)
                return amount
            except ValueError:
                print("Please enter a valid number (e.g., 12.99)")
