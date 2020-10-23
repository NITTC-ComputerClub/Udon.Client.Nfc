import json
import requests

def get_token():
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
            expiratoin_date= "" #encode token and set expirationDate
            data={
                "token":token,
                "expirationDate":
            }
            with open ("database/token.json","w") as jw:
                json.dump(data,jw)
            return token
        else:   #return last token
            return lastToken.token

def record_attendance(memberID):
    token = getToken()
    data = {
        "memberId":memberID
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