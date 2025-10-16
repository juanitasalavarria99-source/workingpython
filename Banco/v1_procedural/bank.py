# bank.py — Versión 1 Procedural

balance = 1000
transactions = []

def deposit():
    global balance
    amount = float(input("Ingrese monto a depositar: "))
    if amount <= 0:
        print("❌ El monto debe ser positivo.")
    else:
        balance += amount
        transactions.append(f"Depósito: +{amount}")
        print(f"✅ Depósito exitoso. Nuevo saldo: {balance}")

def withdraw():
    global balance
    amount = float(input("Ingrese monto a retirar: "))
    if amount <= 0:
        print("❌ El monto debe ser positivo.")
    elif amount > balance:
        print("⚠️ Fondos insuficientes.")
    else:
        balance -= amount
        transactions.append(f"Retiro: -{amount}")
        print(f"✅ Retiro exitoso. Nuevo saldo: {balance}")

def show_balance():
    print(f"💰 Saldo actual: {balance}")

def show_transactions():
    print("📜 Historial de transacciones:")
    for t in transactions:
        print(" -", t)

def main():
    while True:
        print("\n--- MENÚ BANCO ---")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Ver saldo")
        print("4. Ver transacciones")
        print("5. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            show_balance()
        elif choice == "4":
            show_transactions()
        elif choice == "5":
            print("👋 Gracias por usar el sistema bancario.")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    main()
