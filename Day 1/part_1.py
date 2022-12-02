# Find the highest total series of consecutive integers

infile = open('input.txt')

lines = infile.readlines()

max = 0
current_total = 0

for line in lines:
    if line != '\n':
        current_total += int(line)
    else:
        if current_total > max:
            max = current_total
        current_total = 0
print(max)