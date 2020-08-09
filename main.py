import nfc
import binascii
import os
import json
import urllib.request
import urllib.parse


class Reader:
    def read(self):
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
        tagID = str(binascii.hexlify(tag._nfcid))
        print("IDm : {IDm}".format(IDm=tagID))
        self.tagIDbeforeConvert = tagID
        return True


class CardReader(Reader):
    def on_connect(self, tag):
        super().on_connect(tag)
        self.convert_IDm()
        self.recordMemberID()
        return True

    def convert_IDm(self):
        IDbeforeConvert = self.tagIDbeforeConvert
        convertedID = ""
        # convert from IDm to memberID
        self.memberID = convertedID
        return True
        """
        on error 
        [Invalid NFC]
        then
        Recorder.record(memberID)
        in on_connect
        """

    def recordMemberID(self):
        UdonURL = ""  # Udon API Server
        values = {
            "client": os.environ["Client_ID"],  # TODO set client id
            "member": self.memberID
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
        cr.read()
