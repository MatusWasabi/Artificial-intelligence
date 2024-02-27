#####
#
# Name: Matus Yaowvasrisuwan
# Student ID: 633040476-6
#
#####
import random


class Wherewolf:
    sampling_size = 10
    weight = [0] * sampling_size

    def __init__(self, num_wolf, num_villager, interrogation_rounds, wolf_point_opp, wolf_quiet, wolf_point_same, villager_point_opp, villager_quiet, villager_point_same, wolf_trade_role):
        self.total = num_wolf + num_villager
        self.current = 0
        self.seating = ["W"] * num_wolf + ["V"] * num_villager #Create instance seating
        self.samples = []

        for i in range(Wherewolf.sampling_size):
            shuffled_copy = random.sample(self.seating.copy(), len(self.seating))
            self.samples.append(shuffled_copy)
            __class__.weight[i] = 1    

        self.num_wolf = num_wolf
        self.num_villager = num_villager
        self.interrogation_rounds = interrogation_rounds
        self.wolf_point_opp = wolf_point_opp
        self.wolf_quiet = wolf_quiet
        self.wolf_point_same = wolf_point_same
        self.villager_point_opp = villager_point_opp
        self.villager_quiet = villager_quiet
        self.villager_point_same = villager_point_same
        self.wolf_trade_role = wolf_trade_role
        

            
    

    def interrogation(self, hint: list[str]):
        for index in range(len(hint)):
            player_point_from = index
            player_point_to = hint[index]

            for number, sample in enumerate(self.samples):
                if sample[player_point_from - 1] == "W" and sample[player_point_to - 1] == "W":
                    __class__.weight[number] *= self.wolf_point_same * 1 / self.num_wolf

    

    def deduction(self) -> int:
        """
        for each sample
                for each position 
                    keep track which position is most likely to be wolf
                """
        self.current += 1
        return self.current

    def transition(self, revealed: str):
        """for each sample:
                if sample[???][position] != revealed:
                        weight[????] = 0
                        
                resample()"""
        pass


    def resample():
        """
        create array sample2:
        for each sample in sample2:
        x = random depend on weight
        sample2[????] = sample[x]
        weight[???] = 1  
        """