import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import filedialog
from moviepy.editor import *
import os
import imageio
# import nussl
# import scaper
# import torch
# import git+https://github.com/source-separation/tutorial
# import common

class output_file():

    def __init__(self, video):
        self.video = video

class MainWindow():

    def __init__(self, mainWidget):
        self.main_frame = tk.Frame(mainWidget, width=1200, height=800, bg='#E61E4F' )
        self.main_frame.grid(row=0, column=0)
        self.out_of_main = False;
        image1 = Image.open("karaoke-logo.png")
        image2 = image1.resize((200, 200))
        self.test = ImageTk.PhotoImage(image2)
        self.music_path = None
        self.lyrics_path = None

        self.main_gui()

    def select_music_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("WAV Files", "*.wav")])
        print(file_path)
        self.music_path = file_path

    def select_lyrics_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        print(file_path)
        self.lyrics_path = file_path

    def main_gui(self):
        root.title('My Little Karaoke')
        root.configure(bg='#E61E4F')


        self.logo = ttk.Label(self.main_frame, image=self.test)

        self.logo.image = self.test
        self.logo.configure(background='#E61E4F')

        # Position image
        self.logo.grid(row=1, column=1)


        self.create_button = ttk.Button(self.main_frame, text='Utwórz nowe karaoke')
        self.create_button.grid(row=2, column=1)
        self.create_button.bind('<Button-1>', self.create_gui)

        self.archive_button = ttk.Button(self.main_frame, text='Otwórz archiwum')
        self.archive_button.grid(row=3, column=1)
        self.archive_button.bind('<Button-1>', self.archive_gui)

        self.gui_elements = [self.create_button, self.logo, self.archive_button]


    def generate_video(self):
        if self.music_path is not None and self.lyrics_path is not None:

            output = 'Gui/output/output.mp4'

            # Tworzenie sekwencji wideo
            video = ColorClip((640, 480), duration=5, col=(0, 0, 255))

            # Tworzenie sekwencji audio
            audio = AudioFileClip(self.music_path)

            # # Ładowanie tekstu z pliku
            # with open(self.lyrics_path, 'r') as file:
            #     lyrics_text = file.read()
            #
            # # Tworzenie obiektu TextClip z tekstem piosenki
            # lyrics_clip = TextClip(lyrics_text, fontsize=4, color=(255, 255, 255))
            #
            # # Dostosowanie długości klipu tekstowego do długości utworu muzycznego
            # lyrics_clip = lyrics_clip.set_duration(audio.duration)
            #
            # # Połączenie wideo, audio i napisów
            # final_clip = video.set_audio(audio).set_duration(audio.duration).set_pos(('center', 'bottom')).set_mask(lyrics_clip)

            # Połączenie wideo i audio
            final_clip = video.set_audio(audio)

            # Zapisz jako plik MP4
            final_clip.write_videofile(output, codec='libx264', audio_codec='aac', fps=30)

            print("Plik MP4 został wygenerowany.")
        else:
            print("Najpierw wybierz plik muzyczny i tekstowy!")

    def play_video(self):
        if self.music_path != None and self.lyrics_path != None:
            file_path = filedialog.askopenfilename(filetypes=[("Video File", "*.mp4")])
            if file_path:
                video = VideoFileClip(file_path)
                video.preview()
        else:
            print('Najpierw musisz wczytać ścieżkę dźwiękową oraz tekst')

    def create_gui(self, event):

        self.gui_elements_remove(self.gui_elements)
        self.out_of_main = True

        self.back_to_main_button = ttk.Button(self.main_frame, text='Cofnij')
        self.back_to_main_button.grid(row=0, column=0)
        self.back_to_main_button.bind('<Button-1>', self.back_to_main)

        # self.music_label = ttk.Label(self.main_frame, text="Choose a music file:")
        # self.music_label.grid(row=3, column=0)

        self.music_button = ttk.Button(self.main_frame, text='Wybierz plik muzyczny', command=self.select_music_file)
        self.music_button.grid(row=3, column=0)

        # self.text_label = ttk.Label(self.main_frame, text="Choose a text file:")
        # self.text_label.grid(row=4, column=0)

        self.lyrics_button = ttk.Button(self.main_frame, text='Wybierz plik tekstowy', command=self.select_lyrics_file)
        self.lyrics_button.grid(row=4, column=0)

        self.confirm_button = ttk.Button(self.main_frame, text='Zatwierdź', command=self.generate_video)
        self.confirm_button.grid(row=5, column=0)

        self.gui_elements = [self.back_to_main_button, self.music_button, self.lyrics_button, self.confirm_button]

    def archive_gui(self, event):

        self.gui_elements_remove(self.gui_elements)
        self.out_of_main = True



        self.archive_frame = tk.Frame(self.main_frame, width=800, height=500, bg="red")
        try:
            filenames = os.listdir("archive")
        except:
            label = tk.Label(self.archive_frame, text="Brak zapisanych plików")
            label.pack()

        dir_empty = True

        for file in filenames:
            if file.endswith('.mp4'):
                dir_empty = False
                button = tk.Button(self.archive_frame, text=file.title(), command=lambda : self.clip_select(file))
                button.pack()
        if dir_empty:
            label = tk.Label(self.archive_frame, text="Brak zapisanych plików")
            label.pack()



        self.archive_frame.grid(row=1,column=1)



        self.back_to_main_button = ttk.Button(self.main_frame, text='Cofnij')
        self.back_to_main_button.grid(row=0, column=0)
        self.back_to_main_button.bind('<Button-1>', self.back_to_main)

        self.gui_elements = [self.back_to_main_button,
                             self.archive_frame]

    def setings_gui(self, event):
        self.gui_elements_remove(self.gui_elements)

        root.title('Setings')

        self.main_label_1 = ttk.Label(self.main_frame, text='Object_1')
        self.main_label_1.grid(row=2, column=0)

        self.main_menu_button = ttk.Button(self.main_frame, text='Main menu')
        self.main_menu_button.grid(row=0, column=1)
        self.main_menu_button.bind('<Button-1>', self.back_to_main)

        self.out_of_main = 1

        self.gui_elements = [self.main_label_1,
                             self.main_menu_button]

    def back_to_main(self, event):
        if self.out_of_main == True:
            self.gui_elements_remove(self.gui_elements)
        else:
            pass
        self.main_gui()

    def gui_elements_remove(self, elements):
        for element in elements:
            element.destroy()


    def play_from_archive(self, path):
        pass

    def clip_select(self, file):

        self.select_clip_path = ("archive\\" + file.title())
        print(self.select_clip_path)



def main():
    global root

    root = tk.Tk()
    root.geometry('1000x600+100+100')
    root.title("My Little Karaoke")
    icon = tk.PhotoImage(file='karaoke-logo.png')
    root.iconphoto(False, icon)
    window = MainWindow(root)

    root.mainloop()

if __name__ == '__main__':
    main()