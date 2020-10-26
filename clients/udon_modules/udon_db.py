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
    with open("../database/members.json", "r") as f:
            members_data = json.load(f)
            for element in memberJson:  # check this card does not link any users yet
                for user_card in element["IDm"]:
                    if(user_card == new_card):
                        return "already_used"

            members_data[member_name]["IDm"].append(new_card)
            
            try:
                with open("database/members.json", "w") as w:
                    json.dump(members_data, w)
                return "register_succeed"
            except Exception as e:
                print(e)
                return "internal_error"