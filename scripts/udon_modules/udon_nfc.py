import nfc
import binascii
import os
import json

def begin_reading(self):
        clf = nfc.ContactlessFrontend("usb")
        print("Listening")
        clf.connect(rdwr={"on-connect": self.on_connect})
        clf.close()
    else:
        server.send("other_error")

def on_connect(self, tag):
    IDm = str(binascii.hexlify(tag._nfcid))
    print("IDm : {IDm}".format(IDm=tagID))
    return True
