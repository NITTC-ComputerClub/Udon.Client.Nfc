import eel
from udon_modules import udon_card

if __name__ == "__main__":
    @eel.expose
    def start_udon(member_id):                               #This function is used only from JavaScript
        status = udon_card.begin_register_reading(member) 
        return status

    eel.init("web")
    eel.start("registrar.html")
    