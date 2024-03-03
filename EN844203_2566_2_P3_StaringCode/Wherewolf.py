#####
#
# Name: Matus Yaowvasrisuwan
# Student ID: 633040476-6
#
#####
import random


class Wherewolf:
    sampling_size = 10
    weights = [0] * sampling_size

    def __init__(self, num_wolf, num_villager, interrogation_rounds, wolf_point_opp, wolf_quiet, wolf_point_same, villager_point_opp, villager_quiet, villager_point_same, wolf_trade_role):
        self.total = num_wolf + num_villager
        self.current = 0
        self.seating = ["W"] * num_wolf + ["V"] * num_villager #Create instance seating
        self.samples = []

        for i in range(Wherewolf.sampling_size):
            shuffled_copy = random.sample(self.seating.copy(), len(self.seating))
            self.samples.append(shuffled_copy)
            __class__.weights[i] = 1    

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
            player_point_to = hint[index] - 1

            for number, sample in enumerate(self.samples):
                # W Point Same team
                if sample[player_point_from] == "W" and sample[player_point_to] == "W":
                    __class__.weights[number] *= self.wolf_point_same * 1 / self.num_wolf

                # W point opp
                if sample[player_point_from] == "W" and sample[player_point_to] == "V":
                    __class__.weights[number] *= self.wolf_point_opp * 1 / self.num_wolf

                # W stay quiet
                if sample[player_point_from] == "W" and player_point_to == 0:
                    __class__.weights[number] *= self.wolf_quiet * 1 / self.num_wolf

                # V Point Same team
                if sample[player_point_from] == "V" and sample[player_point_to] == "V":
                    __class__.weights[number] *= self.villager_point_same * 1 / self.num_villager

                # V point opp
                if sample[player_point_from] == "V" and sample[player_point_to] == "W":
                    __class__.weights[number] *= self.villager_point_opp * 1 / self.num_villager

                # V stay quiet
                if sample[player_point_from] == "V" and player_point_to == 0:
                    __class__.weights[number] *= self.villager_quiet * 1 / self.num_villager
                    
            __class__.weights = [float(i)/sum(__class__.weights) for i in __class__.weights]


    def deduction(self) -> int:
        """
        for each sample
                for each position 
                    keep track which position is most likely to be wolf
                """
        
        guess = self.weights.index(max(self.weights))
        sample = self.samples[guess] # Pass by value not by reference
        sample = list(sample)
        wolf_location = sample.index("W")
        self.samples[guess][wolf_location] = "-"
        self.current = wolf_location
        
        self.current += 1
        return self.current

    def transition(self, revealed: str):
        """for each sample:
                if sample[???][position] != revealed:
                        weight[????] = 0
                        
                resample()"""
        
        for index, sample in enumerate(self.samples):
            if sample[self.current - 1] != revealed:
                self.weights[index] = 0
            self.resample()
        pass


    def resample(self):
        samples2 = self.samples.copy()

        for index, sample in enumerate(samples2):
            guess = self.weights.index(max(self.weights))
            samples2[guess] = sample
            __class__.weights[index] = 1

        self.samples = samples2

        """
        create array sample2:
        for each sample in sample2:
        x = random depend on weight
        sample2[????] = sample[x]
        weight[???] = 1  
        """