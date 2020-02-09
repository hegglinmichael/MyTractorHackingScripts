
import sys

def get_source_and_dest_mappings(filename):
    source_mapping = {}
    dest_mapping = {}

    with open(filename, "r") as file_ptr:
        for line in file_ptr:
            line = line.replace("-", "")
            line = line.replace("RX", "")
            line = ' '.join(line.split())
            words = line.split(" ")

            source_addr = words[1][6:8]
            destination_addr = words[1][4:6]

            if source_addr in source_mapping:
                if line not in source_mapping[source_addr]:
                    tl = source_mapping[source_addr]
                    tl.append(line)
                    source_mapping[source_addr] = tl

            else:
                source_mapping[source_addr] = [line]

            if destination_addr in dest_mapping:
                if line not in dest_mapping[destination_addr]:
                    tl = dest_mapping[destination_addr]
                    tl.append(line)
                    dest_mapping[destination_addr] = tl
                    
            else:
                dest_mapping[destination_addr] = [line]

    return (source_mapping, dest_mapping)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("usage: python3 source_and_dest_sort.py <file of logged codes file>")
    
    source_mapping, dest_mapping = get_source_and_dest_mappings(sys.argv[1])

    for i in source_mapping:
        print("\n\nSource Code: " + i)
        print("list of lines with this as their source below:")

        for k in source_mapping[i]:
            print(k)

    for i in dest_mapping:
        print("\n\nDestination Code: " + i)
        print("list of lines with this as their destination below:")

        for k in dest_mapping[i]:
            print(k)



