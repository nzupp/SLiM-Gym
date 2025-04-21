# -*- coding: utf-8 -*-
"""
@author: nzupp

Sample PPO example using SB3 for population genetics

Task: Identify the change in mutation rate needed to maintain previous
AFS in a bottleneck
"""

from slim_gym import make_sfs_env
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

def main():
    # Create the environment
    env = make_sfs_env(slim_file="bottleneck.slim")

    # Create PPO model
    model = PPO("MlpPolicy", env, verbose=1)

    # Train the model
    model.learn(total_timesteps=5000)

    # Save the model
    model.save("ppo_sfs_env")

    print("Training complete. Model saved as ppo_sfs_env.zip")

if __name__ == "__main__":
    main()
