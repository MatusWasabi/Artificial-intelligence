#####
#
# Name: Matus Yaowvasrisuwan
# Student ID: 633040476-6
#
#####
import random


class Wherewolf:

    def __init__(self, num_wolf, num_villager, interrogation_rounds, wolf_point_opp, wolf_quiet, wolf_point_same, villager_point_opp, villager_quiet, villager_point_same, wolf_trade_role):
        self.total = num_wolf + num_villager
        self.current = 0
        self.seating = ["W"] * num_wolf + ["V"] * num_villager 
        self.particles = []

        self.sampling_size = num_villager * num_wolf
        self.weights = [0] * self.sampling_size

        for i in range(self.sampling_size):
            shuffled_copy = random.sample(self.seating.copy(), len(self.seating))
            self.particles.append(shuffled_copy)
            self.weights[i] = 1

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

            for index, sample in enumerate(self.particles):

                
                
                
                is_wolf_point_wolf = sample[player_point_from] == "W" and sample[player_point_to] == "W"
                if is_wolf_point_wolf:
                    self.weights[index] *= self.wolf_point_same * 1 / self.num_wolf

                is_wolf_point_vill = sample[player_point_from] == "W" and sample[player_point_to] == "V"
                if is_wolf_point_vill:
                    self.weights[index] *= self.wolf_point_opp * 1 / self.num_wolf

                is_wolf_quiet = sample[player_point_from] == "W" and player_point_to == 0
                if is_wolf_quiet:
                    self.weights[index] *= self.wolf_quiet * 1 / self.num_wolf

                is_vill_point_vill = sample[player_point_from] == "V" and sample[player_point_to] == "V"
                if is_vill_point_vill:
                    self.weights[index] *= self.villager_point_same * 1 / self.num_villager

                is_vill_point_wolf = sample[player_point_from] == "V" and sample[player_point_to] == "W"
                if is_vill_point_wolf:
                    self.weights[index] *= self.villager_point_opp * 1 / self.num_villager

                is_vill_quiet = sample[player_point_from] == "V" and player_point_to == 0
                if is_vill_quiet:
                    self.weights[index] *= self.villager_quiet * 1 / self.num_villager


        norm = self.normalize_against_sum(self.weights)
        self.weights = norm

        

    def normalize_against_sum(self, weights: list[int]) -> float:
        return [float(i)/sum(weights) for i in weights]

                                    
    def deduction(self) -> int:

        particles = random.choices(population = self.particles, weights = self.weights, k = self.sampling_size)
        wolf_chance = [0] * self.total

        for particle in particles:
            for i in range(len(particle)):
                if particle[i] == "W":
                    wolf_chance[i] += 1


        max_wolf_chance = max(wolf_chance)
        seat_with_max_chance = wolf_chance.index(max_wolf_chance)
        self.current = seat_with_max_chance

        self.current += 1
        return self.current

    def transition(self, revealed: str):
        for index, particle in enumerate(self.particles):
            if particle[self.current - 1] != revealed:
                self.mutate(revealed, particle)
                self.weights[index] = 0

        self.kill_in_samples(self.current - 1)
        self.resample()

    def kill_in_samples(self, index_kill: int):
        for particle in self.particles:
            particle[index_kill] = "-"
        pass

    def resample(self):

        particles = self.particles.copy()
        for index in range(len(particles)):
            random_particle = random.choices(particles, weights = self.weights)
            particles[index] = random_particle[0]
            self.weights[index] = 1

        self.particles = particles

    def mutate(self, true_role: str, particle: list):

        wolf_seats = []
        vill_seats = []
        for i in range(len(particle)):
            if particle[i] == "W":
                wolf_seats.append(i)

            if particle[i] == "V":
                vill_seats.append(i)
        
        if true_role == "W":
            random_wolf = random.choice(wolf_seats)
            particle[self.current - 1], particle[random_wolf] = particle[random_wolf], particle[self.current - 1]

        if true_role == "V":
            random_vill = random.choice(vill_seats)
            particle[self.current - 1], particle[random_vill] = particle[random_vill], particle[self.current - 1]

        

