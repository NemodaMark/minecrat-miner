import tkinter as tk
from tkinter import ttk
import pyautogui
import subprocess
import time
from tkinter import messagebox

pickaxe_types = [
    ['Wooden', '1.15'],
    ['Stone', '0.75'],
    ['Iron', '0.5'],
    ['Diamond', '0.4'],
    ['Netherite', '0.35'],
    ['Gold', '0.25'],
]

selected_pickaxe_time = None  # Global variable to hold the selected pickaxe time

def on_select(event):
    global selected_pickaxe_time
    selected_option = dropdown.get()
    for pickaxe in pickaxe_types:
        if pickaxe[0] in selected_option:
            selected_pickaxe_time = float(pickaxe[1])
            break
    print("Selected option:", selected_option)

def start_mine(pickaxe_time):
        # Start Minecraft
    minecraft_window = pyautogui.getWindowsWithTitle('Minecraft')[0]
    if minecraft_window:
        minecraft_window.activate()
        subprocess.Popen(["python", "mine.py", str(pickaxe_time)])
        
    else:
        print("Minecraft window not found.")

def start_minecraft():
    global selected_pickaxe_time
    response = messagebox.askokcancel("Alert", "You can stop the code by holding enter! understood?")
    if response == True:
        start_mine(selected_pickaxe_time)

def on_ok_button_click():
    start_minecraft()

# Create the main window
root = tk.Tk()
root.title("Question")

# Set window size and position
window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a frame with margins
frame = ttk.Frame(root, padding=16)
frame.pack(fill=tk.BOTH, expand=True)

# Create a label
label = ttk.Label(frame, text="Please select a pickaxe:")
label.pack(pady=10)

# Create a dropdown/select widget
options = [f"{pickaxe[0]} pickaxe" for pickaxe in pickaxe_types]
dropdown = ttk.Combobox(frame, values=options, state="readonly")
dropdown.current(0)  # Set the default selection
dropdown.bind("<<ComboboxSelected>>", on_select)  # Bind the event handler
dropdown.pack(pady=5)

# Create an OK button
ok_button = ttk.Button(frame, text="OK", command=on_ok_button_click)
ok_button.pack(pady=10)

# Run the application
root.mainloop()
