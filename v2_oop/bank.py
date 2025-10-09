# bank.py — Versión 2 OOP

class Account:
    def __init__(self, initial_balance=1000):
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("❌ El monto debe ser positivo.")
            return
        self.balance += amount
        self.transactions.append(f"Depósito: +{amount}")
        print(f"✅ Depósito exitoso. Nuevo saldo: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ El monto debe ser positivo.")
        elif amount > self.balance:
            print("⚠️ Fondos insuficientes.")
        else:
            self.balance -= amount
            self.transactions.append(f"Retiro: -{amount}")
            print(f"✅ Retiro exitoso. Nuevo saldo: {self.balance}")

    def show_balance(self):
        print(f"💰 Saldo actual: {self.balance}")

    def show_transactions(self):
        print("📜 Historial de transacciones:")
        for t in self.transactions:
            print(" -", t)


def main():
    account = Account()

    while True:
        print("\n--- MENÚ BANCO (OOP) ---")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Ver saldo")
        print("4. Ver transacciones")
        print("5. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            try:
                amount = float(input("Monto a depositar: "))
                account.deposit(amount)
            except ValueError:
                print("⚠️ Ingrese un número válido.")
        elif choice == "2":
            try:
                amount = float(input("Monto a retirar: "))
                account.withdraw(amount)
            except ValueError:
                print("⚠️ Ingrese un número válido.")
        elif choice == "3":
            account.show_balance()
        elif choice == "4":
            account.show_transactions()
        elif choice == "5":
            print("👋 Gracias por usar el sistema bancario.")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    main()
