import random

target = "genetic algorithms are very cool"
alphabet = list("abcdefghijklmnopqrstuvwxyz ")

def create_popn(size):
    popn = []
    
    for i in range(size):
        individual = ""
        for j in range(len(target)):
            individual += random.choice(alphabet)
        popn.append(individual)

    return popn

def fitness(individual):
    correct = 0
    for ch1, ch2 in zip(individual, target):
        if ch1 == ch2:
            correct += 1

    return correct / len(target)

def crossover(p1, p2):
    crossover_point = random.randint(0, len(p1))

    offspring1 = p2[:crossover_point] + p1[crossover_point:]
    offspring2 = p1[:crossover_point] + p2[crossover_point:]
    return [offspring1, offspring2]

def mutate(individual):
    mutation_rate = 0.1
    new = ""
    for ch in individual:
        if random.random() < mutation_rate:
            new  += random.choice(alphabet)
        else:
            new += ch

    return new

def breed(p1, p2):
    return [mutate(x) for x in crossover(p1, p2)]

def evolve_popn(popn):
    popn = sorted(popn, key = lambda x : fitness(x))
    fittest_score = fitness(popn[-1])
    print (f"BEST IN GENERATION {popn[-1]}, FITNESS {fittest_score}") #Printing the best individual so we can see progress
    if fittest_score == 1:
        return 0 #break out the function since we have found the target
    popn = popn[int(len(popn) * 0.2):] #removing the worst 20% individuals
    new_popn = popn[int(len(popn) * 0.85):] #adding the top 15% individuals straight into the new population

    while len(popn) > 2:
        #selecting pairs are removing it from population
        index1 = random.choice(list(range(len(popn))))
        parent1 = popn[index1]
        popn = popn[:index1] + popn[index1+1:]
        index2 = random.choice(list(range(len(popn))))
        parent2 = popn[index2]
        popn = popn[:index2] + popn[index2+1:]

        
        #producing the offspring and adding it to the new generation
        for offspring in breed(parent1, parent2):
            new_popn.append(offspring)

    return new_popn


popn = create_popn(5000) #create an initial population of 5000

while len(popn) > 1:
    popn = evolve_popn(popn)
    if popn == 0:
        break
