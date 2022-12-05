# Same as part one, but find the top three and add them together

infile = open('input.txt')

lines = infile.readlines()

current_total = 0
totals = []

for line in lines:
    if line != '\n':
        current_total += int(line)
    else:
        totals.append(current_total)
        current_total = 0

totals.sort(reverse=True)

print(totals[0] + totals[1] + totals[2])