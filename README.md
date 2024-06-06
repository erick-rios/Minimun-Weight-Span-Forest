# Proyecto de Algoritmo de Prim para Bosque de Expansión Mínima (MWSF)

Este proyecto implementa el algoritmo de Prim para encontrar el Bosque de Expansión Mínima (MWSF) de un grafo utilizando Python. El script principal lee un archivo de entrada que define los vértices y aristas de un grafo y calcula el MWSF.

## Estructura del Proyecto

- `src/`
  - `main.py`: Script principal que ejecuta el algoritmo de Prim para encontrar el MWSF.
  - `graph.py`: Contiene la implementación de la clase `Graph` que maneja el grafo.
  - `vertex.py`: Contiene la implementación de la clase `Vertex` que representa un vértice del grafo.
  - `edge.py`: Contiene la implementación de la clase `Edge` que representa una arista del grafo.

## Instalación

1. Clona el repositorio:
    ```bash
    cd Erick Rios 2
    ```

2. Asegúrate de tener Python instalado. Este proyecto está probado con Python 3.9. Se recomienda crear un entorno virtual:
    ```bash
    python3 -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias necesarias (si las hay). En este caso, no hay dependencias adicionales fuera de la librería estándar de Python.

## Uso

Para ejecutar el script principal y calcular el MWSF, usa el siguiente comando:
```bash
python -m src.main <input_file>