import nfc
import binascii
import os
import json
from udon_modules import udon_db

clf = nfc.ContactlessFrontend("usb")
udon_status = ""

def read_idm():
    card= clf.connect(rdwr={'on-connect': lambda card: False})
    converted_id = binascii.hexlify(card._nfcid)
    return str(converted_id)


def begin_attendance_reading():
    print("Listening")
    idm= read_idm()
    member_id = udon_db.tomember(idm)
    if(member_id == ""):
        udon_status = "unknown_card" 
    else:
        udon_status = udon_api.record_attendance(member_id) #"record_succeed" or "internal_error"
    return udon_status
