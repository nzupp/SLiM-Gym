# SLiM-Gym
An early development Gymnasium wrapper for the SLiM 4 simulator enabling reinforcement learning for population genetics

## Quick start guide
1. Install via pip: `pip install slim_gym`
2. Install SLiM 4 from the [Messer Lab](https://messerlab.org/slim/) and ensure it's in your system PATH or working directory
3. Run a basic, random agent:

```python
import slim_gym
slim_gym.run_random_agent()
```

Users can also adjust the environment and pass it as a parameter to the random walk algorithm:

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

If these parameters are unfamiliar to you, our more detailed documentation (coming soon) is a great place to start. This environment functions as a Gymnasium environment, and can be used as such downstream. The code for making environments and the random walk algorithm can be found in the examples/ folder.


