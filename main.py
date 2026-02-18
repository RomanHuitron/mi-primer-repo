main_content = '''
#!/usr/bin/env python3
y=9
x=6
print(f"Suma{x}+{y}= {x+y}")
"""
Mi primer script en un repositorio Git.
"""

def saludar(nombre):
    """Retorna un saludo personalizado."""
    return f"Hola, {nombre}! Bienvenido al mundo de Git."


if __name__ == "__main__":
    nombre = input("Como te llamas? ")
    print(saludar(nombre))
'''
