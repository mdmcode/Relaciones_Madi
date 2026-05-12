"""Cálculo de cerraduras de relaciones."""

from __future__ import annotations

from typing import Iterable

Pair = tuple[str, str]


def cerradura_reflexiva(relacion: set[Pair], conjunto_a: Iterable[str]) -> tuple[set[Pair], set[Pair]]:
    """Agrega todos los pares (a,a) faltantes."""
    faltantes = {(a, a) for a in conjunto_a if (a, a) not in relacion}
    resultado = set(relacion) | faltantes
    return faltantes, resultado


def cerradura_simetrica(relacion: set[Pair]) -> tuple[set[Pair], set[Pair]]:
    """Agrega todos los pares inversos faltantes."""
    faltantes = {(b, a) for (a, b) in relacion if (b, a) not in relacion}
    resultado = set(relacion) | faltantes
    return faltantes, resultado


def cerradura_transitiva(relacion: set[Pair]) -> tuple[set[Pair], set[Pair]]:
    """Expande transitivamente hasta alcanzar punto fijo."""
    actual = set(relacion)
    cambio = True
    while cambio:
        cambio = False
        nuevos: set[Pair] = set()
        pares = list(actual)
        for a, b in pares:
            for c, d in pares:
                if b == c and (a, d) not in actual:
                    nuevos.add((a, d))
        if nuevos:
            actual |= nuevos
            cambio = True
    agregados = actual - set(relacion)
    return agregados, actual
