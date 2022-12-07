score = []
def calc_score(your_move, opponent_move):
    global score

    # lose to paper (rock)

    if your_move == "X" and opponent_move == "B":
        score.append(1)

    # draw with scissors (scissors)

    if your_move == "Y" and opponent_move == "C":
        score.append(3)
        score.append(3)

    # win against rock (paper)

    if your_move == "Z" and opponent_move == "A":
        score.append(6)
        score.append(2)

    # lose to scissors (paper)

    if your_move == "X" and opponent_move == "C":
        score.append(2)

    # win vs paper (scissors)

    if your_move == "Z" and opponent_move == "B":
        score.append(6)
        score.append(3)

# draw vs rock

    if your_move == "Y" and opponent_move == "A":
        score.append(3)
        score.append(1)

    #lose against rock (scissors)

    if your_move == "X" and opponent_move == "A":
        score.append(3)

    #draw against paper
    if your_move == "Y" and opponent_move == "B":
        score.append(2)
        score.append(3)

    #win against scissors (rock)
    if your_move == "Z" and opponent_move == "C":
        score.append(6)
        score.append(1)

input = open("day2_input.txt","r")
for line in input:
    print(line[0:1])
    calc_score(line[2:3], line[0:1])

print(sum(score))
input.close()