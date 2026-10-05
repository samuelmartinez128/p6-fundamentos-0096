#Samuel Martinez NC 0096
#Explicaciones y ejemplos

# ------------------------------------------------------------------------------
# 1. VARIABLES
# ------------------------------------------------------------------------------
print("=" * 50)
print(" 1. VARIABLES")
print("=" * 50)

# Ejemplo 1: Crear variables
x = 5
y = "John"
print("[Ejemplo 1]")
print("x:", x)
print("y:", y)

# Ejemplo 2: Cambiar el tipo de dato
x = 4
x = "Sally"
print("\n[Ejemplo 2]")
print("x reorganizado:", x)

# Ejemplo 3: Conversión de tipo (Casting)
x = str(3)
y = int(3)
z = float(3)
print("\n[Ejemplo 3]")
print("Casting:", x, y, z)
print()


# ------------------------------------------------------------------------------
# 2. ASIGNAR MÚLTIPLES VARIABLES
# ------------------------------------------------------------------------------
print("=" * 50)
print(" 2. ASIGNAR MÚLTIPLES VARIABLES")
print("=" * 50)

# Ejemplo 1: Varios valores a múltiples variables
x, y, z = "Naranja", "Plátano", "Cereza"
print("[Ejemplo 1]")
print(x, y, z)

# Ejemplo 2: Un mismo valor a múltiples variables
x = y = z = "Naranja"
print("\n[Ejemplo 2]")
print(x, y, z)

# Ejemplo 3: Desempaquetar una lista
frutas = ["manzana", "plátano", "cereza"]
x, y, z = frutas
print("\n[Ejemplo 3]")
print(x, y, z)
print()


# ------------------------------------------------------------------------------
# 3. TIPOS DE DATOS
# ------------------------------------------------------------------------------
print("=" * 50)
print(" 3. TIPOS DE DATOS")
print("=" * 50)

# Ejemplo 1: Obtener tipo de dato
x = 5
print("[Ejemplo 1]")
print("Tipo de x:", type(x))

# Ejemplo 2: Asignar diferentes tipos
x = "Hola Mundo"
y = 20
z = 20.5
a = ["manzana", "plátano"]
b = ("manzana", "plátano")
c = {"nombre": "John", "edad": 36}
print("\n[Ejemplo 2]")
print("x, y, z:", type(x), type(y), type(z))
print("a, b, c:", type(a), type(b), type(c))

# Ejemplo 3: Definir tipo explícito
x = str("Hola Mundo")
y = int(20)
z = float(20.5)
print("\n[Ejemplo 3]")
print("Constructores:", x, y, z)
print()


# ------------------------------------------------------------------------------