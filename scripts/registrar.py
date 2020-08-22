import json
import nfc
import binascii
import os
from main import CardReader
from websocket_server import WebsocketServer
import collections as cl


class CardRegistrar(CardReader):
    def read(self, client, server, message):
        print(message)
        if(message[:7] == "member:"):
            self.memberName = message[7:]
            print(message[7:])
        elif (message == "client_ready"):
            pass
        else:
            server.send_message_to_all("other_error")
            return True
        clf = nfc.ContactlessFrontend('usb')
        server.send_message_to_all("listening")  # Listening Tag...
        print("Touch me")
        clf.connect(rdwr={'on-connect': self.on_connect})
        clf.close()

    def __init__(self):
        self.firstTouch = True

    def on_connect(self, tag):
        if(self.firstTouch):
            super().on_connect(tag)
            self.firstTouch = False
            server.send_message_to_all("touch_again")
        else:
            print(self.tagIDbeforeConvert)
            print(str(binascii.hexlify(tag._nfcid)))
            if(self.tagIDbeforeConvert == str(binascii.hexlify(tag._nfcid))):
                server.send_message_to_all("registering")
                self.registNewTag()
            else:
                server.send_message_to_all("register_error")
            self.firstTouch = True
        return True

    def registNewTag(self):
        with open("database/members.json", "r") as f:
            memberJson = json.load(f)
            newTagID = self.tagIDbeforeConvert
            for element in memberJson:  # check this card does not link any users yet
                for i in element["IDm"]:
                    if(i == newTagID):
                        server.send_message_to_all("register_error")
                        break
            if(hasattr(self, "memberName") and self.memberName != ""):
                try:
                    for i in memberJson:
                        if(i["name"] == self.memberName):
                            tmp = i["IDm"]
                            tmp.append(newTagID)
                            i["IDm"] = tmp
                            print(tmp)
                            break
                    with open("database/members.json", "w") as fw:
                        json.dump(memberJson, fw)
                    server.send_message_to_all("register_succeed")
                except Exception as e:
                    print(e)
                    server.send_message_to_all("register_error")

            else:
                print("Unknown Error")
                server.send_message_to_all("register_error")


def sendMemberList(client, server):
    memberList = "member-list"
    with open("database/members.json") as f:
        memberJson = json.load(f)
        for i in memberJson:
            memberList += i["name"]+","
    server.send_message_to_all(memberList)


if __name__ == "__main__":
    registrar = CardRegistrar()
    server = WebsocketServer(9999, host="localhost")
    server.set_fn_new_client(sendMemberList)
    server.set_fn_message_received(registrar.read)
    server.run_forever()
