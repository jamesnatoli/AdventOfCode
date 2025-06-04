# 2024 Advent of Code: Day 3
import re

def multiplymuls( line):
    mulsum = 0
    mulmatches = re.findall( r"mul\(\d+,\d+\)", line)
    for mulmatch in mulmatches:
        products = re.findall( r"\d+", mulmatch)
        mulsum = mulsum + int(products[0]) * int(products[1])
        
    return mulsum

def findrecent( inlist, pos):
    for i, ip1 in zip( inlist, inlist[1:]):
        if pos > ip1:
            return i
    return True # just in case

def main():
    with open('inputs/day3.txt') as infile:
        mulsum = 0
        enabledmulsum = 0
        lines = infile.readlines()
        for line in lines:
            # Part 1
            mulsum = mulsum + multiplymuls( line)

            # Part 2
            # test = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
            # splitondont = re.split( r"don\'t\(\)", line)
            # enabledmulsum = enabledmulsum + multiplymuls( splitondont[0])
            # print('SPLIT ON DONT:')
            # for dontsplit in splitondont[1:]:
            #     print(dontsplit)
            #     print()
            #     if re.search( r"do\(\)", dontsplit):
            #         enabledregion = dontsplit[re.search( r"do\(\)", dontsplit).start():]
            #         enabledmulsum = enabledmulsum + multiplymuls( enabledregion)
            dontiters = [ x.start() for x in re.finditer( r"don\'t\(\)", line)]
            doiters = [ x.start() for x in re.finditer( r"do\(\)", line)]
            muliters = re.finditer( r"mul\(\d+,\d+\)", line)

            for mul in muliters:
                if mul.start() < dontiters[0]:
                    enabledmulsum = enabledmulsum + multiplymuls( mul.group())
                else:
                    dontrecent = findrecent( dontiters, mul.start())
                    dorecent = findrecent( doiters, mul.start())
                    if dorecent > dontrecent:
                        print( f'Mul at {mul.start()}: do() at {dorecent} is more recent than don\'t() at {dontrecent}, multiplying {mul.group()}')
                        print(enabledmulsum)
                        enabledmulsum = enabledmulsum + multiplymuls( mul.group())
            
    print(f'Sum of muls: {mulsum}')
    print(f'Sum of enabled muls: {enabledmulsum}')
    return 0

if __name__ == "__main__":
    main()
