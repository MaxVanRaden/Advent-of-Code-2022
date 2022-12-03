
# quick function to make a range() equivalent for characters
# unlike normal range function, include last
def char_range(first, last):
    return (chr(n) for n in range(ord(first), ord(last)+1))

total = 0
priorities = {}
contents = {}

with open("input.txt") as infile:
    lines = infile.readlines()

for char in char_range("a", "z"):
    priorities[char] = ord(char) - 96 # "a" has ascii value 97, so subtract 96 to get priority 1
for char in char_range("A", "Z"):
    priorities[char] = ord(char) - 38 # "A" has ascii value 65, so subtract 38 to get priority 27


if __name__ == '__main__':



    for line in lines:
        print(f"\nRaw line: {line}")
        compartment1 = line[:int(len(line)/2)]
        compartment2 = line[int(len(line)/2):]
        print(f"Compartment 1 contents: {compartment1}\nCompartment 2 contents: {compartment2}")
        
        # Make a dict of the first comparment, then check the items in the second compartment against the first. 
        # I could keep track, but I don't need to. Very much expecting to rue this moment in part two
        for char in compartment1:
            contents[char] = 1
        for char in compartment2:
            if char in contents.keys():
                print(f"Character found in both compartments: {char} - Value of {char}: {priorities[char]}")
                total += priorities[char]
                break
        contents.clear()
    print(f"Total priorities of duplicate items: {total}")
    

