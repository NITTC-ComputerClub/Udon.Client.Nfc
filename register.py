import json
import nfc
import binascii
import os
from main import Reader
from websocket_server import WebsocketServer


class CardRegister(Reader):
    def read(self, client, server, message):
        if(message == "client_ready"):
            clf = nfc.ContactlessFrontend('usb')
            server.send_message_to_all("listening")  # Listening Tag...
            print("Touch me")
            """
                TODO make GUI
                like
                [Listening...]
                """
            clf.connect(rdwr={'on-connect': self.on_connect})
            clf.close()
        else:
            server.send("other_error")

    def on_connect(self, tag):
        super().on_connect(tag)
        server.send_message_to_all("touch_again")
        clf.connect(rdwr={'on-connect': self.eliminateRandomTag})
        return True

    def eliminateRandomTag(self, tag):
        if(tag._nfcid == self.tagIDbeforeConvert):
            server.send_message_to_all("regist_succeed")
            self.registNewTag(tag)
        else:
            server.send_message_to_all("regist_error")
        return True

    def registNewTag(self, tag):
        newTagID = self.tagIDbeforeConvert
        # regist new tag


if __name__ == '__main__':
    register = CardRegister()
    server = WebsocketServer(9999, host="localhost")
    server.set_fn_message_received(register.read)
    server.run_forever()
