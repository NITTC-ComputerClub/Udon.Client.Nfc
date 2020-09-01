import nfc
import binascii
import os
import json
import requests
import time
from websocket_server import WebsocketServer


class CardReader:
    def read(self, client, server, message):
        print(message)
        if(message == "client_ready"):
            clf = nfc.ContactlessFrontend('usb')
            server.send_message_to_all("listening")  # Listening Tag...
            print("Touch me")
            clf.connect(rdwr={'on-connect': self.on_connect})
            clf.close()
        else:
            server.send("other_error")

    def on_connect(self, tag):
        tagID = str(binascii.hexlify(tag._nfcid))
        print("IDm : {IDm}".format(IDm=tagID))
        self.tagIDbeforeConvert = tagID
        return True


class Recorder(CardReader):
    def on_connect(self, tag):
        super().on_connect(tag)
        if(self.convert_IDm()):
            # Sending to server...
            server.send_message_to_all("sending")
            if(self.recordMemberID()):
                # Record succeed!
                server.send_message_to_all("record_succeed")
            else:
                # Record Error
                server.send_message_to_all("other_error")
        else:
            # This tag does not much any member
            server.send_message_to_all("incorrect_tag")

        self.memberID = ""
        self.tagIDbeforeConvert = ""
        return True

    def convert_IDm(self):
        IDbeforeConvert = self.tagIDbeforeConvert
        f = open("database/members.json", "r")
        memberData = json.load(f)
        f.close()
        for member in memberData:
            for i in member["IDm"]:
                if(i == IDbeforeConvert):
                    self.memberID = member["id"]
                    print(member["name"])
                    return True
        return False  # if it does not much any tag
    
    def getToken(self):
        with open("token.json") as j:
            lastToken = json.load(j)
            if(time.time()>lastToken.expirationDate): #expired
                val = {
                    "ClientId":"",
                    "ClientToken":""
                }
                r=requests.post("",data=)
                return
            else:   #return last token
                return lastToken.token
    def recordMemberID(self):
        UdonURL = ""  # Udon API Server
        token=self.getToken()
        
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
    recorder = Recorder()
    server = WebsocketServer(9999, host="localhost")
    server.set_fn_message_received(recorder.read)
    server.run_forever()
