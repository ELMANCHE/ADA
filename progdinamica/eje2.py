# Elias Manchego navarro 
# ejercicio de cambio minimo de monedas
# tambien los resultados se imprimen en la terminal para medir los resultados de manera dinamica  

def cambio_monedas(monedas, cantidad):
    #inicio con un valor infinito para las monedar de dar a cambio por ejemplo si es que queiro dar cambio
    dp = [cantidad + 1] * (cantidad + 1)
    
    # aca guardo que moneda use en cada paso para despues armar la combinacion en reversa
    moneda_usada = [-1] * (cantidad + 1)
    
    # mi caso base: para dar 0 de cambio se necesitan 0 monedas
    dp[0] = 0
    
    # aca empiezo a llenar la tabla dp desde el valor 1 hasta la cantidad objetivo
    for i in range(1, cantidad + 1):
        # pruebo con cada una de las monedas que tengo disponibles
        for moneda in monedas:
            # si la moneda no supera la cantidad actual que estoy evaluando
            if i >= moneda:
                # me fijo si usando esta moneda gasto menos que lo que ya tenia guardado
                if dp[i - moneda] + 1 < dp[i]:
                    dp[i] = dp[i - moneda] + 1
                    moneda_usada[i] = moneda # guardo la moneda ganadora para el recuerdo
                    
    # si es que el calor en dp es mayor que la cantidad entonces no hay cambio 
    if dp[cantidad] > cantidad:
        print("no se puede dar el cambio exacto con esas monedas.")
        return

    # aca viene la reconstruccion del camino en reversa usando el truco de la moneda guardada
    combinacion = []
    actual = cantidad
    while actual > 0:
        c = moneda_usada[actual]
        combinacion.append(c)
        actual -= c # voy retrocediendo en la tabla
        
    # aca muestro los resultados tal cual lo pide la guia
    print(f"Cantidad mínima de monedas: {dp[cantidad]}")
    # con el join lo muestro bonito separado por un " + " como en las escaleras
    print(f"Combinación: {' + '.join(map(str, combinacion))}")
    print(f"Tabla DP:\n{dp}")


# impresion de ejemplos de la guia

print("ejemplo1")
print("Monedas: [1, 3, 4], Cantidad: 6")
cambio_monedas([1, 3, 4], 6)

print("\nejemplo2")
print("Monedas: [1, 2, 5], Cantidad: 11")
cambio_monedas([1, 2, 5], 11)