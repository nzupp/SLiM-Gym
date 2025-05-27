"""
@author: nzupp

Sample environment to test migratory corridor placement (think land bridges over highways)

Extends the main four key functions created by the base env
1) Process initial state
2) Process state
3) Process action
4) Calculate reward

The action taken each step will represent one connection placed on a spatial grid. The 
observation will be based on genetic diversity and inbreeding
"""

import numpy as np
from gymnasium import spaces
from collections import deque
from .. import SLiMGym

class MigratoryCorridorGym(SLiMGym):
    def __init__(self, 
                slim_file,
                migration_rate,
                sampled_individuals,
                num_sites):
        """
        Initalizes the migratory corridor env.
        
        Params:
            slim_file (String): Name of the SLiM script
            
        Returns:
            Nothing       
        """
        
        # Initialize base class with generated script
        super().__init__(slim_file=slim_file)
