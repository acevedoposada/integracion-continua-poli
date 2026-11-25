import json
import threading
import unittest
import urllib.request
from http.server import HTTPServer

from app import Handler, saludo


class PruebasApp(unittest.TestCase):
    def test_saludo(self):
        self.assertEqual(saludo("equipo"), "Hola, equipo. Proyecto de integración continua.")


class PruebasHTTP(unittest.TestCase):
    def test_get_responde_json(self):
        servidor = HTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=servidor.serve_forever, daemon=True).start()
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{servidor.server_port}/") as r:
                self.assertEqual(r.status, 200)
                self.assertEqual(json.load(r), {"mensaje": saludo("equipo"), "estado": "ok"})
        finally:
            servidor.shutdown()
            servidor.server_close()


if __name__ == "__main__":
    unittest.main()
