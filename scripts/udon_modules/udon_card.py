import nfc
import binascii
import os
import json
from udon_modules import udon_db

def begin_attendance_reading():
        clf = nfc.ContactlessFrontend("usb")
        print("Listening")
        clf.connect(rdwr={"on-connect": on_attendance})
        clf.close()

def on_attendance(tag):
    IDm = str(binascii.hexlify(tag._nfcid))
    print("IDm : {IDm}".format(IDm=IDm))
    member_id = udon_db.tomember(IDm)
    #udon_api.record_attendance(member_id)
    print("record succeed")
    return True

def begin_register_reading():
    clf = nfc.ContactlessFrontend("usb")
    print("Listening")
    clf.connect(rdwr={"on-connect": on_register(clf)})

def on_register(tag,clf):
    tag2 = clf.connect(rdwr={'on-connect': lambda tag2: True})
    if(tag._nfcid == tag2._nfcid):
        print("Valid")
        #udon_db.registrar_newtag(member_id,IDm)
    else:
        print("Invalid")



