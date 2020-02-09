

import sys

def remove_duplicate_codes(filename):
    mapping = {}

    with open(filename, "r") as file_ptr:
        for line in file_ptr:
            code = ""
            line = line.replace("-", "")
            line = line.replace("RX", "")
            line = ' '.join(line.split())

            line_pieces = line.split(" ")
            for i in range(3, len(line_pieces)):
                code += line_pieces[i]

            if code not in mapping:
                mapping[code] = 1

    return mapping


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("usage: python3 code_frequency_counter.py <filename>")
    
    removed_dup_mapping = remove_duplicate_codes(sys.argv[1])
    for i in removed_dup_mapping:
        print("Code: " + i)



