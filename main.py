import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import base64

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def text_kaydet():
    baslik = baslik_entry.get()
    mesaj = note_text.get("1.0", END)
    sifre = parola_entry.get()

    if len(baslik) == 0 or len(mesaj) == 0 or len(sifre) == 0:
        messagebox.showwarning(title="Hata!", message="Lütfen bütün boşlukları doldurun.!")
    else:
        #şifreyiaç
        text_sifrele = encode(sifre,mesaj)
        try:
            with open("Şifrelinotlar.txt", "a") as data_file:
                data_file.write(f"\n{baslik}\n{text_sifrele}")
        except FileNotFoundError:
            with open("Şifrelinotlar.txt", "w") as data_file:
                data_file.write(f"\n{baslik}\n{text_sifrele}")
        finally:
            baslik_entry.delete(0, END)
            note_text.delete("1.0", END)
            parola_entry.delete(0, END)
def text_ac():
    text_sifresiniac = note_text.get("1.0", END)
    parola_sifresiniac = parola_entry.get()

    if len(text_sifresiniac) == 0 or len(parola_sifresiniac) == 0:
        messagebox.showwarning(title="Hata!", message="Lütfen bütün boşlukları doldurun.!")
    else:
        try:
            cozulmus_mesaj = decode(parola_sifresiniac, text_sifresiniac)
            note_text.delete("1.0", END)
            note_text.insert("1.0", cozulmus_mesaj)
        except:
            messagebox.showwarning(title="Hata!", message="Lütfen şifrelenmiş mesajı girin.!")

#Sayfa
window = Tk()
window.title("Şifreli Notepad")
window.minsize(height=700, width=400)
window.maxsize(height=700, width=400)
window.config(padx=10, pady=10)

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
parola_entry = tkinter.Entry(width=40, show="*")
parola_entry.pack()

#KaydetVeŞifreleButonu
save_button = tkinter.Button(text="Kaydet Ve Şifrele", command=text_kaydet)
save_button.pack()

#ŞifreyiAçButonu
decrypt_button = tkinter.Button(text="Şifreyi Aç", command=text_ac)
decrypt_button.pack()

window.mainloop()