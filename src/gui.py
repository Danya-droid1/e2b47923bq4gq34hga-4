
import tkinter as tk
from ripemd160 import ripemd160

def encrypt_text():
    text = input_box.get("1.0", tk.END).encode()
    result = ripemd160(text).hex()
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)

def decrypt_text():
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "RIPEMD160 is a hash, cannot be reversed")

root = tk.Tk()
root.title("RIPEMD160 Encryptor")

input_box = tk.Text(root, height=10, width=60)
input_box.pack()

encrypt_btn = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_btn.pack()

decrypt_btn = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_btn.pack()

output_box = tk.Text(root, height=10, width=60)
output_box.pack()

root.mainloop()
