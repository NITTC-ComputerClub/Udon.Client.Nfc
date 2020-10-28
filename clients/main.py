from websocket_server import WebsocketServer
from udon_modules import udon_card

if __name__ == "__main__":
    server = WebsocketServer(9999,host="localhost")
    server.set_fn_message_received(udon_card.begin_attendance)
    server.run_forever()
