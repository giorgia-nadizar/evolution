# competitive coevolution

def evaluate_tournament(predators, prey, k=5):
    predator_fitness = np.zeros(len(predators))
    prey_fitness = np.zeros(len(prey))

    for i, p in enumerate(predators):
        opponents = random.sample(list(prey), k)
        for q in opponents:
            distance = abs(p - q)
            predator_fitness[i] += -distance

    for j, q in enumerate(prey):
        opponents = random.sample(list(predators), k)
        for p in opponents:
            distance = abs(p - q)
            prey_fitness[j] += distance

    return predator_fitness, prey_fitness


def evaluate_with_hof(predators, prey, hof_pred, hof_prey):
    predator_fitness = np.zeros(len(predators))
    prey_fitness = np.zeros(len(prey))

    for i, p in enumerate(predators):
        opponents = list(prey) + hof_prey
        for q in opponents:
            distance = abs(p - q)
            predator_fitness[i] += -distance

    for j, q in enumerate(prey):
        opponents = list(predators) + hof_pred
        for p in opponents:
            distance = abs(p - q)
            prey_fitness[j] += distance

    return predator_fitness, prey_fitness

    
# cooperative coevolution
def component_a(x, params):
    return params[0] * x * x 

def component_b(x, params):
    return params[1] * x + params[2]