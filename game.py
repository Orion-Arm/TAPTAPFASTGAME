import tkinter as tk
from tkinter import messagebox
import time
GAME_TIME = 10

class TapTapFastGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tap Tap Fast")
        
        self.score = 0
        self.time_left = GAME_TIME
        
        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 24))
        self.score_label.pack(pady=10)
        
        self.button = tk.Button(root, text="Click Me!", command=self.click)
        self.button.pack(pady=20)
        
        self.timer_label = tk.Label(root, text=f"Time Left: {self.time_left}", font=("Arial", 18))
        self.timer_label.pack(pady=10)
        
        self.root.after(1000, self.update_timer) 
        
    def click(self):
        if self.time_left > 0:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        
    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time Left: {self.time_left}")
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()
    
    def end_game(self):
        self.button.config(state=tk.DISABLED)
        messagebox.showinfo("Game Over", f"Your score: {self.score}")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = TapTapFastGame(root)
    root.mainloop()
