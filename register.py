import json
import nfc
import binascii
import os
from main import Reader


class CardRegister(Reader):
    def on_connect(self, tag):
        super().on_connect(tag)
        self.registNewTag()

    def registNewTag(self):
        newTagID = self.tagIDbeforeConvert
        # regist new tag


while True:
    register = CardRegister()
    register.read()
