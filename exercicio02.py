import io


def last_lines(text_file, buffer_size=io.DEFAULT_BUFFER_SIZE):
    with open(text_file, "r", buffering=buffer_size) as text:
        for line_reversed in reversed(text.readlines()):
            line_reversed = line_reversed.replace("\n", '')
            line_reversed = bytearray(line_reversed.encode())
            yield f"{line_reversed[:buffer_size].decode()}\n"


if __name__ == '__main__':
    for line in last_lines("arquivos/02/my_file.txt"):
        print(line, end='')
