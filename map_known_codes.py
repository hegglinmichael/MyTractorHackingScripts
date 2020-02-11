
import os
import sys

def map_known_codes(filename):
    known_codes_map = {}

    with open(filename, "r") as file_ptr:
        for line in file_ptr:
            known_codes_map[line[0:4]] = line

    return known_codes_map

def parse_pgn(line):
    line = line.replace("-", "")
    line = line.replace("RX", "")
    line = ' '.join(line.split())

    line_pieces = line.split(" ")
    can_id = line_pieces[1]
    return can_id[2:6]

def tamper_output_stream(known_codes_map):

    for line in sys.stdin:
        temp = line
        pgn = parse_pgn(temp)

        if pgn in known_codes_map:
            line = line.replace('\n', "")
            print(line + "\tDescription: " + known_codes_map[pgn])
        else:
            print(line)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("usage: candump can0 | python3 map_known_codes.py <file full of known codes with their desription>")
        print("\tYou must have a file full of already known codes to use this script")
        print("\tThe functionallity of this script is to map these known pgns and their descriptions to ")
        print("\tThe current incoming stream.")

    known_codes_map = map_known_codes(sys.argv[1])
    tamper_output_stream(known_codes_map)
    sys.exit(0)
