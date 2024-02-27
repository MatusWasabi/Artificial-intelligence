import random
import time
from Wherewolf import Wherewolf


def Initialize_game():
    num_players = random.randint(10, 20)
    N = 0
    M = 0
    roles = ["-"] * (num_players)
    for i in range(num_players):
        if random.random() < 0.5:
            roles[i] = "W"
            N += 1
        else:
            roles[i] = "V"
            M += 1

    R = random.randint(2, 5)
    W_o = random.random()
    W_q = random.random() * (1 - W_o)
    W_s = 1 - W_o - W_q
    V_o = random.random()
    V_q = random.random() * (1 - V_o)
    V_s = 1 - V_o - V_q
    T = random.random()
    total_time = 0

    t_start = time.time()
    mygame = Wherewolf(N, M, R, W_o, W_q, W_s, V_o, V_q, V_s, T)
    t_stop = time.time()
    total_time += (t_stop - t_start)
    return num_players,N,M,roles,R,W_o,W_s,V_o,V_s,T,total_time,mygame

num_players, wolf_num, villager_num, roles, interrogation_round, wolf_oppo, wolf_same, villager_oppo, villager_same, transfer_chance, total_time, mygame = Initialize_game()

def Reveal_roles(roles):
    print("Sneak peek at roles:", roles)

def Deduction_phase(num_players, roles, total_time, mygame):
    print("-----Deduction Phase-----")
    t_start = time.time()
    suspect = mygame.deduction()
    t_stop = time.time()
    total_time += (t_stop - t_start)
    Check_time_out(total_time)
    print("Total time used since last deduction:", total_time, "seconds")
    total_time = 0
    print("Your deduction: " + str(suspect))
    Check_answer_valid(num_players, roles, suspect)
    revealed = roles[suspect - 1]
    roles[suspect - 1] = "-"
    return total_time,revealed

def Check_answer_valid(num_players, roles, suspect):
    if suspect < 1 or suspect > num_players or roles[suspect - 1] == '-':
        print("Invalid answer.")
        print("The game stops.")
        exit()

def Check_time_out(total_time):
    if total_time > 5:
        print("Timed out.")
        print("The game stops.")
        exit()

while wolf_num != 0 and villager_num != 0:
    Reveal_roles(roles)

    # Interrogation
    print("-----Interrogation Phase-----")
    for round in range(interrogation_round):
        hints = [0] * num_players

        for index in range(num_players):
            lf = "S"
            if roles[index] == "W":
                random_chance = random.random()
                if random_chance < wolf_oppo:  # point to other team
                    lf = "V"
                elif random_chance < wolf_oppo + wolf_same:  # point to same team
                    lf = "W"
            elif roles[index] == "V":
                random_chance = random.random()
                if random_chance < villager_oppo:  # point to other team
                    lf = "W"
                elif random_chance < villager_oppo + villager_same:  # point to same team
                    lf = "V"
            l = []

            if roles[index] != "-" and lf != "S":
                for new_wolf_seat in range(num_players):
                    if index != new_wolf_seat and roles[new_wolf_seat] == lf:
                        l.append(new_wolf_seat)
                if len(l) != 0:
                    hints[index] = l[random.randint(0, len(l) - 1)] + 1

        print("Provided Hint: " + str(hints))
        t_start = time.time()
        mygame.interrogation(hints)
        t_stop = time.time()
        total_time += (t_stop - t_start)

    # Deduction
    total_time, revealed = Deduction_phase(num_players, roles, total_time, mygame)


    # Transition
    print("-----Transition Phase-----")
    role = "Wolf" if revealed == "W" else "Villager"
    print("The suspect is revealed as " + role)
    t_start = time.time()
    mygame.transition(revealed)
    t_stop = time.time()
    total_time += (t_stop - t_start)
    if revealed == "W":
        wolf_num -= 1
    else:
        villager_num -= 1

    if wolf_num + villager_num >= 1:
        for index in range(num_players):
            if roles[index] == "W":
                if random.random() < transfer_chance:
                    new_wolf_seat = index - 1
                    if new_wolf_seat < 0:
                        new_wolf_seat += num_players
                    while roles[new_wolf_seat] == "-":
                        new_wolf_seat = new_wolf_seat - 1
                        if new_wolf_seat < 0:
                            new_wolf_seat += num_players
                    tmp = roles[new_wolf_seat]
                    roles[new_wolf_seat] = roles[index]
                    roles[index] = tmp

    print("########## End of iteration ##########")
endgame_message = "There is no villager left. You lose." if wolf_num == 0 else "There is no wolf left. You win!"
print(endgame_message)

