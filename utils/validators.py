"""Validaciones puras para conjuntos y pares."""

from __future__ import annotations

from typing import Iterable

Pair = tuple[str, str]


def validar_conjunto(texto: str, nombre: str = "A", max_elementos: int = 10) -> tuple[bool, list[str], str | None]:
    """Valida un conjunto textual separado por comas."""
    elementos = [item.strip() for item in texto.split(",") if item.strip()]

    if not elementos:
        return False, [], f"El conjunto {nombre} no puede estar vacío."
    if len(elementos) > max_elementos:
        return False, [], f"El conjunto {nombre} no puede tener más de {max_elementos} elementos."
    if len(set(elementos)) != len(elementos):
        return False, [], f"El conjunto {nombre} contiene elementos duplicados."
    return True, elementos, None


def validar_par(
    par: Pair,
    conjunto_a: Iterable[str],
    tipo_relacion: str,
    conjunto_b: Iterable[str] | None = None,
) -> tuple[bool, str | None]:
    """Valida pertenencia de un par ordenado al producto cartesiano permitido."""
    a, b = par
    set_a = set(conjunto_a)
    set_b = set(conjunto_a) if tipo_relacion == "AA" else set(conjunto_b or [])

    if a not in set_a:
        return False, f"El elemento '{a}' no pertenece al conjunto A."
    if b not in set_b:
        destino = "A" if tipo_relacion == "AA" else "B"
        return False, f"El elemento '{b}' no pertenece al conjunto {destino}."
    return True, None
