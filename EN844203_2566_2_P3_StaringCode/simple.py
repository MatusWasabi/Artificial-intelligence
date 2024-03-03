import random
from Wherewolf import Wherewolf

###
# This is just a stub file that provides you a basic understanding of the flow of the game. All information and probability chance does not reflect the real gameplay.
###

N = random.randint(4, 8)
M = random.randint(4, 8)
R = random.randint(2, 5)
W_o = random.random()
W_q = random.random() * (1 - W_o)
W_s = 1 - W_o - W_q
V_o = random.random()
V_q = random.random() * (1 - V_o)
V_s = 1 - V_o - V_q
T = random.random()

mygame = Wherewolf(N, M, R, W_o, W_q, W_s, V_o, V_q, V_s, T)
num_wolves = N
num_villagers = M
seating = ["W"] * N + ["V"] * M
random.shuffle(seating)
print(seating)

while num_wolves != 0 and num_villagers != 0:
    # print(seating)
    # Interrogation
    print("-----Interrogation Phase-----")
    for r in range(R):
        # Hint is which player did each seat pointed to.
        hint = [0] * (N + M)
        for i in range(N + M):
            if seating[i] != "-":
                j = (i + 1) % (N + M)
                while seating[j] == '-':
                    j = (j + 1) % (N + M)
                hint[i] = j + 1
        print("Provided Hint: " + str(hint))
        mygame.interrogation(hint)


    # Deduction
    print("-----Deduction Phase-----")
    suspect = mygame.deduction()
    print("Your deduction: " + str(suspect))
    if suspect < 1 or suspect > (N + M) or seating[suspect - 1] == '-':
        print("Invalid answer.")
        print("The game stops.")
        exit()

    revealed = seating[suspect - 1]
    seating[suspect - 1] = "-"
    # Transition
    print("-----Transition Phase-----")
    role = "Wolf" if revealed == "W" else "Villager"
    print("The suspect is revealed as " + role)
    mygame.transition(revealed)
    if revealed == "W":
        num_wolves -= 1
    else:
        num_villagers -= 1
    print("########## End of iteration ##########")
endgame_message = "There is no villager left. You lose." if num_villagers == 0 else "There is no wolf left. You win!"
print(endgame_message)
