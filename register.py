import json
import nfc
import binascii
import os
from main import Reader
from websocket_server import WebsocketServer


class CardRegister(Reader):
    def __init__(self):
        self.firstTouch = True

    def on_connect(self, tag):
        if(self.firstTouch):
            super().on_connect(tag)
            self.firstTouch = False
            server.send_message_to_all("touch_again")
        else:
            print(self.tagIDbeforeConvert)
            print(str(binascii.hexlify(tag._nfcid)))
            if(self.tagIDbeforeConvert == str(binascii.hexlify(tag._nfcid))):
                server.send_message_to_all("registing")
                self.registNewTag()
            else:
                server.send_message_to_all("cannot_regist_this_tag")
            self.firstTouch = True
        return True

    def registNewTag(self):
        newTagID = self.tagIDbeforeConvert
        # ask member name
        # regist new tag
        server.send_message_to_all("regist_succeed")


if __name__ == '__main__':
    register = CardRegister()
    server = WebsocketServer(9999, host="localhost")
    server.set_fn_message_received(register.read)
    server.run_forever()
