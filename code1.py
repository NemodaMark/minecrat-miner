import pyautogui
import subprocess
import time
import random
import keyboard
import sys

# Retrieve the pickaxe time argument passed from code2.py
pickaxe_time = float(sys.argv[1])

def stop_code():
    # Check if Enter key is pressed
    if keyboard.is_pressed('enter'):
        print("\nEnter key pressed. Stopping...")
        pyautogui.press('esc')
        question = pyautogui.getWindowsWithTitle('Question')[0]
        return True, question.activate()
    return False

def mining():
    global pickaxe_time
    # Find the Minecraft window
    minecraft_window = pyautogui.getWindowsWithTitle('Minecraft')[0]
    if minecraft_window:
        minecraft_window.activate()
        time.sleep(1.5)
        pyautogui.press('esc')
        
        while True:
            time.sleep(0.35)  # Adjust as needed
            # Hold left click for 0.7 seconds
            pyautogui.mouseDown(button='left')
            time.sleep(pickaxe_time + 0.15)  # Adjust as needed
            pyautogui.mouseUp(button='left')

            # Wait before generating a random number
            time.sleep(1)  # Adjust as needed

            # Generate a random number and press it
            i = random.randint(1, 9)
            pyautogui.press(str(i))

            # Check if Enter key is pressed
            if stop_code():
                break
    else:
        print("Minecraft window not found.")

mining()
