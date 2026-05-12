# Relaciones y Funciones en Conjuntos Finitos

Aplicación de escritorio en **Python 3.12+** con **Tkinter + ttk** para una actividad de Matemática Discreta sobre relaciones y funciones en conjuntos finitos.

## Objetivo académico

Permitir ingresar conjuntos finitos y una relación binaria para:
- Diagnosticar propiedades de relaciones (reflexiva, simétrica, transitiva)
- Verificar relación de equivalencia (cuando aplica)
- Calcular cerraduras reflexiva, simétrica y transitiva
- Evaluar si la relación es función de A en B
- Clasificar la función (inyectiva, sobreyectiva, biyectiva)

## Características del sistema

- Selección entre relación sobre **A × A** o relación de **A en B**
- Validación de conjuntos:
  - No vacíos
  - Máximo 10 elementos
  - Sin duplicados
  - Entrada por comas con limpieza de espacios
- Construcción de relación por pares ordenados con:
  - Alta de pares uno por uno
  - Prevención de pares duplicados
  - Validación de pertenencia al dominio/codominio
  - Eliminación de pares seleccionados
  - Limpieza completa de pares
- Panel de resultados con resumen, propiedades, equivalencia, cerraduras y análisis de función

## Estructura del proyecto

```text
main.py
gui/
  app.py
  views.py
logic/
  sets_manager.py
  relation_properties.py
  closures.py
  function_analysis.py
utils/
  formatters.py
  validators.py
tests/
  test_relation_properties.py
  test_closures.py
  test_function_analysis.py
README.md
requirements.txt
```

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

## Ejemplos de uso

### Ejemplo 1: relación de equivalencia en A × A
- A: `1,2,3`
- R: `(1,1), (2,2), (3,3)`

Resultado esperado:
- Reflexiva: Sí
- Simétrica: Sí
- Transitiva: Sí
- Sí es relación de equivalencia

### Ejemplo 2: función biyectiva A -> B
- A: `a,b,c`
- B: `x,y,z`
- R: `(a,x), (b,y), (c,z)`

Resultado esperado:
- Es función: Sí
- Inyectiva: Sí
- Sobreyectiva: Sí
- Biyectiva: Sí

## Algoritmos implementados (resumen)

- **Reflexividad:** verifica `(a,a)` para todo `a` en `A`
- **Simetría:** para cada `(a,b)` exige `(b,a)`
- **Transitividad:** para `(a,b)` y `(b,c)` exige `(a,c)`
- **Cerradura reflexiva:** agrega diagonales faltantes
- **Cerradura simétrica:** agrega inversos faltantes
- **Cerradura transitiva:** iteración hasta punto fijo
- **Función A→B:** cada elemento de `A` tiene una y solo una imagen
- **Inyectividad:** elementos distintos de `A` no comparten imagen
- **Sobreyectividad:** todo elemento de `B` tiene preimagen
- **Biyectividad:** inyectiva y sobreyectiva

## Casos de prueba sugeridos

- Relación reflexiva correcta e incorrecta
- Relación simétrica correcta e incorrecta
- Relación transitiva correcta e incorrecta
- Cerradura reflexiva y simétrica
- Cerradura transitiva con más de una iteración
- Relación que sí es función
- Relación que no es función por múltiples imágenes
- Relación que no es función por elemento sin imagen
- Funciones inyectiva, sobreyectiva y biyectiva

## Ejecución de pruebas

```bash
python -m unittest discover -s tests -v
```
