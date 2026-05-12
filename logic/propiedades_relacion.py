"""Propiedades de relaciones binarias."""

from __future__ import annotations

from typing import Iterable

Pair = tuple[str, str]


def es_reflexiva(relacion: set[Pair], conjunto_a: Iterable[str]) -> tuple[bool, set[Pair]]:
    """Evalúa reflexividad sobre AxA e indica pares faltantes."""
    faltantes = {(a, a) for a in conjunto_a if (a, a) not in relacion}
    return len(faltantes) == 0, faltantes


def es_simetrica(relacion: set[Pair]) -> tuple[bool, set[Pair]]:
    """Evalúa simetría e indica pares faltantes."""
    faltantes = {(b, a) for (a, b) in relacion if (b, a) not in relacion}
    return len(faltantes) == 0, faltantes


def es_transitiva(relacion: set[Pair]) -> tuple[bool, set[Pair]]:
    """Evalúa transitividad e indica pares faltantes."""
    faltantes: set[Pair] = set()
    pares = list(relacion)
    for a, b in pares:
        for c, d in pares:
            if b == c and (a, d) not in relacion:
                faltantes.add((a, d))
    return len(faltantes) == 0, faltantes
