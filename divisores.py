def es_numero_natural(n):

    return n.isdigit() and int(n) > 0

def calcular_divisores(numero):
    #
    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    return divisores

while True:
    try:

        entrada = input("Ingrese un número natural positivo: ")

        if not es_numero_natural(entrada):
            raise ValueError("Debe ingresar un número entero positivo.")

        numero = int(entrada)

        if numero <= 0:
            raise ValueError("Debe ingresar un número mayor a 0.")


        divisores = calcular_divisores(numero)
        print(f"Los divisores de {numero} son: {divisores}")
        break

    except ValueError as ve:

        print(f"Error: {ve}. Por favor, intente nuevamente.")
    except Exception as e:

        print(f"Ocurrió un error inesperado: {e}. Intente de nuevo.")
