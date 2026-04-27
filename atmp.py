from datetime import datetime


class ATM:
    def __init__(self, initial_balance=1000, pin="1234"):
        self.balance = initial_balance
        self.transactions = []
        self.pin = pin

    def authenticate(self):
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your PIN: ")
            if entered_pin == self.pin:
                print("✅ Authentication Successful\n")
                return True
            else:
                attempts -= 1
                print(f"❌ Incorrect PIN! Attempts left: {attempts}")

        print("🚫 Too many failed attempts. Card blocked.")
        return False

    def display_balance(self):
        print(f"\n💰 Current Balance: ₹{self.balance}")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: ₹"))
            if amount <= 0:
                raise ValueError

            self.balance += amount
            self._add_transaction("Deposit", amount)
            print("✅ Deposit successful!")

        except ValueError:
            print("❌ Invalid amount entered!")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                raise ValueError
            if amount > self.balance:
                print("❌ Insufficient balance!")
                return

            self.balance -= amount
            self._add_transaction("Withdraw", amount)
            print("✅ Please collect your cash!")

        except ValueError:
            print("❌ Invalid amount entered!")

    def show_statement(self):
        print("\n📄 Transaction History:")
        if not self.transactions:
            print("No transactions yet.")
            return

        for t in self.transactions:
            print(t)

    def _add_transaction(self, t_type, amount):
        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        record = f"{time} | {t_type} | ₹{amount} | Balance: ₹{self.balance}"
        self.transactions.append(record)

    def menu(self):
        if not self.authenticate():
            return

        while True:
            print("\n====== 🏧 ATM MENU ======")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. View Statement")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                self.display_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                self.show_statement()
            elif choice == '5':
                print("👋 Thank you for using the ATM!")
                break
            else:
                print("❌ Invalid choice!")


# Run the ATM
atm = ATM()
atm.menu()