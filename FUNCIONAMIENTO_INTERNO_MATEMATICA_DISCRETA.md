# Funcionamiento interno del programa (Matemática Discreta)

Este documento explica, de forma técnica y académica, cómo opera internamente la aplicación **Relaciones y Funciones en Conjuntos Finitos**.

## 1) Modelo matemático que implementa el sistema

- **Conjuntos finitos**: \(A\) y, según el modo, \(B\).
- **Relación binaria**: subconjunto \(R \subseteq A \times A\) (modo AA) o \(R \subseteq A \times B\) (modo AB).
- **Función**: caso especial de relación \(f: A \to B\), donde cada elemento de \(A\) tiene exactamente una imagen en \(B\).
- **Propiedades relacionales**: reflexiva, simétrica y transitiva.
- **Cerraduras**: reflexiva, simétrica y transitiva como extensiones mínimas de \(R\).

## 2) Arquitectura interna del proyecto

El programa separa responsabilidades en capas:

- `gui/` → interfaz gráfica y eventos del usuario.
- `logic/` → algoritmos de teoría de relaciones y funciones.
- `utils/` → validación y formateo.
- `tests/` → verificación unitaria de propiedades, cerraduras y funciones.

### Flujo general

1. Usuario ingresa conjuntos en GUI.
2. `logic/gestor_conjuntos.py` valida y guarda estado.
3. Usuario agrega pares ordenados.
4. El estado interno almacena la relación como conjunto de tuplas.
5. Al analizar, `gui/aplicacion.py` invoca algoritmos de `logic/`.
6. Resultados se renderizan en lenguaje matemático en el panel de salida.

## 3) Estructuras de datos clave

- `conjunto_a`, `conjunto_b`: listas de `str` (mantienen orden de ingreso).
- `relacion`: `set[tuple[str, str]]` (evita pares duplicados y permite consulta rápida).
- `RelationState` (`logic/gestor_conjuntos.py`): estado central del dominio.

Interpretación formal:

- Cada par `(x, y)` representa \(xRy\).
- El uso de `set` implementa la idea de relación como **conjunto de pares ordenados**.

## 4) Validaciones de entrada (criterios académicos)

En `utils/validadores.py`:

- Los conjuntos no pueden estar vacíos.
- Máximo 10 elementos por conjunto.
- No se permiten elementos duplicados en el mismo conjunto.
- Todo par agregado debe pertenecer al producto cartesiano permitido:
  - modo AA: \(A \times A\)
  - modo AB: \(A \times B\)

Esto garantiza que la relación ingresada tenga consistencia matemática.

## 5) Algoritmos implementados y significado discreto

### 5.1 Reflexividad (`es_reflexiva`)

Verifica si \((a,a)\in R\) para todo \(a\in A\).

- Salida: `bool` + conjunto de pares diagonales faltantes.
- Idea discreta: inspección de la diagonal de la matriz de relación.

### 5.2 Simetría (`es_simetrica`)

Para cada \((a,b)\in R\), exige \((b,a)\in R\).

- Salida: `bool` + pares inversos faltantes.
- Idea discreta: invariancia frente al intercambio de componentes.

### 5.3 Transitividad (`es_transitiva`)

Si \((a,b)\in R\) y \((b,c)\in R\), entonces \((a,c)\in R\).

- Implementación: doble recorrido sobre pares existentes.
- Salida: `bool` + pares implicados que faltan.
- Idea discreta: cierre por composición de relaciones.

### 5.4 Cerradura reflexiva (`cerradura_reflexiva`)

Agrega todos los \((a,a)\) faltantes de \(A\).

- Devuelve: pares agregados + nueva relación.
- Garantiza la mínima extensión reflexiva.

### 5.5 Cerradura simétrica (`cerradura_simetrica`)

Agrega inversos faltantes \((b,a)\) para cada \((a,b)\).

- Devuelve: pares agregados + nueva relación.
- Garantiza la mínima extensión simétrica.

### 5.6 Cerradura transitiva (`cerradura_transitiva`)

Itera agregando consecuencias transitivas hasta llegar a **punto fijo** (ya no aparecen pares nuevos).

- Devuelve: pares agregados + relación final.
- Idea discreta: construcción de clausura de alcance.

### 5.7 Análisis de función (`es_funcion`, `analizar_*`)

Se evalúa si \(R\) define función \(A\to B\):

- Cada \(a\in A\) tiene al menos una imagen (existencia).
- Cada \(a\in A\) tiene a lo sumo una imagen (unicidad).
- No hay pares fuera de dominio/codominio.

Luego clasifica:

- **Inyectiva**: elementos distintos de \(A\) no comparten imagen.
- **Sobreyectiva**: todo elemento de \(B\) recibe preimagen.
- **Biyectiva**: inyectiva y sobreyectiva.

## 6) Orquestación de la GUI

Archivo principal: `gui/aplicacion.py`.

- Conecta botones/eventos con métodos del controlador.
- Usa `RelationState` como modelo de estado.
- Invoca funciones de `logic/` para análisis formal.
- Construye el reporte final con secciones:
  - Resumen
  - Propiedades
  - Equivalencia
  - Cerraduras
  - Análisis de función

## 7) Relación de equivalencia en el sistema

El programa declara equivalencia solo cuando la relación es sobre \(A\times A\) y cumple:

- reflexiva
- simétrica
- transitiva

Si se trabaja en modo \(A \to B\), indica explícitamente que la equivalencia no aplica formalmente cuando \(A \neq B\).

## 8) Complejidad (visión práctica)

Sea \(n=|R|\), \(m=|A|\):

- Reflexiva: \(O(m)\)
- Simétrica: \(O(n)\)
- Transitiva (verificación): \(O(n^2)\)
- Cerradura transitiva: iterativa, en práctica superior a \(O(n^2)\) según densidad de \(R\)

## 9) Trazabilidad archivo → concepto

- `logic/propiedades_relacion.py` → axiomas de relación.
- `logic/cerraduras.py` → clausuras mínimas.
- `logic/analisis_funcion.py` → definición formal de función y clasificación.
- `utils/validadores.py` → pertenencia y consistencia del producto cartesiano.
- `logic/gestor_conjuntos.py` → estado matemático vigente en sesión.
- `gui/aplicacion.py` y `gui/vistas.py` → interacción usuario ↔ formalismo.

## 10) Cómo descargar las versiones del documento

En GitHub:

1. Abrir `FUNCIONAMIENTO_INTERNO_MATEMATICA_DISCRETA.docx` para descargar la versión Word.
2. En GitHub, abrir el archivo y usar la opción de descarga/guardado del navegador para obtener el `.docx`.
3. Si prefieres, también está `FUNCIONAMIENTO_INTERNO_MATEMATICA_DISCRETA.doc` (texto) y este `.md`.
