import eel
from udon_modules import udon_card
from udon_modules import udon_gui

if __name__ == "__main__":
    @eel.expose
    def callme():
        udon_card.begin_attendance_reading()
    eel.init("web")
    eel.start("main.html")
    