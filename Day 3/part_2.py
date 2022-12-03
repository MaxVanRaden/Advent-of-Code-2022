from part_1 import lines, priorities

total = 0

for i in range(0, len(lines), 3):
    backpack_1 = {}
    backpack_2 = {}

    for item in lines[i]:
        backpack_1[item] = 1
    for item in lines[i+1]:
        backpack_2[item] = 1
    for item in lines[i+2]:
        if item in backpack_1.keys() and item in backpack_2.keys():
            print(f"Badge found: {item}")
            total += priorities[item]
            backpack_1.clear()
            backpack_2.clear()
print(total)
