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
        """
        TODO make GUI
        like
        [Listening...]
        """
        clf.connect(rdwr={'on-connect': self.on_connect})
        clf.close()

    def on_connect(self, tag):
        tagID = str(binascii.hexlify(tag._nfcid))[2:-1]
        print("IDm : {IDm}".format(IDm=tagID))
        memberID = self.convert_IDm(tagID)
        #
        # TODO Record
        return True

    def convert_IDm(self, IDm):
        # convert from IDm to memberID
        return True
        """
        on error 
        [Invalid NFC]
        then
        Recorder.record(memberID)
        in on_connect
        """


class Recorder:
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
    """
        TODO make GUI
        like
        [Starting...]
        """
    print("System Started")
    # TODO GUI
    while True:
        cr = CardReader()
        cr.read_tag()
