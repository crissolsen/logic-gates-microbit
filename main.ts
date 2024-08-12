let hasBeenSelected = 0
let logicGateSelected = ""
let result = 0
input.onButtonPressed(Button.A, function () {
    if (hasBeenSelected == 0) {
        hasBeenSelected = 1
        basic.showString("AND")
        logicGateSelected = "AND"
    }
})
input.onButtonPressed(Button.AB, function () {
    if (hasBeenSelected == 0) {
        hasBeenSelected = 1
        basic.showString("NOT")
        logicGateSelected = "NOT"
    }
})
input.onButtonPressed(Button.B, function () {
    if (hasBeenSelected == 0) {
        hasBeenSelected = 1
        basic.showString("OR")
        logicGateSelected = "OR"
    }
})
function output (logicGate: string) {
    if (logicGate == "AND") {
        if (input.buttonIsPressed(Button.AB)) {
            return 1
        } else {
            return 0
        }
    } else if (logicGate == "OR") {
        if (input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B) || input.buttonIsPressed(Button.AB)) {
            return 1
        } else {
            return 0
        }
    } else if (logicGate == "NOT") {
        if (input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B) || input.buttonIsPressed(Button.AB)) {
            return 0
        } else {
            return 1
        }
    } else {
        return -1
    }
}
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    hasBeenSelected = 0
    logicGateSelected = ""
})
basic.forever(function () {
    while (hasBeenSelected == 1 && logicGateSelected != "") {
        result = output(logicGateSelected)
        while (result != -1) {
            basic.showNumber(result)
            result = output(logicGateSelected)
        }
        basic.clearScreen()
        basic.pause(100)
    }
})
