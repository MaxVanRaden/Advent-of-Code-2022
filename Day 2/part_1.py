# Read lines of letter pairs representing Rock-Paper-Scissors matches and calculate points based on results
# X and A: Rock (+1 point)
# Y and B: Paper (+2 points)
# Z and C: Scissors (+3 points)
# Winning is worth 6 points, drawing is worth 3 points


infile = open('input.txt')

lines = infile.readlines()
points = 0

for line in lines:
    try:
        opponent = line[0]
        player = line[2]
    except BaseException as err:
        print(f"Error occurred: {err}")
        exit()
    if player == 'X':
        points += 1
        if opponent == 'C':
            points += 6
        if opponent == 'A':
            points += 3
    elif player == 'Y':
        points += 2
        if opponent == 'A':
            points += 6  
        if opponent == 'B':
            points += 3
    elif player == 'Z':
        points += 3
        if opponent == 'B':
            points += 6
        elif opponent == "C":
            points += 3
print(f"Total number of points won: {points}. Total matches played: {len(lines)}")