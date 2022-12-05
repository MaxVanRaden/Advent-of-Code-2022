with open("input.txt") as infile:
    lines = infile.readlines()

split_lines = []
count = 0

for line in lines:
    split_line = line.split(",")
    for sub_line in split_line:
        split_lines.append(sub_line.split("-"))

for i in range(0, len(split_lines), 2):
    if split_lines[i][0] <= split_lines[i+1][0] and split_lines[i][1] >= split_lines[i+1][1]:
        count += 1
    elif split_lines[i][0] >= split_lines[i+1][0] and split_lines[i][1] <= split_lines[i+1][1]:
        count += 1
print(count)
