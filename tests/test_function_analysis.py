"""Pruebas de análisis de funciones."""

import unittest

from logic.function_analysis import (
    analizar_biyectividad,
    analizar_inyectividad,
    analizar_sobreyectividad,
    es_funcion,
)


class FunctionAnalysisTests(unittest.TestCase):
    def test_si_es_funcion(self) -> None:
        a = ["1", "2"]
        b = ["x", "y"]
        r = {("1", "x"), ("2", "y")}
        ok, _ = es_funcion(r, a, b)
        self.assertTrue(ok)

    def test_no_es_funcion_por_multiples_imagenes(self) -> None:
        a = ["1", "2"]
        b = ["x", "y"]
        r = {("1", "x"), ("1", "y"), ("2", "y")}
        ok, detalles = es_funcion(r, a, b)
        self.assertFalse(ok)
        self.assertIn("1", detalles["multiples_imagenes"])

    def test_no_es_funcion_por_falta_imagen(self) -> None:
        a = ["1", "2"]
        b = ["x", "y"]
        r = {("1", "x")}
        ok, detalles = es_funcion(r, a, b)
        self.assertFalse(ok)
        self.assertEqual(detalles["sin_imagen"], ["2"])

    def test_inyectiva_sobreyectiva_biyectiva(self) -> None:
        a = ["1", "2"]
        b = ["x", "y"]
        r = {("1", "x"), ("2", "y")}

        inyectiva, _ = analizar_inyectividad(r, a, b)
        sobreyectiva, _ = analizar_sobreyectividad(r, a, b)
        biyectiva, _ = analizar_biyectividad(r, a, b)

        self.assertTrue(inyectiva)
        self.assertTrue(sobreyectiva)
        self.assertTrue(biyectiva)


if __name__ == "__main__":
    unittest.main()
