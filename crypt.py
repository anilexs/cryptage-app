from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox

def encrypt_file(file_path, key):
    cipher_suite = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    cipher_suite = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

def process():
    file_path = destination_entry.get()
    key = key_entry.get().encode()
    
    if encryption_var.get():
        encrypt_file(file_path, key)
        messagebox.showinfo("Cryptage", "Le fichier a été crypté.")
    elif decryption_var.get():
        decrypt_file(file_path, key)
        messagebox.showinfo("Décryptage", "Le fichier a été décrypté.")
    else:
        messagebox.showwarning("Attention", "Sélectionnez une option de cryptage/décryptage.")

app = tk.Tk()
app.title("Application de Cryptage")

destination_label = tk.Label(app, text="Destination du fichier/dossier:")
destination_label.pack()
destination_entry = tk.Entry(app)
destination_entry.pack()

key_label = tk.Label(app, text="Clé:")
key_label.pack()
key_entry = tk.Entry(app)
key_entry.pack()

encryption_var = tk.BooleanVar()
encryption_checkbox = tk.Checkbutton(app, text="Cryptage", variable=encryption_var)
encryption_checkbox.pack()

decryption_var = tk.BooleanVar()
decryption_checkbox = tk.Checkbutton(app, text="Décryptage", variable=decryption_var)
decryption_checkbox.pack()

process_button = tk.Button(app, text="Traiter", command=process)
process_button.pack()

app.mainloop()

