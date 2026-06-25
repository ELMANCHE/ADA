#Elias Manchego navarro 
#ejercicio de escalera
# tambien los resultados se imprimen en la taerminal para medir los resultados de manera dinamica  
def encontrar_caminos(n, dp, camino_actual):
    # si llego al escalon 0 eso quiere decir que llegue a un camino correcto
    if n == 0:
        # los caminos se guardan de manera inversa 
        print(" + ".join(map(str, camino_actual[::-1])))
        return

    # ahora voy a verificar si es posible dar de un escalon en esaclon 
    if n - 1 >= 0 and dp[n - 1] > 0:
        camino_actual.append(1)
        encontrar_caminos(n - 1, dp, camino_actual)
        camino_actual.pop()  # aca esta el famoso backtrack

    # aca si es posible hacerle de 2 en 2 escalones
    if n - 2 >= 0 and dp[n - 2] > 0:
        camino_actual.append(2)
        encontrar_caminos(n - 2, dp, camino_actual)
        camino_actual.pop()  # aca esta el famoso backtrack


def escaleras_completo(n):
    # aca llenare la tabla dp como lo pide el ejemplo de la guia
    dp = [0] * (n + 1)
    dp[0] = 1
    if n >= 1:
        dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    # aca muestro los caminos que se uede hacer para llegar a n escalones
    print(f"para llegar al escalón {n} existen las siguientes formas:")
    encontrar_caminos(n, dp, [])

    # por ultimo la cantidad de caminos diferentes para llegar a n escalones y la tabla dp
    print(f"\nentonces existen {dp[n]} formas distintas")
    print(f"Tabla DP:\n{dp}")


# impresion de ejemplos

print("ejemplo con  n= 4")
escaleras_completo(4)

print("\nejemplo con n= 5")
escaleras_completo(5)