import ray
import numpy as np




@ray.remote
class JobService:
    def __init__(self, num_runs, sim_function):
        self.num_runs = num_runs
        self.sim_function = sim_function

    def start(self):
        results = []
        for x in range(self.num_runs):
            results.append(self.sim_function.remote())
        return ray.get(results)

@ray.remote
def SimulationV1():
    import time
    time.sleep(1)
    return np.random.default_rng().random() * 2

@ray.remote
def SimulationV2():
    import time, numpy as np
    time.sleep(1)
    return np.random.default_rng().random()



if __name__ == "__main__":
    ray.init()

    num_runs = 10

    print("Starting Job Run")
    print("Running 20 tasks")
    references = [SimulationV1.remote() for x in range(20)]
    print("Total: " + str(sum(ray.get(references))))
    print("Running via 2 Actors")
    
    actor_1 = JobService.remote(num_runs, SimulationV1)
    actor_2 = JobService.remote(num_runs, SimulationV2)

    print("starting initial simulation")
    results = actor_1.start.remote()
    print("starting second simulation")
    results_2 = actor_2.start.remote()

    print("Awaiting Results")
    print("Simulation Results: \n==================")
    print("Mean: " + str(np.mean(ray.get(results))))
    print("Mean: " + str(np.mean(ray.get(results_2))))