import tkinter as tk
from tkinter import messagebox


def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)


def handle_encrypt():
    text = entry_text.get()
    shift = int(entry_shift.get())
    encrypted_text = encrypt(text, shift)
    result_var.set("Hasil Enkripsi: " + encrypted_text)


def handle_decrypt():
    text = entry_text.get()
    shift = int(entry_shift.get())
    decrypted_text = decrypt(text, shift)
    result_var.set("Hasil Dekripsi: " + decrypted_text)


window = tk.Tk()
window.title("Caesar Cipher Encryption & Decryption")
window.geometry("1080x720")
window.title("Caesar Cipher GUI Tugas ")
window.configure(bg="#073763")


title_label = tk.Label(window, text="Caesar Cipher ", font=("bold", 45, "bold"), fg="#edf2f4", bg="#000000")
title_label.pack(pady=80)


tk.Label(window, text="Masukkan teks asli :", font=("Helvetica", 20), fg="#edf2f4", bg="#000000").pack(padx=50)
entry_text = tk.Entry(window, width=40, font=("Helvetica", 20))
entry_text.pack(pady=5)


tk.Label(window, text="Masukkan Nilai Pergeseran 1 -25  :", font=("Helvetica", 20), fg="#edf2f4", bg="#000000").pack(pady=5)
entry_shift = tk.Entry(window, width=40, font=("Helvetica", 20))
entry_shift.pack(pady=5)


frame_buttons = tk.Frame(window, bg="#073763")
frame_buttons.pack(pady=15)

button_encrypt = tk.Button(frame_buttons, text="Enkripsi", font=("Helvetica", 10, "bold"), width=20,height=2, bg="#000000", fg="#edf2f4", command=handle_encrypt)
button_encrypt.pack(side=tk.LEFT, padx=60)

button_decrypt = tk.Button(frame_buttons, text="Dekripsi", font=("Helvetica", 10, "bold"), width=20,height=2, bg="#000000", fg="#edf2f4", command=handle_decrypt)
button_decrypt.pack(side=tk.RIGHT, padx=60)


tk.Label(window, text="Hasil:", font=("Helvetica", 20), fg="#edf2f4", bg="#000000").pack(pady=5)
result_var = tk.StringVar()
label_result = tk.Label(window, textvariable=result_var, fg="#9FCA58", bg="#000000", font=("Helvetica", 20, "bold"))
label_result.pack(pady=5)


window.mainloop()
