#alumno: Elias Efrain Manchego Navarro
# en este algoritmo ayudaremos a kim petras a escapar del mall
# kim petras es una persona con discapacidad que necesita salir rapidamente del mall
# usaremos BFS (busqueda por amplitud) para encontrar el camino mas corto

import time  # usare esta solo para medir el tiempo
import random  # para generar mapas random

class escapekimpetras:
    def __init__(self):
        # uso esto para guardar el grafo y sus conexiones
        self.grafo = {}
        # aca guardo la matriz del mall con obstaculos y pasillos
        self.matrizmal = []
        # mapeo de coordenadas a nodos y viceversa
        self.coordanodo = {}
        self.nodoacord = {}

    def maparandombfs(self):
        # genero la matriz 7x7 con obstaculos y pasillos random para kimpetras
        tamaño = 7
        self.matrizmal = []
        contadornodo = 0
        
        # seed para numeros random
        random.seed(int(time.time() * 1000) % 10000)
        
        # genero la matriz
        for i in range(tamaño):
            fila = []
            for j in range(tamaño):
                # bordes siempre obstaculos
                if i == 0 or i == tamaño - 1 or j == 0 or j == tamaño - 1:
                    fila.append("#")
                else:
                    # 35% obstaculos 65% pasillos
                    if random.random() < 0.35:
                        fila.append("#")
                    else:
                        fila.append(".")
                        # registrar pasillos como nodos
                        nodoid = f"N{contadornodo}"
                        self.coordanodo[(i, j)] = nodoid
                        self.nodoacord[nodoid] = (i, j)
                        self.grafo[nodoid] = {}
                        contadornodo += 1
            self.matrizmal.append(fila)

    def conectarnodosbfs(self):
        # conecta los nodos adyacentes para que BFS pueda explorar el grafo
        tamaño = 7
        direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # derecha,abajo,izquierda,arriba
        
        for (i, j), nodou in self.coordanodo.items():
            for di, dj in direcciones:
                ni, nj = i + di, j + dj
                
                # verifico que este dentro de la matriz
                if 0 <= ni < tamaño and 0 <= nj < tamaño:
                    if (ni, nj) in self.coordanodo:
                        nodov = self.coordanodo[(ni, nj)]
                        # peso 1 para todos los movimientos
                        peso = 1
                        self.grafo[nodou][nodov] = peso

    def bfsexploracion(self, origen, destino):
        # BFS para encontrar el camino mas corto desde origen a destino
        # usamos una cola para explorar por amplitud
        
        if origen not in self.grafo or destino not in self.grafo:
            return [], 0
        
        # aca guardo la cola para BFS (lista simple sin usar librerías)
        cola = [origen]
        visitados = {origen}
        padres = {origen: None}
        
        # exploramos por amplitud
        while cola:
            nodoactual = cola.pop(0)  # sacamos el primer elemento de la cola
            
            # si llegamos al destino, terminamos
            if nodoactual == destino:
                break
            
            # exploramos los vecinos del nodo actual
            for vecino, peso in self.grafo[nodoactual].items():
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = nodoactual
                    cola.append(vecino)
        
        # construir la ruta desde origen a destino usando los padres
        if destino not in padres:
            return [], 999999
        
        ruta = []
        nodoactual = destino
        while nodoactual is not None:
            ruta.insert(0, nodoactual)
            nodoactual = padres[nodoactual]
        
        # calcular el costo (distancia) de la ruta
        costototal = len(ruta) - 1  # numero de pasos menos 1
        
        return ruta, costototal

    def interfazvisualbfs(self, ruta, costo, tiempoms):
        # interfaz para mostrar la evacuacion de kimpetras paso a paso
        
        print("KIMPETRAS ESCAPANDO DEL MALL ")
        
        print(f"tiempo de busqueda BFS: {tiempoms:.4f} ms")
        print(f"distancia recorrida: {costo} pasos")
       

        if not ruta:
            print("ay no hay ruta disponible para kimpetras")
            return

        # simulacion paso a paso
        for paso in range(len(ruta)):
            nodoactual = ruta[paso]
            if nodoactual not in self.nodoacord:
                continue
                
            coordactual = self.nodoacord[nodoactual]
            
            print(f"\n[Paso {paso+1}] kimpetras avanza por nodo: {nodoactual} pos: {coordactual}")
            
            # copia de la matriz para visualizar
            matrizvisual = [fila[:] for fila in self.matrizmal]
            
            # marcar el camino de kimpetras
            for j in range(len(ruta)):
                nodo = ruta[j]
                if nodo not in self.nodoacord:
                    continue
                coord = self.nodoacord[nodo]
                i, col = coord
                
                if j == paso:
                    matrizvisual[i][col] = "&"  # kimpetras aqui
                elif j < paso:
                    matrizvisual[i][col] = "*"  # camino recorrido
            
            # imprimir mapa
            print("Mapa BFS (exploración por amplitud):")
            for fila in matrizvisual:
                print("  " + " ".join(f"[{elemento}]" for elemento in fila))
            
            time.sleep(0.7)  # pausa dramatica

        
        print("kimpetras escapp exitosamente!")
        


# ejecutar el programa
if __name__ == "__main__":
    sistema = escapekimpetras()

    # generar mapa
    print("generando mapa random para kimpetras")
    sistema.maparandombfs()
    
    # conectar nodos
    print("conectando pasillos accesibles")
    sistema.conectarnodosbfs()
    
    # mostrar mapa
    print("\nMapa generado:")
    for fila in sistema.matrizmal:
        print("  " + " ".join(f"[{elemento}]" for elemento in fila))
    
    # obtener nodos
    nodos = list(sistema.grafo.keys())
    if len(nodos) < 2:
        print("no hay suficientes pasillos")
    else:
        origen = nodos[0]
        destino = nodos[-1]
        
        print(f"\nkimpetras busca salida de {origen} a {destino}")
        
        # medir tiempo de BFS
        inicioreloj = time.perf_counter()
        rutaoptima, costoier = sistema.bfsexploracion(origen, destino)
        finreloj = time.perf_counter()
        
        tiempoprocesamiento = (finreloj - inicioreloj) * 1000

        # mostrar interfaz
        sistema.interfazvisualbfs(rutaoptima, costoier, tiempoprocesamiento)
