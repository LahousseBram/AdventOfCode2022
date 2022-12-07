from itertools import groupby

inputs = []

for index in range(2251):
    inputs.append(input(""))

filtered = [list(sub) for ele, sub in groupby(inputs, key = bool) if ele]

elves_calories = []
for i in range(len(filtered)):
    sum_of_current_elf = 0
    for ii in range(len(filtered[i])):
        sum_of_current_elf += int(filtered[i][ii])
    elves_calories.append(sum_of_current_elf)

print(filtered)

# most = 0
# second = 0
# third = 0
# for i in range(len(elves_calories)):
#     inserted = False
#     if elves_calories[i]>most and not inserted:
#         most=elves_calories[i]
#         inserted = True
#     elif most > elves_calories[i] > second and not inserted:
#         second=elves_calories[i]
#         inserted = True
#     elif second > elves_calories[i] > third and not inserted:
#         third=elves_calories[i]


#print(max(elves_calories))

elves_calories.sort()
print(elves_calories)
top_3 = elves_calories[-1] + elves_calories[-2] + elves_calories [-3]
print(top_3)