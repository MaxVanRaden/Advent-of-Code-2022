# A - Rock 1, B - Paper 2, C - Scissors 3
# X - Lose, Y - Draw 3, Z - Win 6


infile = open('input.txt')

lines = infile.readlines()
points = 0

for line in lines:
    try:
        opponent = line[0]
        result = line[2]
    except BaseException as err:
        print(f"Error occurred: {err}")
        exit()
    
    if opponent == 'A':
        if result == 'X':
            player = 'C'
        elif result == 'Y':
            player = 'A'
        elif result == 'Z':
            player = 'B'

    elif opponent == 'B':
        if result == 'X':
            player = 'A'
        elif result == 'Y':
            player = 'B'
        elif result == 'Z':
            player = 'C'

    elif opponent == 'C':
        if result == 'X':
            player = 'B'
        elif result == 'Y':
            player = 'C'
        elif result == 'Z':
            player = 'A'
    
    if player == 'A':
        points += 1
    elif player == 'B':
        points += 2
    elif player == 'C':
        points += 3
    
    if result == 'Y':
        points += 3
    elif result == 'Z':
        points += 6

print(f"Total number of points won: {points}. Total matches played: {len(lines)}")
