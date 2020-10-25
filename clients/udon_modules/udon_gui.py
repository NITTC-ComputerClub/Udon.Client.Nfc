import eel

def init():
    eel.init("web")
    eel.start("main.html",block=False)
    while True:
        print("server still")
        eel.sleep(1.0)
def changeto(element_name):
    eel.changeDisplay(element_name)