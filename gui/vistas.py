"""Componentes visuales de la aplicación."""

from __future__ import annotations

import tkinter as tk
from dataclasses import dataclass
from tkinter import ttk


@dataclass
class RelationView:
    """Contenedor de widgets de la interfaz principal."""

    root: tk.Tk

    def __post_init__(self) -> None:
        self.tipo_relacion_var = tk.StringVar(value="AA")
        self.par_primero_var = tk.StringVar()
        self.par_segundo_var = tk.StringVar()

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(3, weight=1)

        self._crear_panel_tipo_relacion()
        self._crear_panel_conjuntos()
        self._crear_panel_relacion()
        self._crear_panel_resultados()

    def _crear_panel_tipo_relacion(self) -> None:
        frame = ttk.LabelFrame(self.root, text="Tipo de relación")
        frame.grid(row=0, column=0, sticky="ew", padx=10, pady=6)

        ttk.Radiobutton(
            frame,
            text="Relación sobre A × A",
            variable=self.tipo_relacion_var,
            value="AA",
        ).grid(row=0, column=0, padx=8, pady=6, sticky="w")

        ttk.Radiobutton(
            frame,
            text="Relación de A en B",
            variable=self.tipo_relacion_var,
            value="AB",
        ).grid(row=0, column=1, padx=8, pady=6, sticky="w")

    def _crear_panel_conjuntos(self) -> None:
        frame = ttk.LabelFrame(self.root, text="Ingreso de conjuntos")
        frame.grid(row=1, column=0, sticky="ew", padx=10, pady=6)
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="A (separado por comas):").grid(row=0, column=0, sticky="w", padx=8, pady=6)
        self.entry_a = ttk.Entry(frame)
        self.entry_a.grid(row=0, column=1, sticky="ew", padx=8, pady=6)

        ttk.Label(frame, text="B (separado por comas):").grid(row=1, column=0, sticky="w", padx=8, pady=6)
        self.entry_b = ttk.Entry(frame)
        self.entry_b.grid(row=1, column=1, sticky="ew", padx=8, pady=6)

        self.btn_cargar = ttk.Button(frame, text="Cargar conjuntos")
        self.btn_cargar.grid(row=0, column=2, rowspan=2, padx=8, pady=6)

    def _crear_panel_relacion(self) -> None:
        frame = ttk.LabelFrame(self.root, text="Relación (pares ordenados)")
        frame.grid(row=2, column=0, sticky="ew", padx=10, pady=6)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(3, weight=1)

        ttk.Label(frame, text="Primer elemento (A):").grid(row=0, column=0, sticky="w", padx=8, pady=4)
        self.combo_primero = ttk.Combobox(frame, textvariable=self.par_primero_var, state="readonly")
        self.combo_primero.grid(row=0, column=1, sticky="ew", padx=8, pady=4)

        ttk.Label(frame, text="Segundo elemento:").grid(row=0, column=2, sticky="w", padx=8, pady=4)
        self.combo_segundo = ttk.Combobox(frame, textvariable=self.par_segundo_var, state="readonly")
        self.combo_segundo.grid(row=0, column=3, sticky="ew", padx=8, pady=4)

        self.btn_agregar = ttk.Button(frame, text="Agregar par")
        self.btn_agregar.grid(row=0, column=4, padx=8, pady=4)

        self.tree = ttk.Treeview(frame, columns=("a", "b"), show="headings", height=6)
        self.tree.heading("a", text="a")
        self.tree.heading("b", text="b")
        self.tree.grid(row=1, column=0, columnspan=4, sticky="ew", padx=8, pady=6)

        btn_frame = ttk.Frame(frame)
        btn_frame.grid(row=1, column=4, sticky="ns", padx=8, pady=6)

        self.btn_eliminar = ttk.Button(btn_frame, text="Eliminar par")
        self.btn_eliminar.grid(row=0, column=0, sticky="ew", pady=2)

        self.btn_limpiar = ttk.Button(btn_frame, text="Limpiar pares")
        self.btn_limpiar.grid(row=1, column=0, sticky="ew", pady=2)

        self.btn_analizar = ttk.Button(btn_frame, text="Analizar relación")
        self.btn_analizar.grid(row=2, column=0, sticky="ew", pady=2)

        self.btn_reiniciar = ttk.Button(btn_frame, text="Reiniciar")
        self.btn_reiniciar.grid(row=3, column=0, sticky="ew", pady=2)

    def _crear_panel_resultados(self) -> None:
        frame = ttk.LabelFrame(self.root, text="Resultados")
        frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=6)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        self.txt_resultados = tk.Text(frame, wrap="word", height=18)
        self.txt_resultados.grid(row=0, column=0, sticky="nsew", padx=8, pady=6)

        scroll = ttk.Scrollbar(frame, orient="vertical", command=self.txt_resultados.yview)
        scroll.grid(row=0, column=1, sticky="ns", pady=6)
        self.txt_resultados.configure(yscrollcommand=scroll.set)

    def actualizar_modo(self) -> None:
        """Ajusta campos según tipo de relación."""
        if self.tipo_relacion_var.get() == "AA":
            self.entry_b.configure(state="disabled")
            self.entry_b.delete(0, tk.END)
        else:
            self.entry_b.configure(state="normal")

    def actualizar_opciones_pares(self, conjunto_a: list[str], conjunto_b: list[str]) -> None:
        """Actualiza los combos de pares ordenados."""
        self.combo_primero["values"] = conjunto_a
        self.combo_segundo["values"] = conjunto_b
        self.par_primero_var.set(conjunto_a[0] if conjunto_a else "")
        self.par_segundo_var.set(conjunto_b[0] if conjunto_b else "")

    def limpiar_resultados(self) -> None:
        """Limpia panel de resultados."""
        self.txt_resultados.delete("1.0", tk.END)

    def set_resultados(self, contenido: str) -> None:
        """Muestra un bloque de resultados."""
        self.limpiar_resultados()
        self.txt_resultados.insert("1.0", contenido)
