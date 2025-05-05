# -*- coding: utf-8 -*-
"""
@author: nzupp

Sample environment to test a genetic rescue scenario

Extends the main four key functions created by the base env
1) Process initial state
2) Process state
3) Process action
4) Calculate reward

The action taken each step will represent the amount of migration
in a given generation. The observation will be based on genetic
diversity and inbreeding
"""

import numpy as np
from gymnasium import spaces
from collections import deque
from .. import SLiMGym
