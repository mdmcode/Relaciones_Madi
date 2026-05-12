"""Pruebas de propiedades de relaciones."""

import unittest

from logic.propiedades_relacion import es_reflexiva, es_simetrica, es_transitiva


class RelationPropertiesTests(unittest.TestCase):
    def test_es_reflexiva_correcta(self) -> None:
        a = ["1", "2"]
        r = {("1", "1"), ("2", "2"), ("1", "2")}
        ok, faltantes = es_reflexiva(r, a)
        self.assertTrue(ok)
        self.assertEqual(faltantes, set())

    def test_es_reflexiva_incorrecta(self) -> None:
        a = ["1", "2"]
        r = {("1", "1")}
        ok, faltantes = es_reflexiva(r, a)
        self.assertFalse(ok)
        self.assertEqual(faltantes, {("2", "2")})

    def test_es_simetrica_correcta(self) -> None:
        r = {("a", "b"), ("b", "a"), ("a", "a")}
        ok, faltantes = es_simetrica(r)
        self.assertTrue(ok)
        self.assertEqual(faltantes, set())

    def test_es_simetrica_incorrecta(self) -> None:
        r = {("a", "b")}
        ok, faltantes = es_simetrica(r)
        self.assertFalse(ok)
        self.assertEqual(faltantes, {("b", "a")})

    def test_es_transitiva_correcta(self) -> None:
        r = {("a", "b"), ("b", "c"), ("a", "c")}
        ok, faltantes = es_transitiva(r)
        self.assertTrue(ok)
        self.assertEqual(faltantes, set())

    def test_es_transitiva_incorrecta(self) -> None:
        r = {("a", "b"), ("b", "c")}
        ok, faltantes = es_transitiva(r)
        self.assertFalse(ok)
        self.assertEqual(faltantes, {("a", "c")})


if __name__ == "__main__":
    unittest.main()
