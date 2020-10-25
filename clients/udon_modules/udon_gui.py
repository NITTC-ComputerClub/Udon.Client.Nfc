import eel
def init(target):
    eel.init("web")
    if(target=="main"):
        eel.start("main.html",block=False)
    else:
        eel.start("registrar.html",block=False)
def changeto(element_name):
    eel.changeDisplay(element_name)