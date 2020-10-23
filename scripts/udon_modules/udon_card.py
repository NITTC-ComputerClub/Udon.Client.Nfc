import nfc
import binascii
import os
import json
from udon_modules import udon_db

clf = nfc.ContactlessFrontend("usb")

def begin_attendance_reading():
    print("Listening")
    clf.connect(rdwr={"on-connect":on_attendance})

def on_attendance(tag):
    IDm = str(binascii.hexlify(tag._nfcid))
    print("IDm : {IDm}".format(IDm=IDm))
    member_id = udon_db.tomember(IDm)
    #udon_api.record_attendance(member_id)
    print("record succeed")
    return True

def begin_register_reading():
    print("Listening")
    clf.connect(rdwr={"on-connect": on_register})

def on_register(tag):
    tag2 = clf.connect(rdwr={'on-connect': lambda tag2: False})
    print(tag2)
    if(tag._nfcid == tag2._nfcid):
        print("Valid")
        #udon_db.registrar_newtag(member_id,IDm)
    else:
        print("Invalid")
    return True



