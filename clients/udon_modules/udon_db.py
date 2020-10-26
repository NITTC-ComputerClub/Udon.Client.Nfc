import json
def tomember(IDm):
        f = open("../database/members.json", "r")
        members_data = json.load(f)
        f.close()
        for member in members_data:
            for i in member["IDm"]:
                if(i == IDm):
                    print(member["name"])
                    return member["id"]
        return ""  # if does not much any tag

def register_newcard(member_name,new_card):
    try:
        members_data=""
        with open("../database/members.json", "r+") as u:
            members_data = json.load(u)
        
        for member in members_data:  # check this card does not link any users yet
            for user_card in member["IDm"]:
                if(user_card == new_card):
                    return "already_used"

        for member in members_data:  # check this card does not link any users yet
            if(member["name"]==member_name):
                member["IDm"].append(idm)
        
        with open("../database/members.json", "w+") as udon_users_data:
            json.dump(members_data, udon_users_data)
        return "register_succeed"

    except Exception as e:
        print(e)
        return "internal_error"