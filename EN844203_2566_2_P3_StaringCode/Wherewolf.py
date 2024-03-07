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
        self.particles = []

        for i in range(Wherewolf.sampling_size):
            shuffled_copy = random.sample(self.seating.copy(), len(self.seating))
            self.particles.append(shuffled_copy)
            __class__.weights[i] = 1    

        # May need to delete these out
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
        

            
    
    # DONE
    def interrogation(self, hint: list[str]):
        for index in range(len(hint)):
            player_point_from = index
            player_point_to = hint[index] - 1

            for number, sample in enumerate(self.particles):
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
                    


    def deduction(self) -> int:

        # Random another set of particles based on weights they have, that will be what state they we will use as based on educated guess
        # Choose from what is most seat likely to be the wolf 
        particles = random.choices(population = self.particles, weights = __class__.weights, k = __class__.sampling_size)

        wolf_chance = [0] * self.total

        for particle in particles:
            for i in range(len(particle)):
                if particle[i] == "W":
                    wolf_chance[i] += 1


        max_wolf_chance = max(wolf_chance)
        seat_with_max_chance = wolf_chance.index(max_wolf_chance)
        self.current = seat_with_max_chance


        self.kill_in_samples(self.current)

        """
        for each sample
                for each position 
                    keep track which position is most likely to be wolf
                """
        self.current += 1
        return self.current
    
    def kill_in_samples(self, index_kill: int):
        for particle in self.particles:
            particle[index_kill] = "-"
        pass

    def transition(self, revealed: str):
        for index, particle in enumerate(self.particles):
            if particle != revealed:
                __class__.weights[index] = 0

        #self.resample() # Do update the educated guess based on coming evidence
        """for each sample:
                if sample[???][position] != revealed:
                        weight[????] = 0
                        
                resample()"""

    def resample(self):

        particles = self.particles.copy()
        for index, particle in enumerate(particles):
            random_particle = random.choices(particles, weights=__class__.weights)
            particle = random_particle
            __class__.weights[index] = 1
        self.particles = particles

        """
        create array sample2:
        for each sample in sample2:
        x = random depend on weight
        sample2[????] = sample[x]
        weight[???] = 1  
        """

        #Mutate and shit