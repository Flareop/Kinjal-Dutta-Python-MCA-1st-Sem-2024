import os

rows , columns = os.get_terminal_size()

smiling_face = '\u263A'

for _ in range(rows):
    print(smiling_face * columns)