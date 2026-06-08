import tkinter as tk
import base64

def encode():
    msg = text1.get("1.0", tk.END)
    encoded = base64.b64encode(msg.encode()).decode()

    text2.delete("1.0", tk.END)
    text2.insert(tk.END, encoded)

def decode():
    msg = text2.get("1.0", tk.END)
    decoded = base64.b64decode(msg).decode()

    text3.delete("1.0", tk.END)
    text3.insert(tk.END, decoded)

root = tk.Tk()
root.title("Text Steganography")

tk.Label(root, text="Enter Message").pack()
text1 = tk.Text(root, height=4, width=40)
text1.pack()

tk.Button(root, text="Encode", command=encode).pack()

tk.Label(root, text="Encoded Text").pack()
text2 = tk.Text(root, height=4, width=40)
text2.pack()

tk.Button(root, text="Decode", command=decode).pack()

tk.Label(root, text="Decoded Text").pack()
text3 = tk.Text(root, height=4, width=40)
text3.pack()

root.mainloop()