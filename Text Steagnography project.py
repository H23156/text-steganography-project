import tkinter as tk
from tkinter import messagebox

# Zero Width Characters
ZERO = "\u200b"   # Binary 0
ONE = "\u200c"    # Binary 1
END = "\u200d"    # End Marker


# Hide Secret Message
def hide_message():

    cover = cover_text.get("1.0", tk.END).strip()
    secret = secret_text.get("1.0", tk.END).strip()

    if cover == "" or secret == "":
        messagebox.showwarning("Warning", "Enter Cover Text and Secret Message")
        return

    # Secret message -> Binary
    binary = ""

    for ch in secret:
        binary += format(ord(ch), "08b")

    # Binary -> Zero Width Characters
    hidden = ""

    for bit in binary:
        if bit == "0":
            hidden += ZERO
        else:
            hidden += ONE

    hidden += END

    final_text.delete("1.0", tk.END)
    final_text.insert(tk.END, cover + hidden)

    messagebox.showinfo("Success", "Message Hidden Successfully")


# Extract Secret Message
def extract_message():

    text = final_text.get("1.0", tk.END)

    binary = ""

    for ch in text:

        if ch == ZERO:
            binary += "0"

        elif ch == ONE:
            binary += "1"

        elif ch == END:
            break

    secret = ""

    for i in range(0, len(binary), 8):

        byte = binary[i:i+8]

        if len(byte) == 8:
            secret += chr(int(byte, 2))

    extracted_text.delete("1.0", tk.END)
    extracted_text.insert(tk.END, secret)


# Clear All
def clear_all():

    cover_text.delete("1.0", tk.END)
    secret_text.delete("1.0", tk.END)
    final_text.delete("1.0", tk.END)
    extracted_text.delete("1.0", tk.END)


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Text Steganography")
root.geometry("1000x700")

tk.Label(root, text="Cover Text", font=("Arial", 12, "bold")).pack()

cover_text = tk.Text(
    root,
    height=5,
    width=60,
    font=("Arial", 12),
    bg="#F5F5F5",      # Background color
    fg="black",          # Text color
    bd=3,                # Border width
    relief="groove",     # Border style
    padx=10,             # Left/Right padding
    pady=10,             #top/Bottom Padding 
    )
cover_text.pack()

tk.Label(root, text="Secret Message", font=("Arial", 12, "bold")).pack()

secret_text = tk.Text(
    root, 
    height=5, 
    width=60,
    font=("Arial", 12),
    bg="#F5F5F5",      # Background color
    fg="black",        # Text color
    bd=3,              # Border width
    relief="groove",   # Border style
    padx=10,           # Left/Right padding
    pady=10,           #top/Bottom Padding 
)
secret_text.pack()

tk.Button(root, text="Hide Message", command=hide_message).pack(pady=5)

tk.Label(root, text="Hidden Text", font=("Arial", 12, "bold")).pack()

final_text = tk.Text(
    root,
    height=5,
    width=60,
    font=("Arial", 12),
    bg="#F5F5F5",      # Background color
    fg="black",          # Text color
    bd=3,                # Border width
    relief="groove",     # Border style
    padx=10,             # Left/Right padding
    pady=10,             #top/Bottom Padding 
)
final_text.pack()

tk.Button(root, text="Extract Message", command=extract_message).pack(pady=5)

tk.Label(root, text="Extracted Message", font=("Arial", 12, "bold")).pack()

extracted_text = tk.Text(
    root,
    height=5,
    width=60,
    font=("Arial", 12),
    bg="#F5F5F5",      # Background color
    fg="black",          # Text color
    bd=3,                # Border width
    relief="groove",     # Border style
    padx=10,             # Left/Right padding
    pady=10,             #top/Bottom Padding 
)
extracted_text.pack()

tk.Button(root, text="Clear", command=clear_all, bg="red", fg="white").pack(pady=10)

root.mainloop()