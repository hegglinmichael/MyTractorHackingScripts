# Michael Hegglin
#   This python file sorts by pgn number.  
#
#   The PGN is made up of the PDU Format and PDU Specific concatenated together 
#   and converted to decimal. A lookup table of PGNs and SPNs is available 
#   as J1939AD from the SAE, another lookup table of ISO CAN Bus standard items can be forund on isobus.net.
#
#   THIS SCRIPT IS MEANT TO WORK WITH NO EXTRA OPTIONS IN CANDUMP
#



import sys

def parse_pgn_from_line(line_str):
    pgn_dec = 0
    pgn_str = ""
    pdu_specific = ""
    pdu_format = ""
    can_id = ""

    line_str = line_str.replace("-", "")
    line_str = line_str.replace("RX", "")
    line_str = ' '.join(line_str.split())

    line_pieces = line_str.split(" ")
    can_id = line_pieces[1]

    pgn_dec = int(can_id[2:6], 16)
    return pgn_dec

def parse_codes(pgn_num_to_find, output_filename):
    mapping = {}
    file = open(output_filename, "w+")

    for line in sys.stdin:
        temp = line
        pgn_dec = parse_pgn_from_line(line)

        print(pgn_dec)
        print(pgn_num_to_find)
        if pgn_dec == int(pgn_num_to_find):
            mapping[temp] = "new"
            file.write(temp)

    file.close()

if __name__ == "__main__":

    if len(sys.argv) != 3 and not sys.argv[1].isdigit():
        print("usage: candump <can0> | python3 pgn_sort.py <pgn code you want to sort by> <output file name.txt>")
        exit(0)

    parse_codes(sys.argv[1], sys.argv[2])

