# Actualizar el README con tu información real
echo '# Aplicación de Cuenta Bancaria

Una aplicación de banco en línea de comandos con versiones procedural y POO, containerizada con Docker.

## Versiones
- **v1_procedural**: Implementación procedural tradicional
- **v2_oop**: Refactor con Programación Orientada a Objetos

## Ejecución Rápida
```bash
# Ejecutar versión POO localmente
python v2_oop/bank.py

# Construir y ejecutar con Docker
docker build -t bank-app .
docker run -it bank-app

# O usar la imagen pre-construida
docker run -it juanita1234/bank-app:latest
