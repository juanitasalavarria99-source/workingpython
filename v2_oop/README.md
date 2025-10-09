# Versión POO - Aplicación de Cuenta Bancaria

## Diseño POO
- **Clase**: BankAccount
- **Métodos principales**: deposit(), withdraw(), check_balance(), show_transactions()
- **Manejo de errores**: Valida cantidades positivas y previene sobregiros

## Ejecución
# Ejecución local
python bank.py

# Ejecución en Docker
docker build -t bank-app ..
docker run -it bank-app
