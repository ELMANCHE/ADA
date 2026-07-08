#alumno: Elias Efrain Manchego Navarro
# En este algoritmo ayudaremos a mi cnatnate favorita del dance europeo
#Inna vino a  visitar Arequipa (algun dia vendra por lo menos al Perú pipipi)

#Bueno ella esta atrapada en el mall en silla de ruedad y necesita salir en un movimiento sisimico tipico de Arequipa
import time  # usare esta libreria solo para medir el tiempo  
import random  # esta es importante porque usare para generar numeros random en el mapa

class escapeinna:
    def __init__(self):
        # uso esto para guardar el grafo y sus conexiones 
        self.grafo = {}
        # esto es para guardar la siguiente posicion en la mejor ruta 
        self.siguiente_nodo = {}
        # este es para representar un valor infinito en la matriz de distancias para el algoritmo de Floyd-Warshall
        self.INF = 999999
        # quiero trabajar el mapa con matrices 
        self.matriz_mall = []
        # aca mapeare las coordenadas de la matriz a los nodos del grafo y viceversa
        self.coord_a_nodo = {}
        self.nodo_a_coord = {}

    def maparandommall(self):
        # aca como le dije anteriormente genero la matriz 7x7 con los obstaculos y pasillos random 
        tamaño = 7
        self.matriz_mall = []
        contador_nodo = 0
        
        # usare seed que es para que los numeros sean random cada vez que se ejecute 
        random.seed(int(time.time() * 1000) % 10000)
        
        # bueno se genera la matriz con obstaculos y pasillos 
        for i in range(tamaño):
            fila = []
            for j in range(tamaño):
                # hare los bordes siempre obstaculos 
                if i == 0 or i == tamaño - 1 or j == 0 or j == tamaño - 1:
                    fila.append("#")
                else:
                    # pondre 35% de obstaculos y 65% de pasillos
                    if random.random() < 0.35:
                        fila.append("#")
                    else:
                        fila.append(".")
                        # registrar los pasillos como nodos 
                        nodo_id = f"N{contador_nodo}"
                        self.coord_a_nodo[(i, j)] = nodo_id
                        self.nodo_a_coord[nodo_id] = (i, j)
                        self.grafo[nodo_id] = {}
                        contador_nodo += 1
            self.matriz_mall.append(fila)

    def conectarnodosdina(self):
        # aca se conecta los nodos que son adyacentes en la matriz y que no son obstaculos
        tamaño = 7
        direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # derecha,izquierda,abajo,arriba
        # ciclo para recorrer cada nodo y conectar con sus vecinos 
        for (i, j), nodo_u in self.coord_a_nodo.items():
            for di, dj in direcciones:
                ni, nj = i + di, j + dj
                
                # verifico que este dentro de la matriz
                if 0 <= ni < tamaño and 0 <= nj < tamaño:
                    if (ni, nj) in self.coord_a_nodo:
                        nodo_v = self.coord_a_nodo[(ni, nj)]
                        # le dare un peso de 1 para que sea mas facil de calcular el IER acumulado
                        peso = 1
                        self.grafo[nodo_u][nodo_v] = peso

    def floydwarshall(self):
        # aca implemento el algoritmo de Floyd-Warshall para encontrar la mejor ruta
        nodos = list(self.grafo.keys())
        
        if len(nodos) == 0:
            return {}
        
        # la matriz de distancias y la matriz de siguiente nodo se inicializan con valores infinitos y None respectivamente
        dist = {u: {v: self.INF for v in nodos} for u in nodos}
        self.siguiente_nodo = {u: {v: None for v in nodos} for u in nodos}

        # iniciar distancias con los pesos de las aristas existentes en el grafo
        for u in nodos:
            dist[u][u] = 0
            for v, peso in self.grafo[u].items():
                dist[u][v] = peso
                self.siguiente_nodo[u][v] = v

        # aca aplico la ecuacion de Floyd-Warshall para actualizar las distancias y los siguientes nodos
        for k in nodos:
            for i in nodos:
                for j in nodos:
                    # si pasa por k y es mejor actualizo la distancia y el siguiente nodo
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        self.siguiente_nodo[i][j] = self.siguiente_nodo[i][k]
        
        return dist

    def construirruta(self, origen_id: str, destino_id: str) -> list:
        #construye la mejor urta desde el origen hasta el destino usando la matriz de siguiente nodo
        u = origen_id
        v = destino_id
        if u not in self.grafo or v not in self.grafo:
            return []
        
        if self.siguiente_nodo[u][v] is None and u != v:
            return []
            
        ruta = [u]
        while u != v:
            u = self.siguiente_nodo[u][v]
            if u is None:
                return []
            ruta.append(u)
        return ruta

    def interfazterminal(self, ruta: list, costo_total: int, tiempo_ms: float):
        # aca se renderiza la interfaz de monitoreo de evacuacion en la terminal porque queria que por lo menos tuviera alguna interfaz y sea divertido ahhahaha
        print(" Es hora evaucar el mall incidente inminente!")
        print(f"tiempo  {tiempo_ms:.4f} ms")
        print(f"esfuerzo que toma {costo_total}")
        print("-"*65)

        if not ruta:
            print("pipipi no hay ninguna ruta disponible ahora ")
            return

        # simulacion de la evacuacion paso a paso mostrando el camino 
        for paso in range(len(ruta)):
            nodo_actual = ruta[paso]
            if nodo_actual not in self.nodo_a_coord:
                continue
                
            coord_actual = self.nodo_a_coord[nodo_actual]
            
            print(f"\n[Paso {paso+1}] Avanzando por el nodo: {nodo_actual} en posición {coord_actual}")
            
            # la copia de la matriz que es el intento de un piso del mall 
            matrizvisual = [fila[:] for fila in self.matriz_mall]
            
            # marcar el camino recorrdio y posicion actual de la persona 
            for j in range(len(ruta)):
                nodo = ruta[j]
                if nodo not in self.nodo_a_coord:
                    continue
                coord = self.nodo_a_coord[nodo]
                i, col = coord
                
                if j == paso:
                    matrizvisual[i][col] = "&"  # la persona hahah
                elif j < paso:
                    matrizvisual[i][col] = "*"  # lo que camino 
            
            # imprimir la matriz en la terminal 
            print("Mapa de Trayecto (Generado Aleatoriamente + Floyd-Warshall):")
            for fila in matrizvisual:
                print("  " + " ".join(f"[{elemento}]" for elemento in fila))
            
            time.sleep(0.7)  # pausa para simular el tiempo de evacuacion y que se vea mas dramatico

        print("Estas a salvo !")


# Caso de prueba para ejecutar el algoritmo 
if __name__ == "__main__":
    sistema = escapeinna()

    # genera la matriz del mall aleatorio 
    print("generando matriz random del mall")
    sistema.maparandommall()
    
    # conectar mos pasillos accesibles en el grafo
    print("conectando pasillos accesibles en el grafo")
    sistema.conectarnodosdina()
    
    # matriz del mall lista para mostrar
    print("\nMapa del mall listo")
    for fila in sistema.matriz_mall:
        print("  " + " ".join(f"[{elemento}]" for elemento in fila))
    
    # obtener nodos accesibles para determinar origen y destino
    nodos = list(sistema.grafo.keys())
    if len(nodos) < 2:
        print("que pena, no hay suficientes pasillos accesibles para evacuar el mall")
    else:
        # Seleccionar primer y último nodo accesible como origen y destino
        origen = nodos[0]
        destino = nodos[-1]
        
        print(f"\nBúsqueda de ruta óptima desde {origen} a {destino}...")
        
        # registro del tiempo  que toma el algoritmo de Floyd-Warshall para encontrar la ruta óptima
        inicio_reloj = time.perf_counter()
        matrizdinamic = sistema.floydwarshall()
        fin_reloj = time.perf_counter()
        
        # convertir el tiempo a milisegundos 
        tiempo_procesamiento_ms = (fin_reloj - inicio_reloj) * 1000

        # consulta la mejor salida desde el origen 
        ruta_optima = sistema.construirruta(origen, destino)
        costo_ier = matrizdinamic[origen][destino]

        # por ultimo todo lo bonito que se ve por cosnola 
        sistema.interfazterminal(ruta_optima, costo_ier, tiempo_procesamiento_ms)
