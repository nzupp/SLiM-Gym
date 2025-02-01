# SLiM-Gym
Gymnasium wrapper for SLiM 4 simulator enabling reinforcement learning for population genetics

## Quick start guide
SLiM-Gym can be quickly downloaded through the command `pip install slim_gym`. This will download nearly all the content needed to use SLiM-Gym- but is notably lacking one important executable: SLiM! We suggest users reference the detailed instructions in the SLiM manual availabe at the Messer Lab website: https://messerlab.org/slim/, and ensure teh slim.exe is available either in the global path or the working directory. Future iterations of this documentation may include more detail on this section but for now we will assume you have access to SLiM.

From here, using SLiM-Gym on the established environments becomes rather trivial. If you want to get started immediately, you can import slim_gym and run an algorithm that will walk through the simulation, choosing random actions:

```python
import slim_gym
slim_gym.run_random_agent()
```

Users can also adjust the environment and pass it as a parameter to our random walk algorithm:

```python
import slim_gym

# Redefine env
output_file='sim.slim'
init_mutation_rate=1e-7
num_sites=999
recomb_rate=1e-8
pop_size=10000
sampled_individuals=25
sfs_stack_size=8
bottleneck=0.99

env = slim_gym.make_env(output_file=output_file,
    init_mutation_rate=init_mutation_rate,
    num_sites=num_sites,
    recomb_rate=recomb_rate,
    pop_size=pop_size,
    sampled_individuals=sampled_individuals,
    sfs_stack_size=sfs_stack_size,
    bottleneck=bottleneck)

slim_gym.run_random_agent(env=env)
```

If these parameters are unfamiliar to you, our more detailed documentation (coming soon) is a great place to start. This environment functions as a Gymnasium enviornment, and can be used as such downstream. The code for making environments and the random walk algorithm can be found in the examples/ folder.


