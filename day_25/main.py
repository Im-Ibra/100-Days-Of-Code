from manager import ExpensesManager

e_manager = ExpensesManager()

keep_going = True

while keep_going:
    user = e_manager.user()
    category = e_manager.choose_category()
    about = e_manager.description()
    price = e_manager.price()

    with open(f"ExpensesFolder/{user}-expenses.txt", mode="a", encoding="utf-8") as expenses:
        expenses.write(f"{e_manager.date}: [{category}] {about}, {price}€\n")

    more = input("Is there more? 'y' or 'n': ").lower()
    if more == "n":
        keep_going = False
    else:
        print("\n" * 20)