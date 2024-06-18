import math

number = int(input("Ingresa un número: "))

if number<0 :
    print("No se puede calcular")
else:
    def raizCuadrada(number):
        return math.sqrt(number)
    try:
        result = raizCuadrada(number)
        print(f"La raíz cuadrada de {number} es {result:.2f}")
    except ValueError:
        print("Error: Ingresa un número válido.")