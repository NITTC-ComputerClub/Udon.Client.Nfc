import nfc
import binascii
import os
import json
import urllib.request
import urllib.parse


class CardReader:
    def read_tag(self):
        clf = nfc.ContactlessFrontend('usb')
        print("Touch me")
        clf.connect(rdwr={'on-connect': self.on_connect})
        clf.close()

    def on_connect(self, tag):
        tagID = str(binascii.hexlify(tag._nfcid))[2:-1]
        print("IDm : {IDm}".format(IDm=tagID)
              )
        return True

    def convert_IDm(self, IDm):
        # convert from IDm to memberID
        return True

    # should import urlib.parse and urlib.request
    def record(self, memberID):
        UdonURL = ""  # Udon API Server
        values = {
            "client": os.environ["Client_ID"],  # TODO set client id
            "member": memberID
        }
        data = urllib.parse.urlencode(values)
        req = urllib.request.Request(UdonURL, data)
        with urllib.request.urlopen(UdonURL, data=req) as res:
            print(res.read)  # TODO read Status Code and output something


if __name__ == '__main__':
    print("System Started")
    while True:
        cr = CardReader()
        cr.read_tag()
