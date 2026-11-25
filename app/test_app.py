import unittest

from app import saludo


class PruebasApp(unittest.TestCase):
    def test_saludo(self):
        self.assertEqual(saludo("equipo"), "Hola, equipo. Proyecto de integración continua.")


if __name__ == "__main__":
    unittest.main()
