import json
import requests
import os

def get_token():
        with open("../database/token.json","r") as j:
            last_token = json.load(j)
        if(time.time()>last_token.expirationDate): #on expired
            data={
                #"clientId":os.environ(""),
                #"clientSecret":
            }
            r=requests.post("https://https://udon.nittc-programming.club/clients/token",
                json.dumps(data),
                headers={
                    "Content-Type": "application/json"
                }
            )
            
            token=r.json().token
            expiratoin_date= "" #TODO encode token and set expirationDate
            data={
                "token":token,
                "expirationDate":expiratoin_date
            }
            with open ("database/token.json","w") as jw:
                json.dump(data,jw)
            return token
        else:  
            return last_token.token

def record_attendance(member_id):
    token = get_token()
    data = {
        "memberId":member_id
    }
    r = requests.post("https://https://udon.nittc-programming.club/record",
        json.dumps(data),
        headers={
                "Content-Type": "application/json"
                "Authorization Bearer {token}".format(token=token)
        })
    if(r.statusCode==200):
        return "record_succeed"
    else:
        print(r.json())
        return "internal_error"