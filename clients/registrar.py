from websocket_server import WebsocketServer
from udon_modules import udon_card
from udon_modules import udon_db

if __name__ == "__main__":
    server = WebsocketServer(9999,host="localhost")
    server.set_fn_message_received(udon_card.begin_register)
    server.run_forever()