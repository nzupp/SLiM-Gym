# -*- coding: utf-8 -*-
"""
@author: nzupp

Creates a SLiM script file for the SFS-based neutral Wright-Fisher simulations
with mutation and a bottleneck
"""

def create_slim_script(output_file, init_mutation_rate, num_sites, recomb_rate, pop_size, sample_size, bottleneck):
    """
    Creates a SLiM script that is SLiM-Gym ready with some custom parameters.

    Params:
        output_file (String): Name of the SLiM script the injector generates. Must end with .slim extension.
        init_mutation_rate (Float): Starting mutation rate of the SLiM simulation.
        num_sites (Int): Number of sites to simulate (recommend under 1k for testing).
        recomb_rate (Float): The recombination rate.
        pop_size (Int): The size of the starting population (assume Ne = Nc under WF).
        sample_size (Int): Number of individuals sampled each step.
        bottleneck (Float): Multiplicative factor by which the mutation rate is decreased.
                            (For example, 0.5 will halve the mutation rate at each update.)
    
    Returns:
        Nothing (the script is written to output_file).
    """
    
    script = f"""initialize() {{
    // The flag file used for communicating the desired population size
    defineConstant("FLAG_FILE", "flag.txt");
    initializeMutationRate({init_mutation_rate});
    initializeMutationType("m1", 0.5, "f", 0.0);
    initializeGenomicElementType("g1", m1, 1.0);
    initializeGenomicElement(g1, 0, {num_sites});
    initializeRecombinationRate({recomb_rate});
}}
1 early() {{
    // Create initial subpopulation with the provided pop_size.
    sim.addSubpop("p1", {pop_size});
    // Initialize a global variable for the mutation rate.
    mutRate = {init_mutation_rate};
}}
900:1000 late() {{
    if (community.tick % 10 == 0) {{
        // Output the state in MS format every 10 ticks.
        g = p1.sampleIndividuals({sample_size}).genomes;
        g.outputMS("state.txt", append=T);
    }}
}}
1001:5000 early() {{
    if (community.tick % 10 == 0) {{
        // Decrease the mutation rate by multiplying it by the bottleneck factor.
        mutRate = mutRate * {bottleneck};
        sim.chromosome.setMutationRate(mutRate);
    }}
}}
1001:5000 late() {{
    if (community.tick % 10 == 0) {{
        // Output state and update population size.
        g = p1.sampleIndividuals({sample_size}).genomes;
        g.outputMS("state.txt", append=T);
        // Delete the flag file, then wait for a new one to be written.
        deleteFile(FLAG_FILE);
        while (fileExists(FLAG_FILE) == F) {{
        }}
        popSizeStr = readFile(FLAG_FILE);
        while (size(popSizeStr) == 0) {{
            popSizeStr = readFile(FLAG_FILE);
        }}
        popSize = asFloat(popSizeStr);
        p1.setSubpopulationSize(popSize);
    }}
}}
5001 late() {{
    // End-of-run signal: wait for flag file and write a "generation_complete" message.
    while (fileExists(FLAG_FILE) == F) {{
    }}
    writeFile("generation_complete.txt", "1");
}}"""

    with open(output_file, 'w') as f:
        f.write(script)
        
