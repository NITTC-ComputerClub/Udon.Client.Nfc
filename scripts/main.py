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
            clf = nfc.ContactlessFrontend("usb")
            server.send_message_to_all("listening")  # Listening Tag...
            print("Touch me")
            clf.connect(rdwr={"on-connect": self.on_connect})
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

    
    def getToken(self):
        with open("database/token.json","r") as j:
            lastToken = json.load(j)
        if(time.time()>lastToken.expirationDate): #expired
            data={
                "clientId":,    #os.environ("")
                "clientSecret":
            }
            r=requests.post("https://https://udon.nittc-programming.club/clients/token",
            json.dumps(data),
            headers={
                "Content-Type": "application/json"
            })
            token=r.json().token
            exDate= "" #encode token and set expirationDate
            data={
                "token":token,
                "expirationDate":
            }
            with open ("database/token.json","w") as jw:
                json.dump(data,jw)
            return token
        else:   #return last token
            return lastToken.token

    def recordMemberID(self):
        token=self.getToken()
        data = {
            "memberId":self.memberID
        }
        r = requests.post("https://https://udon.nittc-programming.club/record",
            json.dumps(data),
            headers={
                    "Content-Type": "application/json"
                    "Authorization":"Bearer {token}".format(token=token)
            })
        if(r.statusCode==200):
            return True
        else:
            print(r.json())
            return False


if __name__ == "__main__":
    recorder = Recorder()
    server = WebsocketServer(9999, host="localhost")
    server.set_fn_message_received(recorder.read)
    server.run_forever()
