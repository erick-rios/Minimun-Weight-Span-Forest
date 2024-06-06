import heapq
from collections import defaultdict
from typing import Dict, List, Tuple, Optional, Any, Union
from src.vertex import Vertex
from src.edge import Edge

class Graph:
    def __init__(self):
        """
        Inicializa un grafo vacío.
        """
        self.vertices: Dict[Any, Vertex] = {}
        self.edges: List[Edge] = []

    def add_vertex(self, id: Any) -> None:
        """
        Añade un vértice al grafo.

        Args:
            id (Any): Identificador del vértice.
        """
        if id not in self.vertices:
            self.vertices[id] = Vertex(id)

    def add_edge(self, u: Any, v: Any, weight: float) -> None:
        """
        Añade una arista al grafo.

        Args:
            u (Any): Nodo de origen de la arista.
            v (Any): Nodo de destino de la arista.
            weight (float): Peso de la arista.
        """
        self.add_vertex(u)
        self.add_vertex(v)
        edge = Edge(u, v, weight)
        self.vertices[u].add_edge(edge)
        self.vertices[v].add_edge(edge)
        self.edges.append(edge)

    def get_vertex(self, id: Any) -> Optional[Vertex]:
        """
        Obtiene un vértice por su identificador.

        Args:
            id (Any): Identificador del vértice.

        Returns:
            Optional[Vertex]: El vértice correspondiente o None si no existe.
        """
        return self.vertices.get(id, None)

    def get_vertices(self) -> List[Vertex]:
        """
        Obtiene una lista de todos los vértices del grafo.

        Returns:
            List[Vertex]: Lista de vértices.
        """
        return list(self.vertices.values())

    @staticmethod
    def parse_input(file_path: str) -> Tuple[List[str], List[Tuple[str, str, int]]]:
        """
        Parsea un archivo de entrada para obtener los vértices y aristas.

        Args:
            file_path (str): Ruta del archivo de entrada.

        Returns:
            Tuple[List[str], List[Tuple[str, str, int]]]: Lista de vértices y lista de aristas (origen, destino, peso).
        """
        with open(file_path, 'r') as f:
            lines = f.readlines()

        vertices = lines[0].strip().split(',')
        edges = []

        for line in lines[1:]:
            try:
                parts = line.strip().split(': ')
                nodes = parts[0].split(',')
                weight = int(parts[1])
                edges.append((nodes[0], nodes[1], weight))
            except (IndexError, ValueError) as e:
                print(f"Skipping invalid line: {line.strip()}")
        
        return vertices, edges

    def build_graph(self, vertices: List[str], edges: List[Tuple[str, str, float]]) -> None:
        """
        Construye el grafo a partir de listas de vértices y aristas.

        Args:
            vertices (List[str]): Lista de identificadores de vértices.
            edges (List[Tuple[str, str, float]]): Lista de aristas (origen, destino, peso).
        """
        for u, v, weight in edges:
            self.add_edge(u, v, weight)

    def prim_mst(self, start: Any) -> List[Tuple[Any, Any, float]]:
        """
        Encuentra el Árbol de Expansión Mínima (MST) utilizando el algoritmo de Prim.

        Args:
            start (Any): Vértice inicial.

        Returns:
            List[Tuple[Any, Any, float]]: Lista de aristas en el MST.
        """
        mst_edges = []
        visited = set()
        min_heap = [(0, start, None)]  # (weight, current_vertex, parent_vertex)
        edge_map = {start: (None, 0)}  # Map of vertex to (parent, weight)

        while min_heap:
            weight, u, parent = heapq.heappop(min_heap)
            if u not in visited:
                visited.add(u)
                if parent is not None:
                    mst_edges.append((parent, u, weight))

                for edge in self.get_vertex(u).edges:
                    v = edge.v if edge.u == u else edge.u
                    if v not in visited:
                        heapq.heappush(min_heap, (edge.weight, v, u))
                        if v not in edge_map or edge.weight < edge_map[v][1]:
                            edge_map[v] = (u, edge.weight)
        
        return mst_edges

    def find_mwsf(self, vertices: List[Any]) -> List[Tuple[Any, Any, float]]:
        """
        Encuentra el Bosque de Expansión Mínima (MWSF) para un conjunto de vértices.

        Args:
            vertices (List[Any]): Lista de identificadores de vértices.

        Returns:
            List[Tuple[Any, Any, float]]: Lista de aristas en el MWSF.
        """
        remaining_vertices = set(vertices)
        mwsf_edges = []

        while remaining_vertices:
            start = remaining_vertices.pop()
            mst_edges = self.prim_mst(start)
            mwsf_edges.extend(mst_edges)
            for _, u, _ in mst_edges:
                remaining_vertices.discard(u)
        
        return mwsf_edges
