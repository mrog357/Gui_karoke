import tkinter as tk
from tkVideoPlayer import TkinterVideo

root = tk.Tk()

videoplayer = TkinterVideo(master=root, scaled=True)
videoplayer.load(r"example.mp4")
videoplayer.pack(expand=True, fill="both")

videoplayer.play() # play the video

# Zmiana rozmiaru wyświetlania
videoplayer.configure(width=1200, height=700)

root.mainloop()
