import tkinter as tk
import threading
import time
import random

class UltraKillParry:
    def __init__(self, root):
        self.root = root
        self.root.title("UltraKill Parry Simulator")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg="black")

        self.canvas = tk.Canvas(root, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.counter_text = self.canvas.create_text(0, 0, text="", font=("DS-Digital", 120, "bold"), fill="lime")
        self.message_text = self.canvas.create_text(0, 0, text="", font=("Impact", 48, "bold"), fill="red")

        self.start_button = tk.Button(root, text="💥 Lancer la Nuke 💥", font=("Helvetica", 24), bg="#cc0000", fg="white", command=self.start_countdown)
        self.start_button.pack(pady=15)

        self.root.bind("<space>", self.try_parry)
        self.root.bind("<Escape>", self.exit_fullscreen)

        self.parry_window = 0.6  # secondes durant lesquelles on peut parry
        self.parry_allowed = False
        self.exploded = False
        self.countdown_thread = None

        self.counter_pos = (self.root.winfo_screenwidth()//2, self.root.winfo_screenheight()//2)
        self.message_pos = (self.counter_pos[0], self.counter_pos[1] + 150)

        self.root.after(100, self.position_texts)

    def position_texts(self):
        self.canvas.coords(self.counter_text, self.counter_pos)
        self.canvas.coords(self.message_text, self.message_pos)

    def exit_fullscreen(self, event):
        self.root.attributes('-fullscreen', False)

    def start_countdown(self):
        if self.countdown_thread and self.countdown_thread.is_alive():
            return
        self.exploded = False
        self.parry_allowed = False
        self.start_button.config(state="disabled")
        self.countdown_thread = threading.Thread(target=self.countdown)
        self.countdown_thread.start()

    def countdown(self):
        total_time = 5.0
        update_interval = 0.05
        start_time = time.time()
        while True:
            elapsed = time.time() - start_time
            remaining = max(0, total_time - elapsed)
            self.update_counter(remaining)
            if remaining <= self.parry_window and not self.parry_allowed:
                self.parry_allowed = True
                self.flash_parry_message()
            if remaining <= 0:
                if not self.exploded:
                    self.exploded = True
                    self.parry_allowed = False
                    self.explode()
                break
            time.sleep(update_interval)

    def update_counter(self, remaining):
        txt = f"{remaining:.1f}"
        # Couleur qui change selon le temps (vert → jaune → rouge)
        if remaining > 2.5:
            color = "lime"
        elif remaining > 1.0:
            color = "yellow"
        else:
            # clignotement rouge
            color = "red" if int(time.time()*5) % 2 == 0 else "darkred"
        self.canvas.itemconfig(self.counter_text, text=txt, fill=color)
        self.root.update()

    def flash_parry_message(self):
        def flash_loop():
            while self.parry_allowed and not self.exploded:
                color = "red" if int(time.time()*5) % 2 == 0 else "darkred"
                self.canvas.itemconfig(self.message_text, text="⚔️ PARRY NOW! ⚔️", fill=color)
                self.root.update()
                time.sleep(0.3)
            self.canvas.itemconfig(self.message_text, text="")
            self.root.update()
        threading.Thread(target=flash_loop).start()

    def try_parry(self, event):
        if self.parry_allowed and not self.exploded:
            self.parry_allowed = False
            self.exploded = True
            self.message_text = self.canvas.create_text(self.counter_pos[0], self.counter_pos[1] + 150, text="🛡️ PARRY RÉUSSI ! 🛡️", font=("Impact", 48, "bold"), fill="lime")
            self.canvas.itemconfig(self.counter_text, text="")
            self.root.update()
            self.start_button.config(state="normal")
        elif not self.exploded:
            self.message_text = self.canvas.create_text(self.counter_pos[0], self.counter_pos[1] + 150, text="⏰ Trop tôt ou trop tard...", font=("Impact", 36, "bold"), fill="orange")
            self.root.update()

    def explode(self):
        self.canvas.delete("all")
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        cx, cy = w // 2, h // 2

        # Clignotement
        for _ in range(6):
            self.canvas.configure(bg=random.choice(["white", "#ff3300", "yellow"]))
            self.root.update()
            time.sleep(0.07)
        self.canvas.configure(bg="black")

        # Explosion cercles
        for r in range(50, max(w, h), 20):
            color = f"#ff{random.randint(50, 150):02x}00"
            self.canvas.create_oval(cx - r, cy - r, cx + r, cy + r, outline=color, width=3)
            self.root.update()
            time.sleep(0.03)

        # Particules
        particules = []
        for _ in range(150):
            angle = random.uniform(0, 2 * 3.1415)
            speed = random.uniform(3, 6)
            x = cx
            y = cy
            dx = math.cos(angle) * speed
            dy = math.sin(angle) * speed
            size = random.randint(3, 7)
            color = random.choice(["#ff6600", "#ffcc00", "#ffaa00", "#ff3300"])
            idp = self.canvas.create_oval(x, y, x + size, y + size, fill=color, outline="")
            particules.append([idp, x, y, dx, dy, size])

        for _ in range(50):
            for p in particules:
                idp, x, y, dx, dy, size = p
                x += dx
                y += dy
                dy += 0.3
                self.canvas.move(idp, dx, dy)
                p[1], p[2] = x, y
                p[3], p[4] = dx, dy
            self.root.update()
            time.sleep(0.03)

        # Texte final
        for i in range(15):
            taille = 48 + 5 * math.sin(i * 0.5)
            self.canvas.delete("texte_final")
            self.canvas.create_text(cx, cy, text="💥 KABOOM 💥", font=("Impact", int(taille)), fill="#ff3300", tag="texte_final")
            self.root.update()
            time.sleep(0.1)

        self.start_button.config(state="normal")

if __name__ == "__main__":
    import math
    root = tk.Tk()
    app = UltraKillParry(root)
    root.mainloop()
