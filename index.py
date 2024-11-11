import tkinter as tk
import time

def on_triple_click(event):
    global click_count, last_click_time
    current_time = time.time()
    # Ako je prošlo manje od 0.5 sekundi od posljednjeg klika, smatramo to troduplim klikom
    if current_time - last_click_time < 0.5:
        click_count += 1
        print(f"Triple click detected! Total clicks: {click_count}")  # Ispisujemo u terminalu
        # Resetujemo vreme posljednjeg klika za sljedeći ciklus
        last_click_time = 0
    else:
        # Ako nije trodupli klik, ažuriramo vreme posljednjeg klika
        last_click_time = current_time

click_count = 0
last_click_time = 0

root = tk.Tk()
label = tk.Label(root, text="Click here")
label.pack()

# Dodajemo event handler za trodupli klik na label
label.bind('<Triple-Button-1>', on_triple_click)

root.mainloop()
