"""Gestión del estado de conjuntos y relación."""

from __future__ import annotations

from dataclasses import dataclass, field

from utils.validators import validar_conjunto, validar_par

Pair = tuple[str, str]


@dataclass
class RelationState:
    """Estado de trabajo de la relación cargada en GUI."""

    tipo_relacion: str = "AA"
    conjunto_a: list[str] = field(default_factory=list)
    conjunto_b: list[str] = field(default_factory=list)
    relacion: set[Pair] = field(default_factory=set)

    def cargar_conjuntos(self, texto_a: str, texto_b: str = "") -> tuple[bool, str | None]:
        """Carga y valida conjuntos A y B según el tipo de relación."""
        ok_a, datos_a, error_a = validar_conjunto(texto_a, "A")
        if not ok_a:
            return False, error_a

        if self.tipo_relacion == "AA":
            self.conjunto_a = datos_a
            self.conjunto_b = list(datos_a)
            self.relacion.clear()
            return True, None

        ok_b, datos_b, error_b = validar_conjunto(texto_b, "B")
        if not ok_b:
            return False, error_b

        self.conjunto_a = datos_a
        self.conjunto_b = datos_b
        self.relacion.clear()
        return True, None

    def agregar_par(self, primero: str, segundo: str) -> tuple[bool, str | None]:
        """Agrega un par validado a la relación."""
        par = (primero.strip(), segundo.strip())
        ok, error = validar_par(par, self.conjunto_a, self.tipo_relacion, self.conjunto_b)
        if not ok:
            return False, error
        if par in self.relacion:
            return False, "El par ya existe en la relación."
        self.relacion.add(par)
        return True, None

    def eliminar_par(self, par: Pair) -> None:
        """Elimina un par existente."""
        self.relacion.discard(par)

    def limpiar_relacion(self) -> None:
        """Limpia todos los pares de la relación."""
        self.relacion.clear()

    def reiniciar(self) -> None:
        """Reinicia el estado completo."""
        self.tipo_relacion = "AA"
        self.conjunto_a.clear()
        self.conjunto_b.clear()
        self.relacion.clear()
