import eel
from udon_modules import udon_card
from udon_modules import udon_db

if __name__ == "__main__":
    @eel.expose
    def read_idm_wrapper():                               #These functions are used only from JavaScript
        idm = udon_card.read_idm()
        return idm

    @eel.expose
    def registrar_wrapper(member_name,idm):
        status = udon_db.register_newcard(member_name,idm)
        return status
    
    
    eel.init("web")
    eel.start("registrar.html")
    