
# importing time and threading
import time
import threading
from pynput.mouse import Button, Controller

# pynput.keyboard is used to watch events of 
# keyboard for start and stop of auto-clicker
from pynput.keyboard import Listener, KeyCode

#enable ANSI escape
import os
os.system("color")
  
# four variables are created to 
# control the auto-clicker
delay = 0.05
button = Button.left
start_stop_key = KeyCode(char='z')
stop_key = KeyCode(char='q')
change_interval = KeyCode(char='p')

# font color
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    

# threading.Thread is used 
# to control clicks
class ClickMouse(threading.Thread):
    
  # delay and button is passed in class 
  # to check execution of auto-clicker
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
  
    def start_clicking(self):
        self.running = True
  
    def stop_clicking(self):
        self.running = False
  
    def exit(self):
        self.stop_clicking()
        self.program_running = False
  
    # method to check and run loop until 
    # it is true another loop will check 
    # if it is set to true or not, 
    # for mouse click it set to button 
    # and delay.
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)
  
  
# instance of mouse controller is created
mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()
  
  
# on_press method takes 
# key as argument
def on_press(key):
    
  # start_stop_key will stop clicking 
  # if running flag is set to true
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
            print(f"{bcolors.FAIL}STOP CLICKING{bcolors.ENDC}")
        else:
            print(f"{bcolors.WARNING}START CLICKING{bcolors.ENDC}")
            click_thread.start_clicking()
              
    # here exit method is called and when 
    # key is pressed it terminates auto clicker
    elif key == stop_key:
        print(f"\n{bcolors.OKGREEN}>>>>Exiting<<<<{bcolors.ENDC}")
        click_thread.exit()
        listener.stop()

    elif key == change_interval:
        _change_interval()

def _change_interval():
    try:
        if click_thread.running:
            click_thread.stop_clicking()
            print(f"{bcolors.FAIL}STOP CLICKING{bcolors.ENDC}")
        click_thread.delay = float(input("\nPlease input the interval you want: "))
        print(f"Click Interval is now {click_thread.delay}s\n")
    except:
        print("\nPlease make sure you entered a number (e.g. 0.1)")
        _change_interval()

  
with Listener(on_press=on_press) as listener:
    print(f"{bcolors.OKGREEN}>>>>Ready<<<<{bcolors.ENDC}\n")
    listener.join()
