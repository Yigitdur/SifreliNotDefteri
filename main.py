import tkinter
from tkinter import *
from PIL import ImageTk, Image

#Sayfa
window = Tk()
window.title("Şifreli Notepad")
window.minsize(height=700, width=400)
window.maxsize(height=700, width=400)
window.config(padx=10, pady=10)

def save_text():
    filename = "Şifreleri-Notlar.txt"
    with open(filename, "a") as f:
        f.write(note_text.get("1.0", END))

#Fotoğraf
image = Image.open("Cok_gizli.png").resize((100, 100))
image = ImageTk.PhotoImage(image)
image_label = Label(window, image=image, pady=50, padx=20)
image_label.pack()

#BaşlıkLabel
entry_label = tkinter.Label(text="Başlığınızı buraya giriniz.", font="Arial")
entry_label.pack()
#BaşlıkEntry
baslik_entry = tkinter.Entry(width=35)
baslik_entry.focus()
baslik_entry.pack()

#NoteLabel
note_label = tkinter.Label(text="Notunuzu buraya giriniz.", font="Arial")
note_label.pack()
#NoteEntry
note_text = tkinter.Text(width=35, height=25)
note_text.pack()

#ParolaLabel
parola_label = tkinter.Label(text="Parolanızı buraya giriniz.", font="Arial")
parola_label.pack()
#ParolaEntry
parola_entry = tkinter.Entry(width=40)
parola_entry.pack()

#KaydetVeŞifreleButonu
save_button = tkinter.Button(text="Kaydet Ve Şifrele", command=save_text)
save_button.pack()

#ŞifreyiAçButonu
decrypt_button = tkinter.Button(text="Şifreyi Aç")
decrypt_button.pack()



window.mainloop()