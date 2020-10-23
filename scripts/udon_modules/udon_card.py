import nfc
import binascii
import os
import json
from udon_modules import udon_db

def begin_reading():
        clf = nfc.ContactlessFrontend("usb")
        print("Listening")
        clf.connect(rdwr={"on-connect": on_connect})
        clf.close()

def on_connect(tag):
    IDm = str(binascii.hexlify(tag._nfcid))
    print("IDm : {IDm}".format(IDm=IDm))
    member_id = udon_db.tomember(IDm)
    #udon_api.record_attendance(member_id)
    print("record succeed")
    return True
