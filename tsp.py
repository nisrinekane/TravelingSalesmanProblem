import random 
import pandas as pd
import numpy as np
from deap import base, creator, tools, algorithms
from visualize import plot_route

#  load data
df = pd.read_csv('data/cities.csv')
cities = df.values

# define fitness function
def fitness(individual):
    """caculate total distance of route"""
    total_distance = 0
    for i in range(len(individual)-1):
        city1 = cities.iloc[individual[i]]
        city2 = cities.iloc[individual[i+1]]
        total_distance += ((city1.X-city2.X)**2 + (city1.Y-city2.Y)**2)**0.5
    return total_distance,

# define mutation func:
def mutation(individual):
    """swap two cities in route"""
    idx1, idx2 = random.sample(range(len(individual)), 2)
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

# define crossover
def crossover(ind1, ind2):
    """crossover rtwo routes"""
    pass

# set up toolbox
creator.create('FitnessMin', base.Fitness, weights=(-1.0,))
creator.create('Individual', list, fitness=creator.FitnessMin)
toolbox = base.Toolbox()
toolbox.register('indices', random.sample, range(len(cities)), len(cities))
toolbox.register('individual', tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register('population', tools.initRepeat, list, toolbox.individual)

def distance(city1, city2):
    dist = np.sqrt((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2)
    # print(f"Distance between {city1} and {city2} is {dist}")
    return dist

def route_distance(individual):
    dist = sum(distance(cities[individual[i-1]], cities[individual[i]]) for i in range(len(individual)))
    return (dist,)  # return as tuple

toolbox.register('evaluate', route_distance)
toolbox.register('mate', tools.cxOrdered)
toolbox.register('mutate', tools.mutShuffleIndexes, indpb=0.05)
toolbox.register('select', tools.selTournament, tournsize=3)

# main evolutionary loop:
def main():
    pop = toolbox.population(n=100)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register('avg', np.mean)
    stats.register('std', np.std)
    stats.register('min', np.min)
    stats.register('max', np.max)

    pop, log = algorithms.eaSimple(pop, toolbox, 
                                        cxpb=0.7, mutpb=0.2, 
                                        ngen=100, 
                                        stats=stats, 
                                        halloffame=hof, 
                                        verbose=True)
    # print(f"Initial population: {pop}")
    child1, child2 = toolbox.mate(pop[0], pop[1])
    toolbox.mutate(child1)
    toolbox.mutate(child2)
    selected = toolbox.select(pop + [child1, child2], len(pop))
    # print(f"Population after one generation: {selected}")
    best_ind = tools.selBest(pop, 1)[0]
    print('Best individual is %s, %s' % (best_ind, best_ind.fitness.values))
    plot_route(best_ind, cities)
    return pop, log, hof

if __name__ == '__main__':
    pop, log, hof = main()

