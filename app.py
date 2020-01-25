#!/usr/bin/env Python3

import tkinter as tk
from cipherclass import Decoder


def close_app():
    window.destroy()


def run_app():
    print('Running...')
    ciphertext = str(cipher_input_entry.get())
    COLS = int(col_input_entry.get())
    ROWS = int(row_input_entry.get())
    key = str(keys_input_entry.get())
    print(f"\nCiphertext = {ciphertext}")
    print(f"Trying {COLS} columns")
    print(f"Trying {ROWS} rows")
    print(f"Trying key = {key}")
    cipherlist = list(ciphertext.split())
    dc = Decoder(ROWS, COLS)
    dc.validate_col_row(cipherlist)
    key_int = dc.key_to_int(key)
    translation_matrix = dc.build_matrix(key_int, cipherlist)
    plaintext = dc.decrypt(translation_matrix)
    start_output["text"] = plaintext

    # print(f"\nplaintext = {plaintext}")


window = tk.Tk()  # or root=tk.Tk()
window.configure(bg='grey')

window.title("Desktop Decoder")
# window.geometry("600x600") - can set initial size or let it default (by frame size?)
window.resizable(width="True", height="True")  # doesn't allow resizing when False

# 4 frames on top of each other (inside window/root)
frame_header = tk.Frame(window, bd=2)
center_frame = tk.Frame(window, bd=20, bg='grey')
text_frame = tk.Frame(window)
bottom_frame = tk.Frame(window, pady=5, bg='grey')

# 3 additional frames that go inside center_frame
frame_main1 = tk.Frame(center_frame, borderwidth=0, relief='sunken', bg='grey')
frame_cipher = tk.Frame(center_frame, relief='sunken', bg='grey')
frame_keys = tk.Frame(center_frame, borderwidth=0, relief='sunken', bg='grey')

# 1 frame to go inside text_frame
output = tk.Frame(text_frame, borderwidth=3, relief='sunken')

# initially fill additional frames with prompt for user input
row_input = tk.Label(frame_main1, text="# of ROWS: ", bg='grey')
col_input = tk.Label(frame_main1, text="# of COLUMNS:", bg='grey')
cipher_input = tk.Label(frame_cipher, text="Input encoded message", bg='grey')
keys_input = tk.Label(frame_keys, text='Input keys', bg='grey')
start_output = tk.Label(output, text="Translation will appear here", width=50)

# the inputs should all be ints or strings
row_input1, col_input1, cipher_input1, keys_input1 = tk.IntVar(), tk.IntVar(), \
                                                     tk.StringVar(), tk.StringVar()

row_input_entry = tk.Entry(frame_main1, textvariable=row_input1, width=4, bd=3, highlightthickness=0)
col_input_entry = tk.Entry(frame_main1, textvariable=col_input1, width=4, bd=3, highlightthickness=0)
keys_input_entry = tk.Entry(frame_keys, textvariable=keys_input1, width=10, bd=3, highlightthickness=0)
cipher_input_entry = tk.Entry(frame_cipher, textvariable=cipher_input1, width=50, bd=3, highlightthickness=0)

# packing the items
frame_cipher.pack(fill='x', pady=5)
frame_main1.pack(fill='x', pady=5)
frame_keys.pack(fill='x', pady=5)
output.pack(fill='x', pady=0)

row_input.pack(side='left')
row_input_entry.pack(side='left', padx=3)

col_input_entry.pack(side='right')
col_input.pack(side='right', padx=3)

start_output.pack(side='right', padx=3)
cipher_input.pack(side='left')
cipher_input_entry.pack(side='left')

keys_input.pack(side='left')
keys_input_entry.pack(side='left', padx=0)

frame_header.grid(row=0, column=0)
center_frame.grid(row=1, column=0)
text_frame.grid(row=2, column=0)
bottom_frame.grid(row=3, column=0)

header = tk.Label(frame_header, text="Desktop Decoder Tool", bg='black', fg='white', height='3', width='50')
header.grid(row=0, column=0)

# rphoto = tk.PhotoImage(file = r"/Users/keeney/Desktop/Cipher/run.png")
# rphoto = rphoto.subsample(9)

button_run = tk.Button(bottom_frame, text='Run', width=10, command=run_app, relief='raised', highlightthickness=0, highlightbackground='blue')

button_close = tk.Button(bottom_frame, text="Exit", command=close_app, width=10, relief='raised', highlightthickness=0)

button_run.grid(column=0, row=0, sticky='e', padx=100, pady=10)
button_close.grid(column=1, row=0, sticky='e', padx=100, pady=10)

window.mainloop()
