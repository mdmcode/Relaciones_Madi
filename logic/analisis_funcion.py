"""Análisis de funciones de A en B."""

from __future__ import annotations

from collections import defaultdict
from typing import Iterable

Pair = tuple[str, str]


def es_funcion(relacion: set[Pair], conjunto_a: Iterable[str], conjunto_b: Iterable[str]) -> tuple[bool, dict[str, object]]:
    """Verifica si la relación cumple la definición de función A->B."""
    set_a = set(conjunto_a)
    set_b = set(conjunto_b)
    imagenes_por_a: dict[str, set[str]] = {a: set() for a in set_a}
    pares_fuera_dominio: set[Pair] = set()
    pares_fuera_codominio: set[Pair] = set()

    for a, b in relacion:
        if a in imagenes_por_a:
            imagenes_por_a[a].add(b)
        else:
            pares_fuera_dominio.add((a, b))
        if b not in set_b:
            pares_fuera_codominio.add((a, b))

    sin_imagen = sorted([a for a, imgs in imagenes_por_a.items() if len(imgs) == 0])
    multiples_imagenes = {a: sorted(imgs) for a, imgs in imagenes_por_a.items() if len(imgs) > 1}

    es = not sin_imagen and not multiples_imagenes and not pares_fuera_dominio and not pares_fuera_codominio
    detalles: dict[str, object] = {
        "sin_imagen": sin_imagen,
        "multiples_imagenes": multiples_imagenes,
        "pares_fuera_dominio": sorted(pares_fuera_dominio),
        "pares_fuera_codominio": sorted(pares_fuera_codominio),
    }
    return es, detalles


def analizar_inyectividad(relacion: set[Pair], conjunto_a: Iterable[str], conjunto_b: Iterable[str]) -> tuple[bool, dict[str, list[str]]]:
    """Analiza si una función es inyectiva."""
    set_a = set(conjunto_a)
    imagen_a_preimagenes: dict[str, set[str]] = defaultdict(set)

    for a, b in relacion:
        if a in set_a:
            imagen_a_preimagenes[b].add(a)

    conflictos = {b: sorted(pre) for b, pre in imagen_a_preimagenes.items() if len(pre) > 1}
    return len(conflictos) == 0, conflictos


def analizar_sobreyectividad(relacion: set[Pair], conjunto_a: Iterable[str], conjunto_b: Iterable[str]) -> tuple[bool, list[str]]:
    """Analiza si una función es sobreyectiva."""
    set_a = set(conjunto_a)
    set_b = set(conjunto_b)
    imagenes = {b for a, b in relacion if a in set_a}
    faltantes = sorted(set_b - imagenes)
    return len(faltantes) == 0, faltantes


def analizar_biyectividad(relacion: set[Pair], conjunto_a: Iterable[str], conjunto_b: Iterable[str]) -> tuple[bool, dict[str, object]]:
    """Analiza si una función es biyectiva."""
    es_iny, conflictos = analizar_inyectividad(relacion, conjunto_a, conjunto_b)
    es_sob, faltantes = analizar_sobreyectividad(relacion, conjunto_a, conjunto_b)
    return es_iny and es_sob, {
        "inyectiva": es_iny,
        "sobreyectiva": es_sob,
        "conflictos_inyectividad": conflictos,
        "faltantes_sobreyectividad": faltantes,
    }
