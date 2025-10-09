# Aplicación de Cuenta Bancaria

Una aplicación de banco en línea de comandos con versiones procedural y POO, containerizada con Docker.

## Versiones
- **v1_procedural**: Implementación procedural tradicional
- **v2_oop**: Refactor con Programación Orientada a Objetos

## Ejecución Rápida
# Ejecutar versión POO localmente
python v2_oop/bank_app.py

# Construir y ejecutar con Docker
docker build -t bank-app .
docker run -it bank-app

## Características
- Depositar/Retirar fondos
- Consultar saldo
- Historial de transacciones
- Validación de entrada
- No permite sobregiros
