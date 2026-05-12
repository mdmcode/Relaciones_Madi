"""Pruebas de cerraduras."""

import unittest

from logic.cerraduras import cerradura_reflexiva, cerradura_simetrica, cerradura_transitiva


class ClosuresTests(unittest.TestCase):
    def test_cerradura_reflexiva(self) -> None:
        a = ["1", "2"]
        r = {("1", "2")}
        agregados, resultado = cerradura_reflexiva(r, a)
        self.assertEqual(agregados, {("1", "1"), ("2", "2")})
        self.assertEqual(resultado, {("1", "2"), ("1", "1"), ("2", "2")})

    def test_cerradura_simetrica(self) -> None:
        r = {("a", "b")}
        agregados, resultado = cerradura_simetrica(r)
        self.assertEqual(agregados, {("b", "a")})
        self.assertEqual(resultado, {("a", "b"), ("b", "a")})

    def test_cerradura_transitiva_varios_pasos(self) -> None:
        r = {("a", "b"), ("b", "c"), ("c", "d")}
        agregados, resultado = cerradura_transitiva(r)
        self.assertEqual(agregados, {("a", "c"), ("b", "d"), ("a", "d")})
        self.assertEqual(resultado, r | {("a", "c"), ("b", "d"), ("a", "d")})


if __name__ == "__main__":
    unittest.main()
