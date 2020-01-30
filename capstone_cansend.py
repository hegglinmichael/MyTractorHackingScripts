
import sys
import string
import subprocess

def parse_line(filename):

    try:
        with open(filename, "r") as file_ptr:
            for line in file_ptr:
                part1 = ""
                part2 = ""
                code_to_send = "#"
                line = line.replace("-", "")
                line = line.replace("RX", "")
                line = ' '.join(line.split())
                words = line.split(" ")

                part1 = words[1]
                
                for num in range(3, 11):
                    if (len(words) > num and all(c in string.hexdigits for c in words[num])):
                        part2 = part2 + words[num]

                code_to_send = "#" + part1 + part2
                p = subprocess.Popen(["cansend", "can0", code_to_send], stdout=subprocess.PIPE, shell=True)
                sleep(10)
                p.kill()

    except:
        print("failed to run second check.  Failed to open file for reading")

if __name__ == "__main__":
    parse_line(sys.argv[1]);
