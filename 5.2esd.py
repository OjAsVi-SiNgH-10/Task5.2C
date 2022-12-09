from tkinter import*            ## importing the Tkinter library 
import tkinter.font             ## importing FOnt from Tkinter library
from gpiozero import LED            
import RPi.GPIO                 ## importing GPIO library
RPi.GPIO.setwarnings(False)
RPi.GPIO.setmode(RPi.GPIO.BCM) 

## Initialising input pins for the three LEDs 
red_Led = LED (14)
green_Led = LED (15)
blue_Led = LED (18)

## GUI DEFINITIONS ##
win = Tk()                  ## To create interface with GUI toolkit
win.title("LED - GUI")      ## Set the name of the title 
myFont = tkinter.font. Font(family = 'Helvetica', size = 12, weight = "bold")       ## Choosing the font for the title
count = IntVar()

### EVENT FUNCTIONS ### 
def redledControl():
    if red_Led.is_lit:
        red_Led.off()
        redledButton["text"] = "Turn RED LED on"
    else:
        red_Led.on()
        redledButton["text"] = "Turn RED LED off"
        green_Led.off()
        greenledButton["text"] = "Turn GREEN LED on"
        blue_Led.off()
        blueledButton["text"] = "Turn BLUE LED on"

def blueledControl():
    if blue_Led.is_lit:
        blue_Led.off()
        blueledButton["text"] = "Turn BLUE LED on"
    else:
        blue_Led.on()
        blueledButton["text"] = "Turn BLUE LED off"
        red_Led.off()
        redledButton["text"] = "Turn RED LED on"
        green_Led.off()
        greenledButton["text"] = "Turn GREEN LED on"

def greenledControl():
    if green_Led.is_lit:
        green_Led.off()
        greenledButton["text"] = "Turn GREEN LED on"
    else:
        green_Led.on()
        greenledButton["text"] = "Turn GREEN LED off"
        red_Led.off()
        redledButton["text"] = "Turn RED LED on"
        blue_Led.off()
        blueledButton["text"] = "Turn BLUE LED on"

def close():
    RPi.GPIO.cleanup()
    win.destroy()

### WIDGETS ###
redledButton = Button (win, text = 'Turn RED LED On', font = myFont, command = redledControl, bg = 'red', height = 1, width = 24)
redledButton.grid (row=0, column=1)

greenledButton = Button (win, text = 'Turn GREEN LED On', font = myFont, command = greenledControl, bg = 'green', height = 1, width = 24)
greenledButton.grid (row=1, column=1)

blueledButton = Button (win, text = 'Turn BLUE LED On', font = myFont, command = blueledControl, bg = 'blue', height = 1, width = 24)
blueledButton.grid (row=2, column=1)

exitButton = Button (win, text = 'Exit', font = myFont, command = close, bg = 'green', height = 1, width = 6)
exitButton.grid (row=3, column=1)

win.protocol("WM_DELETE_WINDOW", close) # exit cleanly
win.mainloop()                          # Loop forever
