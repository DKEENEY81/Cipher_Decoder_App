#!/usr/bin/env Python3

import tkinter as tk
from tkinter import ttk
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
    print(f"\nplaintext = {plaintext}")

window = tk.Tk()  # or root=tk.Tk()
#window.configure(bg='grey')

window.title("Desktop Decoder")
# window.geometry("600x600") - can set initial size or let it default (by frame size?)
window.resizable(width="True", height="True")  # doesn't allow resizing when False

# three frames on top of each other (inside window/root)
frame_header = tk.Frame(window, borderwidth=2, pady=2)
center_frame = tk.Frame(window, borderwidth=2, pady=5)
bottom_frame = tk.Frame(window, borderwidth=2, pady=5)

# 3 additional frames that go inside center_frame
frame_main1 = tk.Frame(center_frame, borderwidth=2, relief='sunken')
# frame_main2 = tk.Frame(center_frame, borderwidth=2, relief='sunken')
frame_cipher = tk.Frame(center_frame, borderwidth=2, relief='sunken')
frame_keys = tk.Frame(center_frame, borderwidth=2, relief='sunken')

# initially fill additional frames with prompt for user input
row_input = tk.Label(frame_main1, text="# of ROWS: ")
col_input = tk.Label(frame_main1, text="# of COLUMNS:")
cipher_input = tk.Label(frame_cipher, text="Input encoded message")
keys_input = tk.Label(frame_keys, text='Input keys')

# the inputs should all be ints or strings
row_input1, col_input1, cipher_input1, keys_input1 = tk.IntVar(), tk.IntVar(), \
                                                     tk.StringVar(), tk.StringVar()


row_input_entry = tk.Entry(frame_main1, textvariable=row_input1, width=4)
col_input_entry = tk.Entry(frame_main1, textvariable=col_input1, width=4)
keys_input_entry = tk.Entry(frame_keys, textvariable=keys_input1, width=10)
cipher_input_entry = tk.Entry(frame_cipher, textvariable=cipher_input1, width=50)



# packing the items
frame_cipher.pack(fill='x', pady=2)
frame_main1.pack(fill='x', pady=2)
# frame_main2.pack(fill='x', pady=2)
frame_keys.pack(fill='x', pady=2)

row_input.pack(side='left')
row_input_entry.pack(side='left', padx=1)

col_input_entry.pack(side='right')
col_input.pack(side='right', padx=3)


cipher_input.pack(side='left')
cipher_input_entry.pack(side='left')

keys_input.pack(side='left')
keys_input_entry.pack(side='left')


frame_header.grid(row=0, column=0)
center_frame.grid(row=1, column=0)
bottom_frame.grid(row=2, column=0)

header = tk.Label(frame_header, text="Desktop Decoder Tool", bg='grey', fg='black', height='3', width='50')
header.grid(row=0, column=0)

button_run =ttk.Button(bottom_frame, text='Run', command=run_app, width=10, style='black/orange.TButton')
# can't seem to change button color - mac-os related?
button_close = ttk.Button(bottom_frame, text="Exit", command=close_app, width=10, style='black/orange.TButton')


button_run.grid(column =0, row=0, sticky='e', padx=100, pady=2)
button_close.grid(column=1, row=0, sticky='e', padx=100, pady=2)



window.mainloop()
