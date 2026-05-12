"""Funciones de formato para mostrar resultados en GUI."""

from __future__ import annotations

from typing import Iterable

Pair = tuple[str, str]


def _sorted_pairs(pares: Iterable[Pair]) -> list[Pair]:
    return sorted(set(pares), key=lambda x: (x[0], x[1]))


def formatear_conjunto(elementos: Iterable[str]) -> str:
    """Devuelve un conjunto en formato matemático."""
    datos = sorted(set(elementos))
    return "{" + ", ".join(datos) + "}"


def formatear_relacion(pares: Iterable[Pair]) -> str:
    """Devuelve una relación en formato matemático."""
    ordenados = _sorted_pairs(pares)
    contenido = ", ".join(f"({a}, {b})" for a, b in ordenados)
    return "{" + contenido + "}"


def formatear_pares_faltantes(pares: Iterable[Pair]) -> str:
    """Devuelve texto para pares faltantes o agregados."""
    ordenados = _sorted_pairs(pares)
    if not ordenados:
        return "Ninguno"
    return ", ".join(f"({a}, {b})" for a, b in ordenados)
