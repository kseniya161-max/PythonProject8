from http.server import BaseHTTPRequestHandler, HTTPServer
import time

# Настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")
        self.end_headers()  # Завершение заголовков ответа

        # Открываем HTML-файла
        with open("contacts.html", "r", encoding="utf-8") as file:
            html_content = file.read()  # Чтение содержимого файла
        self.wfile.write(bytes(html_content, "utf-8"))  # Отправка содержимого HTML-файла


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
