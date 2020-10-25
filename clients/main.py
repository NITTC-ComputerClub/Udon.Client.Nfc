import eel
from udon_modules import udon_card
from udon_modules import udon_gui

if __name__ == "__main__":
    @eel.expose
    def start_udon():                               #This function is used only from JavaScript
        status = udon_card.begin_attendance_reading() 
        return status

    eel.init("web")
    eel.start("main.html")
    