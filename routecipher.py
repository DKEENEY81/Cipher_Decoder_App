#!/usr/bin/env python3
import sys

# ===============================================
# USER INPUT:

# the string to be decrypted, place between triple quotes
ciphertext = '''16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19'''

# number of columns in the transposition matrix
COLS = 4

# number of rows in the transposition matrix
ROWS = 5

# key with spaces between numbers, negative reads up column
key = '-1 2 -3 4'  # negative indicates read UP column


# END USER INPUT - DO NOT EDIT BELOW
# =================================================


def validate_col_row(cipherlist):
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher):  # exludes 1 column ciphers
        if not len_cipher % i:
            factors.append(i)
    print("\nLength of cipher = {}".format(len_cipher))
    print("Acceptable column/row values include: {}".format(factors))
    print()
    if ROWS * COLS != len_cipher:
        print("\nError - Input Columns & Rows not factors of length "
              "of cipher. Terminating program.", file=sys.stderr)
        sys.exit(1)


def key_to_int(key):
    key_int = [int(i) for i in key.split()]
    key_int_lo = min(key_int)
    key_int_hi = max(key_int)
    if len(key_int) != COLS or key_int_lo < -COLS or key_int_hi > COLS \
            or 0 in key_int:
        print('\nError - Problem with key. Terminating.', file=sys.stderr)
        sys.exit(1)
    else:
        return key_int


def build_matrix(key_int, cipherlist):
    translation_matrix = [None] * COLS
    start = 0
    stop = ROWS
    for k in key_int:
        if k < 0:  # reading bottom-to-top of column
            col_items = cipherlist[start:stop]
        elif k > 0:  # reading top-to-bottom of column
            col_items = list((reversed(cipherlist[start:stop])))
        translation_matrix[abs(k) - 1] = col_items
        start += ROWS
        stop += ROWS
    return translation_matrix


def decrypt(translation_matrix):
    # Loop through nested lists, popping off last value
    plaintext = ''
    for i in range(ROWS):
        for matrix_col in translation_matrix:
            word = str(matrix_col.pop())
            plaintext += word + ' '
    return plaintext


def main():
    """Run program with decrypted plaintext"""
    print("\nCiphertext = {}".format(ciphertext))
    print("Trying {} columns".format(COLS))
    print("Trying {} rows".format(ROWS))
    print("Trying key = {}".format(key))
    cipherlist = list(ciphertext.split())
    validate_col_row(cipherlist)
    key_int = key_to_int(key)
    translation_matrix = build_matrix(key_int, cipherlist)
    plaintext = decrypt(translation_matrix)
    print(("\nplaintext = {}".format(plaintext)))


if __name__ == '__main__':
    main()
