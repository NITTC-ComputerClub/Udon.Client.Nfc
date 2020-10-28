import nfc
import binascii
import os
import json
from udon_modules import udon_db
from udon_modules import udon_api

clf = nfc.ContactlessFrontend("usb")

def read_idm():
    card= clf.connect(rdwr={'on-connect': lambda card: False})
    converted_id = binascii.hexlify(card._nfcid)
    return str(converted_id)


def begin_attendance(client,server,message):
    print("Listening")
    idm= read_idm()
    member_id = udon_db.tomember(idm)


    if(member_id == ""):
        server.send_message_to_all("unknown_card")
        return True
    else:
        server.send_message_to_all("sending")
        udon_status = udon_api.record_attendance(member_id) #"record_succeed" or "connection_error"
        server.send_message_to_all(udon_status)
       
    
    

    