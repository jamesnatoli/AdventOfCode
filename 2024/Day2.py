# 2024 Advent of Code: Puzzle 2

def checkLevel( level):
    safe = True
    increasing = False
    decreasing = False
    for x, y in zip( level, level[1:]):
        if y > x:
            if decreasing:
                safe = False
            increasing = True
            if y - x > 3:
                safe = False
        elif y < x:
            if increasing:
                safe = False
            decreasing = True
            if y - x < -3:
                safe = False
        elif y == x:
            safe = False
    return safe

def main():
    safesum = 0
    damped_safesum = 0
    with open('inputs/day2.txt') as infile:
        lines = infile.readlines()
        for line in lines:
            intlist = [ int(x) for x in line.split()]
            if checkLevel(intlist):
                safesum = safesum + 1
            else: # brute force check each element
                print(f'Bad List: {intlist}')
                templist = []
                for i, _ in enumerate(intlist):
                    templist = [ x for x in intlist] # need to deep copy this
                    templist.pop(i)
                    if checkLevel(templist):
                        damped_safesum = damped_safesum + 1
                        break
                        
    print(f'Safe Reports: {safesum}')
    print(f'Safe Reports with Dampener: {safesum + damped_safesum}')

    return 0

if __name__ == "__main__":
    main()

    
