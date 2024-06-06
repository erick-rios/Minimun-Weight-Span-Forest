from typing import Any, List
from src.edge import Edge

class Vertex:
    def __init__(self, id: Any) -> None:
        """
        Inicializa un vértice en un grafo.

        Args:
            id (Any): Identificador del vértice.
        """
        self.id: Any = id
        self.edges: List[Edge] = []

    def add_edge(self, edge: Edge) -> None:
        """
        Añade una arista a la lista de aristas conectadas a este vértice.

        Args:
            edge (Edge): La arista a añadir.
        """
        self.edges.append(edge)

