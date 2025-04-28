import pygame
import time
import tkinter as tk
import threading
import random

# Initialize pygame mixer
pygame.mixer.init()

# Load your Sparta Remix file
pygame.mixer.music.load("sparta_remix.mp3")

# Function to create a crazy error popup
def popup_error_hyper(message):
    def show():
        window = tk.Tk()
        window.title("ERROR!")
        w, h = 300, 100
        x = random.randint(0, window.winfo_screenwidth() - w)
        y = random.randint(0, window.winfo_screenheight() - h)
        window.geometry(f"{w}x{h}+{x}+{y}")
        
        # Random background color
        bg_color = random.choice(["red", "blue", "yellow", "magenta", "cyan", "lime", "orange"])
        window.configure(bg=bg_color)
        
        label = tk.Label(window, text=message, fg="white", bg=bg_color, font=("Arial", 16, "bold"))
        label.pack(expand=True)

        # Shaking effect
        def shake():
            for _ in range(10):
                try:
                    dx = random.randint(-10, 10)
                    dy = random.randint(-10, 10)
                    window.geometry(f"{w}x{h}+{x+dx}+{y+dy}")
                    time.sleep(0.05)
                except:
                    break

        threading.Thread(target=shake).start()

        # Auto-close after 2.5 seconds
        window.after(2500, window.destroy)
        window.mainloop()
        
    threading.Thread(target=show).start()

# Error messages
error_messages = [
    "CRITICAL FAILURE!",
    "MEMORY LEAK!",
    "ACCESS DENIED!",
    "HARDWARE MALFUNCTION!",
    "SOFTWARE CORRUPTION!",
    "STACK SMASH DETECTED!",
    "BOOTLOADER FAILURE!",
    "NO SIGNAL!",
    "VIRUS DETECTED!",
    "KERNEL PANIC!",
]

# Start playing the music
pygame.mixer.music.play()

# Beat timings in seconds (adjust for your remix version)
beat_times = [1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.2, 5.4, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11]

# Start syncing
start_time = time.time()

for beat in beat_times:
    # Wait until the beat moment
    while time.time() - start_time < beat:
        time.sleep(0.005)
    # Spawn 3-5 hyper popups per beat
    for _ in range(random.randint(3, 5)):
        popup_error_hyper(random.choice(error_messages))

# Keep program alive until music ends
while pygame.mixer.music.get_busy():
    time.sleep(1)

print("Absolute Chaos Over!")