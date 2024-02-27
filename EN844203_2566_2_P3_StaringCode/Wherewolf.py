#####
#
# Name: Matus Yaowvasrisuwan
# Student ID: 633040476-6
#
#####
import random


class Wherewolf:
    sampling_size = 10

    def __init__(self, num_wolf, num_villager, interrogation_rounds, wolf_point_opp, wolf_stay_quiet, wolf_point_same, villager_point_opp, villager_stay_quiet, villager_point_same, wolf_trade_role):
        self.total = num_wolf + num_villager
        self.current = 0
        self.seating = ["W"] * num_wolf + ["V"] * num_wolf #Create instance seating
        self.samplings = []

        for i in range(Wherewolf.sampling_size):
            shuffled_copy = random.sample(self.seating.copy(), len(self.seating))
            self.samplings.append(shuffled_copy)
    
        
        
        

    def interrogation(self, hint: list[str]):
        self.hint = hint
        pass

    def deduction(self) -> int:
        self.current += 1
        return self.current

    def transition(self, revealed: str):
        pass
