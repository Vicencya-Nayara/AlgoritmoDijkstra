import heapq

def dijkstra(grafo, inicio):
    caminhos_mais_curtos = {inicio: (None, 0)}
    fila = [(0, inicio)]
    while fila:
        (dist, no_atual) = heapq.heappop(fila)
        for vizinho, distancia in grafo[no_atual].items():
            distancia_antiga = caminhos_mais_curtos.get(vizinho, (None, float('inf')))[1]
            nova_distancia = dist + distancia
            if nova_distancia < distancia_antiga:
                caminhos_mais_curtos[vizinho] = (no_atual, nova_distancia)
                heapq.heappush(fila, (nova_distancia, vizinho))
    # Construir os caminhos
    caminhos = {}
    for no in caminhos_mais_curtos:
        caminho = []
        no_atual = no
        while no_atual is not None:
            caminho.append(no_atual)
            proximo_no = caminhos_mais_curtos[no_atual][0]
            no_atual = proximo_no
        # Reverter o caminho para ir do início ao fim
        caminho = caminho[::-1]
        caminhos[no] = caminho
    return caminhos_mais_curtos, caminhos

grafo = {
    0: {2: 1, 4: 3},
    1: {2: 1, 3: 4},
    2: {0: 1, 1: 1, 3: 2, 4: 1},
    3: {1: 4, 2: 2, 4: 1},
    4: {0: 3, 2: 1, 3: 1}
}

vertice_inicial = 2
destino = 4

distancias, caminhos = dijkstra(grafo, vertice_inicial)

print(f"Distância mínima: {distancias[destino][1]}")
print(f"Caminho mínimo: {caminhos[destino]}")
