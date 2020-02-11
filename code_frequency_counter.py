

import sys

def parse_pgn(line):
    line = line.replace("-", "")
    line = line.replace("RX", "")
    line = ' '.join(line.split())

    line_pieces = line.split(" ")
    can_id = line_pieces[1]
    return can_id[2:6]

def remove_duplicate_codes(filename):
    mapping = {}

    with open(filename, "r") as file_ptr:
        for line in file_ptr:
            temp = line
            pgn = parse_pgn(temp)

            if pgn not in mapping:
                mapping[pgn] = line[0:len(line) - 1]

    return mapping


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("usage: python3 code_frequency_counter.py <filename>")
    
    removed_dup_mapping = remove_duplicate_codes(sys.argv[1])
    for i in removed_dup_mapping:
        print(removed_dup_mapping[i])



