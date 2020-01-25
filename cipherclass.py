#!/usr/bin/env python3
import sys


class Decoder:
    def __init__(self, rows, cols):
        print("initiating")
        self.ROWS = rows
        self.COLS = cols

    def validate_col_row(self, cipherlist):
        factors = []
        len_cipher = len(cipherlist)
        for i in range(2, len_cipher):  # excludes 1 column ciphers
            if not len_cipher % i:
                factors.append(i)
        print("\nLength of cipher = {}".format(len_cipher))
        print("Acceptable column/row values include: {}".format(factors))
        print()
        if self.ROWS * self.COLS != len_cipher:
            print("\nError - Input Columns & Rows not factors of length "
                  "of cipher. Terminating program.", file=sys.stderr)
            sys.exit(1)

    def key_to_int(self, key):
        key_int = [int(i) for i in key.split()]
        key_int_lo = min(key_int)
        key_int_hi = max(key_int)
        if len(key_int) != self.COLS or key_int_lo < -self.COLS or key_int_hi > self.COLS \
                or 0 in key_int:
            print('\nError - Problem with key. Terminating.', file=sys.stderr)
            sys.exit(1)
        else:
            return key_int

    def build_matrix(self, key_int, cipherlist):
        translation_matrix = [None] * self.COLS
        start = 0
        stop = self.ROWS
        for k in key_int:
            if k < 0:  # reading bottom-to-top of column
                col_items = cipherlist[start:stop]
            elif k > 0:  # reading top-to-bottom of column
                col_items = list(reversed(cipherlist[start:stop]))
            translation_matrix[abs(k) - 1] = col_items
            start += self.ROWS  # increment start of slice
            stop += self.ROWS  # increment end of slice
        return translation_matrix

    def decrypt(self, translation_matrix):
        # Loop through nested lists, popping off last value
        plaintext = ''
        for i in range(self.ROWS):
            for matrix_col in translation_matrix:
                word = str(matrix_col.pop())
                plaintext += word + ' '
        return plaintext
