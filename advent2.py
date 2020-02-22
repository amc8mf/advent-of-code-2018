import csv

def getChecksum(file):
    with open(file) as tsv:
        checksum = 0
        for line in csv.reader(tsv, dialect ="excel-tab"):
            line = list(map(int, line))
            maxi = max(line)
            mini = min(line)
            checksum += (int(maxi) - int(mini))
    return checksum

print(getChecksum("A2_input.txt"))
