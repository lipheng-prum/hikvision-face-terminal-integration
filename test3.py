from pynput.mouse import Controller
import keyboard
import time

# Create an instance of the Controller class
mouse = Controller()
running = False
def scroll_up():
    mouse.scroll(0, 1)  # Scroll up
    print("scroll up")

def scroll_down():
    mouse.scroll(0, -1)  # Scroll down

def scrolling_loop():
    interval = 40
    while not keyboard.is_pressed('esc'):
        print(running)
        scroll_up()
        print("Scrolled Up")
        time.sleep(interval)

        scroll_down()
        print("Scrolled Down")
        time.sleep(interval)

print("Press 'P' to start scrolling and 'ESC' to exit.")

while True:
    if keyboard.is_pressed('p') and not running:
        print("Starting scrolling...")
        running = True
        scrolling_loop()
        running = False
        print("Scrolling stopped. Press 'P' to start again or 'ESC' to exit.")

    if keyboard.is_pressed('esc'):
        print("Exiting...")
        break
    time.sleep(0.1)  # Prevent high CPU usage
