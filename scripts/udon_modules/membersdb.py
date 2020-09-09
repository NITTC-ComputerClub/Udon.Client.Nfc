def to_member_id(nfc_id):
        with  open("database/members.json", "r") as md:
            members_data = json.load(md)
            matched_member=""
            for member in members_data:
                for member_nfc_id in member["IDm"]:
                    if(member_nfc_id == nfc_id):
                        matched_member=member["id"]
                        break
            return matched_member

def register_nfcid(member_name,nfc_id):