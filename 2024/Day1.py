# Advent Of Code: Puzzle 1

def main():
    # Part 1
    list1 = []
    list2 = []
    
    with open('inputs/Day1.txt') as infile:
        lines = infile.readlines()
        for line in lines:
            list1.append( int(line.split()[0]))
            list2.append( int(line.split()[1]))

    list1.sort()
    list2.sort()

    distance = 0
    for x, y in zip(list1, list2):
        distance = distance + abs(x - y)

    print(f'Distance: {distance}')

    # Part 2
    similarity = 0
    for x, y in zip(list1, list2):
        if x in list2:
            similarity = similarity + (x * list2.count(x))

    print(f'Similarity: {similarity}')
    return 0

if __name__ == "__main__":
    main()
