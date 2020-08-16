import nfc
import binascii
import os
import json
import urllib.request
import urllib.parse
from websocket_server import WebsocketServer


class Reader:
    def read(self, client, server, message):
        print(message)
        if(message == "client_ready"):
            clf = nfc.ContactlessFrontend('usb')
            server.send_message_to_all("listening")  # Listening Tag...
            print("Touch me")
            """
                TODO make GUI
                like
                [Listening...]
                """
            clf.connect(rdwr={'on-connect': self.on_connect})
            clf.close()
        else:
            server.send("other_error")

    def on_connect(self, tag):
        tagID = str(binascii.hexlify(tag._nfcid))
        print("IDm : {IDm}".format(IDm=tagID))
        self.tagIDbeforeConvert = tagID
        return True


class CardReader(Reader):
    def on_connect(self, tag):
        super().on_connect(tag)

        if(self.convert_IDm()):
            # Sending to server...
            server.send_message_to_all("sending")
        else:
            # This tag does not much any member
            server.send_message_to_all("incorrect_tag")
        if(self.recordMemberID()):
            # Record succeed!
            server.send_message_to_all("record_succeed")
        else:
            # Record Error
            server.send_message_to_all("other_error")
        self.convert_IDm = ""
        self.memberID = ""
        self.tagIDbeforeConvert = ""
        return True

    def convert_IDm(self):
        IDbeforeConvert = self.tagIDbeforeConvert
        convertedID = ""
        # convert from IDm to memberID
        # if does not much any member return False
        self.memberID = convertedID
        return True

    def recordMemberID(self):
        UdonURL = ""  # Udon API Server
        """values = {
            "client": os.environ["Client_ID"],  # TODO set client id
            "member": self.memberID
        }
        data = urllib.parse.urlencode(values)
        req = urllib.request.Request(UdonURL, data)
        with urllib.request.urlopen(UdonURL, data=req) as res:
            print(res.read)  # TODO read Status Code and output something
            # If error occured,return False
        """
        return True


if __name__ == '__main__':
    cr = CardReader()
    server = WebsocketServer(9999, host="localhost")
    server.set_fn_message_received(cr.read)
    server.run_forever()
