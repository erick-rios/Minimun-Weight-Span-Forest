import sys
from typing import List, Tuple
from src.graph import Graph

def main() -> None:
    """
    Función principal que ejecuta el script para encontrar el Bosque de Expansión Mínima (MWSF) 
    utilizando el algoritmo de Prim.

    Lee un archivo de entrada que especifica los vértices y aristas de un grafo,
    construye el grafo y luego encuentra y muestra el MWSF.

    El archivo de entrada debe tener el siguiente formato:
    - La primera línea contiene una lista de vértices separados por comas.
    - Las líneas subsiguientes contienen pares de vértices y el peso de la arista entre ellos,
      separados por comas y un punto y coma. Ejemplo:
      1,5: 1
      2,5: 2
      3,4: 3

    Uso:
        python prim.py <input_file>
    """
    if len(sys.argv) != 2:
        print("Usage: python prim.py <input_file>")
        return
    
    file_path: str = sys.argv[1]
    result = Graph.parse_input(file_path)
    vertices: List[str] = result[0]
    edges: List[Tuple[str, str, int]] = result[1]
    graph: Graph = Graph()
    graph.build_graph(vertices, edges)
    mwsf_edges: List[Tuple[str, str, float]] = graph.find_mwsf(vertices)

    print("Elementos del bosque de arboles generadores de peso minimo")
    for u, v, weight in mwsf_edges:
        print(f"{u},{v}: {weight}")

if __name__ == "__main__":
    main()


