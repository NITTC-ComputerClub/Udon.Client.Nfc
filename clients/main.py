import eel
from udon_modules import udon_card


if __name__ == "__main__":
    eel.init("web")
    eel.start("main.html")
    while True:
        udon_card.begin_attendance_reading()