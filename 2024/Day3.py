# 2024 Advent of Code: Day 3OA
import re

def multiplymuls( line):
    mulsum = 0
    mulmatches = re.findall( r"mul\(\d+,\d+\)", line)
    for mulmatch in mulmatches:
        products = re.findall( r"\d+", mulmatch)
        mulsum = mulsum + int(products[0]) * int(products[1])
        
    return mulsum

def findrecent( inlist, pos):
    if pos < inlist[0]: # mul is before first
        return False

    for i, ip1 in zip( inlist, inlist[1:]):
        if (pos > i) and (pos < ip1):
            return i
        
    return inlist[-1] # mul is after last

def main():
    with open('inputs/day3.txt') as infile:
        mulsum = 0
        enabledmulsum = 0
        lines = infile.readlines()
        alltext = ""
        
        # Part 1
        for line in lines:
            mulsum = mulsum + multiplymuls( line)
            alltext = alltext + line # ignore the line breaks so that don't() commands carry through

        # Part 2
        test = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        dontiters = [ x.start() for x in re.finditer( r"don\'t\(\)", alltext)]
        doiters = [ x.start() for x in re.finditer( r"do\(\)", alltext)]
        muliters = re.finditer( r"mul\(\d+,\d+\)", alltext)

        for mul in muliters:
            if not findrecent( dontiters, mul.start()): # muls are enabled at start by default
                enabledmulsum = enabledmulsum + multiplymuls( mul.group())
            elif findrecent( doiters, mul.start()) > findrecent( dontiters, mul.start()): # do() is more recent
                enabledmulsum = enabledmulsum + multiplymuls( mul.group())
            else: # dummy statement, but this is where we'll skip multiplying because of a recent don't()
                pass

    print(f'Sum of muls: {mulsum}')
    print(f'Sum of enabled muls: {enabledmulsum}')
    return 0

if __name__ == "__main__":
    main()
