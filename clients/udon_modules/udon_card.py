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
    if(member_id == ""):
        udon_status = "unknown_card" 
    else:
        udon_status = udon_api.record_attendance(member_id) #"record_succeed" or "internal_error"
    return True

#registrar

def begin_register_reading(member_id):
    print("Listening")
    clf.connect(rdwr={"on-connect": on_register(member_id)})
    return udon_status

def on_register(card,member_id):
    card2 = clf.connect(rdwr={'on-connect': lambda card2: False})
    if(card._nfcid == card2._nfcid):
        udon_status = udon_db.register_newcard(member_id,card._nfcid)
    else:
        udon_status = "unavailable_card"
    return True
