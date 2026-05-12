"""Aplicación Tkinter para relaciones y funciones."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox

from gui.vistas import RelationView
from logic.cerraduras import cerradura_reflexiva, cerradura_simetrica, cerradura_transitiva
from logic.analisis_funcion import (
    analizar_biyectividad,
    analizar_inyectividad,
    analizar_sobreyectividad,
    es_funcion,
)
from logic.propiedades_relacion import es_reflexiva, es_simetrica, es_transitiva
from logic.gestor_conjuntos import RelationState
from utils.formateadores import formatear_conjunto, formatear_pares_faltantes, formatear_relacion


class RelationApp(tk.Tk):
    """Ventana principal de la aplicación."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Relaciones y Funciones - Matemática Discreta")
        self.geometry("980x780")

        self.state_model = RelationState()
        self.view = RelationView(self)

        self._conectar_eventos()
        self.view.actualizar_modo()

    def _conectar_eventos(self) -> None:
        self.view.tipo_relacion_var.trace_add("write", self._on_tipo_relacion_change)
        self.view.btn_cargar.configure(command=self.cargar_conjuntos)
        self.view.btn_agregar.configure(command=self.agregar_par)
        self.view.btn_eliminar.configure(command=self.eliminar_par)
        self.view.btn_limpiar.configure(command=self.limpiar_pares)
        self.view.btn_analizar.configure(command=self.analizar)
        self.view.btn_reiniciar.configure(command=self.reiniciar)

    def _on_tipo_relacion_change(self, *_: object) -> None:
        self.state_model.tipo_relacion = self.view.tipo_relacion_var.get()
        self.view.actualizar_modo()

    def cargar_conjuntos(self) -> None:
        ok, error = self.state_model.cargar_conjuntos(self.view.entry_a.get(), self.view.entry_b.get())
        if not ok:
            messagebox.showerror("Error de validación", error)
            return

        self._refrescar_tabla()
        self.view.actualizar_opciones_pares(self.state_model.conjunto_a, self.state_model.conjunto_b)
        self.view.set_resultados("Conjuntos cargados correctamente. Agrega pares y luego analiza la relación.")

    def agregar_par(self) -> None:
        primero = self.view.par_primero_var.get()
        segundo = self.view.par_segundo_var.get()
        ok, error = self.state_model.agregar_par(primero, segundo)
        if not ok:
            messagebox.showerror("Error al agregar par", error)
            return
        self._refrescar_tabla()

    def eliminar_par(self) -> None:
        seleccion = self.view.tree.selection()
        if not seleccion:
            messagebox.showerror("Error", "Selecciona un par para eliminar.")
            return

        item = self.view.tree.item(seleccion[0])
        par = (str(item["values"][0]), str(item["values"][1]))
        self.state_model.eliminar_par(par)
        self._refrescar_tabla()

    def limpiar_pares(self) -> None:
        self.state_model.limpiar_relacion()
        self._refrescar_tabla()

    def reiniciar(self) -> None:
        self.state_model.reiniciar()
        self.view.tipo_relacion_var.set("AA")
        self.view.entry_a.delete(0, tk.END)
        self.view.entry_b.configure(state="normal")
        self.view.entry_b.delete(0, tk.END)
        self.view.actualizar_modo()
        self.view.actualizar_opciones_pares([], [])
        self._refrescar_tabla()
        self.view.limpiar_resultados()

    def _refrescar_tabla(self) -> None:
        for item in self.view.tree.get_children():
            self.view.tree.delete(item)
        for a, b in sorted(self.state_model.relacion, key=lambda x: (x[0], x[1])):
            self.view.tree.insert("", tk.END, values=(a, b))

    def analizar(self) -> None:
        if not self.state_model.conjunto_a:
            messagebox.showerror("Error", "Primero debes cargar los conjuntos.")
            return

        a = self.state_model.conjunto_a
        b = self.state_model.conjunto_b
        r = self.state_model.relacion
        tipo = self.state_model.tipo_relacion

        lineas: list[str] = []
        lineas.append("RESUMEN")
        lineas.append(f"A = {formatear_conjunto(a)}")
        lineas.append(f"B = {formatear_conjunto(b)}")
        lineas.append(f"R = {formatear_relacion(r)}")
        lineas.append("")

        lineas.append("PROPIEDADES")
        reflexiva_no_aplica = tipo == "AB" and set(a) != set(b)
        if reflexiva_no_aplica:
            lineas.append("- Reflexiva: No aplica formalmente para relación de A en B con A != B.")
            ref_ok, ref_faltantes = False, set()
        else:
            ref_ok, ref_faltantes = es_reflexiva(r, a)
            lineas.append(f"- Reflexiva: {'Sí' if ref_ok else 'No'}")
            if not ref_ok:
                lineas.append(f"  Pares faltantes: {formatear_pares_faltantes(ref_faltantes)}")

        sim_ok, sim_faltantes = es_simetrica(r)
        lineas.append(f"- Simétrica: {'Sí' if sim_ok else 'No'}")
        if not sim_ok:
            lineas.append(f"  Pares faltantes: {formatear_pares_faltantes(sim_faltantes)}")

        trans_ok, trans_faltantes = es_transitiva(r)
        lineas.append(f"- Transitiva: {'Sí' if trans_ok else 'No'}")
        if not trans_ok:
            lineas.append(f"  Pares faltantes: {formatear_pares_faltantes(trans_faltantes)}")

        lineas.append("")
        lineas.append("EQUIVALENCIA")
        if tipo == "AA":
            es_equiv = ref_ok and sim_ok and trans_ok
            veredicto = "Sí es relación de equivalencia" if es_equiv else "No es relación de equivalencia"
            lineas.append(veredicto)
            lineas.append(
                f"Justificación: reflexiva={ref_ok}, simétrica={sim_ok}, transitiva={trans_ok}."
            )
        else:
            lineas.append("No aplica: el veredicto de equivalencia se evalúa solo para relación sobre A × A.")

        lineas.append("")
        lineas.append("CERRADURAS")
        if reflexiva_no_aplica:
            lineas.append("- Cerradura reflexiva: No aplica formalmente para A != B.")
        else:
            add_ref, rel_ref = cerradura_reflexiva(r, a)
            lineas.append(f"- Cerradura reflexiva, nuevos pares: {formatear_pares_faltantes(add_ref)}")
            lineas.append(f"  Relación resultante: {formatear_relacion(rel_ref)}")

        add_sim, rel_sim = cerradura_simetrica(r)
        lineas.append(f"- Cerradura simétrica, nuevos pares: {formatear_pares_faltantes(add_sim)}")
        lineas.append(f"  Relación resultante: {formatear_relacion(rel_sim)}")

        add_trans, rel_trans = cerradura_transitiva(r)
        lineas.append(f"- Cerradura transitiva, nuevos pares: {formatear_pares_faltantes(add_trans)}")
        lineas.append(f"  Relación resultante: {formatear_relacion(rel_trans)}")

        lineas.append("")
        lineas.append("ANÁLISIS DE FUNCIÓN")
        fn_ok, detalles_fn = es_funcion(r, a, b)
        if fn_ok:
            lineas.append("- Es función de A en B: Sí")
            inyectiva, conflictos = analizar_inyectividad(r, a, b)
            sobreyectiva, faltantes_sob = analizar_sobreyectividad(r, a, b)
            biyectiva, _ = analizar_biyectividad(r, a, b)

            lineas.append(f"- Inyectiva: {'Sí' if inyectiva else 'No'}")
            if not inyectiva:
                lineas.append(f"  Imágenes repetidas: {conflictos}")

            lineas.append(f"- Sobreyectiva: {'Sí' if sobreyectiva else 'No'}")
            if not sobreyectiva:
                lineas.append(f"  Elementos de B sin preimagen: {', '.join(faltantes_sob)}")

            lineas.append(f"- Biyectiva: {'Sí' if biyectiva else 'No'}")
        else:
            lineas.append("- Es función de A en B: No")
            sin_imagen = detalles_fn["sin_imagen"]
            multiples = detalles_fn["multiples_imagenes"]
            fuera_dominio = detalles_fn["pares_fuera_dominio"]
            fuera_codominio = detalles_fn["pares_fuera_codominio"]
            if sin_imagen:
                lineas.append(f"  Faltan imágenes para: {', '.join(sin_imagen)}")
            if multiples:
                lineas.append(f"  Múltiples imágenes detectadas: {multiples}")
            if fuera_dominio:
                lineas.append(f"  Pares fuera de A: {fuera_dominio}")
            if fuera_codominio:
                lineas.append(f"  Pares fuera de B: {fuera_codominio}")

        self.view.set_resultados("\n".join(lineas))


def run_app() -> None:
    """Ejecuta la aplicación."""
    app = RelationApp()
    app.mainloop()
