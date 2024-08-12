def on_button_pressed_a():
    global hasBeenSelected, logicGateSelected
    if hasBeenSelected == 0:
        hasBeenSelected = 1
        basic.show_string("AND")
        logicGateSelected = "AND"
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global hasBeenSelected, logicGateSelected
    if hasBeenSelected == 0:
        hasBeenSelected = 1
        basic.show_string("NOT")
        logicGateSelected = "NOT"
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global hasBeenSelected, logicGateSelected
    if hasBeenSelected == 0:
        hasBeenSelected = 1
        basic.show_string("OR")
        logicGateSelected = "OR"
input.on_button_pressed(Button.B, on_button_pressed_b)

def output(logicGate: str):
    if logicGate == "AND":
        if input.button_is_pressed(Button.AB):
            return 1
        elif input.button_is_pressed(Button.B):
            return 0
        elif input.button_is_pressed(Button.A):
            return 0
    elif logicGate == "OR":
        if input.button_is_pressed(Button.A):
            return 1
        elif input.button_is_pressed(Button.B):
            return 1
        elif input.button_is_pressed(Button.AB):
            return 1
        else:
            return 0
    elif logicGate == "NOT":
        if input.button_is_pressed(Button.A):
            return 0
        elif input.button_is_pressed(Button.B):
            return 0
        elif input.button_is_pressed(Button.AB):
            return 0
        else:
            return 1
    else:
        return -1

def on_logo_pressed():
    global hasBeenSelected, logicGateSelected
    hasBeenSelected = 0
    logicGateSelected = ""
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

logicGateSelected = ""
hasBeenSelected = 0
hasBeenSelected = 0
logicGateSelected = ""

def on_forever():
    while hasBeenSelected == 1 and logicGateSelected != "":
        serial.write_line("" + str((output(logicGateSelected))))
        while output(logicGateSelected) != -1:
            basic.show_number(output(logicGateSelected))
        basic.pause(100)
        basic.clear_screen()
basic.forever(on_forever)
