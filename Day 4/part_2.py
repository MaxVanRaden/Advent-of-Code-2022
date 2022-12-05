with open("input.txt") as infile:
    lines = infile.readlines()

split_lines = []
count = 0

for line in lines:
    split_line = line.split(",")
    for sub_line in split_line:
        split_lines.append(sub_line.split("-"))

for i in range(0, len(split_lines), 2):
    set1 = set(range(int(split_lines[i][0]), int(split_lines[i][1])+1))
    set2 = set(range(int(split_lines[i+1][0]), int(split_lines[i+1][1])+1))
    if len(set1.intersection(set2)) > 0:
        count += 1
print(count)