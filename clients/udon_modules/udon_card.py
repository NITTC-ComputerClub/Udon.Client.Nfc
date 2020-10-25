import nfc
import binascii
import os
import json
from udon_modules import udon_db

clf = nfc.ContactlessFrontend("usb")
udon_status = ""

def begin_attendance_reading():
    print("Listening")
    clf.connect(rdwr={"on-connect":on_attendance})
    return udon_status

def on_attendance(tag):
    IDm = str(binascii.hexlify(tag._nfcid))
    print("IDm : {IDm}".format(IDm=IDm))
    member_id = udon_db.tomember(IDm)
    udon_status = udon_api.record_attendance(member_id)
    return True

#registrar

def begin_register_reading():
    print("Listening")
    clf.connect(rdwr={"on-connect": on_register})

def on_register(tag):
    tag2 = clf.connect(rdwr={'on-connect': lambda tag2: False})
    print(tag2)
    if(tag._nfcid == tag2._nfcid):
        print("Valid")
        #udon_db.register_newtag(member_id,IDm)
    else:
        print("Invalid")
    return True
