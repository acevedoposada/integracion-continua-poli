from http.server import BaseHTTPRequestHandler, HTTPServer
import json


def saludo(nombre):
    return f"Hola, {nombre}. Proyecto de integración continua."


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"mensaje": saludo("equipo"), "estado": "ok"}, ensure_ascii=False).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()
