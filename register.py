import json
import nfc
import binascii
import os
from main import Reader
from websocket_server import WebsocketServer


class CardRegister(Reader):
    def on_connect(self, tag):
        super().on_connect(tag)
        self.registNewTag()
        return True

    def registNewTag(self):
        newTagID = self.tagIDbeforeConvert
        # regist new tag


while True:
    register = CardRegister()
    register.read()
