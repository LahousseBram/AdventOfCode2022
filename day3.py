input = open("day3_input.txt","r")
found = []
priorities = []
for line in input:
    part1 = line[0:len(line)//2]
    part2 = line[len(line)//2:len(line)]

    for i in range(len(part1)):
        for ii in range(len(part2)):
            if part1[i] == part2[ii] and part2[ii] not in found:
                found.append(part1[i])
                break

for i in range(len(found)):
        u_value = ord(found[i])
        if 65 <= u_value <= 90:
            priorities.append(u_value - 38)
        elif 97 <= u_value <= 122:
            priorities.append(u_value - 96)

print(sum(priorities))