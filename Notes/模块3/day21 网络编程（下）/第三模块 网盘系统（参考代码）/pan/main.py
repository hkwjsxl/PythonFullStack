from src.handlers.pan import PanHandler
from src.server import Server
from src.select_server import SelectServer

if __name__ == '__main__':
    # server = Server()
    server = SelectServer()
    server.run(PanHandler)
