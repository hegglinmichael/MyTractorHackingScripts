##
#  Michael Hegglin --> Team Kangaroo, Winter 2020
#  Description:
#       This python file is meant to take the incoming streamed data
#       (data that has already been broken up into its appropriate bits from
#       the open source candump program.)  It can also take in a log file created
#       from the candump program
#                                                                                   ____
#  @(params) : there are lots of options to use with this file so please run:           |
#               $> python3 capstone_cansniffer.py -h                                    |
#                                                                                       |- future capstone group please
#              It will explain all the useages and give examples of each to make it     |- read
#              easy on you                                                              |
#                                                                                   ____|
##

import sys
import time

#  Description:
#       This method will show all codes and their frequencies
#       These codes will be diff'd from between a working file and a broken file
#
def code_diff(broken_code_mapping, working_code_mapping, filename):
    filename = filename + "_filter.txt"
    filter_file = open(filename, "w+")

    print("--------------------------------------------------------------------------")
    print("CODES IN THE BROKEN CODES LOG THAT ARE NOT IN THE WORKING CODES LOG")
    print("--------------------------------------------------------------------------")

    for code in broken_code_mapping:
        if code not in working_code_mapping:
            print("Code: " + code + "\tFrequency: " + str(broken_code_mapping[code]))
        else:
            filter_file.write(code)
            filter_file.write('\n')

    print("\n\n\n--------------------------------------------------------------------------")
    print("CODES IN THE WORKING CODES LOG THAT ARE NOT IN THE BROKEN CODES LOG")
    print("--------------------------------------------------------------------------")

    for code in working_code_mapping:
        if code not in broken_code_mapping:
            print("Code: " + code + "\tFrequency: " + str(working_code_mapping[code]))
        else:
            filter_file.write(code)
            filter_file.write('\n')

    filter_file.close()
    return 0

#  Description:
#       This method will get the codes with frequencies 
#       equal to or below the frequency number that the user input
#
#  @(param1:int) : The frequency number the user specified
#
def codes_below_freq(code_mapping, freq_num):
    for key in code_mapping:
        if code_mapping[key] <= freq_num:
            print("Code: " + key + "\tFrequency: " + str(code_mapping[key]))

    return 0

#  Description:
#       This method will get the codes frequencies of all numbers
#
#  @(param1:string) : The filename where the codes are being streamed to
#
def code_freq(code_mapping):
    for code in code_mapping:
        print("Code: " + code + "\tFrequency: " + str(code_mapping[code]))

#  Description:
#       This method will parse the working log file.  It will put all codes into
#       a dictionary.  The codes will be the key, and there will be a 
#       frequency count as the value
#  
#  @(param1:string) : name of a log file with working codes
#
def load_dictionary(filename):
    code_mapping = {}

    try:
        with open(filename, "r") as file_ptr:
                for line in file_ptr:
                    words = line.split("]")
                    code = words[1].split("'")[0]
                    code = code[2:]
                    code = code.replace('\n', "")
                    if code in code_mapping:
                        code_mapping[code] = code_mapping[code] + 1
                    elif code != "":
                        code_mapping[code] = 1
    except:
        print("--------------------------------------------------------------------------")
        print("Failed to load from input file!!!! check to make sure input file matches format of")
        print("candump open source project")
        print("--------------------------------------------------------------------------")

    return code_mapping

#  Description:
#       This method will take in a stream from the candump terminal
#
def get_file_stream(filtername):
    mapping_filter = {}

    try:
        with open(filtername, "r") as file_ptr:
            for line in file_ptr:
                line = line.replace('\n', "")
                if line in mapping_filter:
                    mapping_filter[line] = mapping_filter[line] + 1
                elif line != "":
                    mapping_filter[line] = 1
    except:
        print("--------------------------------------------------------------------------")
        print("Failed to read in filter data!!!!!")
        print("--------------------------------------------------------------------------")

    for line in sys.stdin:
        words = line.split("]")
        code = words[1].split("'")[0]
        code = code[2:]
        code = code.replace('\n', "")
        if code not in mapping_filter:
            print("line : "+ code, end="\r")
            time.sleep(.1)

    print()

#  Description:
#       This method is only run if this python file is run separately on 
#       it's own (python streamparser.py <log name here>).  It allows 
#       a developer to see codes in a log that stand out
#  
#  @(params) : parameters for the function can be looked at with -h option
#
#
if __name__ == "__main__":

    if "-h" in sys.argv or "-help" in sys.argv or "--help" in sys.argv:
        print("\nUsage options: (python3 capstone_cansniffer.py [OPTIONS])")
        print("Standard Usage: python3 capstone_cansniffer.py <file1 broken codes> <file2 working codes>\n")
        print("-s : terminal pipe, data is being streamed to")
        print("\t-Example: candump [OPTIONS] | python3 capstone_cansniffer.py -s <filter file>\n")
        print("-f : single file input, dumps the frequency of each code in the terminal")
        print("\t-Example: python3 capstone_cansniffer.py -f <file1>\n")
        print("-cbf : single file input, gets all codes with a frequency lower than the number specified")
        print("\t-Example: python3 capstone_cansniffer.py -cbf <file1> <frequency number>\n")
        print("--help or -h : help to show options\n")
        sys.exit(0)

    if "-s" in sys.argv and len(sys.argv) == 3:
        get_file_stream(sys.argv[2])
        sys.exit(0)

    if "-f" in sys.argv and len(sys.argv) == 3:
        code_mapping = load_dictionary(sys.argv[2])
        code_freq(code_mapping)
        sys.exit(0)

    if "-cbf" in sys.argv and len(sys.argv) == 4:
        code_mapping = load_dictionary(sys.argv[2])
        codes_below_freq(code_mapping, int(sys.argv[3]))
        sys.exit(0)

    if (len(sys.argv) < 3):
        print("Hey, cansniffer here! I need a log file name as input when run offline. ")
        print("Please enter the below when running for standard usage:")
        print("python3 streamparser.py <file1 broken codes here> <file2 working codes here>")
        sys.exit(-1)

    broken_codes_mapping = load_dictionary(sys.argv[1])
    working_codes_mapping = load_dictionary(sys.argv[2])
    sys.exit(code_diff(broken_codes_mapping, working_codes_mapping, sys.argv[1]))
