from typing import Any

class Edge:
    def __init__(self, u: Any, v: Any, weight: float) -> None:
        """
        Inicializa una arista (Edge) en un grafo.

        Args:
            u (Any): El nodo de origen de la arista.
            v (Any): El nodo de destino de la arista.
            weight (float): El peso de la arista.
        """
        self.u = u
        self.v = v
        self.weight = weight

    def __lt__(self, other: 'Edge') -> bool:
        """
        Compara dos aristas basándose en su peso.

        Args:
            other (Edge): Otra arista a comparar.

        Returns:
            bool: True si el peso de esta arista es menor que el peso de la otra arista, False en caso contrario.
        """
        return self.weight < other.weight
