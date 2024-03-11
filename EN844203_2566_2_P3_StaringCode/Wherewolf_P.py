#####
#
# Name: POTSAWAT LALITLAKKANAKUL
# Student ID: 633040222-7
#
#####

import random

class Wherewolf:
    PARTICLE_COUNT = 1000

    def __init__(self,N,M,R,W_o,W_q,W_s,V_o,V_q,V_s,T):
        self.N = N
        self.M = M
        self.R = R
        self.W_o = W_o
        self.W_q = W_q
        self.W_s = W_s
        self.V_o = V_o
        self.V_q = V_q
        self.V_s = V_s
        self.T = T

        self.total = N+M
        self.current = 0
        self.seating = ["W"] * N + ["V"] * M
        self.particles = []

        for _ in range(Wherewolf.PARTICLE_COUNT):
            shuffled = random.sample(self.seating.copy(), len(self.seating))
            self.particles.append(shuffled)

        self.weights = [1] * Wherewolf.PARTICLE_COUNT

    def interrogation(self,hint):
        for index in range(len(hint)):
            from_seat = index
            to_seat = hint[index] - 1

            for i, sample in enumerate(self.particles):
                if sample[from_seat] != "-":
                    if sample[from_seat] == "W":
                        if sample[to_seat] == "W":
                            self.weights[i] *= self.W_s
                        elif sample[to_seat] == "V":
                            self.weights[i] *= self.W_o
                        else:
                            self.weights[i] *= self.W_q
                    else:
                        if sample[to_seat] == "V":
                            self.weights[i] *= self.V_s
                        elif sample[to_seat] == "W":
                            self.weights[i] *= self.V_o
                        else:
                            self.weights[i] *= self.V_q

    def deduction(self):
        # Find the remaining seats that not eliminate yet
        remaining = [i for i, role in enumerate(self.seating) if role != "-"]
        
        # To track the maximum likelihood and the suspect candidates
        max_likelihood = 0
        candidates = []

        for seat in remaining:
            wolf_count = sum(1 for particle in self.particles if particle[seat] == "W")

            # Update the maximum likelihood and the list of suspect candidates
            if wolf_count > max_likelihood:
                max_likelihood = wolf_count
                candidates = [seat]
            elif wolf_count == max_likelihood:
                candidates.append(seat)

        # Random select suspect from candidates with more likelihood
        self.current = random.choice(candidates)
        
        # Update seats/particles to mark the suspect as eliminated
        for particle in self.particles:
            particle[self.current] = "-"
        self.seating[self.current] = "-"

        self.current += 1
        return self.current

    def transition(self,revealed):
        for index, particle in enumerate(self.particles):
            if particle != revealed:
                self.weights[index] = 0

        new_particles = random.choices(self.particles, weights=self.weights, k=Wherewolf.PARTICLE_COUNT)
        self.particles = new_particles

